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


class BenchmarkTicket(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "createdAt",
            "agentId",
            "benchmarkTicketId",
            "attempt",
            "benchmarkId",
            "ticketId",
            "updatedAt",
        }
        
        class properties:
            
            
            class benchmarkTicketId(
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
                ) -> 'benchmarkTicketId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class benchmarkId(
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
                ) -> 'benchmarkId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class ticketId(
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
                ) -> 'ticketId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class agentId(
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
                ) -> 'agentId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            attempt = schemas.AnyTypeSchema
            
            
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
            __annotations__ = {
                "benchmarkTicketId": benchmarkTicketId,
                "benchmarkId": benchmarkId,
                "ticketId": ticketId,
                "agentId": agentId,
                "attempt": attempt,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
            }

    
    createdAt: MetaOapg.properties.createdAt
    agentId: MetaOapg.properties.agentId
    benchmarkTicketId: MetaOapg.properties.benchmarkTicketId
    attempt: MetaOapg.properties.attempt
    benchmarkId: MetaOapg.properties.benchmarkId
    ticketId: MetaOapg.properties.ticketId
    updatedAt: MetaOapg.properties.updatedAt
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["benchmarkTicketId"]) -> MetaOapg.properties.benchmarkTicketId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["benchmarkId"]) -> MetaOapg.properties.benchmarkId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ticketId"]) -> MetaOapg.properties.ticketId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agentId"]) -> MetaOapg.properties.agentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attempt"]) -> MetaOapg.properties.attempt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["benchmarkTicketId", "benchmarkId", "ticketId", "agentId", "attempt", "createdAt", "updatedAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["benchmarkTicketId"]) -> MetaOapg.properties.benchmarkTicketId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["benchmarkId"]) -> MetaOapg.properties.benchmarkId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ticketId"]) -> MetaOapg.properties.ticketId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agentId"]) -> MetaOapg.properties.agentId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attempt"]) -> MetaOapg.properties.attempt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["benchmarkTicketId", "benchmarkId", "ticketId", "agentId", "attempt", "createdAt", "updatedAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        createdAt: typing.Union[MetaOapg.properties.createdAt, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        agentId: typing.Union[MetaOapg.properties.agentId, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        benchmarkTicketId: typing.Union[MetaOapg.properties.benchmarkTicketId, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        attempt: typing.Union[MetaOapg.properties.attempt, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        benchmarkId: typing.Union[MetaOapg.properties.benchmarkId, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        ticketId: typing.Union[MetaOapg.properties.ticketId, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BenchmarkTicket':
        return super().__new__(
            cls,
            *_args,
            createdAt=createdAt,
            agentId=agentId,
            benchmarkTicketId=benchmarkTicketId,
            attempt=attempt,
            benchmarkId=benchmarkId,
            ticketId=ticketId,
            updatedAt=updatedAt,
            _configuration=_configuration,
            **kwargs,
        )