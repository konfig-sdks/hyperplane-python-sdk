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


class RequiredModelsMerchantInfo(TypedDict):
    pass

class OptionalModelsMerchantInfo(TypedDict, total=False):
    # Merchant business name
    business_name: str

    # Merchant category
    category: str

    # Merchant CNAE
    cnae: str

    # Merchant CNPJ
    cnpj: str

    # Merchant name
    name: str

class ModelsMerchantInfo(RequiredModelsMerchantInfo, OptionalModelsMerchantInfo):
    pass
