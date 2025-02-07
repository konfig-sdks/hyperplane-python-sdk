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

from hyperplane_python_sdk.type.models_top_level_category_cashflow import ModelsTopLevelCategoryCashflow

class RequiredModelsUserCashflowPerCategoryResponse(TypedDict):
    pass

class OptionalModelsUserCashflowPerCategoryResponse(TypedDict, total=False):
    # Inflow discriminated by category
    inflow_categories: typing.List[ModelsTopLevelCategoryCashflow]

    # Outflow discriminated by category
    outflow_categories: typing.List[ModelsTopLevelCategoryCashflow]

    # User identifier
    user_id: str

class ModelsUserCashflowPerCategoryResponse(RequiredModelsUserCashflowPerCategoryResponse, OptionalModelsUserCashflowPerCategoryResponse):
    pass
