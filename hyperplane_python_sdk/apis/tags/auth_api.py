# coding: utf-8

"""
    Hyperplane API Gateway

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from hyperplane_python_sdk.paths.auth_token.post import GetToken
from hyperplane_python_sdk.apis.tags.auth_api_raw import AuthApiRaw


class AuthApi(
    GetToken,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AuthApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AuthApiRaw(api_client)
