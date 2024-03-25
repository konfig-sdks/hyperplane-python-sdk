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

from hyperplane_python_sdk.pydantic.models_facet_weight_object import ModelsFacetWeightObject
from hyperplane_python_sdk.pydantic.models_persona_create_request_locations import ModelsPersonaCreateRequestLocations

class ModelsPersonaCreateRequest(BaseModel):
    # A name for describing this persona. Used for easy human-friendly identification.
    persona_name: str = Field(alias='persona_name')

    # Optional list of behavioral facet component objects. Each object outlines how a user's likelihood to consume from a particular company's products and how much it contributes to the persona definition. If left empty, no company-based scoring is done. Company facets can be found by listing personas of facet type 'company'. Facet name must be a valid company facet in the persona taxonomy.
    company_facets: typing.Optional[typing.List[ModelsFacetWeightObject]] = Field(None, alias='company_facets')

    # Optional list of interest facet component objects. Defines how much each demographic attribute (location, affluence, household composition, etc.)  weighs in the persona. If left empty, no demographic-based scoring is done. Demographic facets can be found by listing personas of facet type 'demographic'. Facet name must be a valid demographic facet in the persona taxonomy.
    demographic_facets: typing.Optional[typing.List[ModelsFacetWeightObject]] = Field(None, alias='demographic_facets')

    # Optional list of interest facet component objects. Each object represents how much an interest weighs in the persona. If left empty, no interest-based scoring is done. Interests can be found by listing personas of facet type 'interest'. Facet name must be a valid interest in the persona taxonomy.
    interest_facets: typing.Optional[typing.List[ModelsFacetWeightObject]] = Field(None, alias='interest_facets')

    locations: typing.Optional[ModelsPersonaCreateRequestLocations] = Field(None, alias='locations')

    # Optional list of pre-defined persona facet component objects. Each object outlines how a pre-defined persona ('Car Owners' or 'International Travelers') contributes to the persona definition. If left empty, no predefined personas are incorporated into the persona definition. Pre-defined personas have been optimized for financial use cases and have been validated at scale. They can be found by listing personas of facet type 'pre_defined_persona'. Facet name must be a valid pre-defined persona facet in the persona taxonomy.
    pre_defined_personas: typing.Optional[typing.List[ModelsFacetWeightObject]] = Field(None, alias='pre_defined_personas')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
