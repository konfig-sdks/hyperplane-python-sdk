import typing_extensions

from hyperplane_python_sdk.apis.tags import TagValues
from hyperplane_python_sdk.apis.tags.auto_ml_service_api import AutoMLServiceApi
from hyperplane_python_sdk.apis.tags.personas_api import PersonasApi
from hyperplane_python_sdk.apis.tags.enriched_transactions_api import EnrichedTransactionsApi
from hyperplane_python_sdk.apis.tags.users_api import UsersApi
from hyperplane_python_sdk.apis.tags.auth_api import AuthApi
from hyperplane_python_sdk.apis.tags.client_api import ClientApi
from hyperplane_python_sdk.apis.tags.health_api import HealthApi
from hyperplane_python_sdk.apis.tags.statistics_api import StatisticsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTO_ML_SERVICE: AutoMLServiceApi,
        TagValues.PERSONAS: PersonasApi,
        TagValues.ENRICHED_TRANSACTIONS: EnrichedTransactionsApi,
        TagValues.USERS: UsersApi,
        TagValues.AUTH: AuthApi,
        TagValues.CLIENT: ClientApi,
        TagValues.HEALTH: HealthApi,
        TagValues.STATISTICS: StatisticsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTO_ML_SERVICE: AutoMLServiceApi,
        TagValues.PERSONAS: PersonasApi,
        TagValues.ENRICHED_TRANSACTIONS: EnrichedTransactionsApi,
        TagValues.USERS: UsersApi,
        TagValues.AUTH: AuthApi,
        TagValues.CLIENT: ClientApi,
        TagValues.HEALTH: HealthApi,
        TagValues.STATISTICS: StatisticsApi,
    }
)
