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


class ModelsUserTransactionsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Historic of enriched transactions of a given user
    """


    class MetaOapg:
        required = {
            "pagination_metadata",
            "user_id",
            "enriched_transactions",
        }
        
        class properties:
            
            
            class enriched_transactions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ModelsTransactionEnrichmentResponse']:
                        return ModelsTransactionEnrichmentResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ModelsTransactionEnrichmentResponse'], typing.List['ModelsTransactionEnrichmentResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'enriched_transactions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ModelsTransactionEnrichmentResponse':
                    return super().__getitem__(i)
        
            @staticmethod
            def pagination_metadata() -> typing.Type['ModelsPaginationMetadata']:
                return ModelsPaginationMetadata
            user_id = schemas.StrSchema
            __annotations__ = {
                "enriched_transactions": enriched_transactions,
                "pagination_metadata": pagination_metadata,
                "user_id": user_id,
            }
    
    pagination_metadata: 'ModelsPaginationMetadata'
    user_id: MetaOapg.properties.user_id
    enriched_transactions: MetaOapg.properties.enriched_transactions
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enriched_transactions"]) -> MetaOapg.properties.enriched_transactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pagination_metadata"]) -> 'ModelsPaginationMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["enriched_transactions", "pagination_metadata", "user_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enriched_transactions"]) -> MetaOapg.properties.enriched_transactions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pagination_metadata"]) -> 'ModelsPaginationMetadata': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enriched_transactions", "pagination_metadata", "user_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pagination_metadata: 'ModelsPaginationMetadata',
        user_id: typing.Union[MetaOapg.properties.user_id, str, ],
        enriched_transactions: typing.Union[MetaOapg.properties.enriched_transactions, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelsUserTransactionsResponse':
        return super().__new__(
            cls,
            *args,
            pagination_metadata=pagination_metadata,
            user_id=user_id,
            enriched_transactions=enriched_transactions,
            _configuration=_configuration,
            **kwargs,
        )

from hyperplane_python_sdk.model.models_pagination_metadata import ModelsPaginationMetadata
from hyperplane_python_sdk.model.models_transaction_enrichment_response import ModelsTransactionEnrichmentResponse
