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

class TicketsResponse(BaseModel):
    """
    TicketsResponse
    """
    tickets: Optional[Any] = Field(...)
    __properties = ["tickets"]

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
    def from_json(cls, json_str: str) -> TicketsResponse:
        """Create an instance of TicketsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if tickets (nullable) is None
        # and __fields_set__ contains the field
        if self.tickets is None and "tickets" in self.__fields_set__:
            _dict['tickets'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TicketsResponse:
        """Create an instance of TicketsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TicketsResponse.parse_obj(obj)

        _obj = TicketsResponse.parse_obj({
            "tickets": obj.get("tickets")
        })
        return _obj


