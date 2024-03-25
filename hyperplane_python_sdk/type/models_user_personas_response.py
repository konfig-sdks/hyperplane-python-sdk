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

from hyperplane_python_sdk.type.models_user_persona_score import ModelsUserPersonaScore

class RequiredModelsUserPersonasResponse(TypedDict):
    # Ranked list of personas for this user
    persona_scores: typing.List[ModelsUserPersonaScore]

    # Unique identifier for the user
    user_id: str

class OptionalModelsUserPersonasResponse(TypedDict, total=False):
    pass

class ModelsUserPersonasResponse(RequiredModelsUserPersonasResponse, OptionalModelsUserPersonasResponse):
    pass
