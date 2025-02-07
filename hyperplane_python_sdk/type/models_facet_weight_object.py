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


class RequiredModelsFacetWeightObject(TypedDict):
    # Name of the facet
    name: str

    # Weight of the facet
    weight: typing.Union[int, float]

class OptionalModelsFacetWeightObject(TypedDict, total=False):
    pass

class ModelsFacetWeightObject(RequiredModelsFacetWeightObject, OptionalModelsFacetWeightObject):
    pass
