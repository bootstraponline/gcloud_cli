"""Generated client library for monitoring version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.monitoring.v1 import monitoring_v1_messages as messages


class MonitoringV1(base_api.BaseApiClient):
  """Generated client library for service monitoring version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://monitoring.googleapis.com/'
  MTLS_BASE_URL = 'https://monitoring.mtls.googleapis.com/'

  _PACKAGE = 'monitoring'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/monitoring', 'https://www.googleapis.com/auth/monitoring.read', 'https://www.googleapis.com/auth/monitoring.write']
  _VERSION = 'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'MonitoringV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new monitoring handle."""
    url = url or self.BASE_URL
    super(MonitoringV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_dashboards = self.ProjectsDashboardsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsDashboardsService(base_api.BaseApiService):
    """Service class for the projects_dashboards resource."""

    _NAME = 'projects_dashboards'

    def __init__(self, client):
      super(MonitoringV1.ProjectsDashboardsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new custom dashboard. For examples on how you can use this API to create dashboards, see Managing dashboards by API. This method requires the monitoring.dashboards.create permission on the specified project. For more information about permissions, see Cloud Identity and Access Management.

      Args:
        request: (MonitoringProjectsDashboardsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Dashboard) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/dashboards',
        http_method='POST',
        method_id='monitoring.projects.dashboards.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/dashboards',
        request_field='dashboard',
        request_type_name='MonitoringProjectsDashboardsCreateRequest',
        response_type_name='Dashboard',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes an existing custom dashboard.This method requires the monitoring.dashboards.delete permission on the specified dashboard. For more information, see Google Cloud IAM (https://cloud.google.com/iam).

      Args:
        request: (MonitoringProjectsDashboardsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/dashboards/{dashboardsId}',
        http_method='DELETE',
        method_id='monitoring.projects.dashboards.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='MonitoringProjectsDashboardsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Fetches a specific dashboard.This method requires the monitoring.dashboards.get permission on the specified dashboard. For more information, see Google Cloud IAM (https://cloud.google.com/iam).

      Args:
        request: (MonitoringProjectsDashboardsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Dashboard) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/dashboards/{dashboardsId}',
        http_method='GET',
        method_id='monitoring.projects.dashboards.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='MonitoringProjectsDashboardsGetRequest',
        response_type_name='Dashboard',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists the existing dashboards.This method requires the monitoring.dashboards.list permission on the specified project. For more information, see Google Cloud IAM (https://cloud.google.com/iam).

      Args:
        request: (MonitoringProjectsDashboardsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDashboardsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/dashboards',
        http_method='GET',
        method_id='monitoring.projects.dashboards.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/dashboards',
        request_field='',
        request_type_name='MonitoringProjectsDashboardsListRequest',
        response_type_name='ListDashboardsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Replaces an existing custom dashboard with a new definition.This method requires the monitoring.dashboards.update permission on the specified dashboard. For more information, see Google Cloud IAM (https://cloud.google.com/iam).

      Args:
        request: (MonitoringProjectsDashboardsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Dashboard) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/dashboards/{dashboardsId}',
        http_method='PATCH',
        method_id='monitoring.projects.dashboards.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='dashboard',
        request_type_name='MonitoringProjectsDashboardsPatchRequest',
        response_type_name='Dashboard',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(MonitoringV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
