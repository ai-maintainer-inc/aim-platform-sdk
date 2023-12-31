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
from aim_platform_sdk.models.bid import Bid  # noqa: E501
from aim_platform_sdk.rest import ApiException

class TestBid(unittest.TestCase):
    """Bid unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Bid
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Bid`
        """
        model = aim_platform_sdk.models.bid.Bid()  # noqa: E501
        if include_optional :
            return Bid(
                operator_id = None, 
                bid_id = None, 
                ticket_id = None, 
                agent_id = None, 
                rate = None, 
                status = open, 
                created_at = None, 
                updated_at = None
            )
        else :
            return Bid(
                operator_id = None,
                bid_id = None,
                ticket_id = None,
                agent_id = None,
                rate = None,
                status = open,
                created_at = None,
                updated_at = None,
        )
        """

    def testBid(self):
        """Test Bid"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
