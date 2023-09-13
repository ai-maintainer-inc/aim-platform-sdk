# coding: utf-8

"""
    Marketplace API

    An API for the AI Maintainer Marketplace

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import aim_platform_sdk
from aim_platform_sdk.models.errors_response import ErrorsResponse  # noqa: E501
from aim_platform_sdk.rest import ApiException

class TestErrorsResponse(unittest.TestCase):
    """ErrorsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ErrorsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorsResponse`
        """
        model = aim_platform_sdk.models.errors_response.ErrorsResponse()  # noqa: E501
        if include_optional :
            return ErrorsResponse(
                errors = None
            )
        else :
            return ErrorsResponse(
                errors = None,
        )
        """

    def testErrorsResponse(self):
        """Test ErrorsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
