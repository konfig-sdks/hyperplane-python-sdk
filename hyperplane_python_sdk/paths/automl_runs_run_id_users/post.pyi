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

from hyperplane_python_sdk.model.models_tag_categorical_attribute_filter import ModelsTagCategoricalAttributeFilter as ModelsTagCategoricalAttributeFilterSchema
from hyperplane_python_sdk.model.models_auto_ml_run_users_get_response import ModelsAutoMLRunUsersGetResponse as ModelsAutoMLRunUsersGetResponseSchema
from hyperplane_python_sdk.model.models_auto_ml_run_users_get_request import ModelsAutoMLRunUsersGetRequest as ModelsAutoMLRunUsersGetRequestSchema
from hyperplane_python_sdk.model.models_user_metadata import ModelsUserMetadata as ModelsUserMetadataSchema

from hyperplane_python_sdk.type.models_auto_ml_run_users_get_response import ModelsAutoMLRunUsersGetResponse
from hyperplane_python_sdk.type.models_user_metadata import ModelsUserMetadata
from hyperplane_python_sdk.type.models_tag_categorical_attribute_filter import ModelsTagCategoricalAttributeFilter
from hyperplane_python_sdk.type.models_auto_ml_run_users_get_request import ModelsAutoMLRunUsersGetRequest

from ...api_client import Dictionary
from hyperplane_python_sdk.pydantic.models_user_metadata import ModelsUserMetadata as ModelsUserMetadataPydantic
from hyperplane_python_sdk.pydantic.models_tag_categorical_attribute_filter import ModelsTagCategoricalAttributeFilter as ModelsTagCategoricalAttributeFilterPydantic
from hyperplane_python_sdk.pydantic.models_auto_ml_run_users_get_request import ModelsAutoMLRunUsersGetRequest as ModelsAutoMLRunUsersGetRequestPydantic
from hyperplane_python_sdk.pydantic.models_auto_ml_run_users_get_response import ModelsAutoMLRunUsersGetResponse as ModelsAutoMLRunUsersGetResponsePydantic

# Query params


class PageNumberSchema(
    schemas.IntSchema
):
    pass


