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

from hyperplane_python_sdk.model.models_auto_ml_lookalike_create_request import ModelsAutoMLLookalikeCreateRequest as ModelsAutoMLLookalikeCreateRequestSchema
from hyperplane_python_sdk.model.models_auto_ml_lookalike_create_response import ModelsAutoMLLookalikeCreateResponse as ModelsAutoMLLookalikeCreateResponseSchema
from hyperplane_python_sdk.model.models_lookalike_label import ModelsLookalikeLabel as ModelsLookalikeLabelSchema

from hyperplane_python_sdk.type.models_lookalike_label import ModelsLookalikeLabel
from hyperplane_python_sdk.type.models_auto_ml_lookalike_create_request import ModelsAutoMLLookalikeCreateRequest
from hyperplane_python_sdk.type.models_auto_ml_lookalike_create_response import ModelsAutoMLLookalikeCreateResponse

from ...api_client import Dictionary
from hyperplane_python_sdk.pydantic.models_lookalike_label import ModelsLookalikeLabel as ModelsLookalikeLabelPydantic
from hyperplane_python_sdk.pydantic.models_auto_ml_lookalike_create_response import ModelsAutoMLLookalikeCreateResponse as ModelsAutoMLLookalikeCreateResponsePydantic
from hyperplane_python_sdk.pydantic.models_auto_ml_lookalike_create_request import ModelsAutoMLLookalikeCreateRequest as ModelsAutoMLLookalikeCreateRequestPydantic

# Query params
ModelVersionSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'model_version': typing.Union[ModelVersionSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_model_version = api_client.QueryParameter(
    name="model_version",
    style=api_client.ParameterStyle.FORM,
    schema=ModelVersionSchema,
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
# body param
SchemaForRequestBodyApplicationJson = ModelsAutoMLLookalikeCreateRequestSchema


request_body_models_auto_ml_lookalike_create_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ModelsAutoMLLookalikeCreateResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ModelsAutoMLLookalikeCreateResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ModelsAutoMLLookalikeCreateResponse


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

    def _create_lookalike_request_mapped_args(
        self,
        engagement_type: str,
        positive_label_users: typing.List[ModelsLookalikeLabel],
        negative_label_users: typing.Optional[typing.List[ModelsLookalikeLabel]] = None,
        run_description: typing.Optional[str] = None,
        model_version: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _body = {}
        if engagement_type is not None:
            _body["engagement_type"] = engagement_type
        if negative_label_users is not None:
            _body["negative_label_users"] = negative_label_users
        if positive_label_users is not None:
            _body["positive_label_users"] = positive_label_users
        if run_description is not None:
            _body["run_description"] = run_description
        args.body = _body
        if model_version is not None:
            _query_params["model_version"] = model_version
        if module_id is not None:
            _header_params["module-id"] = module_id
        args.query = _query_params
        args.header = _header_params
        return args

    async def _acreate_lookalike_request_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
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
        Create an AutoML lookalike request
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_model_version,
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
            path_template='/automl/lookalike',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_models_auto_ml_lookalike_create_request.serialize(body, content_type)
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


    def _create_lookalike_request_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
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
        Create an AutoML lookalike request
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_model_version,
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
            path_template='/automl/lookalike',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_models_auto_ml_lookalike_create_request.serialize(body, content_type)
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


class CreateLookalikeRequestRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_lookalike_request(
        self,
        engagement_type: str,
        positive_label_users: typing.List[ModelsLookalikeLabel],
        negative_label_users: typing.Optional[typing.List[ModelsLookalikeLabel]] = None,
        run_description: typing.Optional[str] = None,
        model_version: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_lookalike_request_mapped_args(
            engagement_type=engagement_type,
            positive_label_users=positive_label_users,
            negative_label_users=negative_label_users,
            run_description=run_description,
            model_version=model_version,
            module_id=module_id,
        )
        return await self._acreate_lookalike_request_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def create_lookalike_request(
        self,
        engagement_type: str,
        positive_label_users: typing.List[ModelsLookalikeLabel],
        negative_label_users: typing.Optional[typing.List[ModelsLookalikeLabel]] = None,
        run_description: typing.Optional[str] = None,
        model_version: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_lookalike_request_mapped_args(
            engagement_type=engagement_type,
            positive_label_users=positive_label_users,
            negative_label_users=negative_label_users,
            run_description=run_description,
            model_version=model_version,
            module_id=module_id,
        )
        return self._create_lookalike_request_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
        )

class CreateLookalikeRequest(BaseApi):

    async def acreate_lookalike_request(
        self,
        engagement_type: str,
        positive_label_users: typing.List[ModelsLookalikeLabel],
        negative_label_users: typing.Optional[typing.List[ModelsLookalikeLabel]] = None,
        run_description: typing.Optional[str] = None,
        model_version: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ModelsAutoMLLookalikeCreateResponsePydantic:
        raw_response = await self.raw.acreate_lookalike_request(
            engagement_type=engagement_type,
            positive_label_users=positive_label_users,
            negative_label_users=negative_label_users,
            run_description=run_description,
            model_version=model_version,
            module_id=module_id,
            **kwargs,
        )
        if validate:
            return ModelsAutoMLLookalikeCreateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ModelsAutoMLLookalikeCreateResponsePydantic, raw_response.body)
    
    
    def create_lookalike_request(
        self,
        engagement_type: str,
        positive_label_users: typing.List[ModelsLookalikeLabel],
        negative_label_users: typing.Optional[typing.List[ModelsLookalikeLabel]] = None,
        run_description: typing.Optional[str] = None,
        model_version: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ModelsAutoMLLookalikeCreateResponsePydantic:
        raw_response = self.raw.create_lookalike_request(
            engagement_type=engagement_type,
            positive_label_users=positive_label_users,
            negative_label_users=negative_label_users,
            run_description=run_description,
            model_version=model_version,
            module_id=module_id,
        )
        if validate:
            return ModelsAutoMLLookalikeCreateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ModelsAutoMLLookalikeCreateResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        engagement_type: str,
        positive_label_users: typing.List[ModelsLookalikeLabel],
        negative_label_users: typing.Optional[typing.List[ModelsLookalikeLabel]] = None,
        run_description: typing.Optional[str] = None,
        model_version: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_lookalike_request_mapped_args(
            engagement_type=engagement_type,
            positive_label_users=positive_label_users,
            negative_label_users=negative_label_users,
            run_description=run_description,
            model_version=model_version,
            module_id=module_id,
        )
        return await self._acreate_lookalike_request_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        engagement_type: str,
        positive_label_users: typing.List[ModelsLookalikeLabel],
        negative_label_users: typing.Optional[typing.List[ModelsLookalikeLabel]] = None,
        run_description: typing.Optional[str] = None,
        model_version: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_lookalike_request_mapped_args(
            engagement_type=engagement_type,
            positive_label_users=positive_label_users,
            negative_label_users=negative_label_users,
            run_description=run_description,
            model_version=model_version,
            module_id=module_id,
        )
        return self._create_lookalike_request_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
        )

