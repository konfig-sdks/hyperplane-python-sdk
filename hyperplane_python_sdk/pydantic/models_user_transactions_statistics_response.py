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


class ModelsUserTransactionsStatisticsResponse(BaseModel):
    # Number of transactions
    transaction_count: int = Field(alias='transaction_count')

    # Average transaction value
    average_transaction_value: typing.Optional[typing.Union[int, float]] = Field(None, alias='average_transaction_value')

    # Median transaction value
    median_transaction_value: typing.Optional[typing.Union[int, float]] = Field(None, alias='median_transaction_value')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
