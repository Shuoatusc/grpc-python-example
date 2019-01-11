# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TransferService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TransferService.proto',
  package='com.example.grpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15TransferService.proto\x12\x10\x63om.example.grpc\"]\n\x0fTransferRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ity\x18\x02 \x01(\t\x12\x10\n\x08zip_code\x18\x03 \x01(\x05\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x03(\t\x12\x0b\n\x03ssn\x18\x05 \x01(\x05\"+\n\x10TransferResponse\x12\x17\n\x0freceived_notice\x18\x01 \x01(\t2d\n\x0fTransferService\x12Q\n\x08transfer\x12!.com.example.grpc.TransferRequest\x1a\".com.example.grpc.TransferResponseb\x06proto3')
)




_TRANSFERREQUEST = _descriptor.Descriptor(
  name='TransferRequest',
  full_name='com.example.grpc.TransferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='com.example.grpc.TransferRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='city', full_name='com.example.grpc.TransferRequest.city', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zip_code', full_name='com.example.grpc.TransferRequest.zip_code', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='com.example.grpc.TransferRequest.address', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ssn', full_name='com.example.grpc.TransferRequest.ssn', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=136,
)


_TRANSFERRESPONSE = _descriptor.Descriptor(
  name='TransferResponse',
  full_name='com.example.grpc.TransferResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='received_notice', full_name='com.example.grpc.TransferResponse.received_notice', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['TransferRequest'] = _TRANSFERREQUEST
DESCRIPTOR.message_types_by_name['TransferResponse'] = _TRANSFERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransferRequest = _reflection.GeneratedProtocolMessageType('TransferRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERREQUEST,
  __module__ = 'TransferService_pb2'
  # @@protoc_insertion_point(class_scope:com.example.grpc.TransferRequest)
  ))
_sym_db.RegisterMessage(TransferRequest)

TransferResponse = _reflection.GeneratedProtocolMessageType('TransferResponse', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERRESPONSE,
  __module__ = 'TransferService_pb2'
  # @@protoc_insertion_point(class_scope:com.example.grpc.TransferResponse)
  ))
_sym_db.RegisterMessage(TransferResponse)



_TRANSFERSERVICE = _descriptor.ServiceDescriptor(
  name='TransferService',
  full_name='com.example.grpc.TransferService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=183,
  serialized_end=283,
  methods=[
  _descriptor.MethodDescriptor(
    name='transfer',
    full_name='com.example.grpc.TransferService.transfer',
    index=0,
    containing_service=None,
    input_type=_TRANSFERREQUEST,
    output_type=_TRANSFERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSFERSERVICE)

DESCRIPTOR.services_by_name['TransferService'] = _TRANSFERSERVICE

# @@protoc_insertion_point(module_scope)
