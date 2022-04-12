# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from lightly.openapi_generated.swagger_client.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class DockerAuthorizationRequest(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'timestamp',
        'taskDescription',
    ))

    @classmethod
    @property
    def timestamp(cls) -> typing.Type['Timestamp']:
        return Timestamp

    @classmethod
    @property
    def taskDescription(cls) -> typing.Type['DockerTaskDescription']:
        return DockerTaskDescription


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        timestamp: timestamp,
        taskDescription: taskDescription,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'DockerAuthorizationRequest':
        return super().__new__(
            cls,
            *args,
            timestamp=timestamp,
            taskDescription=taskDescription,
            _configuration=_configuration,
            **kwargs,
        )

from lightly.openapi_generated.swagger_client.model.docker_task_description import DockerTaskDescription
from lightly.openapi_generated.swagger_client.model.timestamp import Timestamp