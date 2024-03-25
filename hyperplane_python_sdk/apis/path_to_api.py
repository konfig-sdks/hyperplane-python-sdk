import typing_extensions

from hyperplane_python_sdk.paths import PathValues
from hyperplane_python_sdk.apis.paths.auth_token import AuthToken
from hyperplane_python_sdk.apis.paths.automl_lookalike import AutomlLookalike
from hyperplane_python_sdk.apis.paths.automl_runs import AutomlRuns
from hyperplane_python_sdk.apis.paths.automl_runs_run_id import AutomlRunsRunId
from hyperplane_python_sdk.apis.paths.automl_runs_run_id_generate_batch_scores import AutomlRunsRunIdGenerateBatchScores
from hyperplane_python_sdk.apis.paths.automl_runs_run_id_rescore import AutomlRunsRunIdRescore
from hyperplane_python_sdk.apis.paths.automl_runs_run_id_status import AutomlRunsRunIdStatus
from hyperplane_python_sdk.apis.paths.automl_runs_run_id_status_batch_scores import AutomlRunsRunIdStatusBatchScores
from hyperplane_python_sdk.apis.paths.automl_runs_run_id_users import AutomlRunsRunIdUsers
from hyperplane_python_sdk.apis.paths.automl_users import AutomlUsers
from hyperplane_python_sdk.apis.paths.batch_user_personas import BatchUserPersonas
from hyperplane_python_sdk.apis.paths.client_access_key_id import ClientAccessKeyId
from hyperplane_python_sdk.apis.paths.health import Health
from hyperplane_python_sdk.apis.paths.module_transaction_enrichment_statistics import ModuleTransactionEnrichmentStatistics
from hyperplane_python_sdk.apis.paths.module_transaction_enrichment_users import ModuleTransactionEnrichmentUsers
from hyperplane_python_sdk.apis.paths.persona import Persona
from hyperplane_python_sdk.apis.paths.persona_persona_id import PersonaPersonaId
from hyperplane_python_sdk.apis.paths.persona_persona_id_percentile_score import PersonaPersonaIdPercentileScore
from hyperplane_python_sdk.apis.paths.persona_persona_id_users import PersonaPersonaIdUsers
from hyperplane_python_sdk.apis.paths.statistics_latest_month import StatisticsLatestMonth
from hyperplane_python_sdk.apis.paths.user_user_id_cashflow_categories import UserUserIdCashflowCategories
from hyperplane_python_sdk.apis.paths.user_user_id_cashflow_history import UserUserIdCashflowHistory
from hyperplane_python_sdk.apis.paths.user_user_id_cashflow_statistics import UserUserIdCashflowStatistics
from hyperplane_python_sdk.apis.paths.user_user_id_transactions import UserUserIdTransactions
from hyperplane_python_sdk.apis.paths.user_user_id_transactions_statistics import UserUserIdTransactionsStatistics
from hyperplane_python_sdk.apis.paths.users_user_id_personas import UsersUserIdPersonas

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTH_TOKEN: AuthToken,
        PathValues.AUTOML_LOOKALIKE: AutomlLookalike,
        PathValues.AUTOML_RUNS: AutomlRuns,
        PathValues.AUTOML_RUNS_RUN_ID: AutomlRunsRunId,
        PathValues.AUTOML_RUNS_RUN_ID_GENERATE_BATCH_SCORES: AutomlRunsRunIdGenerateBatchScores,
        PathValues.AUTOML_RUNS_RUN_ID_RESCORE: AutomlRunsRunIdRescore,
        PathValues.AUTOML_RUNS_RUN_ID_STATUS: AutomlRunsRunIdStatus,
        PathValues.AUTOML_RUNS_RUN_ID_STATUS_BATCH_SCORES: AutomlRunsRunIdStatusBatchScores,
        PathValues.AUTOML_RUNS_RUN_ID_USERS: AutomlRunsRunIdUsers,
        PathValues.AUTOML_USERS: AutomlUsers,
        PathValues.BATCH_USER_PERSONAS: BatchUserPersonas,
        PathValues.CLIENT_ACCESS_KEY_ID: ClientAccessKeyId,
        PathValues.HEALTH: Health,
        PathValues.MODULE_TRANSACTIONENRICHMENT_STATISTICS: ModuleTransactionEnrichmentStatistics,
        PathValues.MODULE_TRANSACTIONENRICHMENT_USERS: ModuleTransactionEnrichmentUsers,
        PathValues.PERSONA: Persona,
        PathValues.PERSONA_PERSONA_ID: PersonaPersonaId,
        PathValues.PERSONA_PERSONA_ID_PERCENTILE_SCORE: PersonaPersonaIdPercentileScore,
        PathValues.PERSONA_PERSONA_ID_USERS: PersonaPersonaIdUsers,
        PathValues.STATISTICS_LATEST_MONTH: StatisticsLatestMonth,
        PathValues.USER_USER_ID_CASHFLOW_CATEGORIES: UserUserIdCashflowCategories,
        PathValues.USER_USER_ID_CASHFLOW_HISTORY: UserUserIdCashflowHistory,
        PathValues.USER_USER_ID_CASHFLOW_STATISTICS: UserUserIdCashflowStatistics,
        PathValues.USER_USER_ID_TRANSACTIONS: UserUserIdTransactions,
        PathValues.USER_USER_ID_TRANSACTIONS_STATISTICS: UserUserIdTransactionsStatistics,
        PathValues.USERS_USER_ID_PERSONAS: UsersUserIdPersonas,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTH_TOKEN: AuthToken,
        PathValues.AUTOML_LOOKALIKE: AutomlLookalike,
        PathValues.AUTOML_RUNS: AutomlRuns,
        PathValues.AUTOML_RUNS_RUN_ID: AutomlRunsRunId,
        PathValues.AUTOML_RUNS_RUN_ID_GENERATE_BATCH_SCORES: AutomlRunsRunIdGenerateBatchScores,
        PathValues.AUTOML_RUNS_RUN_ID_RESCORE: AutomlRunsRunIdRescore,
        PathValues.AUTOML_RUNS_RUN_ID_STATUS: AutomlRunsRunIdStatus,
        PathValues.AUTOML_RUNS_RUN_ID_STATUS_BATCH_SCORES: AutomlRunsRunIdStatusBatchScores,
        PathValues.AUTOML_RUNS_RUN_ID_USERS: AutomlRunsRunIdUsers,
        PathValues.AUTOML_USERS: AutomlUsers,
        PathValues.BATCH_USER_PERSONAS: BatchUserPersonas,
        PathValues.CLIENT_ACCESS_KEY_ID: ClientAccessKeyId,
        PathValues.HEALTH: Health,
        PathValues.MODULE_TRANSACTIONENRICHMENT_STATISTICS: ModuleTransactionEnrichmentStatistics,
        PathValues.MODULE_TRANSACTIONENRICHMENT_USERS: ModuleTransactionEnrichmentUsers,
        PathValues.PERSONA: Persona,
        PathValues.PERSONA_PERSONA_ID: PersonaPersonaId,
        PathValues.PERSONA_PERSONA_ID_PERCENTILE_SCORE: PersonaPersonaIdPercentileScore,
        PathValues.PERSONA_PERSONA_ID_USERS: PersonaPersonaIdUsers,
        PathValues.STATISTICS_LATEST_MONTH: StatisticsLatestMonth,
        PathValues.USER_USER_ID_CASHFLOW_CATEGORIES: UserUserIdCashflowCategories,
        PathValues.USER_USER_ID_CASHFLOW_HISTORY: UserUserIdCashflowHistory,
        PathValues.USER_USER_ID_CASHFLOW_STATISTICS: UserUserIdCashflowStatistics,
        PathValues.USER_USER_ID_TRANSACTIONS: UserUserIdTransactions,
        PathValues.USER_USER_ID_TRANSACTIONS_STATISTICS: UserUserIdTransactionsStatistics,
        PathValues.USERS_USER_ID_PERSONAS: UsersUserIdPersonas,
    }
)
