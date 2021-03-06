# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class RegistrationStateOperations(object):
    """RegistrationStateOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to use for the request. Supported versions include: 2018-04-01. Constant value: "2018-04-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config
        self.api_version = "2018-04-01"

    def get_registration_state(
            self, id, custom_headers=None, raw=False, **operation_config):
        """Gets the device registration state.

        :param id: Registration ID.
        :type id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeviceRegistrationState or ClientRawResponse if raw=true
        :rtype: ~serviceswagger.models.DeviceRegistrationState or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ProvisioningServiceErrorDetailsException<serviceswagger.models.ProvisioningServiceErrorDetailsException>`
        """
        # Construct URL
        url = '/registrations/{id}'
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200, 400, 401, 404, 429, 500]:
            raise models.ProvisioningServiceErrorDetailsException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeviceRegistrationState', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def delete_registration_state(
            self, id, if_match=None, custom_headers=None, raw=False, **operation_config):
        """Deletes the device registration.

        :param id: Registration ID.
        :type id: str
        :param if_match: The ETag of the registration status record.
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ProvisioningServiceErrorDetailsException<serviceswagger.models.ProvisioningServiceErrorDetailsException>`
        """
        # Construct URL
        url = '/registrations/{id}'
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [204, 400, 401, 404, 409, 412, 429, 500]:
            raise models.ProvisioningServiceErrorDetailsException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def query_registration_state(
            self, id, custom_headers=None, raw=False, **operation_config):
        """Gets the registration state of devices in this enrollmentGroup.

        :param id: Enrollment group ID.
        :type id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~serviceswagger.models.DeviceRegistrationState] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ProvisioningServiceErrorDetailsException<serviceswagger.models.ProvisioningServiceErrorDetailsException>`
        """
        # Construct URL
        url = '/registrations/{id}/query'
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200, 400, 401, 404, 429, 500]:
            raise models.ProvisioningServiceErrorDetailsException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[DeviceRegistrationState]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
