"""Generated client library for eventarc version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.eventarc.v1 import eventarc_v1_messages as messages


class EventarcV1(base_api.BaseApiClient):
  """Generated client library for service eventarc version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://eventarc.googleapis.com/'
  MTLS_BASE_URL = 'https://eventarc.mtls.googleapis.com/'

  _PACKAGE = 'eventarc'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'EventarcV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new eventarc handle."""
    url = url or self.BASE_URL
    super(EventarcV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_channels = self.ProjectsLocationsChannelsService(self)
    self.projects_locations_ingresses = self.ProjectsLocationsIngressesService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_triggers = self.ProjectsLocationsTriggersService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsChannelsService(base_api.BaseApiService):
    """Service class for the projects_locations_channels resource."""

    _NAME = 'projects_locations_channels'

    def __init__(self, client):
      super(EventarcV1.ProjectsLocationsChannelsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a new channel in a particular project and location.

      Args:
        request: (EventarcProjectsLocationsChannelsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/channels',
        http_method='POST',
        method_id='eventarc.projects.locations.channels.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['channelId', 'validateOnly'],
        relative_path='v1/{+parent}/channels',
        request_field='channel',
        request_type_name='EventarcProjectsLocationsChannelsCreateRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete a single channel.

      Args:
        request: (EventarcProjectsLocationsChannelsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/channels/{channelsId}',
        http_method='DELETE',
        method_id='eventarc.projects.locations.channels.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['validateOnly'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='EventarcProjectsLocationsChannelsDeleteRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get a single Channel.

      Args:
        request: (EventarcProjectsLocationsChannelsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Channel) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/channels/{channelsId}',
        http_method='GET',
        method_id='eventarc.projects.locations.channels.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='EventarcProjectsLocationsChannelsGetRequest',
        response_type_name='Channel',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List channels.

      Args:
        request: (EventarcProjectsLocationsChannelsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListChannelsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/channels',
        http_method='GET',
        method_id='eventarc.projects.locations.channels.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['orderBy', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/channels',
        request_field='',
        request_type_name='EventarcProjectsLocationsChannelsListRequest',
        response_type_name='ListChannelsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update a single channel.

      Args:
        request: (EventarcProjectsLocationsChannelsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/channels/{channelsId}',
        http_method='PATCH',
        method_id='eventarc.projects.locations.channels.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask', 'validateOnly'],
        relative_path='v1/{+name}',
        request_field='channel',
        request_type_name='EventarcProjectsLocationsChannelsPatchRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsLocationsIngressesService(base_api.BaseApiService):
    """Service class for the projects_locations_ingresses resource."""

    _NAME = 'projects_locations_ingresses'

    def __init__(self, client):
      super(EventarcV1.ProjectsLocationsIngressesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a new ingress in a particular project and location.

      Args:
        request: (EventarcProjectsLocationsIngressesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/ingresses',
        http_method='POST',
        method_id='eventarc.projects.locations.ingresses.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['ingressId', 'validateOnly'],
        relative_path='v1/{+parent}/ingresses',
        request_field='ingress',
        request_type_name='EventarcProjectsLocationsIngressesCreateRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete a single ingress.

      Args:
        request: (EventarcProjectsLocationsIngressesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/ingresses/{ingressesId}',
        http_method='DELETE',
        method_id='eventarc.projects.locations.ingresses.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['validateOnly'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='EventarcProjectsLocationsIngressesDeleteRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get a single Ingress.

      Args:
        request: (EventarcProjectsLocationsIngressesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Ingress) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/ingresses/{ingressesId}',
        http_method='GET',
        method_id='eventarc.projects.locations.ingresses.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='EventarcProjectsLocationsIngressesGetRequest',
        response_type_name='Ingress',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List ingresses.

      Args:
        request: (EventarcProjectsLocationsIngressesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListIngressesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/ingresses',
        http_method='GET',
        method_id='eventarc.projects.locations.ingresses.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['orderBy', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/ingresses',
        request_field='',
        request_type_name='EventarcProjectsLocationsIngressesListRequest',
        response_type_name='ListIngressesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update a single ingress.

      Args:
        request: (EventarcProjectsLocationsIngressesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/ingresses/{ingressesId}',
        http_method='PATCH',
        method_id='eventarc.projects.locations.ingresses.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask', 'validateOnly'],
        relative_path='v1/{+name}',
        request_field='ingress',
        request_type_name='EventarcProjectsLocationsIngressesPatchRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(EventarcV1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (EventarcProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='eventarc.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:cancel',
        request_field='googleLongrunningCancelOperationRequest',
        request_type_name='EventarcProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (EventarcProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='eventarc.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='EventarcProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (EventarcProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='eventarc.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='EventarcProjectsLocationsOperationsGetRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/*/operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

      Args:
        request: (EventarcProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='eventarc.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/operations',
        request_field='',
        request_type_name='EventarcProjectsLocationsOperationsListRequest',
        response_type_name='GoogleLongrunningListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsTriggersService(base_api.BaseApiService):
    """Service class for the projects_locations_triggers resource."""

    _NAME = 'projects_locations_triggers'

    def __init__(self, client):
      super(EventarcV1.ProjectsLocationsTriggersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a new trigger in a particular project and location.

      Args:
        request: (EventarcProjectsLocationsTriggersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/triggers',
        http_method='POST',
        method_id='eventarc.projects.locations.triggers.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['triggerId', 'validateOnly'],
        relative_path='v1/{+parent}/triggers',
        request_field='trigger',
        request_type_name='EventarcProjectsLocationsTriggersCreateRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete a single trigger.

      Args:
        request: (EventarcProjectsLocationsTriggersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/triggers/{triggersId}',
        http_method='DELETE',
        method_id='eventarc.projects.locations.triggers.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['allowMissing', 'etag', 'validateOnly'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='EventarcProjectsLocationsTriggersDeleteRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get a single trigger.

      Args:
        request: (EventarcProjectsLocationsTriggersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Trigger) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/triggers/{triggersId}',
        http_method='GET',
        method_id='eventarc.projects.locations.triggers.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='EventarcProjectsLocationsTriggersGetRequest',
        response_type_name='Trigger',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

      Args:
        request: (EventarcProjectsLocationsTriggersGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/triggers/{triggersId}:getIamPolicy',
        http_method='GET',
        method_id='eventarc.projects.locations.triggers.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=['options_requestedPolicyVersion'],
        relative_path='v1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name='EventarcProjectsLocationsTriggersGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List triggers.

      Args:
        request: (EventarcProjectsLocationsTriggersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTriggersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/triggers',
        http_method='GET',
        method_id='eventarc.projects.locations.triggers.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['orderBy', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/triggers',
        request_field='',
        request_type_name='EventarcProjectsLocationsTriggersListRequest',
        response_type_name='ListTriggersResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update a single trigger.

      Args:
        request: (EventarcProjectsLocationsTriggersPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/triggers/{triggersId}',
        http_method='PATCH',
        method_id='eventarc.projects.locations.triggers.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['allowMissing', 'updateMask', 'validateOnly'],
        relative_path='v1/{+name}',
        request_field='trigger',
        request_type_name='EventarcProjectsLocationsTriggersPatchRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

      Args:
        request: (EventarcProjectsLocationsTriggersSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/triggers/{triggersId}:setIamPolicy',
        http_method='POST',
        method_id='eventarc.projects.locations.triggers.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1/{+resource}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='EventarcProjectsLocationsTriggersSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

      Args:
        request: (EventarcProjectsLocationsTriggersTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/triggers/{triggersId}:testIamPermissions',
        http_method='POST',
        method_id='eventarc.projects.locations.triggers.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1/{+resource}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='EventarcProjectsLocationsTriggersTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(EventarcV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (EventarcProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='eventarc.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='EventarcProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (EventarcProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='eventarc.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/locations',
        request_field='',
        request_type_name='EventarcProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(EventarcV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
