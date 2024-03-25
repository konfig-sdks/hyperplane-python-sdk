# coding: utf-8

"""
    Hyperplane API Gateway

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
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

from hyperplane_python_sdk import schemas  # noqa: F401


class ModelsNumericalAttributeFilter(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Definition of a filter on an attribute of numerical type.
    """


    class MetaOapg:
        required = {
            "min_value",
            "max_value",
        }
        
        class properties:
            max_value = schemas.NumberSchema
            min_value = schemas.NumberSchema
            __annotations__ = {
                "max_value": max_value,
                "min_value": min_value,
            }
    
    min_value: MetaOapg.properties.min_value
    max_value: MetaOapg.properties.max_value
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_value"]) -> MetaOapg.properties.max_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min_value"]) -> MetaOapg.properties.min_value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["max_value", "min_value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_value"]) -> MetaOapg.properties.max_value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min_value"]) -> MetaOapg.properties.min_value: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["max_value", "min_value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        min_value: typing.Union[MetaOapg.properties.min_value, decimal.Decimal, int, float, ],
        max_value: typing.Union[MetaOapg.properties.max_value, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelsNumericalAttributeFilter':
        return super().__new__(
            cls,
            *args,
            min_value=min_value,
            max_value=max_value,
            _configuration=_configuration,
            **kwargs,
        )
