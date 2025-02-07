# coding: utf-8

"""
    Hyperplane API Gateway

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from hyperplane_python_sdk.pydantic.models_persona_user import ModelsPersonaUser

class ModelsPersonaUsersResponse(BaseModel):
    # Top users belonging to this persona
    users: typing.List[ModelsPersonaUser] = Field(alias='users')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
