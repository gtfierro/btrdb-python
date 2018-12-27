# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import btrdb.grpcinterface.btrdb_pb2 as btrdb__pb2


class BTrDBStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RawValues = channel.unary_stream(
        '/grpcinterface.BTrDB/RawValues',
        request_serializer=btrdb__pb2.RawValuesParams.SerializeToString,
        response_deserializer=btrdb__pb2.RawValuesResponse.FromString,
        )
    self.AlignedWindows = channel.unary_stream(
        '/grpcinterface.BTrDB/AlignedWindows',
        request_serializer=btrdb__pb2.AlignedWindowsParams.SerializeToString,
        response_deserializer=btrdb__pb2.AlignedWindowsResponse.FromString,
        )
    self.Windows = channel.unary_stream(
        '/grpcinterface.BTrDB/Windows',
        request_serializer=btrdb__pb2.WindowsParams.SerializeToString,
        response_deserializer=btrdb__pb2.WindowsResponse.FromString,
        )
    self.StreamInfo = channel.unary_unary(
        '/grpcinterface.BTrDB/StreamInfo',
        request_serializer=btrdb__pb2.StreamInfoParams.SerializeToString,
        response_deserializer=btrdb__pb2.StreamInfoResponse.FromString,
        )
    self.SetStreamAnnotations = channel.unary_unary(
        '/grpcinterface.BTrDB/SetStreamAnnotations',
        request_serializer=btrdb__pb2.SetStreamAnnotationsParams.SerializeToString,
        response_deserializer=btrdb__pb2.SetStreamAnnotationsResponse.FromString,
        )
    self.SetStreamTags = channel.unary_unary(
        '/grpcinterface.BTrDB/SetStreamTags',
        request_serializer=btrdb__pb2.SetStreamTagsParams.SerializeToString,
        response_deserializer=btrdb__pb2.SetStreamTagsResponse.FromString,
        )
    self.Create = channel.unary_unary(
        '/grpcinterface.BTrDB/Create',
        request_serializer=btrdb__pb2.CreateParams.SerializeToString,
        response_deserializer=btrdb__pb2.CreateResponse.FromString,
        )
    self.ListCollections = channel.unary_stream(
        '/grpcinterface.BTrDB/ListCollections',
        request_serializer=btrdb__pb2.ListCollectionsParams.SerializeToString,
        response_deserializer=btrdb__pb2.ListCollectionsResponse.FromString,
        )
    self.LookupStreams = channel.unary_stream(
        '/grpcinterface.BTrDB/LookupStreams',
        request_serializer=btrdb__pb2.LookupStreamsParams.SerializeToString,
        response_deserializer=btrdb__pb2.LookupStreamsResponse.FromString,
        )
    self.Nearest = channel.unary_unary(
        '/grpcinterface.BTrDB/Nearest',
        request_serializer=btrdb__pb2.NearestParams.SerializeToString,
        response_deserializer=btrdb__pb2.NearestResponse.FromString,
        )
    self.Changes = channel.unary_stream(
        '/grpcinterface.BTrDB/Changes',
        request_serializer=btrdb__pb2.ChangesParams.SerializeToString,
        response_deserializer=btrdb__pb2.ChangesResponse.FromString,
        )
    self.Insert = channel.unary_unary(
        '/grpcinterface.BTrDB/Insert',
        request_serializer=btrdb__pb2.InsertParams.SerializeToString,
        response_deserializer=btrdb__pb2.InsertResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/grpcinterface.BTrDB/Delete',
        request_serializer=btrdb__pb2.DeleteParams.SerializeToString,
        response_deserializer=btrdb__pb2.DeleteResponse.FromString,
        )
    self.Info = channel.unary_unary(
        '/grpcinterface.BTrDB/Info',
        request_serializer=btrdb__pb2.InfoParams.SerializeToString,
        response_deserializer=btrdb__pb2.InfoResponse.FromString,
        )
    self.FaultInject = channel.unary_unary(
        '/grpcinterface.BTrDB/FaultInject',
        request_serializer=btrdb__pb2.FaultInjectParams.SerializeToString,
        response_deserializer=btrdb__pb2.FaultInjectResponse.FromString,
        )
    self.Flush = channel.unary_unary(
        '/grpcinterface.BTrDB/Flush',
        request_serializer=btrdb__pb2.FlushParams.SerializeToString,
        response_deserializer=btrdb__pb2.FlushResponse.FromString,
        )
    self.Obliterate = channel.unary_unary(
        '/grpcinterface.BTrDB/Obliterate',
        request_serializer=btrdb__pb2.ObliterateParams.SerializeToString,
        response_deserializer=btrdb__pb2.ObliterateResponse.FromString,
        )
    self.GetMetadataUsage = channel.unary_unary(
        '/grpcinterface.BTrDB/GetMetadataUsage',
        request_serializer=btrdb__pb2.MetadataUsageParams.SerializeToString,
        response_deserializer=btrdb__pb2.MetadataUsageResponse.FromString,
        )
    self.GenerateCSV = channel.unary_stream(
        '/grpcinterface.BTrDB/GenerateCSV',
        request_serializer=btrdb__pb2.GenerateCSVParams.SerializeToString,
        response_deserializer=btrdb__pb2.GenerateCSVResponse.FromString,
        )
    self.SQLQuery = channel.unary_stream(
        '/grpcinterface.BTrDB/SQLQuery',
        request_serializer=btrdb__pb2.SQLQueryParams.SerializeToString,
        response_deserializer=btrdb__pb2.SQLQueryResponse.FromString,
        )


class BTrDBServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RawValues(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AlignedWindows(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Windows(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetStreamAnnotations(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetStreamTags(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListCollections(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LookupStreams(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Nearest(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Changes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Insert(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Info(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FaultInject(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Flush(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Obliterate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMetadataUsage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GenerateCSV(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SQLQuery(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BTrDBServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RawValues': grpc.unary_stream_rpc_method_handler(
          servicer.RawValues,
          request_deserializer=btrdb__pb2.RawValuesParams.FromString,
          response_serializer=btrdb__pb2.RawValuesResponse.SerializeToString,
      ),
      'AlignedWindows': grpc.unary_stream_rpc_method_handler(
          servicer.AlignedWindows,
          request_deserializer=btrdb__pb2.AlignedWindowsParams.FromString,
          response_serializer=btrdb__pb2.AlignedWindowsResponse.SerializeToString,
      ),
      'Windows': grpc.unary_stream_rpc_method_handler(
          servicer.Windows,
          request_deserializer=btrdb__pb2.WindowsParams.FromString,
          response_serializer=btrdb__pb2.WindowsResponse.SerializeToString,
      ),
      'StreamInfo': grpc.unary_unary_rpc_method_handler(
          servicer.StreamInfo,
          request_deserializer=btrdb__pb2.StreamInfoParams.FromString,
          response_serializer=btrdb__pb2.StreamInfoResponse.SerializeToString,
      ),
      'SetStreamAnnotations': grpc.unary_unary_rpc_method_handler(
          servicer.SetStreamAnnotations,
          request_deserializer=btrdb__pb2.SetStreamAnnotationsParams.FromString,
          response_serializer=btrdb__pb2.SetStreamAnnotationsResponse.SerializeToString,
      ),
      'SetStreamTags': grpc.unary_unary_rpc_method_handler(
          servicer.SetStreamTags,
          request_deserializer=btrdb__pb2.SetStreamTagsParams.FromString,
          response_serializer=btrdb__pb2.SetStreamTagsResponse.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=btrdb__pb2.CreateParams.FromString,
          response_serializer=btrdb__pb2.CreateResponse.SerializeToString,
      ),
      'ListCollections': grpc.unary_stream_rpc_method_handler(
          servicer.ListCollections,
          request_deserializer=btrdb__pb2.ListCollectionsParams.FromString,
          response_serializer=btrdb__pb2.ListCollectionsResponse.SerializeToString,
      ),
      'LookupStreams': grpc.unary_stream_rpc_method_handler(
          servicer.LookupStreams,
          request_deserializer=btrdb__pb2.LookupStreamsParams.FromString,
          response_serializer=btrdb__pb2.LookupStreamsResponse.SerializeToString,
      ),
      'Nearest': grpc.unary_unary_rpc_method_handler(
          servicer.Nearest,
          request_deserializer=btrdb__pb2.NearestParams.FromString,
          response_serializer=btrdb__pb2.NearestResponse.SerializeToString,
      ),
      'Changes': grpc.unary_stream_rpc_method_handler(
          servicer.Changes,
          request_deserializer=btrdb__pb2.ChangesParams.FromString,
          response_serializer=btrdb__pb2.ChangesResponse.SerializeToString,
      ),
      'Insert': grpc.unary_unary_rpc_method_handler(
          servicer.Insert,
          request_deserializer=btrdb__pb2.InsertParams.FromString,
          response_serializer=btrdb__pb2.InsertResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=btrdb__pb2.DeleteParams.FromString,
          response_serializer=btrdb__pb2.DeleteResponse.SerializeToString,
      ),
      'Info': grpc.unary_unary_rpc_method_handler(
          servicer.Info,
          request_deserializer=btrdb__pb2.InfoParams.FromString,
          response_serializer=btrdb__pb2.InfoResponse.SerializeToString,
      ),
      'FaultInject': grpc.unary_unary_rpc_method_handler(
          servicer.FaultInject,
          request_deserializer=btrdb__pb2.FaultInjectParams.FromString,
          response_serializer=btrdb__pb2.FaultInjectResponse.SerializeToString,
      ),
      'Flush': grpc.unary_unary_rpc_method_handler(
          servicer.Flush,
          request_deserializer=btrdb__pb2.FlushParams.FromString,
          response_serializer=btrdb__pb2.FlushResponse.SerializeToString,
      ),
      'Obliterate': grpc.unary_unary_rpc_method_handler(
          servicer.Obliterate,
          request_deserializer=btrdb__pb2.ObliterateParams.FromString,
          response_serializer=btrdb__pb2.ObliterateResponse.SerializeToString,
      ),
      'GetMetadataUsage': grpc.unary_unary_rpc_method_handler(
          servicer.GetMetadataUsage,
          request_deserializer=btrdb__pb2.MetadataUsageParams.FromString,
          response_serializer=btrdb__pb2.MetadataUsageResponse.SerializeToString,
      ),
      'GenerateCSV': grpc.unary_stream_rpc_method_handler(
          servicer.GenerateCSV,
          request_deserializer=btrdb__pb2.GenerateCSVParams.FromString,
          response_serializer=btrdb__pb2.GenerateCSVResponse.SerializeToString,
      ),
      'SQLQuery': grpc.unary_stream_rpc_method_handler(
          servicer.SQLQuery,
          request_deserializer=btrdb__pb2.SQLQueryParams.FromString,
          response_serializer=btrdb__pb2.SQLQueryResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpcinterface.BTrDB', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
