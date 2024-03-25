# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from hyperplane_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    AUTH_TOKEN = "/auth/token"
    AUTOML_LOOKALIKE = "/automl/lookalike"
    AUTOML_RUNS = "/automl/runs"
    AUTOML_RUNS_RUN_ID = "/automl/runs/{run_id}"
    AUTOML_RUNS_RUN_ID_GENERATE_BATCH_SCORES = "/automl/runs/{run_id}/generate_batch_scores"
    AUTOML_RUNS_RUN_ID_RESCORE = "/automl/runs/{run_id}/rescore"
    AUTOML_RUNS_RUN_ID_STATUS = "/automl/runs/{run_id}/status"
    AUTOML_RUNS_RUN_ID_STATUS_BATCH_SCORES = "/automl/runs/{run_id}/status_batch_scores"
    AUTOML_RUNS_RUN_ID_USERS = "/automl/runs/{run_id}/users"
    AUTOML_USERS = "/automl/users"
    BATCH_USER_PERSONAS = "/batch/user/personas"
    CLIENT_ACCESS_KEY_ID = "/client/{access_key_id}"
    HEALTH = "/health"
    MODULE_TRANSACTIONENRICHMENT_STATISTICS = "/module/transaction-enrichment/statistics"
    MODULE_TRANSACTIONENRICHMENT_USERS = "/module/transaction-enrichment/users"
    PERSONA = "/persona"
    PERSONA_PERSONA_ID = "/persona/{persona_id}"
    PERSONA_PERSONA_ID_PERCENTILE_SCORE = "/persona/{persona_id}/percentile_score"
    PERSONA_PERSONA_ID_USERS = "/persona/{persona_id}/users"
    STATISTICS_LATEST_MONTH = "/statistics/latest_month"
    USER_USER_ID_CASHFLOW_CATEGORIES = "/user/{user_id}/cashflow/categories"
    USER_USER_ID_CASHFLOW_HISTORY = "/user/{user_id}/cashflow/history"
    USER_USER_ID_CASHFLOW_STATISTICS = "/user/{user_id}/cashflow/statistics"
    USER_USER_ID_TRANSACTIONS = "/user/{user_id}/transactions"
    USER_USER_ID_TRANSACTIONS_STATISTICS = "/user/{user_id}/transactions/statistics"
    USERS_USER_ID_PERSONAS = "/users/{user_id}/personas"
