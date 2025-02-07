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


class ModelsCategoryCashflow(BaseModel):
    # Aggregate amount for the given category
    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    # Human-friendly category name
    name: typing.Optional[str] = Field(None, alias='name')

    # Absolute amount flow for the category
    percentage: typing.Optional[typing.Union[int, float]] = Field(None, alias='percentage')

    # Human-friendly category taxonomy path
    taxonomy_path: typing.Optional[str] = Field(None, alias='taxonomy_path')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
