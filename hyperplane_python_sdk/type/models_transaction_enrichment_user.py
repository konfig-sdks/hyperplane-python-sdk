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


class RequiredModelsTransactionEnrichmentUser(TypedDict):
    # Date for first transaction registered for a given user.
    first_transaction_date: str

    # Date for last transaction registered for a given user.
    last_transaction_date: str

    # Unique user identifier
    user_id: str

class OptionalModelsTransactionEnrichmentUser(TypedDict, total=False):
    pass

class ModelsTransactionEnrichmentUser(RequiredModelsTransactionEnrichmentUser, OptionalModelsTransactionEnrichmentUser):
    pass
