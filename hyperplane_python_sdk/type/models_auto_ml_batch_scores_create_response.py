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


class RequiredModelsAutoMLBatchScoresCreateResponse(TypedDict):
    # Path where parquet file with the batch scores will be written
    path: str

class OptionalModelsAutoMLBatchScoresCreateResponse(TypedDict, total=False):
    pass

class ModelsAutoMLBatchScoresCreateResponse(RequiredModelsAutoMLBatchScoresCreateResponse, OptionalModelsAutoMLBatchScoresCreateResponse):
    pass
