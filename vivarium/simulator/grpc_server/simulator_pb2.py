# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simulator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fsimulator.proto\x12\tsimulator\x1a\x1bgoogle/protobuf/empty.proto\"\x14\n\x04Name\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x14\n\x04Time\x12\x0c\n\x04time\x18\x01 \x01(\x05\"2\n\x05Slice\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0c\n\x04stop\x18\x02 \x01(\x05\x12\x0c\n\x04step\x18\x03 \x01(\x05\"$\n\x0eSerializedDict\x12\x12\n\nserialized\x18\x01 \x01(\t\"\xcf\x01\n\x10SimulationConfig\x12\x10\n\x08\x62ox_size\x18\x01 \x01(\x02\x12\x0f\n\x07map_dim\x18\x02 \x01(\x05\x12\x10\n\x08n_agents\x18\x03 \x01(\x05\x12\x15\n\rnum_steps_lax\x18\x04 \x01(\x05\x12\x15\n\rnum_lax_loops\x18\x05 \x01(\x05\x12\n\n\x02\x64t\x18\x06 \x01(\x02\x12\x0c\n\x04\x66req\x18\x07 \x01(\x02\x12\x17\n\x0fneighbor_radius\x18\x08 \x01(\x02\x12\x0e\n\x06to_jit\x18\t \x01(\x08\x12\x15\n\ruse_fori_loop\x18\n \x01(\x08\"h\n\x1aSimulationConfigSenderName\x12+\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x1b.simulator.SimulationConfig\x12\x1d\n\x04name\x18\x02 \x01(\x0b\x32\x0f.simulator.Name\"0\n\x1aSimulationConfigSerialized\x12\x12\n\nserialized\x18\x01 \x01(\t\"\x17\n\x08\x41gentIdx\x12\x0b\n\x03idx\x18\x01 \x03(\x05\"\xc5\x01\n\x0b\x41gentConfig\x12\x16\n\x0ewheel_diameter\x18\x01 \x01(\x02\x12\x13\n\x0b\x62\x61se_length\x18\x02 \x01(\x02\x12\x11\n\tspeed_mul\x18\x03 \x01(\x02\x12\x11\n\ttheta_mul\x18\x04 \x01(\x02\x12\x16\n\x0eproxs_dist_max\x18\x06 \x01(\x02\x12\x15\n\rproxs_cos_min\x18\x07 \x01(\x02\x12\x10\n\x08\x62\x65havior\x18\x08 \x01(\t\x12\r\n\x05\x63olor\x18\t \x01(\t\x12\x13\n\x0b\x65ntity_type\x18\n \x01(\x05\"\x83\x01\n\x18\x41gentConfigIdxSenderName\x12&\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x16.simulator.AgentConfig\x12\x1d\n\x04name\x18\x02 \x01(\x0b\x32\x0f.simulator.Name\x12 \n\x03idx\x18\x03 \x01(\x0b\x32\x13.simulator.AgentIdx\"b\n\x18SerializedDictSenderName\x12\'\n\x04\x64ict\x18\x01 \x01(\x0b\x32\x19.simulator.SerializedDict\x12\x1d\n\x04name\x18\x02 \x01(\x0b\x32\x0f.simulator.Name\"\x87\x01\n\x1bSerializedDictIdxSenderName\x12\'\n\x04\x64ict\x18\x01 \x01(\x0b\x32\x19.simulator.SerializedDict\x12\x1d\n\x04name\x18\x02 \x01(\x0b\x32\x0f.simulator.Name\x12 \n\x03idx\x18\x03 \x01(\x0b\x32\x13.simulator.AgentIdx\"=\n\x0c\x41gentConfigs\x12-\n\ragent_configs\x18\x01 \x03(\x0b\x32\x16.simulator.AgentConfig\"_\n\x13\x41llConfigSerialized\x12\x19\n\x11simulation_config\x18\x01 \x01(\t\x12\x15\n\ragent_configs\x18\x02 \x01(\t\x12\x16\n\x0eobject_configs\x18\x03 \x01(\t\"+\n\x15\x41gentConfigSerialized\x12\x12\n\nserialized\x18\x01 \x01(\t\",\n\x16\x41gentConfigsSerialized\x12\x12\n\nserialized\x18\x01 \x03(\t\"\x1a\n\x07NDArray\x12\x0f\n\x07ndarray\x18\x01 \x01(\x0c\"X\n\tRigidBody\x12\"\n\x06\x63\x65nter\x18\x01 \x01(\x0b\x32\x12.simulator.NDArray\x12\'\n\x0borientation\x18\x02 \x01(\x0b\x32\x12.simulator.NDArray\"\xc0\x02\n\x08NVEState\x12&\n\x08position\x18\x01 \x01(\x0b\x32\x14.simulator.RigidBody\x12&\n\x08momentum\x18\x02 \x01(\x0b\x32\x14.simulator.RigidBody\x12#\n\x05\x66orce\x18\x03 \x01(\x0b\x32\x14.simulator.RigidBody\x12\"\n\x04mass\x18\x04 \x01(\x0b\x32\x14.simulator.RigidBody\x12$\n\x08\x64iameter\x18\x05 \x01(\x0b\x32\x12.simulator.NDArray\x12\'\n\x0b\x65ntity_type\x18\x06 \x01(\x0b\x32\x12.simulator.NDArray\x12&\n\nentity_idx\x18\x07 \x01(\x0b\x32\x12.simulator.NDArray\x12$\n\x08\x66riction\x18\x08 \x01(\x0b\x32\x12.simulator.NDArray\"\x90\x03\n\nAgentState\x12#\n\x07nve_idx\x18\x01 \x01(\x0b\x32\x12.simulator.NDArray\x12 \n\x04prox\x18\x02 \x01(\x0b\x32\x12.simulator.NDArray\x12!\n\x05motor\x18\x03 \x01(\x0b\x32\x12.simulator.NDArray\x12$\n\x08\x62\x65havior\x18\x04 \x01(\x0b\x32\x12.simulator.NDArray\x12*\n\x0ewheel_diameter\x18\x05 \x01(\x0b\x32\x12.simulator.NDArray\x12%\n\tspeed_mul\x18\x06 \x01(\x0b\x32\x12.simulator.NDArray\x12%\n\ttheta_mul\x18\x07 \x01(\x0b\x32\x12.simulator.NDArray\x12*\n\x0eproxs_dist_max\x18\x08 \x01(\x0b\x32\x12.simulator.NDArray\x12)\n\rproxs_cos_min\x18\t \x01(\x0b\x32\x12.simulator.NDArray\x12!\n\x05\x63olor\x18\n \x01(\x0b\x32\x12.simulator.NDArray\"\x7f\n\x0bObjectState\x12#\n\x07nve_idx\x18\x01 \x01(\x0b\x32\x12.simulator.NDArray\x12(\n\x0c\x63ustom_field\x18\x02 \x01(\x0b\x32\x12.simulator.NDArray\x12!\n\x05\x63olor\x18\x03 \x01(\x0b\x32\x12.simulator.NDArray\"\x89\x01\n\x05State\x12&\n\tnve_state\x18\x01 \x01(\x0b\x32\x13.simulator.NVEState\x12*\n\x0b\x61gent_state\x18\x02 \x01(\x0b\x32\x15.simulator.AgentState\x12,\n\x0cobject_state\x18\x03 \x01(\x0b\x32\x16.simulator.ObjectState\"U\n\tMotorInfo\x12&\n\tagent_idx\x18\x01 \x01(\x0b\x32\x13.simulator.AgentIdx\x12\x11\n\tmotor_idx\x18\x02 \x01(\x05\x12\r\n\x05value\x18\x03 \x01(\x02\")\n\x05Motor\x12\x11\n\tagent_idx\x18\x01 \x01(\x05\x12\r\n\x05motor\x18\x02 \x03(\x02\"\'\n\x04Prox\x12\x11\n\tagent_idx\x18\x01 \x01(\x05\x12\x0c\n\x04prox\x18\x02 \x03(\x02\"/\n\x08\x42\x65havior\x12\x11\n\tagent_idx\x18\x01 \x01(\x05\x12\x10\n\x08\x66unction\x18\x02 \x01(\x0c\"h\n\x0bStateChange\x12\x0f\n\x07nve_idx\x18\x01 \x03(\x05\x12\x0f\n\x07\x63ol_idx\x18\x02 \x03(\x05\x12\x14\n\x0cnested_field\x18\x03 \x03(\t\x12!\n\x05value\x18\x04 \x01(\x0b\x32\x12.simulator.NDArray\"<\n\rAddAgentInput\x12\x10\n\x08n_agents\x18\x01 \x01(\x05\x12\x19\n\x11serialized_config\x18\x02 \x01(\t\"$\n\x0eIsStartedState\x12\x12\n\nis_started\x18\x01 \x01(\x08\x32\xbf\x10\n\x0fSimulatorServer\x12S\n\x1aGetSimulationConfigMessage\x12\x16.google.protobuf.Empty\x1a\x1b.simulator.SimulationConfig\"\x00\x12`\n\x1dGetSimulationConfigSerialized\x12\x16.google.protobuf.Empty\x1a%.simulator.SimulationConfigSerialized\"\x00\x12\x42\n\x12GetRecordedChanges\x12\x0f.simulator.Name\x1a\x19.simulator.SerializedDict\"\x00\x12R\n\x16GetAllConfigSerialized\x12\x16.google.protobuf.Empty\x1a\x1e.simulator.AllConfigSerialized\"\x00\x12I\n\x15GetAgentConfigMessage\x12\x16.google.protobuf.Empty\x1a\x16.simulator.AgentConfig\"\x00\x12S\n\x18GetAgentConfigSerialized\x12\x13.simulator.AgentIdx\x1a .simulator.AgentConfigSerialized\"\x00\x12X\n\x19GetAgentConfigsSerialized\x12\x16.google.protobuf.Empty\x1a!.simulator.AgentConfigsSerialized\"\x00\x12\x44\n\x0fGetAgentConfigs\x12\x16.google.protobuf.Empty\x1a\x17.simulator.AgentConfigs\"\x00\x12?\n\x0eGetAgentConfig\x12\x13.simulator.AgentIdx\x1a\x16.simulator.AgentConfig\"\x00\x12=\n\x12SensoryMotorStream\x12\x10.simulator.Motor\x1a\x0f.simulator.Prox\"\x00(\x01\x30\x01\x12\x41\n\x0eNVEStateStream\x12\x16.google.protobuf.Empty\x1a\x13.simulator.NVEState\"\x00\x30\x01\x12\x41\n\rStopNVEStream\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12>\n\rStartBehavior\x12\x13.simulator.Behavior\x1a\x16.google.protobuf.Empty\"\x00\x12\x30\n\tAgentStep\x12\x10.simulator.Motor\x1a\x0f.simulator.Prox\"\x00\x12\x32\n\x04Step\x12\x16.google.protobuf.Empty\x1a\x10.simulator.State\"\x00\x12`\n\x1dSetSimulationConfigSerialized\x12%.simulator.SimulationConfigSerialized\x1a\x16.google.protobuf.Empty\"\x00\x12T\n\x13SetSimulationConfig\x12#.simulator.SerializedDictSenderName\x1a\x16.google.protobuf.Empty\"\x00\x12R\n\x0eSetAgentConfig\x12&.simulator.SerializedDictIdxSenderName\x1a\x16.simulator.AgentConfig\"\x00\x12;\n\tSetMotors\x12\x14.simulator.MotorInfo\x1a\x16.google.protobuf.Empty\"\x00\x12\x36\n\x08GetState\x12\x16.google.protobuf.Empty\x1a\x10.simulator.State\"\x00\x12<\n\x0bGetNVEState\x12\x16.google.protobuf.Empty\x1a\x13.simulator.NVEState\"\x00\x12@\n\rGetAgentState\x12\x16.google.protobuf.Empty\x1a\x15.simulator.AgentState\"\x00\x12\x42\n\x0eGetObjectState\x12\x16.google.protobuf.Empty\x1a\x16.simulator.ObjectState\"\x00\x12<\n\x08SetState\x12\x16.simulator.StateChange\x1a\x16.google.protobuf.Empty\"\x00\x12<\n\tAddAgents\x12\x18.simulator.AddAgentInput\x1a\x13.simulator.AgentIdx\"\x00\x12=\n\x0cRemoveAgents\x12\x13.simulator.AgentIdx\x1a\x16.google.protobuf.Empty\"\x00\x12@\n\tIsStarted\x12\x16.google.protobuf.Empty\x1a\x19.simulator.IsStartedState\"\x00\x12\x39\n\x05Start\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12\x38\n\x04Stop\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12:\n\rGetChangeTime\x12\x16.google.protobuf.Empty\x1a\x0f.simulator.Time\"\x00\x42\x34\n\x1aio.grpc.examples.simulatorB\x0eSimulatorProtoP\x01\xa2\x02\x03SIMb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'simulator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032io.grpc.examples.simulatorB\016SimulatorProtoP\001\242\002\003SIM'
  _globals['_NAME']._serialized_start=59
  _globals['_NAME']._serialized_end=79
  _globals['_TIME']._serialized_start=81
  _globals['_TIME']._serialized_end=101
  _globals['_SLICE']._serialized_start=103
  _globals['_SLICE']._serialized_end=153
  _globals['_SERIALIZEDDICT']._serialized_start=155
  _globals['_SERIALIZEDDICT']._serialized_end=191
  _globals['_SIMULATIONCONFIG']._serialized_start=194
  _globals['_SIMULATIONCONFIG']._serialized_end=401
  _globals['_SIMULATIONCONFIGSENDERNAME']._serialized_start=403
  _globals['_SIMULATIONCONFIGSENDERNAME']._serialized_end=507
  _globals['_SIMULATIONCONFIGSERIALIZED']._serialized_start=509
  _globals['_SIMULATIONCONFIGSERIALIZED']._serialized_end=557
  _globals['_AGENTIDX']._serialized_start=559
  _globals['_AGENTIDX']._serialized_end=582
  _globals['_AGENTCONFIG']._serialized_start=585
  _globals['_AGENTCONFIG']._serialized_end=782
  _globals['_AGENTCONFIGIDXSENDERNAME']._serialized_start=785
  _globals['_AGENTCONFIGIDXSENDERNAME']._serialized_end=916
  _globals['_SERIALIZEDDICTSENDERNAME']._serialized_start=918
  _globals['_SERIALIZEDDICTSENDERNAME']._serialized_end=1016
  _globals['_SERIALIZEDDICTIDXSENDERNAME']._serialized_start=1019
  _globals['_SERIALIZEDDICTIDXSENDERNAME']._serialized_end=1154
  _globals['_AGENTCONFIGS']._serialized_start=1156
  _globals['_AGENTCONFIGS']._serialized_end=1217
  _globals['_ALLCONFIGSERIALIZED']._serialized_start=1219
  _globals['_ALLCONFIGSERIALIZED']._serialized_end=1314
  _globals['_AGENTCONFIGSERIALIZED']._serialized_start=1316
  _globals['_AGENTCONFIGSERIALIZED']._serialized_end=1359
  _globals['_AGENTCONFIGSSERIALIZED']._serialized_start=1361
  _globals['_AGENTCONFIGSSERIALIZED']._serialized_end=1405
  _globals['_NDARRAY']._serialized_start=1407
  _globals['_NDARRAY']._serialized_end=1433
  _globals['_RIGIDBODY']._serialized_start=1435
  _globals['_RIGIDBODY']._serialized_end=1523
  _globals['_NVESTATE']._serialized_start=1526
  _globals['_NVESTATE']._serialized_end=1846
  _globals['_AGENTSTATE']._serialized_start=1849
  _globals['_AGENTSTATE']._serialized_end=2249
  _globals['_OBJECTSTATE']._serialized_start=2251
  _globals['_OBJECTSTATE']._serialized_end=2378
  _globals['_STATE']._serialized_start=2381
  _globals['_STATE']._serialized_end=2518
  _globals['_MOTORINFO']._serialized_start=2520
  _globals['_MOTORINFO']._serialized_end=2605
  _globals['_MOTOR']._serialized_start=2607
  _globals['_MOTOR']._serialized_end=2648
  _globals['_PROX']._serialized_start=2650
  _globals['_PROX']._serialized_end=2689
  _globals['_BEHAVIOR']._serialized_start=2691
  _globals['_BEHAVIOR']._serialized_end=2738
  _globals['_STATECHANGE']._serialized_start=2740
  _globals['_STATECHANGE']._serialized_end=2844
  _globals['_ADDAGENTINPUT']._serialized_start=2846
  _globals['_ADDAGENTINPUT']._serialized_end=2906
  _globals['_ISSTARTEDSTATE']._serialized_start=2908
  _globals['_ISSTARTEDSTATE']._serialized_end=2944
  _globals['_SIMULATORSERVER']._serialized_start=2947
  _globals['_SIMULATORSERVER']._serialized_end=5058
# @@protoc_insertion_point(module_scope)
