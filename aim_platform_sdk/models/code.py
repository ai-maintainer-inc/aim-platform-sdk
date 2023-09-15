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

class Code(BaseModel):
    """
    Information about where to find the code associated with a ticket or artifact.
    """
    owner: Optional[Any] = Field(..., description="The userName of the code repository owner.")
    repo: Optional[Any] = Field(..., description="The name of the code repository.")
    branch: Optional[Any] = Field(..., description="The name of the relevant branch in the code repository.")
    commit: Optional[Any] = Field(..., description="The commit hash of the relevant commit in the code repository.")
    __properties = ["owner", "repo", "branch", "commit"]

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
    def from_json(cls, json_str: str) -> Code:
        """Create an instance of Code from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if owner (nullable) is None
        # and __fields_set__ contains the field
        if self.owner is None and "owner" in self.__fields_set__:
            _dict['owner'] = None

        # set to None if repo (nullable) is None
        # and __fields_set__ contains the field
        if self.repo is None and "repo" in self.__fields_set__:
            _dict['repo'] = None

        # set to None if branch (nullable) is None
        # and __fields_set__ contains the field
        if self.branch is None and "branch" in self.__fields_set__:
            _dict['branch'] = None

        # set to None if commit (nullable) is None
        # and __fields_set__ contains the field
        if self.commit is None and "commit" in self.__fields_set__:
            _dict['commit'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Code:
        """Create an instance of Code from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Code.parse_obj(obj)

        _obj = Code.parse_obj({
            "owner": obj.get("owner"),
            "repo": obj.get("repo"),
            "branch": obj.get("branch"),
            "commit": obj.get("commit")
        })
        return _obj


