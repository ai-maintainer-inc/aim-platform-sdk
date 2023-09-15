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
from pydantic import BaseModel, Field, validator

class ManageUserArtifactRequest(BaseModel):
    """
    ManageUserArtifactRequest
    """
    artifact_id: Optional[Any] = Field(..., alias="artifactId", description="The Id of the artifact.")
    action: Optional[Any] = Field(..., description="The action to take on the artifact.")
    __properties = ["artifactId", "action"]

    @validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('accept', 'close'):
            raise ValueError("must be one of enum values ('accept', 'close')")
        return value

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
    def from_json(cls, json_str: str) -> ManageUserArtifactRequest:
        """Create an instance of ManageUserArtifactRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if artifact_id (nullable) is None
        # and __fields_set__ contains the field
        if self.artifact_id is None and "artifact_id" in self.__fields_set__:
            _dict['artifactId'] = None

        # set to None if action (nullable) is None
        # and __fields_set__ contains the field
        if self.action is None and "action" in self.__fields_set__:
            _dict['action'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ManageUserArtifactRequest:
        """Create an instance of ManageUserArtifactRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ManageUserArtifactRequest.parse_obj(obj)

        _obj = ManageUserArtifactRequest.parse_obj({
            "artifact_id": obj.get("artifactId"),
            "action": obj.get("action")
        })
        return _obj


