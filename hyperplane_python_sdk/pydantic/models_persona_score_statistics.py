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

from hyperplane_python_sdk.pydantic.models_persona_score_percentiles import ModelsPersonaScorePercentiles

class ModelsPersonaScoreStatistics(BaseModel):
    # Highest persona score assigned to a user for this persona
    maximum_user_score: typing.Union[int, float] = Field(alias='maximum_user_score')

    # Lowest persona score assigned to a user for this persona
    minimum_user_score: typing.Union[int, float] = Field(alias='minimum_user_score')

    # Score threshold used to determine whether a user belongs to this persona
    persona_score_threshold: typing.Union[int, float] = Field(alias='persona_score_threshold')

    # Average score over all scored users in this persona
    score_average: typing.Union[int, float] = Field(alias='score_average')

    # Percentile distribution of scores for users who have been assigned a score for this persona
    score_percentiles: ModelsPersonaScorePercentiles = Field(alias='score_percentiles')

    # Standard deviation over all scored users in this persona
    score_standard_deviation: typing.Union[int, float] = Field(alias='score_standard_deviation')

    # Total number of users who meet or exceed the score threshold to be considered part of this persona.
    total_users_above_threshold: int = Field(alias='total_users_above_threshold')

    # Total number of users who have received a score for this persona.
    total_users_with_non_zero_score: int = Field(alias='total_users_with_non_zero_score')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
