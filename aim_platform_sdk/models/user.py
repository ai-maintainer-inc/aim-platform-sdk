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

class User(BaseModel):
    """
    User
    """
    user_id: Optional[Any] = Field(..., alias="userId", description="The Id of the user.")
    user_name: Optional[Any] = Field(..., alias="userName", description="The unique name of the user.")
    email: Optional[Any] = Field(..., description="The email address of the user.")
    created_at: Optional[Any] = Field(..., alias="createdAt", description="The date and time the user was created.")
    updated_at: Optional[Any] = Field(..., alias="updatedAt", description="The date and time the user was last updated.")
    __properties = ["userId", "userName", "email", "createdAt", "updatedAt"]

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
    def from_json(cls, json_str: str) -> User:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id is None and "user_id" in self.__fields_set__:
            _dict['userId'] = None

        # set to None if user_name (nullable) is None
        # and __fields_set__ contains the field
        if self.user_name is None and "user_name" in self.__fields_set__:
            _dict['userName'] = None

        # set to None if email (nullable) is None
        # and __fields_set__ contains the field
        if self.email is None and "email" in self.__fields_set__:
            _dict['email'] = None

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
    def from_dict(cls, obj: dict) -> User:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return User.parse_obj(obj)

        _obj = User.parse_obj({
            "user_id": obj.get("userId"),
            "user_name": obj.get("userName"),
            "email": obj.get("email"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj


