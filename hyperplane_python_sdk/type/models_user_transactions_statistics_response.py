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


class RequiredModelsUserTransactionsStatisticsResponse(TypedDict):
    # Number of transactions
    transaction_count: int

class OptionalModelsUserTransactionsStatisticsResponse(TypedDict, total=False):
    # Average transaction value
    average_transaction_value: typing.Union[int, float]

    # Median transaction value
    median_transaction_value: typing.Union[int, float]

class ModelsUserTransactionsStatisticsResponse(RequiredModelsUserTransactionsStatisticsResponse, OptionalModelsUserTransactionsStatisticsResponse):
    pass
