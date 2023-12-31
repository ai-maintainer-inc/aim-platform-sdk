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
from aim_platform_sdk.models.benchmark_ticket import BenchmarkTicket  # noqa: E501
from aim_platform_sdk.rest import ApiException

class TestBenchmarkTicket(unittest.TestCase):
    """BenchmarkTicket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BenchmarkTicket
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BenchmarkTicket`
        """
        model = aim_platform_sdk.models.benchmark_ticket.BenchmarkTicket()  # noqa: E501
        if include_optional :
            return BenchmarkTicket(
                benchmark_ticket_id = None, 
                benchmark_id = None, 
                ticket_id = None, 
                agent_id = None, 
                attempt = None, 
                created_at = None, 
                updated_at = None
            )
        else :
            return BenchmarkTicket(
                benchmark_ticket_id = None,
                benchmark_id = None,
                ticket_id = None,
                agent_id = None,
                attempt = None,
                created_at = None,
                updated_at = None,
        )
        """

    def testBenchmarkTicket(self):
        """Test BenchmarkTicket"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
