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

from hyperplane_python_sdk.type.models_lookalike_label import ModelsLookalikeLabel

class RequiredModelsAutoMLLookalikeCreateRequest(TypedDict):
    # Intended use case of this product, between MULTI_ENGAGE and SINGLE_ENGAGE
    engagement_type: str

    # List of positive users in lookalike model. Model will be trained to identify users similar to these users. This list must contain at least ten elements.
    positive_label_users: typing.List[ModelsLookalikeLabel]

class OptionalModelsAutoMLLookalikeCreateRequest(TypedDict, total=False):
    # List of negative users in lookalike model. Model will be trained to identify users dissimilar to these users. If None, negative users will be generated from data. List length must be either 0 or greater than 10.
    negative_label_users: typing.List[ModelsLookalikeLabel]

    # Custom run description to attach to run
    run_description: str

class ModelsAutoMLLookalikeCreateRequest(RequiredModelsAutoMLLookalikeCreateRequest, OptionalModelsAutoMLLookalikeCreateRequest):
    pass
