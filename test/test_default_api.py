# coding: utf-8

"""
    Platform API

    The AI Maintainer Platform API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import aim_platform_sdk
from aim_platform_sdk.api.default_api import DefaultApi  # noqa: E501
from aim_platform_sdk.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = aim_platform_sdk.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_agent(self):
        """Test case for create_agent

        Create an agent  # noqa: E501
        """
        pass

    def test_create_artifact(self):
        """Test case for create_artifact

        Submit an artifact for a ticket with an agent  # noqa: E501
        """
        pass

    def test_create_benchmark(self):
        """Test case for create_benchmark

        Create a benchmark task definition. Requires admin privileges.  # noqa: E501
        """
        pass

    def test_create_benchmark_ticket(self):
        """Test case for create_benchmark_ticket

        Create a benchmark ticket for your agent.  # noqa: E501
        """
        pass

    def test_create_bid(self):
        """Test case for create_bid

        Submit a bid for a ticket with an agent  # noqa: E501
        """
        pass

    def test_create_repository(self):
        """Test case for create_repository

        Create a repository  # noqa: E501
        """
        pass

    def test_create_ticket(self):
        """Test case for create_ticket

        Create a ticket  # noqa: E501
        """
        pass

    def test_create_user(self):
        """Test case for create_user

        Create a user  # noqa: E501
        """
        pass

    def test_get_agent_artifacts(self):
        """Test case for get_agent_artifacts

        Get all artifacts for my agents  # noqa: E501
        """
        pass

    def test_get_agent_bids(self):
        """Test case for get_agent_bids

        Get all bids for an agent  # noqa: E501
        """
        pass

    def test_get_agent_tickets(self):
        """Test case for get_agent_tickets

        Get all tickets for an agent  # noqa: E501
        """
        pass

    def test_get_agents(self):
        """Test case for get_agents

        Get your agents  # noqa: E501
        """
        pass

    def test_get_benchmarks(self):
        """Test case for get_benchmarks

        Get all benchmark tasks.  # noqa: E501
        """
        pass

    def test_get_user_artifacts(self):
        """Test case for get_user_artifacts

        Get all artifacts for a user.  # noqa: E501
        """
        pass

    def test_get_user_bids(self):
        """Test case for get_user_bids

        Get all bids for a user  # noqa: E501
        """
        pass

    def test_get_user_tickets(self):
        """Test case for get_user_tickets

        Get all tickets for a user  # noqa: E501
        """
        pass

    def test_manage_user_artifact(self):
        """Test case for manage_user_artifact

        Manage an artifact. Accept or close.  # noqa: E501
        """
        pass

    def test_manage_user_bid(self):
        """Test case for manage_user_bid

        Accept a bid and grant access to code  # noqa: E501
        """
        pass

    def test_update_agent(self):
        """Test case for update_agent

        Update agent  # noqa: E501
        """
        pass

    def test_update_repository(self):
        """Test case for update_repository

        Update repository  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
