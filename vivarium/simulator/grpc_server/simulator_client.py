import json

import grpc
from vivarium.simulator.grpc_server import simulator_pb2_grpc
import vivarium.simulator.grpc_server.simulator_pb2 as simulator_pb2

from vivarium.simulator.config import SimulatorConfig, AgentConfig
from vivarium.simulator.sim_computation import NVEState
from vivarium.simulator.simulator_client_abc import SimulatorClient

from jax_md.rigid_body import RigidBody

from numproto.numproto import ndarray_to_proto, proto_to_ndarray

Empty = simulator_pb2.google_dot_protobuf_dot_empty__pb2.Empty


class SimulatorGRPCClient(SimulatorClient):
    def __init__(self, name=None):
        self.name = name
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = simulator_pb2_grpc.SimulatorServerStub(channel)

    def start(self):
        self.stub.Start(Empty())

    def stop(self):
        self.stub.Stop(Empty())

    def get_change_time(self):
        return self.stub.GetChangeTime(Empty()).time

    def get_sim_config(self):
        serialized = self.stub.GetSimulationConfigSerialized(Empty()).serialized
        return SimulatorConfig(**SimulatorConfig.param.deserialize_parameters(serialized))

    def get_recorded_changes(self):
        changes = self.stub.GetRecordedChanges(simulator_pb2.Name(name=self.name))
        d = json.loads(changes.serialized_dict)
        if changes.has_entity_behaviors:
            d['entity_behaviors'] = proto_to_ndarray(changes.entity_behaviors)
        return d

    def get_agent_config(self, idx):
        print('get_agent_config')
        serialized = self.stub.GetAgentConfigSerialized(simulator_pb2.AgentIdx(idx=idx)).serialized
        return AgentConfig(**AgentConfig.param.deserialize_parameters(serialized))

    def get_agent_configs(self):
        serialized = self.stub.GetAgentConfigsSerialized(Empty()).serialized
        return [AgentConfig(**AgentConfig.param.deserialize_parameters(s)) for s in serialized]

    def set_simulation_config(self, simulation_config_dict):
        print('set_simulation_config', simulation_config_dict)
        serial_dict = json.dumps(simulation_config_dict)
        serial_dict = simulator_pb2.SerializedDict(serialized=serial_dict)
        name = simulator_pb2.Name(name=self.name)
        dict_sender_name = simulator_pb2.SerializedDictSenderName(name=name, dict=serial_dict)
        self.stub.SetSimulationConfig(dict_sender_name)

    def set_agent_config(self, selected_agents, agent_config_dict):
        print('set_agent_config', agent_config_dict)
        serial_dict = json.dumps(agent_config_dict)
        serial_dict = simulator_pb2.SerializedDict(serialized=serial_dict)
        name = simulator_pb2.Name(name=self.name)
        idx = simulator_pb2.AgentIdx(idx=selected_agents)
        dict_idx_sender_name = simulator_pb2.SerializedDictIdxSenderName(name=name, dict=serial_dict, idx=idx)
        self.stub.SetAgentConfig(dict_idx_sender_name)

    def set_motors(self, selected_agents, motor_idx, value):
        agent_idx = simulator_pb2.AgentIdx(idx=selected_agents)
        motor_info = simulator_pb2.MotorInfo(agent_idx=agent_idx, motor_idx=motor_idx, value=value)
        self.stub.SetMotors(motor_info)

    def set_state(self, agent_indexes, nested_field, value):
        agent_idx = simulator_pb2.AgentIdx(idx=agent_indexes)
        state_change = simulator_pb2.StateChange(agent_idx=agent_idx, nested_field=nested_field,
                                                 value=ndarray_to_proto(value))
        self.stub.SetState(state_change)

    def set_simulation_config_serialized(self, simulation_config):
        serialized = simulation_config.param.serialize_parameters(subset=simulation_config.export_fields)
        self.stub.SetSimulationConfigSerialized(simulator_pb2.SimulationConfigSerialized(serialized=serialized))

    def get_state(self):
        return self.stub.GetStateMessage(Empty())


    def get_nve_state(self):
        state = self.stub.GetNVEState(Empty())
        return NVEState(position=RigidBody(center=proto_to_ndarray(state.position.center).astype(float),
                                           orientation=proto_to_ndarray(state.position.orientation).astype(float)),
                        momentum=RigidBody(center=proto_to_ndarray(state.momentum.center).astype(float),
                                           orientation=proto_to_ndarray(state.momentum.orientation).astype(float)),
                        force=RigidBody(center=proto_to_ndarray(state.force.center).astype(float),
                                        orientation=proto_to_ndarray(state.force.orientation).astype(float)),
                        mass=RigidBody(center=proto_to_ndarray(state.mass.center).astype(float),
                                       orientation=proto_to_ndarray(state.mass.orientation).astype(float)),
                        idx=proto_to_ndarray(state.idx).astype(int),
                        prox=proto_to_ndarray(state.prox).astype(float),
                        motor=proto_to_ndarray(state.motor).astype(float),
                        behavior=proto_to_ndarray(state.behavior).astype(int),
                        wheel_diameter=proto_to_ndarray(state.wheel_diameter).astype(float),
                        base_length=proto_to_ndarray(state.base_length).astype(float),
                        speed_mul=proto_to_ndarray(state.speed_mul).astype(float),
                        theta_mul=proto_to_ndarray(state.theta_mul).astype(float),
                        proxs_dist_max=proto_to_ndarray(state.proxs_dist_max).astype(float),
                        proxs_cos_min=proto_to_ndarray(state.proxs_cos_min).astype(float),
                        color=proto_to_ndarray(state.color).astype(float),
                        entity_type=proto_to_ndarray(state.entity_type).astype(int)
                        )

    def add_agents(self, n_agents, agent_config):
        d = agent_config.param.serialize_parameters(subset=agent_config.export_fields)
        # config = simulator_pb2.AgentConfig(**agent_config.to_dict())
        input = simulator_pb2.AddAgentInput(n_agents=n_agents,
                                            serialized_config=d)
        return self.stub.AddAgents(input)
    def is_started(self):
        return self.stub.IsStarted(Empty()).is_started

