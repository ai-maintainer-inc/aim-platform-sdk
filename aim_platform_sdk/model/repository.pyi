# coding: utf-8

"""
    Marketplace API

    An API for the AI Maintainer Marketplace  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from aim_platform_sdk import schemas  # noqa: F401


class Repository(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "createdAt",
            "ownerName",
            "repositoryId",
            "isPublic",
            "ownerId",
            "repositoryName",
            "updatedAt",
        }
        
        class properties:
            
            
            class repositoryId(
                schemas.UUIDBase,
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    format = 'uuid'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'repositoryId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class ownerId(
                schemas.UUIDBase,
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    format = 'uuid'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'ownerId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            ownerName = schemas.AnyTypeSchema
            repositoryName = schemas.AnyTypeSchema
            
            
            class createdAt(
                schemas.DateTimeBase,
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'createdAt':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class updatedAt(
                schemas.DateTimeBase,
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'updatedAt':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            isPublic = schemas.AnyTypeSchema
            __annotations__ = {
                "repositoryId": repositoryId,
                "ownerId": ownerId,
                "ownerName": ownerName,
                "repositoryName": repositoryName,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
                "isPublic": isPublic,
            }

    
    createdAt: MetaOapg.properties.createdAt
    ownerName: MetaOapg.properties.ownerName
    repositoryId: MetaOapg.properties.repositoryId
    isPublic: MetaOapg.properties.isPublic
    ownerId: MetaOapg.properties.ownerId
    repositoryName: MetaOapg.properties.repositoryName
    updatedAt: MetaOapg.properties.updatedAt
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repositoryId"]) -> MetaOapg.properties.repositoryId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerId"]) -> MetaOapg.properties.ownerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerName"]) -> MetaOapg.properties.ownerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repositoryName"]) -> MetaOapg.properties.repositoryName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPublic"]) -> MetaOapg.properties.isPublic: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["repositoryId", "ownerId", "ownerName", "repositoryName", "createdAt", "updatedAt", "isPublic", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repositoryId"]) -> MetaOapg.properties.repositoryId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerId"]) -> MetaOapg.properties.ownerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerName"]) -> MetaOapg.properties.ownerName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repositoryName"]) -> MetaOapg.properties.repositoryName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPublic"]) -> MetaOapg.properties.isPublic: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["repositoryId", "ownerId", "ownerName", "repositoryName", "createdAt", "updatedAt", "isPublic", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        createdAt: typing.Union[MetaOapg.properties.createdAt, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        ownerName: typing.Union[MetaOapg.properties.ownerName, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        repositoryId: typing.Union[MetaOapg.properties.repositoryId, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        isPublic: typing.Union[MetaOapg.properties.isPublic, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        ownerId: typing.Union[MetaOapg.properties.ownerId, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        repositoryName: typing.Union[MetaOapg.properties.repositoryName, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Repository':
        return super().__new__(
            cls,
            *_args,
            createdAt=createdAt,
            ownerName=ownerName,
            repositoryId=repositoryId,
            isPublic=isPublic,
            ownerId=ownerId,
            repositoryName=repositoryName,
            updatedAt=updatedAt,
            _configuration=_configuration,
            **kwargs,
        )
