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

class Benchmark(BaseModel):
    """
    Benchmark
    """
    benchmark_id: Optional[Any] = Field(..., alias="benchmarkId", description="The Id of the benchmark.")
    title: Optional[Any] = Field(..., description="A short title for the benchmark task.")
    description: Optional[Any] = Field(..., description="A longer description of the benchmark with detailed instructions.")
    link: Optional[Any] = Field(..., description="A link to the original benchmark design (e.g. github).")
    author_id: Optional[Any] = Field(..., alias="authorId", description="The Id of the author of the benchmark.")
    author_name: Optional[Any] = Field(..., alias="authorName", description="The unique name of the author of the benchmark.")
    public: Optional[Any] = Field(..., description="Whether repository information is included in the benchmark.")
    code: Optional[Code] = Field(None, description="Information about the code repository associated with the benchmark.")
    difficulty: Optional[Any] = Field(..., description="The difficulty of the benchmark.")
    created_at: Optional[Any] = Field(..., alias="createdAt", description="The date and time the benchmark was created.")
    updated_at: Optional[Any] = Field(..., alias="updatedAt", description="The date and time the benchmark was last updated.")
    __properties = ["benchmarkId", "title", "description", "link", "authorId", "authorName", "public", "code", "difficulty", "createdAt", "updatedAt"]

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
    def from_json(cls, json_str: str) -> Benchmark:
        """Create an instance of Benchmark from a JSON string"""
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
        # set to None if benchmark_id (nullable) is None
        # and __fields_set__ contains the field
        if self.benchmark_id is None and "benchmark_id" in self.__fields_set__:
            _dict['benchmarkId'] = None

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

        # set to None if author_id (nullable) is None
        # and __fields_set__ contains the field
        if self.author_id is None and "author_id" in self.__fields_set__:
            _dict['authorId'] = None

        # set to None if author_name (nullable) is None
        # and __fields_set__ contains the field
        if self.author_name is None and "author_name" in self.__fields_set__:
            _dict['authorName'] = None

        # set to None if public (nullable) is None
        # and __fields_set__ contains the field
        if self.public is None and "public" in self.__fields_set__:
            _dict['public'] = None

        # set to None if difficulty (nullable) is None
        # and __fields_set__ contains the field
        if self.difficulty is None and "difficulty" in self.__fields_set__:
            _dict['difficulty'] = None

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
    def from_dict(cls, obj: dict) -> Benchmark:
        """Create an instance of Benchmark from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Benchmark.parse_obj(obj)

        _obj = Benchmark.parse_obj({
            "benchmark_id": obj.get("benchmarkId"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "link": obj.get("link"),
            "author_id": obj.get("authorId"),
            "author_name": obj.get("authorName"),
            "public": obj.get("public"),
            "code": Code.from_dict(obj.get("code")) if obj.get("code") is not None else None,
            "difficulty": obj.get("difficulty"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj


