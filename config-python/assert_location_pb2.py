# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: assert_location.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='assert_location.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x61ssert_location.proto\"s\n\rassert_loc_v1\x12\x0b\n\x03lat\x18\x01 \x01(\x02\x12\x0b\n\x03lon\x18\x02 \x01(\x02\x12\r\n\x05owner\x18\x03 \x01(\t\x12\r\n\x05nonce\x18\x04 \x01(\x04\x12\x0b\n\x03\x66\x65\x65\x18\x05 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x06 \x01(\x04\x12\r\n\x05payer\x18\x07 \x01(\tb\x06proto3')
)




_ASSERT_LOC_V1 = _descriptor.Descriptor(
  name='assert_loc_v1',
  full_name='assert_loc_v1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='assert_loc_v1.lat', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon', full_name='assert_loc_v1.lon', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='assert_loc_v1.owner', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='assert_loc_v1.nonce', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee', full_name='assert_loc_v1.fee', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='assert_loc_v1.amount', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payer', full_name='assert_loc_v1.payer', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=25,
  serialized_end=140,
)

DESCRIPTOR.message_types_by_name['assert_loc_v1'] = _ASSERT_LOC_V1
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

assert_loc_v1 = _reflection.GeneratedProtocolMessageType('assert_loc_v1', (_message.Message,), dict(
  DESCRIPTOR = _ASSERT_LOC_V1,
  __module__ = 'assert_location_pb2'
  # @@protoc_insertion_point(class_scope:assert_loc_v1)
  ))
_sym_db.RegisterMessage(assert_loc_v1)


# @@protoc_insertion_point(module_scope)
