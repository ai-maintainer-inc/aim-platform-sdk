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

class CreateBidRequest(BaseModel):
    """
    CreateBidRequest
    """
    ticket_id: Optional[Any] = Field(..., alias="ticketId", description="The Id of the ticket the bid is for.")
    agent_id: Optional[Any] = Field(..., alias="agentId", description="The Id of the agent making the bid.")
    rate: Optional[Any] = Field(..., description="Unused.")
    __properties = ["ticketId", "agentId", "rate"]

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
    def from_json(cls, json_str: str) -> CreateBidRequest:
        """Create an instance of CreateBidRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if ticket_id (nullable) is None
        # and __fields_set__ contains the field
        if self.ticket_id is None and "ticket_id" in self.__fields_set__:
            _dict['ticketId'] = None

        # set to None if agent_id (nullable) is None
        # and __fields_set__ contains the field
        if self.agent_id is None and "agent_id" in self.__fields_set__:
            _dict['agentId'] = None

        # set to None if rate (nullable) is None
        # and __fields_set__ contains the field
        if self.rate is None and "rate" in self.__fields_set__:
            _dict['rate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateBidRequest:
        """Create an instance of CreateBidRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateBidRequest.parse_obj(obj)

        _obj = CreateBidRequest.parse_obj({
            "ticket_id": obj.get("ticketId"),
            "agent_id": obj.get("agentId"),
            "rate": obj.get("rate")
        })
        return _obj


