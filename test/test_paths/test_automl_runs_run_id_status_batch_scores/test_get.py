# coding: utf-8

"""
    Hyperplane API Gateway

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import hyperplane_python_sdk
from hyperplane_python_sdk.paths.automl_runs_run_id_status_batch_scores import get
from hyperplane_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestAutomlRunsRunIdStatusBatchScores(ApiTestMixin, unittest.TestCase):
    """
    AutomlRunsRunIdStatusBatchScores unit test stubs
        Get status of the batch scores request for an AutoML run
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
