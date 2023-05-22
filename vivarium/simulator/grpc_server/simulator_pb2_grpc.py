# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import simulator_pb2 as simulator__pb2


class SimulatorServerStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSimulationConfigMessage = channel.unary_unary(
                '/simulator.SimulatorServer/GetSimulationConfigMessage',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=simulator__pb2.SimulationConfig.FromString,
                )
        self.GetSimulationConfigSerialized = channel.unary_unary(
                '/simulator.SimulatorServer/GetSimulationConfigSerialized',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=simulator__pb2.SimulationConfigSerialized.FromString,
                )
        self.GetRecordedChanges = channel.unary_unary(
                '/simulator.SimulatorServer/GetRecordedChanges',
                request_serializer=simulator__pb2.Name.SerializeToString,
                response_deserializer=simulator__pb2.SerializedDict.FromString,
                )
        self.GetAgentConfigMessage = channel.unary_unary(
                '/simulator.SimulatorServer/GetAgentConfigMessage',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=simulator__pb2.AgentConfig.FromString,
                )
        self.GetAgentConfigSerialized = channel.unary_unary(
                '/simulator.SimulatorServer/GetAgentConfigSerialized',
                request_serializer=simulator__pb2.AgentIdx.SerializeToString,
                response_deserializer=simulator__pb2.AgentConfigSerialized.FromString,
                )
        self.GetAgentConfigs = channel.unary_unary(
                '/simulator.SimulatorServer/GetAgentConfigs',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=simulator__pb2.AgentConfigs.FromString,
                )
        self.GetAgentConfig = channel.unary_unary(
                '/simulator.SimulatorServer/GetAgentConfig',
                request_serializer=simulator__pb2.AgentIdx.SerializeToString,
                response_deserializer=simulator__pb2.AgentConfig.FromString,
                )
        self.SetSimulationConfigSerialized = channel.unary_unary(
                '/simulator.SimulatorServer/SetSimulationConfigSerialized',
                request_serializer=simulator__pb2.SimulationConfigSerialized.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SetSimulationConfig = channel.unary_unary(
                '/simulator.SimulatorServer/SetSimulationConfig',
                request_serializer=simulator__pb2.SerializedDictSenderName.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SetAgentConfig = channel.unary_unary(
                '/simulator.SimulatorServer/SetAgentConfig',
                request_serializer=simulator__pb2.SerializedDictIdxSenderName.SerializeToString,
                response_deserializer=simulator__pb2.AgentConfig.FromString,
                )
        self.SetMotors = channel.unary_unary(
                '/simulator.SimulatorServer/SetMotors',
                request_serializer=simulator__pb2.MotorInfo.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SetState = channel.unary_unary(
                '/simulator.SimulatorServer/SetState',
                request_serializer=simulator__pb2.StateChange.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetNVEState = channel.unary_unary(
                '/simulator.SimulatorServer/GetNVEState',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=simulator__pb2.NVEState.FromString,
                )
        self.IsStarted = channel.unary_unary(
                '/simulator.SimulatorServer/IsStarted',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=simulator__pb2.IsStartedState.FromString,
                )
        self.Start = channel.unary_unary(
                '/simulator.SimulatorServer/Start',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Stop = channel.unary_unary(
                '/simulator.SimulatorServer/Stop',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetChangeTime = channel.unary_unary(
                '/simulator.SimulatorServer/GetChangeTime',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=simulator__pb2.Time.FromString,
                )


class SimulatorServerServicer(object):
    """Interface exported by the server.
    """

    def GetSimulationConfigMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSimulationConfigSerialized(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRecordedChanges(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAgentConfigMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAgentConfigSerialized(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAgentConfigs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAgentConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSimulationConfigSerialized(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSimulationConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAgentConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetMotors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNVEState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsStarted(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Start(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stop(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChangeTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimulatorServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSimulationConfigMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSimulationConfigMessage,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=simulator__pb2.SimulationConfig.SerializeToString,
            ),
            'GetSimulationConfigSerialized': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSimulationConfigSerialized,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=simulator__pb2.SimulationConfigSerialized.SerializeToString,
            ),
            'GetRecordedChanges': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRecordedChanges,
                    request_deserializer=simulator__pb2.Name.FromString,
                    response_serializer=simulator__pb2.SerializedDict.SerializeToString,
            ),
            'GetAgentConfigMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAgentConfigMessage,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=simulator__pb2.AgentConfig.SerializeToString,
            ),
            'GetAgentConfigSerialized': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAgentConfigSerialized,
                    request_deserializer=simulator__pb2.AgentIdx.FromString,
                    response_serializer=simulator__pb2.AgentConfigSerialized.SerializeToString,
            ),
            'GetAgentConfigs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAgentConfigs,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=simulator__pb2.AgentConfigs.SerializeToString,
            ),
            'GetAgentConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAgentConfig,
                    request_deserializer=simulator__pb2.AgentIdx.FromString,
                    response_serializer=simulator__pb2.AgentConfig.SerializeToString,
            ),
            'SetSimulationConfigSerialized': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSimulationConfigSerialized,
                    request_deserializer=simulator__pb2.SimulationConfigSerialized.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetSimulationConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSimulationConfig,
                    request_deserializer=simulator__pb2.SerializedDictSenderName.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetAgentConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAgentConfig,
                    request_deserializer=simulator__pb2.SerializedDictIdxSenderName.FromString,
                    response_serializer=simulator__pb2.AgentConfig.SerializeToString,
            ),
            'SetMotors': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMotors,
                    request_deserializer=simulator__pb2.MotorInfo.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetState': grpc.unary_unary_rpc_method_handler(
                    servicer.SetState,
                    request_deserializer=simulator__pb2.StateChange.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetNVEState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNVEState,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=simulator__pb2.NVEState.SerializeToString,
            ),
            'IsStarted': grpc.unary_unary_rpc_method_handler(
                    servicer.IsStarted,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=simulator__pb2.IsStartedState.SerializeToString,
            ),
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Stop': grpc.unary_unary_rpc_method_handler(
                    servicer.Stop,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetChangeTime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChangeTime,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=simulator__pb2.Time.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'simulator.SimulatorServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SimulatorServer(object):
    """Interface exported by the server.
    """

    @staticmethod
    def GetSimulationConfigMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/GetSimulationConfigMessage',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            simulator__pb2.SimulationConfig.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSimulationConfigSerialized(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/GetSimulationConfigSerialized',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            simulator__pb2.SimulationConfigSerialized.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRecordedChanges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/GetRecordedChanges',
            simulator__pb2.Name.SerializeToString,
            simulator__pb2.SerializedDict.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAgentConfigMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/GetAgentConfigMessage',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            simulator__pb2.AgentConfig.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAgentConfigSerialized(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/GetAgentConfigSerialized',
            simulator__pb2.AgentIdx.SerializeToString,
            simulator__pb2.AgentConfigSerialized.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAgentConfigs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/GetAgentConfigs',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            simulator__pb2.AgentConfigs.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAgentConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/GetAgentConfig',
            simulator__pb2.AgentIdx.SerializeToString,
            simulator__pb2.AgentConfig.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSimulationConfigSerialized(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/SetSimulationConfigSerialized',
            simulator__pb2.SimulationConfigSerialized.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSimulationConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/SetSimulationConfig',
            simulator__pb2.SerializedDictSenderName.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAgentConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/SetAgentConfig',
            simulator__pb2.SerializedDictIdxSenderName.SerializeToString,
            simulator__pb2.AgentConfig.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetMotors(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/SetMotors',
            simulator__pb2.MotorInfo.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/SetState',
            simulator__pb2.StateChange.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNVEState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/GetNVEState',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            simulator__pb2.NVEState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IsStarted(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/IsStarted',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            simulator__pb2.IsStartedState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/Start',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/Stop',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetChangeTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simulator.SimulatorServer/GetChangeTime',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            simulator__pb2.Time.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
