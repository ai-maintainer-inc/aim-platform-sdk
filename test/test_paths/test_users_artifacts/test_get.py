# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import aim_platform_sdk
from aim_platform_sdk.paths.users_artifacts import get  # noqa: E501
from aim_platform_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestUsersArtifacts(ApiTestMixin, unittest.TestCase):
    """
    UsersArtifacts unit test stubs
        Get all artifacts for a user.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
