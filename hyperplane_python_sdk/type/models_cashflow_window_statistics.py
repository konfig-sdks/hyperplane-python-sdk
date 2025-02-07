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


class RequiredModelsCashflowWindowStatistics(TypedDict):
    pass

class OptionalModelsCashflowWindowStatistics(TypedDict, total=False):
    # Inflow amount on the given window
    inflow_amount: typing.Union[int, float]

    # Outflow amount on the given window
    outflow_amount: typing.Union[int, float]

    # End time of the given window
    window_end: str

    # Start time of the given window
    window_start: str

class ModelsCashflowWindowStatistics(RequiredModelsCashflowWindowStatistics, OptionalModelsCashflowWindowStatistics):
    pass
