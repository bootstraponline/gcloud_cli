"""Generated client library for osconfig version v1alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.osconfig.v1alpha import osconfig_v1alpha_messages as messages


class OsconfigV1alpha(base_api.BaseApiClient):
  """Generated client library for service osconfig version v1alpha."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://osconfig.googleapis.com/'
  MTLS_BASE_URL = 'https://osconfig.mtls.googleapis.com/'

  _PACKAGE = 'osconfig'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'OsconfigV1alpha'
  _URL_VERSION = 'v1alpha'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new osconfig handle."""
    url = url or self.BASE_URL
    super(OsconfigV1alpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_instanceOSPoliciesCompliances = self.ProjectsLocationsInstanceOSPoliciesCompliancesService(self)
    self.projects_locations_instances_inventories = self.ProjectsLocationsInstancesInventoriesService(self)
    self.projects_locations_instances_vulnerabilityReports = self.ProjectsLocationsInstancesVulnerabilityReportsService(self)
    self.projects_locations_instances = self.ProjectsLocationsInstancesService(self)
    self.projects_locations_osPolicyAssignments_operations = self.ProjectsLocationsOsPolicyAssignmentsOperationsService(self)
    self.projects_locations_osPolicyAssignments = self.ProjectsLocationsOsPolicyAssignmentsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsInstanceOSPoliciesCompliancesService(base_api.BaseApiService):
    """Service class for the projects_locations_instanceOSPoliciesCompliances resource."""

    _NAME = 'projects_locations_instanceOSPoliciesCompliances'

    def __init__(self, client):
      super(OsconfigV1alpha.ProjectsLocationsInstanceOSPoliciesCompliancesService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Get OS policies compliance data for the specified Compute Engine instance.

      Args:
        request: (OsconfigProjectsLocationsInstanceOSPoliciesCompliancesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (InstanceOSPoliciesCompliance) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/instanceOSPoliciesCompliances/{instanceOSPoliciesCompliancesId}',
        http_method='GET',
        method_id='osconfig.projects.locations.instanceOSPoliciesCompliances.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsLocationsInstanceOSPoliciesCompliancesGetRequest',
        response_type_name='InstanceOSPoliciesCompliance',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List OS policies compliance data for all Compute Engine instances in the specified zone.

      Args:
        request: (OsconfigProjectsLocationsInstanceOSPoliciesCompliancesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListInstanceOSPoliciesCompliancesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/instanceOSPoliciesCompliances',
        http_method='GET',
        method_id='osconfig.projects.locations.instanceOSPoliciesCompliances.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/instanceOSPoliciesCompliances',
        request_field='',
        request_type_name='OsconfigProjectsLocationsInstanceOSPoliciesCompliancesListRequest',
        response_type_name='ListInstanceOSPoliciesCompliancesResponse',
        supports_download=False,
    )

  class ProjectsLocationsInstancesInventoriesService(base_api.BaseApiService):
    """Service class for the projects_locations_instances_inventories resource."""

    _NAME = 'projects_locations_instances_inventories'

    def __init__(self, client):
      super(OsconfigV1alpha.ProjectsLocationsInstancesInventoriesService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""List inventory data for all VM instances in the specified zone.

      Args:
        request: (OsconfigProjectsLocationsInstancesInventoriesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListInventoriesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}/inventories',
        http_method='GET',
        method_id='osconfig.projects.locations.instances.inventories.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken', 'view'],
        relative_path='v1alpha/{+parent}/inventories',
        request_field='',
        request_type_name='OsconfigProjectsLocationsInstancesInventoriesListRequest',
        response_type_name='ListInventoriesResponse',
        supports_download=False,
    )

  class ProjectsLocationsInstancesVulnerabilityReportsService(base_api.BaseApiService):
    """Service class for the projects_locations_instances_vulnerabilityReports resource."""

    _NAME = 'projects_locations_instances_vulnerabilityReports'

    def __init__(self, client):
      super(OsconfigV1alpha.ProjectsLocationsInstancesVulnerabilityReportsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""List vulnerability reports for all VM instances in the specified zone.

      Args:
        request: (OsconfigProjectsLocationsInstancesVulnerabilityReportsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListVulnerabilityReportsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}/vulnerabilityReports',
        http_method='GET',
        method_id='osconfig.projects.locations.instances.vulnerabilityReports.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/vulnerabilityReports',
        request_field='',
        request_type_name='OsconfigProjectsLocationsInstancesVulnerabilityReportsListRequest',
        response_type_name='ListVulnerabilityReportsResponse',
        supports_download=False,
    )

  class ProjectsLocationsInstancesService(base_api.BaseApiService):
    """Service class for the projects_locations_instances resource."""

    _NAME = 'projects_locations_instances'

    def __init__(self, client):
      super(OsconfigV1alpha.ProjectsLocationsInstancesService, self).__init__(client)
      self._upload_configs = {
          }

    def GetInventory(self, request, global_params=None):
      r"""Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

      Args:
        request: (OsconfigProjectsLocationsInstancesGetInventoryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Inventory) The response message.
      """
      config = self.GetMethodConfig('GetInventory')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetInventory.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}/inventory',
        http_method='GET',
        method_id='osconfig.projects.locations.instances.getInventory',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['view'],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsLocationsInstancesGetInventoryRequest',
        response_type_name='Inventory',
        supports_download=False,
    )

    def GetVulnerabilityReport(self, request, global_params=None):
      r"""Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

      Args:
        request: (OsconfigProjectsLocationsInstancesGetVulnerabilityReportRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (VulnerabilityReport) The response message.
      """
      config = self.GetMethodConfig('GetVulnerabilityReport')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetVulnerabilityReport.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}/vulnerabilityReport',
        http_method='GET',
        method_id='osconfig.projects.locations.instances.getVulnerabilityReport',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsLocationsInstancesGetVulnerabilityReportRequest',
        response_type_name='VulnerabilityReport',
        supports_download=False,
    )

  class ProjectsLocationsOsPolicyAssignmentsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_osPolicyAssignments_operations resource."""

    _NAME = 'projects_locations_osPolicyAssignments_operations'

    def __init__(self, client):
      super(OsconfigV1alpha.ProjectsLocationsOsPolicyAssignmentsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments/{osPolicyAssignmentsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='osconfig.projects.locations.osPolicyAssignments.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments/{osPolicyAssignmentsId}/operations/{operationsId}',
        http_method='GET',
        method_id='osconfig.projects.locations.osPolicyAssignments.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsOsPolicyAssignmentsService(base_api.BaseApiService):
    """Service class for the projects_locations_osPolicyAssignments resource."""

    _NAME = 'projects_locations_osPolicyAssignments'

    def __init__(self, client):
      super(OsconfigV1alpha.ProjectsLocationsOsPolicyAssignmentsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a new OS policy assignment. This also creates the first revision of the OS policy assignment. This method returns a long running operation(LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments',
        http_method='POST',
        method_id='osconfig.projects.locations.osPolicyAssignments.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['osPolicyAssignmentId'],
        relative_path='v1alpha/{+parent}/osPolicyAssignments',
        request_field='oSPolicyAssignment',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete the OS policy assignment. This creates a new revision of the OS policy assignment. This method returns a long running operation(LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO. If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments/{osPolicyAssignmentsId}',
        http_method='DELETE',
        method_id='osconfig.projects.locations.osPolicyAssignments.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Retrieve an existing OS policy assignment. This always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID. Format: projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}@{revisionId}.

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (OSPolicyAssignment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments/{osPolicyAssignmentsId}',
        http_method='GET',
        method_id='osconfig.projects.locations.osPolicyAssignments.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsGetRequest',
        response_type_name='OSPolicyAssignment',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List the OS policy assignments under the parent resource. For each OS policy assignment, the latest revision is returned.

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOSPolicyAssignmentsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments',
        http_method='GET',
        method_id='osconfig.projects.locations.osPolicyAssignments.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/osPolicyAssignments',
        request_field='',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsListRequest',
        response_type_name='ListOSPolicyAssignmentsResponse',
        supports_download=False,
    )

    def ListRevisions(self, request, global_params=None):
      r"""List the OS policy assignment revisions for a given OS policy assignment.

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsListRevisionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOSPolicyAssignmentRevisionsResponse) The response message.
      """
      config = self.GetMethodConfig('ListRevisions')
      return self._RunMethod(
          config, request, global_params=global_params)

    ListRevisions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments/{osPolicyAssignmentsId}:listRevisions',
        http_method='GET',
        method_id='osconfig.projects.locations.osPolicyAssignments.listRevisions',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}:listRevisions',
        request_field='',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsListRevisionsRequest',
        response_type_name='ListOSPolicyAssignmentRevisionsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update an existing OS policy assignment. This creates a new revision of the OS policy assignment. This method returns a long running operation(LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments/{osPolicyAssignmentsId}',
        http_method='PATCH',
        method_id='osconfig.projects.locations.osPolicyAssignments.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha/{+name}',
        request_field='oSPolicyAssignment',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(OsconfigV1alpha.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(OsconfigV1alpha.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
