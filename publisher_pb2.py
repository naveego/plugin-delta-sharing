# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: publisher.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fpublisher.proto\x12\x03pub\"f\n\x0c\x44\x61taVersions\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x18\n\x10job_data_version\x18\x02 \x01(\r\x12\x10\n\x08shape_id\x18\x03 \x01(\t\x12\x1a\n\x12shape_data_version\x18\x04 \x01(\r\"\xaf\x01\n\x10\x43onfigureRequest\x12 \n\tlog_level\x18\x01 \x01(\x0e\x32\r.pub.LogLevel\x12\x15\n\rlog_directory\x18\x02 \x01(\t\x12\x1b\n\x13permanent_directory\x18\x03 \x01(\t\x12\x1b\n\x13temporary_directory\x18\x04 \x01(\t\x12(\n\rdata_versions\x18\x05 \x01(\x0b\x32\x11.pub.DataVersions\"\x13\n\x11\x43onfigureResponse\"\xa1\x01\n\x0e\x43onnectRequest\x12\x15\n\rsettings_json\x18\x02 \x01(\t\x12\x34\n\x13oauth_configuration\x18\x03 \x01(\x0b\x32\x17.pub.OAuthConfiguration\x12\x18\n\x10oauth_state_json\x18\x04 \x01(\t\x12(\n\rdata_versions\x18\x05 \x01(\x0b\x32\x11.pub.DataVersions\"r\n\x0f\x43onnectResponse\x12\x16\n\x0esettings_error\x18\x01 \x01(\t\x12\x18\n\x10\x63onnection_error\x18\x02 \x01(\t\x12\x13\n\x0boauth_error\x18\x03 \x01(\t\x12\x18\n\x10oauth_state_json\x18\x04 \x01(\t\"\xed\x01\n\x0bReadRequest\x12\x1b\n\x06schema\x18\x01 \x01(\x0b\x32\x0b.pub.Schema\x12\r\n\x05limit\x18\x02 \x01(\r\x12#\n\x07\x66ilters\x18\x03 \x03(\x0b\x32\x12.pub.PublishFilter\x12\x1f\n\x17real_time_settings_json\x18\x06 \x01(\t\x12\x1c\n\x14real_time_state_json\x18\x07 \x01(\t\x12\x0e\n\x06job_id\x18\x08 \x01(\t\x12\x14\n\x0c\x64\x61ta_version\x18\t \x01(\r\x12(\n\rdata_versions\x18\n \x01(\x0b\x32\x11.pub.DataVersions\"\x8f\x01\n\rPublishFilter\x12%\n\x04kind\x18\x01 \x01(\x0e\x32\x17.pub.PublishFilter.Kind\x12\x13\n\x0bproperty_id\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"3\n\x04Kind\x12\n\n\x06\x45QUALS\x10\x00\x12\r\n\tLESS_THAN\x10\x01\x12\x10\n\x0cGREATER_THAN\x10\x02\"\x9c\x01\n\x16\x44iscoverSchemasRequest\x12.\n\x04mode\x18\x01 \x01(\x0e\x32 .pub.DiscoverSchemasRequest.Mode\x12\x1f\n\nto_refresh\x18\x02 \x03(\x0b\x32\x0b.pub.Schema\x12\x13\n\x0bsample_size\x18\x04 \x01(\r\"\x1c\n\x04Mode\x12\x07\n\x03\x41LL\x10\x00\x12\x0b\n\x07REFRESH\x10\x01\"7\n\x17\x44iscoverSchemasResponse\x12\x1c\n\x07schemas\x18\x01 \x03(\x0b\x32\x0b.pub.Schema\"\xc4\x02\n\x06Schema\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12!\n\nproperties\x18\x04 \x03(\x0b\x32\r.pub.Property\x12\x19\n\x05\x63ount\x18\x05 \x01(\x0b\x32\n.pub.Count\x12\x1b\n\x06sample\x18\x06 \x03(\x0b\x32\x0b.pub.Record\x12\r\n\x05query\x18\x07 \x01(\t\x12\x1b\n\x13publisher_meta_json\x18\x08 \x01(\t\x12\x0e\n\x06\x65rrors\x18\t \x03(\t\x12:\n\x13\x64\x61ta_flow_direction\x18\n \x01(\x0e\x32\x1d.pub.Schema.DataFlowDirection\"8\n\x11\x44\x61taFlowDirection\x12\x08\n\x04READ\x10\x00\x12\t\n\x05WRITE\x10\x01\x12\x0e\n\nREAD_WRITE\x10\x02\"g\n\x05\x43ount\x12\x1d\n\x04kind\x18\x01 \x01(\x0e\x32\x0f.pub.Count.Kind\x12\r\n\x05value\x18\x02 \x01(\x05\"0\n\x04Kind\x12\x0f\n\x0bUNAVAILABLE\x10\x00\x12\x0c\n\x08\x45STIMATE\x10\x01\x12\t\n\x05\x45XACT\x10\x02\"\xea\x01\n\x08Property\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x1f\n\x04type\x18\x04 \x01(\x0e\x32\x11.pub.PropertyType\x12\x0e\n\x06is_key\x18\x05 \x01(\x08\x12\x19\n\x11is_create_counter\x18\x06 \x01(\x08\x12\x19\n\x11is_update_counter\x18\x07 \x01(\x08\x12\x1b\n\x13publisher_meta_json\x18\x08 \x01(\t\x12\x16\n\x0etype_at_source\x18\t \x01(\t\x12\x13\n\x0bis_nullable\x18\n \x01(\x08\"\x13\n\x11\x44isconnectRequest\"\x14\n\x12\x44isconnectResponse\"\x93\x02\n\x06Record\x12\"\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x12.pub.Record.Action\x12\x11\n\tdata_json\x18\x02 \x01(\t\x12\x1c\n\x14real_time_state_json\x18\x03 \x01(\t\x12\r\n\x05\x63\x61use\x18\x04 \x01(\t\x12\x16\n\x0e\x63orrelation_id\x18\x05 \x01(\t\x12\x11\n\trecord_id\x18\x06 \x01(\t\x12$\n\x08versions\x18\x07 \x03(\x0b\x32\x12.pub.RecordVersion\"T\n\x06\x41\x63tion\x12\n\n\x06UPSERT\x10\x00\x12\n\n\x06INSERT\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\x12\x1a\n\x16REAL_TIME_STATE_COMMIT\x10\x04\"\x89\x01\n\rRecordVersion\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12\x11\n\tschema_id\x18\x03 \x01(\t\x12\x11\n\trecord_id\x18\x04 \x01(\t\x12\x11\n\tdata_json\x18\x05 \x01(\t\x12\x18\n\x10schema_data_json\x18\x06 \x01(\t\"D\n\x15\x43onfigureQueryRequest\x12+\n\x04\x66orm\x18\x01 \x01(\x0b\x32\x1d.pub.ConfigurationFormRequest\"c\n\x16\x43onfigureQueryResponse\x12,\n\x04\x66orm\x18\x01 \x01(\x0b\x32\x1e.pub.ConfigurationFormResponse\x12\x1b\n\x06schema\x18\x02 \x01(\x0b\x32\x0b.pub.Schema\"w\n\x1a\x43onfigureConnectionRequest\x12+\n\x04\x66orm\x18\x01 \x01(\x0b\x32\x1d.pub.ConfigurationFormRequest\x12,\n\x0f\x63onnect_request\x18\x02 \x01(\x0b\x32\x13.pub.ConnectRequest\"{\n\x1b\x43onfigureConnectionResponse\x12,\n\x04\x66orm\x18\x01 \x01(\x0b\x32\x1e.pub.ConfigurationFormResponse\x12.\n\x10\x63onnect_response\x18\x02 \x01(\x0b\x32\x14.pub.ConnectResponse\"d\n\x18\x43onfigureRealTimeRequest\x12+\n\x04\x66orm\x18\x01 \x01(\x0b\x32\x1d.pub.ConfigurationFormRequest\x12\x1b\n\x06schema\x18\x02 \x01(\x0b\x32\x0b.pub.Schema\"I\n\x19\x43onfigureRealTimeResponse\x12,\n\x04\x66orm\x18\x01 \x01(\x0b\x32\x1e.pub.ConfigurationFormResponse\"R\n\x18\x43onfigurationFormRequest\x12\x11\n\tdata_json\x18\x01 \x01(\t\x12\x12\n\nstate_json\x18\x02 \x01(\t\x12\x0f\n\x07is_save\x18\x03 \x01(\x08\"\x92\x01\n\x19\x43onfigurationFormResponse\x12\x13\n\x0bschema_json\x18\x01 \x01(\t\x12\x0f\n\x07ui_json\x18\x02 \x01(\t\x12\x12\n\nstate_json\x18\x03 \x01(\t\x12\x11\n\tdata_json\x18\x04 \x01(\t\x12\x18\n\x10\x64\x61ta_errors_json\x18\x05 \x01(\t\x12\x0e\n\x06\x65rrors\x18\x06 \x03(\t\"]\n\x15\x42\x65ginOAuthFlowRequest\x12.\n\rconfiguration\x18\x01 \x01(\x0b\x32\x17.pub.OAuthConfiguration\x12\x14\n\x0credirect_url\x18\x02 \x01(\t\"3\n\x16\x42\x65ginOAuthFlowResponse\x12\x19\n\x11\x61uthorization_url\x18\x01 \x01(\t\"w\n\x18\x43ompleteOAuthFlowRequest\x12.\n\rconfiguration\x18\x01 \x01(\x0b\x32\x17.pub.OAuthConfiguration\x12\x14\n\x0credirect_url\x18\x02 \x01(\t\x12\x15\n\rredirect_body\x18\x03 \x01(\t\"Z\n\x12OAuthConfiguration\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x15\n\rclient_secret\x18\x02 \x01(\t\x12\x1a\n\x12\x63onfiguration_json\x18\x03 \x01(\t\"5\n\x19\x43ompleteOAuthFlowResponse\x12\x18\n\x10oauth_state_json\x18\x01 \x01(\t\"D\n\x15\x43onfigureWriteRequest\x12+\n\x04\x66orm\x18\x01 \x01(\x0b\x32\x1d.pub.ConfigurationFormRequest\"c\n\x16\x43onfigureWriteResponse\x12,\n\x04\x66orm\x18\x01 \x01(\x0b\x32\x1e.pub.ConfigurationFormResponse\x12\x1b\n\x06schema\x18\x02 \x01(\x0b\x32\x0b.pub.Schema\"\x97\x01\n\x1b\x43onfigureReplicationRequest\x12+\n\x04\x66orm\x18\x01 \x01(\x0b\x32\x1d.pub.ConfigurationFormRequest\x12\x1b\n\x06schema\x18\x02 \x01(\x0b\x32\x0b.pub.Schema\x12.\n\x08versions\x18\x03 \x03(\x0b\x32\x1c.pub.ReplicationWriteVersion\"L\n\x1c\x43onfigureReplicationResponse\x12,\n\x04\x66orm\x18\x01 \x01(\x0b\x32\x1e.pub.ConfigurationFormResponse\"\xab\x01\n\x13PrepareWriteRequest\x12\x1a\n\x12\x63ommit_sla_seconds\x18\x01 \x01(\x05\x12\x1b\n\x06schema\x18\x02 \x01(\x0b\x32\x0b.pub.Schema\x12\x31\n\x0breplication\x18\x03 \x01(\x0b\x32\x1c.pub.ReplicationWriteRequest\x12(\n\rdata_versions\x18\x04 \x01(\x0b\x32\x11.pub.DataVersions\"`\n\x17ReplicationWriteRequest\x12.\n\x08versions\x18\x01 \x03(\x0b\x32\x1c.pub.ReplicationWriteVersion\x12\x15\n\rsettings_json\x18\x02 \x01(\t\"\xd4\x02\n\x17ReplicationWriteVersion\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x17\n\x0f\x63onnection_name\x18\x02 \x01(\t\x12\x0e\n\x06job_id\x18\x03 \x01(\t\x12\x10\n\x08job_name\x18\x04 \x01(\t\x12\x11\n\tschema_id\x18\x05 \x01(\t\x12\x13\n\x0bschema_name\x18\x06 \x01(\t\x12g\n\x1f\x63\x61ptured_schema_data_properties\x18\x07 \x03(\x0b\x32>.pub.ReplicationWriteVersion.CapturedSchemaDataPropertiesEntry\x1aV\n!CapturedSchemaDataPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0e\x32\x11.pub.PropertyType:\x02\x38\x01\"\x16\n\x14PrepareWriteResponse\"2\n\tRecordAck\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"@\n\x1e\x44iscoverRelatedEntitiesRequest\x12\x1e\n\tto_relate\x18\x01 \x03(\x0b\x32\x0b.pub.Schema\"O\n\x1f\x44iscoverRelatedEntitiesResponse\x12,\n\x10related_entities\x18\x01 \x03(\x0b\x32\x12.pub.RelatedEntity\"\x9f\x01\n\rRelatedEntity\x12\x11\n\tschema_id\x18\x01 \x01(\t\x12\x17\n\x0fsource_resource\x18\x02 \x01(\t\x12\x15\n\rsource_column\x18\x03 \x01(\t\x12\x18\n\x10\x66oreign_resource\x18\x04 \x01(\t\x12\x16\n\x0e\x66oreign_column\x18\x05 \x01(\t\x12\x19\n\x11relationship_name\x18\x06 \x01(\t*?\n\x08LogLevel\x12\t\n\x05\x45rror\x10\x00\x12\x08\n\x04Warn\x10\x01\x12\x08\n\x04Info\x10\x02\x12\t\n\x05\x44\x65\x62ug\x10\x03\x12\t\n\x05Trace\x10\x04*\x92\x01\n\x0cPropertyType\x12\n\n\x06STRING\x10\x00\x12\x08\n\x04\x42OOL\x10\x02\x12\x0b\n\x07INTEGER\x10\x03\x12\t\n\x05\x46LOAT\x10\x04\x12\x0b\n\x07\x44\x45\x43IMAL\x10\x05\x12\x08\n\x04\x44\x41TE\x10\x06\x12\x08\n\x04TIME\x10\x07\x12\x0c\n\x08\x44\x41TETIME\x10\x08\x12\x08\n\x04TEXT\x10\t\x12\x08\n\x04\x42LOB\x10\n\x12\x08\n\x04JSON\x10\x0b\x12\x07\n\x03XML\x10\x0c\x32\x83\x0b\n\tPublisher\x12<\n\tConfigure\x12\x15.pub.ConfigureRequest\x1a\x16.pub.ConfigureResponse\"\x00\x12\x36\n\x07\x43onnect\x12\x13.pub.ConnectRequest\x1a\x14.pub.ConnectResponse\"\x00\x12?\n\x0e\x43onnectSession\x12\x13.pub.ConnectRequest\x1a\x14.pub.ConnectResponse\"\x00\x30\x01\x12P\n\x0e\x44iscoverShapes\x12\x1b.pub.DiscoverSchemasRequest\x1a\x1c.pub.DiscoverSchemasResponse\"\x03\x88\x02\x01\x12N\n\x0f\x44iscoverSchemas\x12\x1b.pub.DiscoverSchemasRequest\x1a\x1c.pub.DiscoverSchemasResponse\"\x00\x12\x45\n\x15\x44iscoverSchemasStream\x12\x1b.pub.DiscoverSchemasRequest\x1a\x0b.pub.Schema\"\x00\x30\x01\x12\x35\n\rPublishStream\x12\x10.pub.ReadRequest\x1a\x0b.pub.Record\"\x03\x88\x02\x01\x30\x01\x12/\n\nReadStream\x12\x10.pub.ReadRequest\x1a\x0b.pub.Record\"\x00\x30\x01\x12?\n\nDisconnect\x12\x16.pub.DisconnectRequest\x1a\x17.pub.DisconnectResponse\"\x00\x12Z\n\x13\x43onfigureConnection\x12\x1f.pub.ConfigureConnectionRequest\x1a .pub.ConfigureConnectionResponse\"\x00\x12K\n\x0e\x43onfigureQuery\x12\x1a.pub.ConfigureQueryRequest\x1a\x1b.pub.ConfigureQueryResponse\"\x00\x12T\n\x11\x43onfigureRealTime\x12\x1d.pub.ConfigureRealTimeRequest\x1a\x1e.pub.ConfigureRealTimeResponse\"\x00\x12K\n\x0e\x42\x65ginOAuthFlow\x12\x1a.pub.BeginOAuthFlowRequest\x1a\x1b.pub.BeginOAuthFlowResponse\"\x00\x12T\n\x11\x43ompleteOAuthFlow\x12\x1d.pub.CompleteOAuthFlowRequest\x1a\x1e.pub.CompleteOAuthFlowResponse\"\x00\x12K\n\x0e\x43onfigureWrite\x12\x1a.pub.ConfigureWriteRequest\x1a\x1b.pub.ConfigureWriteResponse\"\x00\x12]\n\x14\x43onfigureReplication\x12 .pub.ConfigureReplicationRequest\x1a!.pub.ConfigureReplicationResponse\"\x00\x12\x45\n\x0cPrepareWrite\x12\x18.pub.PrepareWriteRequest\x1a\x19.pub.PrepareWriteResponse\"\x00\x12\x30\n\x0bWriteStream\x12\x0b.pub.Record\x1a\x0e.pub.RecordAck\"\x00(\x01\x30\x01\x12\x66\n\x17\x44iscoverRelatedEntities\x12#.pub.DiscoverRelatedEntitiesRequest\x1a$.pub.DiscoverRelatedEntitiesResponse\"\x00\x42 Z\x05./pub\xaa\x02\x16\x41unalytics.Sdk.Pluginsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'publisher_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\005./pub\252\002\026Aunalytics.Sdk.Plugins'
  _REPLICATIONWRITEVERSION_CAPTUREDSCHEMADATAPROPERTIESENTRY._options = None
  _REPLICATIONWRITEVERSION_CAPTUREDSCHEMADATAPROPERTIESENTRY._serialized_options = b'8\001'
  _PUBLISHER.methods_by_name['DiscoverShapes']._options = None
  _PUBLISHER.methods_by_name['DiscoverShapes']._serialized_options = b'\210\002\001'
  _PUBLISHER.methods_by_name['PublishStream']._options = None
  _PUBLISHER.methods_by_name['PublishStream']._serialized_options = b'\210\002\001'
  _LOGLEVEL._serialized_start=4985
  _LOGLEVEL._serialized_end=5048
  _PROPERTYTYPE._serialized_start=5051
  _PROPERTYTYPE._serialized_end=5197
  _DATAVERSIONS._serialized_start=24
  _DATAVERSIONS._serialized_end=126
  _CONFIGUREREQUEST._serialized_start=129
  _CONFIGUREREQUEST._serialized_end=304
  _CONFIGURERESPONSE._serialized_start=306
  _CONFIGURERESPONSE._serialized_end=325
  _CONNECTREQUEST._serialized_start=328
  _CONNECTREQUEST._serialized_end=489
  _CONNECTRESPONSE._serialized_start=491
  _CONNECTRESPONSE._serialized_end=605
  _READREQUEST._serialized_start=608
  _READREQUEST._serialized_end=845
  _PUBLISHFILTER._serialized_start=848
  _PUBLISHFILTER._serialized_end=991
  _PUBLISHFILTER_KIND._serialized_start=940
  _PUBLISHFILTER_KIND._serialized_end=991
  _DISCOVERSCHEMASREQUEST._serialized_start=994
  _DISCOVERSCHEMASREQUEST._serialized_end=1150
  _DISCOVERSCHEMASREQUEST_MODE._serialized_start=1122
  _DISCOVERSCHEMASREQUEST_MODE._serialized_end=1150
  _DISCOVERSCHEMASRESPONSE._serialized_start=1152
  _DISCOVERSCHEMASRESPONSE._serialized_end=1207
  _SCHEMA._serialized_start=1210
  _SCHEMA._serialized_end=1534
  _SCHEMA_DATAFLOWDIRECTION._serialized_start=1478
  _SCHEMA_DATAFLOWDIRECTION._serialized_end=1534
  _COUNT._serialized_start=1536
  _COUNT._serialized_end=1639
  _COUNT_KIND._serialized_start=1591
  _COUNT_KIND._serialized_end=1639
  _PROPERTY._serialized_start=1642
  _PROPERTY._serialized_end=1876
  _DISCONNECTREQUEST._serialized_start=1878
  _DISCONNECTREQUEST._serialized_end=1897
  _DISCONNECTRESPONSE._serialized_start=1899
  _DISCONNECTRESPONSE._serialized_end=1919
  _RECORD._serialized_start=1922
  _RECORD._serialized_end=2197
  _RECORD_ACTION._serialized_start=2113
  _RECORD_ACTION._serialized_end=2197
  _RECORDVERSION._serialized_start=2200
  _RECORDVERSION._serialized_end=2337
  _CONFIGUREQUERYREQUEST._serialized_start=2339
  _CONFIGUREQUERYREQUEST._serialized_end=2407
  _CONFIGUREQUERYRESPONSE._serialized_start=2409
  _CONFIGUREQUERYRESPONSE._serialized_end=2508
  _CONFIGURECONNECTIONREQUEST._serialized_start=2510
  _CONFIGURECONNECTIONREQUEST._serialized_end=2629
  _CONFIGURECONNECTIONRESPONSE._serialized_start=2631
  _CONFIGURECONNECTIONRESPONSE._serialized_end=2754
  _CONFIGUREREALTIMEREQUEST._serialized_start=2756
  _CONFIGUREREALTIMEREQUEST._serialized_end=2856
  _CONFIGUREREALTIMERESPONSE._serialized_start=2858
  _CONFIGUREREALTIMERESPONSE._serialized_end=2931
  _CONFIGURATIONFORMREQUEST._serialized_start=2933
  _CONFIGURATIONFORMREQUEST._serialized_end=3015
  _CONFIGURATIONFORMRESPONSE._serialized_start=3018
  _CONFIGURATIONFORMRESPONSE._serialized_end=3164
  _BEGINOAUTHFLOWREQUEST._serialized_start=3166
  _BEGINOAUTHFLOWREQUEST._serialized_end=3259
  _BEGINOAUTHFLOWRESPONSE._serialized_start=3261
  _BEGINOAUTHFLOWRESPONSE._serialized_end=3312
  _COMPLETEOAUTHFLOWREQUEST._serialized_start=3314
  _COMPLETEOAUTHFLOWREQUEST._serialized_end=3433
  _OAUTHCONFIGURATION._serialized_start=3435
  _OAUTHCONFIGURATION._serialized_end=3525
  _COMPLETEOAUTHFLOWRESPONSE._serialized_start=3527
  _COMPLETEOAUTHFLOWRESPONSE._serialized_end=3580
  _CONFIGUREWRITEREQUEST._serialized_start=3582
  _CONFIGUREWRITEREQUEST._serialized_end=3650
  _CONFIGUREWRITERESPONSE._serialized_start=3652
  _CONFIGUREWRITERESPONSE._serialized_end=3751
  _CONFIGUREREPLICATIONREQUEST._serialized_start=3754
  _CONFIGUREREPLICATIONREQUEST._serialized_end=3905
  _CONFIGUREREPLICATIONRESPONSE._serialized_start=3907
  _CONFIGUREREPLICATIONRESPONSE._serialized_end=3983
  _PREPAREWRITEREQUEST._serialized_start=3986
  _PREPAREWRITEREQUEST._serialized_end=4157
  _REPLICATIONWRITEREQUEST._serialized_start=4159
  _REPLICATIONWRITEREQUEST._serialized_end=4255
  _REPLICATIONWRITEVERSION._serialized_start=4258
  _REPLICATIONWRITEVERSION._serialized_end=4598
  _REPLICATIONWRITEVERSION_CAPTUREDSCHEMADATAPROPERTIESENTRY._serialized_start=4512
  _REPLICATIONWRITEVERSION_CAPTUREDSCHEMADATAPROPERTIESENTRY._serialized_end=4598
  _PREPAREWRITERESPONSE._serialized_start=4600
  _PREPAREWRITERESPONSE._serialized_end=4622
  _RECORDACK._serialized_start=4624
  _RECORDACK._serialized_end=4674
  _DISCOVERRELATEDENTITIESREQUEST._serialized_start=4676
  _DISCOVERRELATEDENTITIESREQUEST._serialized_end=4740
  _DISCOVERRELATEDENTITIESRESPONSE._serialized_start=4742
  _DISCOVERRELATEDENTITIESRESPONSE._serialized_end=4821
  _RELATEDENTITY._serialized_start=4824
  _RELATEDENTITY._serialized_end=4983
  _PUBLISHER._serialized_start=5200
  _PUBLISHER._serialized_end=6611
# @@protoc_insertion_point(module_scope)
