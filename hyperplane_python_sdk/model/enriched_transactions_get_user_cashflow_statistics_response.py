# coding: utf-8

"""
    Hyperplane API Gateway

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from hyperplane_python_sdk import schemas  # noqa: F401


class EnrichedTransactionsGetUserCashflowStatisticsResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ModelsAccountCashflowOverview']:
            return ModelsAccountCashflowOverview

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ModelsAccountCashflowOverview'], typing.List['ModelsAccountCashflowOverview']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EnrichedTransactionsGetUserCashflowStatisticsResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ModelsAccountCashflowOverview':
        return super().__getitem__(i)

from hyperplane_python_sdk.model.models_account_cashflow_overview import ModelsAccountCashflowOverview