class PageSizeSchema(
    schemas.IntSchema
):
    pass
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'page_number': typing.Union[PageNumberSchema, decimal.Decimal, int, ],
        'page_size': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


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
# Path params
RunIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'run_id': typing.Union[RunIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_run_id = api_client.PathParameter(
    name="run_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=RunIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ModelsAutoMLRunUsersGetRequestSchema


request_body_models_auto_ml_run_users_get_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ModelsAutoMLRunUsersGetResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ModelsAutoMLRunUsersGetResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ModelsAutoMLRunUsersGetResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_top_users_excluding_training_mapped_args(
        self,
        run_id: str,
        allow_users: typing.Optional[typing.List[ModelsUserMetadata]] = None,
        block_users: typing.Optional[typing.List[ModelsUserMetadata]] = None,
        tag_filters: typing.Optional[typing.List[ModelsTagCategoricalAttributeFilter]] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if allow_users is not None:
            _body["allow_users"] = allow_users
        if block_users is not None:
            _body["block_users"] = block_users
        if tag_filters is not None:
            _body["tag_filters"] = tag_filters
        args.body = _body
        if page_number is not None:
            _query_params["page_number"] = page_number
        if page_size is not None:
            _query_params["page_size"] = page_size
        if run_id is not None:
            _path_params["run_id"] = run_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_top_users_excluding_training_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get top users from a specified AutoML run excluding training users
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_run_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
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
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/automl/runs/{run_id}/users',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_models_auto_ml_run_users_get_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _get_top_users_excluding_training_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get top users from a specified AutoML run excluding training users
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_run_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
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
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/automl/runs/{run_id}/users',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_models_auto_ml_run_users_get_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class GetTopUsersExcludingTrainingRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_top_users_excluding_training(
        self,
        run_id: str,
        allow_users: typing.Optional[typing.List[ModelsUserMetadata]] = None,
        block_users: typing.Optional[typing.List[ModelsUserMetadata]] = None,
        tag_filters: typing.Optional[typing.List[ModelsTagCategoricalAttributeFilter]] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_top_users_excluding_training_mapped_args(
            run_id=run_id,
            allow_users=allow_users,
            block_users=block_users,
            tag_filters=tag_filters,
            page_number=page_number,
            page_size=page_size,
        )
        return await self._aget_top_users_excluding_training_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_top_users_excluding_training(
        self,
        run_id: str,
        allow_users: typing.Optional[typing.List[ModelsUserMetadata]] = None,
        block_users: typing.Optional[typing.List[ModelsUserMetadata]] = None,
        tag_filters: typing.Optional[typing.List[ModelsTagCategoricalAttributeFilter]] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_top_users_excluding_training_mapped_args(
            run_id=run_id,
            allow_users=allow_users,
            block_users=block_users,
            tag_filters=tag_filters,
            page_number=page_number,
            page_size=page_size,
        )
        return self._get_top_users_excluding_training_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class GetTopUsersExcludingTraining(BaseApi):

    async def aget_top_users_excluding_training(
        self,
        run_id: str,
        allow_users: typing.Optional[typing.List[ModelsUserMetadata]] = None,
        block_users: typing.Optional[typing.List[ModelsUserMetadata]] = None,
        tag_filters: typing.Optional[typing.List[ModelsTagCategoricalAttributeFilter]] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> ModelsAutoMLRunUsersGetResponsePydantic:
        raw_response = await self.raw.aget_top_users_excluding_training(
            run_id=run_id,
            allow_users=allow_users,
            block_users=block_users,
            tag_filters=tag_filters,
            page_number=page_number,
            page_size=page_size,
            **kwargs,
        )
        if validate:
            return ModelsAutoMLRunUsersGetResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ModelsAutoMLRunUsersGetResponsePydantic, raw_response.body)
    
    
    def get_top_users_excluding_training(
        self,
        run_id: str,
        allow_users: typing.Optional[typing.List[ModelsUserMetadata]] = None,
        block_users: typing.Optional[typing.List[ModelsUserMetadata]] = None,
        tag_filters: typing.Optional[typing.List[ModelsTagCategoricalAttributeFilter]] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        validate: bool = False,
    ) -> ModelsAutoMLRunUsersGetResponsePydantic:
        raw_response = self.raw.get_top_users_excluding_training(
            run_id=run_id,
            allow_users=allow_users,
            block_users=block_users,
            tag_filters=tag_filters,
            page_number=page_number,
            page_size=page_size,
        )
        if validate:
            return ModelsAutoMLRunUsersGetResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ModelsAutoMLRunUsersGetResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        run_id: str,
        allow_users: typing.Optional[typing.List[ModelsUserMetadata]] = None,
        block_users: typing.Optional[typing.List[ModelsUserMetadata]] = None,
        tag_filters: typing.Optional[typing.List[ModelsTagCategoricalAttributeFilter]] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_top_users_excluding_training_mapped_args(
            run_id=run_id,
            allow_users=allow_users,
            block_users=block_users,
            tag_filters=tag_filters,
            page_number=page_number,
            page_size=page_size,
        )
        return await self._aget_top_users_excluding_training_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        run_id: str,
        allow_users: typing.Optional[typing.List[ModelsUserMetadata]] = None,
        block_users: typing.Optional[typing.List[ModelsUserMetadata]] = None,
        tag_filters: typing.Optional[typing.List[ModelsTagCategoricalAttributeFilter]] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_top_users_excluding_training_mapped_args(
            run_id=run_id,
            allow_users=allow_users,
            block_users=block_users,
            tag_filters=tag_filters,
            page_number=page_number,
            page_size=page_size,
        )
        return self._get_top_users_excluding_training_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

