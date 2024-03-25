# coding: utf-8

"""
    Hyperplane API Gateway

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from hyperplane_python_sdk.paths.user_user_id_transactions.get import GetHistoryRaw
from hyperplane_python_sdk.paths.module_transaction_enrichment_statistics.get import GetStatisticsRaw
from hyperplane_python_sdk.paths.user_user_id_cashflow_categories.get import GetUserCashflowCategoriesRaw
from hyperplane_python_sdk.paths.user_user_id_cashflow_history.get import GetUserCashflowHistoryRaw
from hyperplane_python_sdk.paths.user_user_id_cashflow_statistics.get import GetUserCashflowStatisticsRaw
from hyperplane_python_sdk.paths.user_user_id_transactions_statistics.get import GetUserStatisticsRaw
from hyperplane_python_sdk.paths.module_transaction_enrichment_users.get import ListUsersRaw


class EnrichedTransactionsApiRaw(
    GetHistoryRaw,
    GetStatisticsRaw,
    GetUserCashflowCategoriesRaw,
    GetUserCashflowHistoryRaw,
    GetUserCashflowStatisticsRaw,
    GetUserStatisticsRaw,
    ListUsersRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
