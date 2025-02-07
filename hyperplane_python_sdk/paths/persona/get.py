# coding: utf-8

"""
    Hyperplane API Gateway

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from hyperplane_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from hyperplane_python_sdk.api_response import AsyncGeneratorResponse
from hyperplane_python_sdk import api_client, exceptions
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

from hyperplane_python_sdk.model.models_list_personas_response import ModelsListPersonasResponse as ModelsListPersonasResponseSchema
from hyperplane_python_sdk.model.api_err_response import ApiErrResponse as ApiErrResponseSchema

from hyperplane_python_sdk.type.api_err_response import ApiErrResponse
from hyperplane_python_sdk.type.models_list_personas_response import ModelsListPersonasResponse

from ...api_client import Dictionary
from hyperplane_python_sdk.pydantic.models_list_personas_response import ModelsListPersonasResponse as ModelsListPersonasResponsePydantic
from hyperplane_python_sdk.pydantic.api_err_response import ApiErrResponse as ApiErrResponsePydantic

from . import path

# Query params
FacetTypesSchema = schemas.StrSchema


class PageNumberSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_minimum = 1


class PageSizeSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_maximum = 10000
        inclusive_minimum = 1
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'facet_types': typing.Union[FacetTypesSchema, str, ],
        'page_number': typing.Union[PageNumberSchema, decimal.Decimal, int, ],
        'page_size': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_facet_types = api_client.QueryParameter(
    name="facet_types",
    style=api_client.ParameterStyle.FORM,
    schema=FacetTypesSchema,
    explode=True,
)
request_query_page_number = api_client.QueryParameter(
    name="page_number",
    style=api_client.ParameterStyle.FORM,
    schema=PageNumberSchema,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="page_size",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
# Header params
ModuleIdSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'module-id': typing.Union[ModuleIdSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_module_id = api_client.HeaderParameter(
    name="module-id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ModuleIdSchema,
)
_auth = [
    'PASETO',
]
SchemaFor200ResponseBodyApplicationJson = ModelsListPersonasResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ModelsListPersonasResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ModelsListPersonasResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ApiErrResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ApiErrResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ApiErrResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ApiErrResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ApiErrResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ApiErrResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_existing_mapped_args(
        self,
        facet_types: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        if facet_types is not None:
            _query_params["facet_types"] = facet_types
        if page_number is not None:
            _query_params["page_number"] = page_number
        if page_size is not None:
            _query_params["page_size"] = page_size
        if module_id is not None:
            _header_params["module-id"] = module_id
        args.query = _query_params
        args.header = _header_params
        return args

    async def _alist_existing_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List existing personas.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_facet_types,
            request_query_page_number,
            request_query_page_size,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_module_id,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/persona',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_existing_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List existing personas.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_facet_types,
            request_query_page_number,
            request_query_page_size,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_module_id,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/persona',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListExistingRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_existing(
        self,
        facet_types: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_existing_mapped_args(
            facet_types=facet_types,
            module_id=module_id,
            page_number=page_number,
            page_size=page_size,
        )
        return await self._alist_existing_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def list_existing(
        self,
        facet_types: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_existing_mapped_args(
            facet_types=facet_types,
            module_id=module_id,
            page_number=page_number,
            page_size=page_size,
        )
        return self._list_existing_oapg(
            query_params=args.query,
            header_params=args.header,
        )

class ListExisting(BaseApi):

    async def alist_existing(
        self,
        facet_types: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> ModelsListPersonasResponsePydantic:
        raw_response = await self.raw.alist_existing(
            facet_types=facet_types,
            module_id=module_id,
            page_number=page_number,
            page_size=page_size,
            **kwargs,
        )
        if validate:
            return ModelsListPersonasResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ModelsListPersonasResponsePydantic, raw_response.body)
    
    
    def list_existing(
        self,
        facet_types: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        validate: bool = False,
    ) -> ModelsListPersonasResponsePydantic:
        raw_response = self.raw.list_existing(
            facet_types=facet_types,
            module_id=module_id,
            page_number=page_number,
            page_size=page_size,
        )
        if validate:
            return ModelsListPersonasResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ModelsListPersonasResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        facet_types: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_existing_mapped_args(
            facet_types=facet_types,
            module_id=module_id,
            page_number=page_number,
            page_size=page_size,
        )
        return await self._alist_existing_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def get(
        self,
        facet_types: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_existing_mapped_args(
            facet_types=facet_types,
            module_id=module_id,
            page_number=page_number,
            page_size=page_size,
        )
        return self._list_existing_oapg(
            query_params=args.query,
            header_params=args.header,
        )

