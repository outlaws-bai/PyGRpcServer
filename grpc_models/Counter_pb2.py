# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Counter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rCounter.proto\x12\rorg.m2sec.rpc\"%\n\x06Header\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x82\x01\n\x07Request\x12\r\n\x05isSSL\x18\x01 \x01(\x08\x12\x13\n\x0bhttpVersion\x18\x02 \x01(\t\x12\x0e\n\x06method\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\t\x12%\n\x06header\x18\x05 \x03(\x0b\x32\x15.org.m2sec.rpc.Header\x12\x0f\n\x07\x63ontent\x18\x06 \x01(\x0c\"\xac\x01\n\x11RequestAndSetting\x12\'\n\x07request\x18\x01 \x01(\x0b\x32\x16.org.m2sec.rpc.Request\x12>\n\x07setting\x18\x02 \x03(\x0b\x32-.org.m2sec.rpc.RequestAndSetting.SettingEntry\x1a.\n\x0cSettingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"{\n\x08Response\x12\x13\n\x0bhttpVersion\x18\x01 \x01(\t\x12\x12\n\nstatusCode\x18\x02 \x01(\x05\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12%\n\x06header\x18\x04 \x03(\x0b\x32\x15.org.m2sec.rpc.Header\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\x0c\"\xb0\x01\n\x12ResponseAndSetting\x12)\n\x08response\x18\x01 \x01(\x0b\x32\x17.org.m2sec.rpc.Response\x12?\n\x07setting\x18\x02 \x03(\x0b\x32..org.m2sec.rpc.ResponseAndSetting.SettingEntry\x1a.\n\x0cSettingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\xd6\x02\n\x0e\x43ounterService\x12M\n\x11hookRequestToBurp\x12 .org.m2sec.rpc.RequestAndSetting\x1a\x16.org.m2sec.rpc.Request\x12O\n\x13hookRequestToServer\x12 .org.m2sec.rpc.RequestAndSetting\x1a\x16.org.m2sec.rpc.Request\x12P\n\x12hookResponseToBurp\x12!.org.m2sec.rpc.ResponseAndSetting\x1a\x17.org.m2sec.rpc.Response\x12R\n\x14hookResponseToClient\x12!.org.m2sec.rpc.ResponseAndSetting\x1a\x17.org.m2sec.rpc.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Counter_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _REQUESTANDSETTING_SETTINGENTRY._options = None
  _REQUESTANDSETTING_SETTINGENTRY._serialized_options = b'8\001'
  _RESPONSEANDSETTING_SETTINGENTRY._options = None
  _RESPONSEANDSETTING_SETTINGENTRY._serialized_options = b'8\001'
  _globals['_HEADER']._serialized_start=32
  _globals['_HEADER']._serialized_end=69
  _globals['_REQUEST']._serialized_start=72
  _globals['_REQUEST']._serialized_end=202
  _globals['_REQUESTANDSETTING']._serialized_start=205
  _globals['_REQUESTANDSETTING']._serialized_end=377
  _globals['_REQUESTANDSETTING_SETTINGENTRY']._serialized_start=331
  _globals['_REQUESTANDSETTING_SETTINGENTRY']._serialized_end=377
  _globals['_RESPONSE']._serialized_start=379
  _globals['_RESPONSE']._serialized_end=502
  _globals['_RESPONSEANDSETTING']._serialized_start=505
  _globals['_RESPONSEANDSETTING']._serialized_end=681
  _globals['_RESPONSEANDSETTING_SETTINGENTRY']._serialized_start=331
  _globals['_RESPONSEANDSETTING_SETTINGENTRY']._serialized_end=377
  _globals['_COUNTERSERVICE']._serialized_start=684
  _globals['_COUNTERSERVICE']._serialized_end=1026
# @@protoc_insertion_point(module_scope)