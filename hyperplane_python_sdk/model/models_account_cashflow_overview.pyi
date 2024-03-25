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


class ModelsAccountCashflowOverview(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Cashflow details for a given account of a given user
    """


    class MetaOapg:
        required = {
            "net_cashflow_amount",
            "account_type",
            "outflow_amount",
            "inflow_amount",
        }
        
        class properties:
            account_type = schemas.StrSchema
            inflow_amount = schemas.NumberSchema
            net_cashflow_amount = schemas.NumberSchema
            outflow_amount = schemas.NumberSchema
            __annotations__ = {
                "account_type": account_type,
                "inflow_amount": inflow_amount,
                "net_cashflow_amount": net_cashflow_amount,
                "outflow_amount": outflow_amount,
            }
    
    net_cashflow_amount: MetaOapg.properties.net_cashflow_amount
    account_type: MetaOapg.properties.account_type
    outflow_amount: MetaOapg.properties.outflow_amount
    inflow_amount: MetaOapg.properties.inflow_amount
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_type"]) -> MetaOapg.properties.account_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inflow_amount"]) -> MetaOapg.properties.inflow_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["net_cashflow_amount"]) -> MetaOapg.properties.net_cashflow_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outflow_amount"]) -> MetaOapg.properties.outflow_amount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["account_type", "inflow_amount", "net_cashflow_amount", "outflow_amount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_type"]) -> MetaOapg.properties.account_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inflow_amount"]) -> MetaOapg.properties.inflow_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["net_cashflow_amount"]) -> MetaOapg.properties.net_cashflow_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outflow_amount"]) -> MetaOapg.properties.outflow_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["account_type", "inflow_amount", "net_cashflow_amount", "outflow_amount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        net_cashflow_amount: typing.Union[MetaOapg.properties.net_cashflow_amount, decimal.Decimal, int, float, ],
        account_type: typing.Union[MetaOapg.properties.account_type, str, ],
        outflow_amount: typing.Union[MetaOapg.properties.outflow_amount, decimal.Decimal, int, float, ],
        inflow_amount: typing.Union[MetaOapg.properties.inflow_amount, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelsAccountCashflowOverview':
        return super().__new__(
            cls,
            *args,
            net_cashflow_amount=net_cashflow_amount,
            account_type=account_type,
            outflow_amount=outflow_amount,
            inflow_amount=inflow_amount,
            _configuration=_configuration,
            **kwargs,
        )
