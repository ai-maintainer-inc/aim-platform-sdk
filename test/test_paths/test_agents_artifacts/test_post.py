# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import aim_platform_sdk
from aim_platform_sdk.paths.agents_artifacts import post  # noqa: E501
from aim_platform_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestAgentsArtifacts(ApiTestMixin, unittest.TestCase):
    """
    AgentsArtifacts unit test stubs
        Submit an artifact for a ticket with an agent  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 201






if __name__ == '__main__':
    unittest.main()
