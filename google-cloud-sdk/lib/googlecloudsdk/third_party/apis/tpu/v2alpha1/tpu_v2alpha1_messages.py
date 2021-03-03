"""Generated message classes for tpu version v2alpha1.

TPU API provides customers with access to Google TPU technology.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'tpu'


class AcceleratorType(_messages.Message):
  r"""A accelerator type that a Node can be configured with.

  Fields:
    name: The resource name.
    type: the accelerator type.
  """

  name = _messages.StringField(1)
  type = _messages.StringField(2)


class AccessConfig(_messages.Message):
  r"""An access config attached to the TPU worker.

  Fields:
    externalIp: Output only. An external IP address associated with the TPU
      worker.
  """

  externalIp = _messages.StringField(1)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); } The JSON
  representation for `Empty` is empty JSON object `{}`.
  """



class ListAcceleratorTypesResponse(_messages.Message):
  r"""Response for ListAcceleratorTypes.

  Fields:
    acceleratorTypes: The listed nodes.
    nextPageToken: The next page token or empty if none.
    unreachable: Locations that could not be reached.
  """

  acceleratorTypes = _messages.MessageField('AcceleratorType', 1, repeated=True)
  nextPageToken = _messages.StringField(2)
  unreachable = _messages.StringField(3, repeated=True)


class ListLocationsResponse(_messages.Message):
  r"""The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListNodesResponse(_messages.Message):
  r"""Response for ListNodes.

  Fields:
    nextPageToken: The next page token or empty if none.
    nodes: The listed nodes.
    unreachable: Locations that could not be reached.
  """

  nextPageToken = _messages.StringField(1)
  nodes = _messages.MessageField('Node', 2, repeated=True)
  unreachable = _messages.StringField(3, repeated=True)


class ListOperationsResponse(_messages.Message):
  r"""The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class ListRuntimeVersionsResponse(_messages.Message):
  r"""Response for ListRuntimeVersions.

  Fields:
    nextPageToken: The next page token or empty if none.
    runtimeVersions: The listed nodes.
    unreachable: Locations that could not be reached.
  """

  nextPageToken = _messages.StringField(1)
  runtimeVersions = _messages.MessageField('RuntimeVersion', 2, repeated=True)
  unreachable = _messages.StringField(3, repeated=True)


