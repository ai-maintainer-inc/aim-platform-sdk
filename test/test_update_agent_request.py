# coding: utf-8

"""
    Platform API

    The AI Maintainer Platform API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import aim_platform_sdk
from aim_platform_sdk.models.update_agent_request import UpdateAgentRequest  # noqa: E501
from aim_platform_sdk.rest import ApiException

class TestUpdateAgentRequest(unittest.TestCase):
    """UpdateAgentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateAgentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateAgentRequest`
        """
        model = aim_platform_sdk.models.update_agent_request.UpdateAgentRequest()  # noqa: E501
        if include_optional :
            return UpdateAgentRequest(
                agent_id = None, 
                webhook_url = None, 
                webhook_secret = None
            )
        else :
            return UpdateAgentRequest(
                agent_id = None,
        )
        """

    def testUpdateAgentRequest(self):
        """Test UpdateAgentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
