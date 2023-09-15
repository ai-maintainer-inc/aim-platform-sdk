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
from aim_platform_sdk.models.create_artifact_request import CreateArtifactRequest  # noqa: E501
from aim_platform_sdk.rest import ApiException

class TestCreateArtifactRequest(unittest.TestCase):
    """CreateArtifactRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateArtifactRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateArtifactRequest`
        """
        model = aim_platform_sdk.models.create_artifact_request.CreateArtifactRequest()  # noqa: E501
        if include_optional :
            return CreateArtifactRequest(
                bid_id = None, 
                code = aim_platform_sdk.models.code.Code(
                    owner = null, 
                    repo = null, 
                    branch = null, 
                    commit = null, ), 
                draft = None
            )
        else :
            return CreateArtifactRequest(
                bid_id = None,
                code = aim_platform_sdk.models.code.Code(
                    owner = null, 
                    repo = null, 
                    branch = null, 
                    commit = null, ),
        )
        """

    def testCreateArtifactRequest(self):
        """Test CreateArtifactRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
