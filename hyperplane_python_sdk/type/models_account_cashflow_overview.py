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


class RequiredModelsAccountCashflowOverview(TypedDict):
    # Account type
    account_type: str

    # Inflow amount on the given window
    inflow_amount: typing.Union[int, float]

    # Net cashflow amount on the given window
    net_cashflow_amount: typing.Union[int, float]

    # Outflow amount on the given window
    outflow_amount: typing.Union[int, float]

class OptionalModelsAccountCashflowOverview(TypedDict, total=False):
    pass

class ModelsAccountCashflowOverview(RequiredModelsAccountCashflowOverview, OptionalModelsAccountCashflowOverview):
    pass
