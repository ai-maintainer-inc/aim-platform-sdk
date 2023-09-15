# coding: utf-8

"""
    Platform API

    The AI Maintainer Platform API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, Field

class BenchmarkTicket(BaseModel):
    """
    BenchmarkTicket
    """
    benchmark_ticket_id: Optional[Any] = Field(..., alias="benchmarkTicketId", description="The Id of the benchmark ticket.")
    benchmark_id: Optional[Any] = Field(..., alias="benchmarkId", description="The Id of the benchmark.")
    ticket_id: Optional[Any] = Field(..., alias="ticketId", description="The Id of the ticket.")
    agent_id: Optional[Any] = Field(..., alias="agentId", description="The Id of the agent.")
    attempt: Optional[Any] = Field(..., description="The attempt number of the benchmark ticket.")
    created_at: Optional[Any] = Field(..., alias="createdAt", description="The date and time the benchmark ticket was created.")
    updated_at: Optional[Any] = Field(..., alias="updatedAt", description="The date and time the benchmark ticket was last updated.")
    __properties = ["benchmarkTicketId", "benchmarkId", "ticketId", "agentId", "attempt", "createdAt", "updatedAt"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BenchmarkTicket:
        """Create an instance of BenchmarkTicket from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if benchmark_ticket_id (nullable) is None
        # and __fields_set__ contains the field
        if self.benchmark_ticket_id is None and "benchmark_ticket_id" in self.__fields_set__:
            _dict['benchmarkTicketId'] = None

        # set to None if benchmark_id (nullable) is None
        # and __fields_set__ contains the field
        if self.benchmark_id is None and "benchmark_id" in self.__fields_set__:
            _dict['benchmarkId'] = None

        # set to None if ticket_id (nullable) is None
        # and __fields_set__ contains the field
        if self.ticket_id is None and "ticket_id" in self.__fields_set__:
            _dict['ticketId'] = None

        # set to None if agent_id (nullable) is None
        # and __fields_set__ contains the field
        if self.agent_id is None and "agent_id" in self.__fields_set__:
            _dict['agentId'] = None

        # set to None if attempt (nullable) is None
        # and __fields_set__ contains the field
        if self.attempt is None and "attempt" in self.__fields_set__:
            _dict['attempt'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['createdAt'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updatedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BenchmarkTicket:
        """Create an instance of BenchmarkTicket from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BenchmarkTicket.parse_obj(obj)

        _obj = BenchmarkTicket.parse_obj({
            "benchmark_ticket_id": obj.get("benchmarkTicketId"),
            "benchmark_id": obj.get("benchmarkId"),
            "ticket_id": obj.get("ticketId"),
            "agent_id": obj.get("agentId"),
            "attempt": obj.get("attempt"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj


