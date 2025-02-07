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

from hyperplane_python_sdk.type.models_categorical_attribute_filter import ModelsCategoricalAttributeFilter
from hyperplane_python_sdk.type.models_numerical_attribute_filter import ModelsNumericalAttributeFilter
from hyperplane_python_sdk.type.models_post_persona_users_request_blocklist import ModelsPostPersonaUsersRequestBlocklist
from hyperplane_python_sdk.type.models_timestamp_attribute_filter import ModelsTimestampAttributeFilter

class RequiredModelsPostPersonaUsersRequest(TypedDict):
    blocklist: ModelsPostPersonaUsersRequestBlocklist

    # Filter branch based on a list of allowed values
    branch: ModelsCategoricalAttributeFilter

class OptionalModelsPostPersonaUsersRequest(TypedDict, total=False):
    # Filter birth date based on a date range
    birth_date: ModelsTimestampAttributeFilter

    # Filter cbo code based on a list of allowed values
    cbo_code: ModelsCategoricalAttributeFilter

    # Filter declared monthly income based on a numeric range
    declared_monthly_income: ModelsNumericalAttributeFilter

    # Filter job title based on a list of allowed values
    job_title: ModelsCategoricalAttributeFilter

class ModelsPostPersonaUsersRequest(RequiredModelsPostPersonaUsersRequest, OptionalModelsPostPersonaUsersRequest):
    pass
