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


class ModelsPersonaUsersResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Response of users linked to a given persona
    """


    class MetaOapg:
        required = {
            "users",
        }
        
        class properties:
            
            
            class users(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ModelsPersonaUser']:
                        return ModelsPersonaUser
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ModelsPersonaUser'], typing.List['ModelsPersonaUser']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'users':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ModelsPersonaUser':
                    return super().__getitem__(i)
            __annotations__ = {
                "users": users,
            }
    
    users: MetaOapg.properties.users
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["users"]) -> MetaOapg.properties.users: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["users", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["users"]) -> MetaOapg.properties.users: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["users", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        users: typing.Union[MetaOapg.properties.users, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelsPersonaUsersResponse':
        return super().__new__(
            cls,
            *args,
            users=users,
            _configuration=_configuration,
            **kwargs,
        )

from hyperplane_python_sdk.model.models_persona_user import ModelsPersonaUser
