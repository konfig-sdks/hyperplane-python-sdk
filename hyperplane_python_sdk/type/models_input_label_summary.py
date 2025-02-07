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

from hyperplane_python_sdk.type.models_input_label_summary_label_weight_counts import ModelsInputLabelSummaryLabelWeightCounts
from hyperplane_python_sdk.type.models_input_label_summary_monthly_counts import ModelsInputLabelSummaryMonthlyCounts
from hyperplane_python_sdk.type.models_input_label_summary_monthly_positive_rates import ModelsInputLabelSummaryMonthlyPositiveRates

class RequiredModelsInputLabelSummary(TypedDict):
    # Number of labels that were provided by the user.
    num_input_labels: int

    # Number of distinct users that were provided by the user
    num_input_users: int

    # Number of data rows that will be used in training
    num_matched_labels: int

    # Number of distinct users that will be used in training
    num_training_users: int

class OptionalModelsInputLabelSummary(TypedDict, total=False):
    label_weight_counts: ModelsInputLabelSummaryLabelWeightCounts

    monthly_counts: ModelsInputLabelSummaryMonthlyCounts

    monthly_positive_rates: ModelsInputLabelSummaryMonthlyPositiveRates

class ModelsInputLabelSummary(RequiredModelsInputLabelSummary, OptionalModelsInputLabelSummary):
    pass