class Location(_messages.Message):
  r"""A resource that represents Google Cloud Platform location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    displayName: The friendly name for this location, typically a nearby city
      name. For example, "Tokyo".
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  displayName = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  locationId = _messages.StringField(3)
  metadata = _messages.MessageField('MetadataValue', 4)
  name = _messages.StringField(5)


class NetworkConfig(_messages.Message):
  r"""Network related configurations.

  Fields:
    enableExternalIps: Indicates that external IP addresses would be
      associated with the TPU workers. If set to false, the specified
      subnetwork or network should have Private Google Access enabled.
    network: The name of the network for the TPU node. It must be a
      preexisting Google Compute Engine network. If none is provided,
      "default" will be used.
    subnetwork: The name of the subnetwork for the TPU node. It must be a
      preexisting Google Compute Engine subnetwork. If none is provided,
      "default" will be used.
  """

  enableExternalIps = _messages.BooleanField(1)
  network = _messages.StringField(2)
  subnetwork = _messages.StringField(3)


class NetworkEndpoint(_messages.Message):
  r"""A network endpoint over which a TPU worker can be reached.

  Fields:
    accessConfig: The access config for the TPU worker.
    ipAddress: The internal IP address of this network endpoint.
    port: The port of this network endpoint.
  """

  accessConfig = _messages.MessageField('AccessConfig', 1)
  ipAddress = _messages.StringField(2)
  port = _messages.IntegerField(3, variant=_messages.Variant.INT32)


class Node(_messages.Message):
  r"""A TPU instance.

  Enums:
    ApiVersionValueValuesEnum: Output only. The API version that created this
      Node.
    HealthValueValuesEnum: The health status of the TPU node.
    StateValueValuesEnum: Output only. The current state for the TPU Node.

  Messages:
    LabelsValue: Resource labels to represent user-provided metadata.
    MetadataValue: Custom metadata to apply to the TPU Node. Can set startup-
      script and shutdown-script

  Fields:
    acceleratorType: Required. The type of hardware accelerators associated
      with this node.
    apiVersion: Output only. The API version that created this Node.
    cidrBlock: The CIDR block that the TPU node will use when selecting an IP
      address. This CIDR block must be a /29 block; the Compute Engine
      networks API forbids a smaller block, and using a larger block would be
      wasteful (a node can only consume one IP address). Errors will occur if
      the CIDR block has already been used for a currently existing TPU node,
      the CIDR block conflicts with any subnetworks in the user's provided
      network, or the provided network is peered with another network that is
      using that CIDR block.
    createTime: Output only. The time when the node was created.
    description: The user-supplied description of the TPU. Maximum of 512
      characters.
    health: The health status of the TPU node.
    healthDescription: Output only. If this field is populated, it contains a
      description of why the TPU Node is unhealthy.
    id: Output only. The unique identifier for the TPU Node.
    labels: Resource labels to represent user-provided metadata.
    metadata: Custom metadata to apply to the TPU Node. Can set startup-script
      and shutdown-script
    name: Output only. Immutable. The name of the TPU.
    networkConfig: Network configurations for the TPU node.
    networkEndpoints: Output only. The network endpoints where TPU workers can
      be accessed and sent work. It is recommended that runtime clients of the
      node reach out to the 0th entry in this map first.
    runtimeVersion: Required. The runtime version running in the Node.
    schedulingConfig: The scheduling options for this node.
    serviceAccount: The Google Cloud Platform Service Account to be used by
      the TPU node VMs. If None is specified, the default compute service
      account will be used.
    state: Output only. The current state for the TPU Node.
    symptoms: Output only. The Symptoms that have occurred to the TPU Node.
    tags: Tags to apply to the TPU Node. Tags are used to identify valid
      sources or targets for network firewalls.
    useTpuVm: Output only.
  """

  class ApiVersionValueValuesEnum(_messages.Enum):
    r"""Output only. The API version that created this Node.

    Values:
      API_VERSION_UNSPECIFIED: API version is unknown.
      V1_ALPHA1: TPU API V1Alpha1 version.
      V1: TPU API V1 version.
      V2_ALPHA1: TPU API V2Alpha1 version.
    """
    API_VERSION_UNSPECIFIED = 0
    V1_ALPHA1 = 1
    V1 = 2
    V2_ALPHA1 = 3

  class HealthValueValuesEnum(_messages.Enum):
    r"""The health status of the TPU node.

    Values:
      HEALTH_UNSPECIFIED: Health status is unknown: not initialized or failed
        to retrieve.
      HEALTHY: The resource is healthy.
      TIMEOUT: The resource is unresponsive.
      UNHEALTHY_TENSORFLOW: The in-guest ML stack is unhealthy.
      UNHEALTHY_MAINTENANCE: The node is under maintenance/priority boost
        caused rescheduling and will resume running once rescheduled.
    """
    HEALTH_UNSPECIFIED = 0
    HEALTHY = 1
    TIMEOUT = 2
    UNHEALTHY_TENSORFLOW = 3
    UNHEALTHY_MAINTENANCE = 4

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. The current state for the TPU Node.

    Values:
      STATE_UNSPECIFIED: TPU node state is not known/set.
      CREATING: TPU node is being created.
      READY: TPU node has been created and is fully usable.
      RESTARTING: TPU node is restarting.
      REIMAGING: TPU node is undergoing reimaging.
      DELETING: TPU node is being deleted.
      REPAIRING: TPU node is being repaired and may be unusable. Details can
        be found in the `help_description` field.
      STOPPED: TPU node is stopped.
      STOPPING: TPU node is currently stopping.
      STARTING: TPU node is currently starting.
      PREEMPTED: TPU node has been preempted. Only applies to Preemptible TPU
        Nodes.
      TERMINATED: TPU node has been terminated due to maintenance or has
        reached the end of its life cycle (for preemptible nodes).
      HIDING: TPU node is currently hiding.
      HIDDEN: TPU node has been hidden.
      UNHIDING: TPU node is currently unhiding.
    """
    STATE_UNSPECIFIED = 0
    CREATING = 1
    READY = 2
    RESTARTING = 3
    REIMAGING = 4
    DELETING = 5
    REPAIRING = 6
    STOPPED = 7
    STOPPING = 8
    STARTING = 9
    PREEMPTED = 10
    TERMINATED = 11
    HIDING = 12
    HIDDEN = 13
    UNHIDING = 14

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Resource labels to represent user-provided metadata.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Custom metadata to apply to the TPU Node. Can set startup-script and
    shutdown-script

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Additional properties of type MetadataValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  acceleratorType = _messages.StringField(1)
  apiVersion = _messages.EnumField('ApiVersionValueValuesEnum', 2)
  cidrBlock = _messages.StringField(3)
  createTime = _messages.StringField(4)
  description = _messages.StringField(5)
  health = _messages.EnumField('HealthValueValuesEnum', 6)
  healthDescription = _messages.StringField(7)
  id = _messages.IntegerField(8)
  labels = _messages.MessageField('LabelsValue', 9)
  metadata = _messages.MessageField('MetadataValue', 10)
  name = _messages.StringField(11)
  networkConfig = _messages.MessageField('NetworkConfig', 12)
  networkEndpoints = _messages.MessageField('NetworkEndpoint', 13, repeated=True)
  runtimeVersion = _messages.StringField(14)
  schedulingConfig = _messages.MessageField('SchedulingConfig', 15)
  serviceAccount = _messages.MessageField('ServiceAccount', 16)
  state = _messages.EnumField('StateValueValuesEnum', 17)
  symptoms = _messages.MessageField('Symptom', 18, repeated=True)
  tags = _messages.StringField(19, repeated=True)
  useTpuVm = _messages.BooleanField(20)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success. If
      the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal response of the operation in case of success. If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation. It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata. Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success. If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`. If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource. For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name. For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OperationMetadata(_messages.Message):
  r"""Represents the metadata of the long-running operation.

  Fields:
    apiVersion: [Output only] API version used to start the operation.
    cancelRequested: [Output only] Identifies whether the user has requested
      cancellation of the operation. Operations that have successfully been
      cancelled have Operation.error value with a google.rpc.Status.code of 1,
      corresponding to `Code.CANCELLED`.
    createTime: [Output only] The time the operation was created.
    endTime: [Output only] The time the operation finished running.
    statusDetail: [Output only] Human-readable status of the operation, if
      any.
    target: [Output only] Server-defined resource path for the target of the
      operation.
    verb: [Output only] Name of the verb executed by the operation.
  """

  apiVersion = _messages.StringField(1)
  cancelRequested = _messages.BooleanField(2)
  createTime = _messages.StringField(3)
  endTime = _messages.StringField(4)
  statusDetail = _messages.StringField(5)
  target = _messages.StringField(6)
  verb = _messages.StringField(7)


class RuntimeVersion(_messages.Message):
  r"""A runtime version that a Node can be configured with.

  Fields:
    name: The resource name.
    version: The runtime version.
  """

  name = _messages.StringField(1)
  version = _messages.StringField(2)


class SchedulingConfig(_messages.Message):
  r"""Sets the scheduling options for this node.

  Fields:
    preemptible: Defines whether the node is preemptible.
    reserved: Whether the node is created under a reservation.
  """

  preemptible = _messages.BooleanField(1)
  reserved = _messages.BooleanField(2)


class ServiceAccount(_messages.Message):
  r"""A service account.

  Fields:
    email: Email address of the service account. If empty, default Compute
      service account will be used.
    scope: The list of scopes to be made available for this service account.
      If empty, access to all Cloud APIs will be allowed.
  """

  email = _messages.StringField(1)
  scope = _messages.StringField(2, repeated=True)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class StartNodeRequest(_messages.Message):
  r"""Request for StartNode."""


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details. You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details. There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class StopNodeRequest(_messages.Message):
  r"""Request for StopNode."""


class Symptom(_messages.Message):
  r"""A Symptom instance.

  Enums:
    SymptomTypeValueValuesEnum: Type of the Symptom.

  Fields:
    createTime: Timestamp when the Symptom is created.
    details: Detailed information of the current Symptom.
    symptomType: Type of the Symptom.
    workerId: A string used to uniquely distinguish a worker within a TPU
      node.
  """

  class SymptomTypeValueValuesEnum(_messages.Enum):
    r"""Type of the Symptom.

    Values:
      SYMPTOM_TYPE_UNSPECIFIED: Unspecified symptom.
      LOW_MEMORY: TPU VM memory is low.
      OUT_OF_MEMORY: TPU runtime is out of memory.
      EXECUTE_TIMED_OUT: TPU runtime execution has timed out.
      MESH_BUILD_FAIL: TPU runtime fails to construct a mesh that recognizes
        each TPU device's neighbors.
      HBM_OUT_OF_MEMORY: TPU HBM is out of memory.
      PROJECT_ABUSE: Abusive behaviors have been identified on the current
        project.
    """
    SYMPTOM_TYPE_UNSPECIFIED = 0
    LOW_MEMORY = 1
    OUT_OF_MEMORY = 2
    EXECUTE_TIMED_OUT = 3
    MESH_BUILD_FAIL = 4
    HBM_OUT_OF_MEMORY = 5
    PROJECT_ABUSE = 6

  createTime = _messages.StringField(1)
  details = _messages.StringField(2)
  symptomType = _messages.EnumField('SymptomTypeValueValuesEnum', 3)
  workerId = _messages.StringField(4)


class TpuProjectsLocationsAcceleratorTypesGetRequest(_messages.Message):
  r"""A TpuProjectsLocationsAcceleratorTypesGetRequest object.

  Fields:
    name: Required. The resource name.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsAcceleratorTypesListRequest(_messages.Message):
  r"""A TpuProjectsLocationsAcceleratorTypesListRequest object.

  Fields:
    filter: List filter.
    orderBy: Sort results.
    pageSize: The maximum number of items to return.
    pageToken: The next_page_token value returned from a previous List
      request, if any.
    parent: Required. The parent resource name.
  """

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)


class TpuProjectsLocationsGetRequest(_messages.Message):
  r"""A TpuProjectsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsListRequest(_messages.Message):
  r"""A TpuProjectsLocationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The resource that owns the locations collection, if applicable.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class TpuProjectsLocationsNodesCreateRequest(_messages.Message):
  r"""A TpuProjectsLocationsNodesCreateRequest object.

  Fields:
    node: A Node resource to be passed as the request body.
    nodeId: The unqualified resource name.
    parent: Required. The parent resource name.
  """

  node = _messages.MessageField('Node', 1)
  nodeId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class TpuProjectsLocationsNodesDeleteRequest(_messages.Message):
  r"""A TpuProjectsLocationsNodesDeleteRequest object.

  Fields:
    name: Required. The resource name.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsNodesGetRequest(_messages.Message):
  r"""A TpuProjectsLocationsNodesGetRequest object.

  Fields:
    name: Required. The resource name.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsNodesListRequest(_messages.Message):
  r"""A TpuProjectsLocationsNodesListRequest object.

  Fields:
    pageSize: The maximum number of items to return.
    pageToken: The next_page_token value returned from a previous List
      request, if any.
    parent: Required. The parent resource name.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class TpuProjectsLocationsNodesPatchRequest(_messages.Message):
  r"""A TpuProjectsLocationsNodesPatchRequest object.

  Fields:
    name: Output only. Immutable. The name of the TPU.
    node: A Node resource to be passed as the request body.
    updateMask: Required. Mask of fields from Node to update. Supported
      fields: None.
  """

  name = _messages.StringField(1, required=True)
  node = _messages.MessageField('Node', 2)
  updateMask = _messages.StringField(3)


class TpuProjectsLocationsNodesStartRequest(_messages.Message):
  r"""A TpuProjectsLocationsNodesStartRequest object.

  Fields:
    name: The resource name.
    startNodeRequest: A StartNodeRequest resource to be passed as the request
      body.
  """

  name = _messages.StringField(1, required=True)
  startNodeRequest = _messages.MessageField('StartNodeRequest', 2)


class TpuProjectsLocationsNodesStopRequest(_messages.Message):
  r"""A TpuProjectsLocationsNodesStopRequest object.

  Fields:
    name: The resource name.
    stopNodeRequest: A StopNodeRequest resource to be passed as the request
      body.
  """

  name = _messages.StringField(1, required=True)
  stopNodeRequest = _messages.MessageField('StopNodeRequest', 2)


class TpuProjectsLocationsOperationsCancelRequest(_messages.Message):
  r"""A TpuProjectsLocationsOperationsCancelRequest object.

  Fields:
    name: The name of the operation resource to be cancelled.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsOperationsDeleteRequest(_messages.Message):
  r"""A TpuProjectsLocationsOperationsDeleteRequest object.

  Fields:
    name: The name of the operation resource to be deleted.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsOperationsGetRequest(_messages.Message):
  r"""A TpuProjectsLocationsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsOperationsListRequest(_messages.Message):
  r"""A TpuProjectsLocationsOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class TpuProjectsLocationsRuntimeVersionsGetRequest(_messages.Message):
  r"""A TpuProjectsLocationsRuntimeVersionsGetRequest object.

  Fields:
    name: Required. The resource name.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsRuntimeVersionsListRequest(_messages.Message):
  r"""A TpuProjectsLocationsRuntimeVersionsListRequest object.

  Fields:
    filter: List filter.
    orderBy: Sort results.
    pageSize: The maximum number of items to return.
    pageToken: The next_page_token value returned from a previous List
      request, if any.
    parent: Required. The parent resource name.
  """

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
