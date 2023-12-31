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
from aim_platform_sdk.models.code import Code

class CreateBenchmarkRequest(BaseModel):
    """
    CreateBenchmarkRequest
    """
    title: Optional[Any] = Field(..., description="A short title for the benchmark task.")
    description: Optional[Any] = Field(..., description="A longer description of the benchmark with detailed instructions.")
    link: Optional[Any] = Field(..., description="A link to the original benchmark design (e.g. github).")
    code: Code = Field(..., description="Information about the code repository associated with the benchmark.")
    public: Optional[Any] = Field(None, description="Optional. Defaults to false. Whether repository information is included in the benchmark.")
    difficulty: Optional[Any] = Field(..., description="The difficulty of the benchmark.")
    __properties = ["title", "description", "link", "code", "public", "difficulty"]

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
    def from_json(cls, json_str: str) -> CreateBenchmarkRequest:
        """Create an instance of CreateBenchmarkRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of code
        if self.code:
            _dict['code'] = self.code.to_dict()
        # set to None if title (nullable) is None
        # and __fields_set__ contains the field
        if self.title is None and "title" in self.__fields_set__:
            _dict['title'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if link (nullable) is None
        # and __fields_set__ contains the field
        if self.link is None and "link" in self.__fields_set__:
            _dict['link'] = None

        # set to None if public (nullable) is None
        # and __fields_set__ contains the field
        if self.public is None and "public" in self.__fields_set__:
            _dict['public'] = None

        # set to None if difficulty (nullable) is None
        # and __fields_set__ contains the field
        if self.difficulty is None and "difficulty" in self.__fields_set__:
            _dict['difficulty'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateBenchmarkRequest:
        """Create an instance of CreateBenchmarkRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateBenchmarkRequest.parse_obj(obj)

        _obj = CreateBenchmarkRequest.parse_obj({
            "title": obj.get("title"),
            "description": obj.get("description"),
            "link": obj.get("link"),
            "code": Code.from_dict(obj.get("code")) if obj.get("code") is not None else None,
            "public": obj.get("public"),
            "difficulty": obj.get("difficulty")
        })
        return _obj


