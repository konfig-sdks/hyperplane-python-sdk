operation_parameter_map = {
    '/auth/token-POST': {
        'parameters': [
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
        ]
    },
    '/automl/lookalike-POST': {
        'parameters': [
            {
                'name': 'engagement_type'
            },
            {
                'name': 'positive_label_users'
            },
            {
                'name': 'negative_label_users'
            },
            {
                'name': 'run_description'
            },
            {
                'name': 'model_version'
            },
            {
                'name': 'module-id'
            },
        ]
    },
    '/automl/runs-GET': {
        'parameters': [
            {
                'name': 'module-id'
            },
        ]
    },
    '/automl/users-GET': {
        'parameters': [
            {
                'name': 'module-id'
            },
            {
                'name': 'page_number'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/automl/runs/{run_id}/status-GET': {
        'parameters': [
            {
                'name': 'run_id'
            },
        ]
    },
    '/automl/runs/{run_id}/status_batch_scores-GET': {
        'parameters': [
            {
                'name': 'run_id'
            },
        ]
    },
    '/automl/runs/{run_id}-GET': {
        'parameters': [
            {
                'name': 'run_id'
            },
        ]
    },
    '/automl/runs/{run_id}/users-POST': {
        'parameters': [
            {
                'name': 'run_id'
            },
            {
                'name': 'allow_users'
            },
            {
                'name': 'block_users'
            },
            {
                'name': 'tag_filters'
            },
            {
                'name': 'page_number'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/automl/runs/{run_id}/rescore-POST': {
        'parameters': [
            {
                'name': 'run_id'
            },
        ]
    },
    '/automl/runs/{run_id}/generate_batch_scores-POST': {
        'parameters': [
            {
                'name': 'run_id'
            },
            {
                'name': 'module-id'
            },
        ]
    },
    '/client/{access_key_id}-GET': {
        'parameters': [
            {
                'name': 'access_key_id'
            },
        ]
    },
    '/user/{user_id}/transactions-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'module-id'
            },
            {
                'name': 'page_number'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'flow_type'
            },
            {
                'name': 'min_amount'
            },
            {
                'name': 'max_amount'
            },
            {
                'name': 'account_type'
            },
            {
                'name': 'categories'
            },
            {
                'name': 'search_name'
            },
        ]
    },
    '/module/transaction-enrichment/statistics-GET': {
        'parameters': [
            {
                'name': 'module-id'
            },
        ]
    },
    '/user/{user_id}/cashflow/categories-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'module-id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'account_type'
            },
        ]
    },
    '/user/{user_id}/cashflow/history-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'module-id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'aggregation'
            },
            {
                'name': 'account_type'
            },
        ]
    },
    '/user/{user_id}/cashflow/statistics-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'module-id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
        ]
    },
    '/user/{user_id}/transactions/statistics-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'module-id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'flow_type'
            },
            {
                'name': 'min_amount'
            },
            {
                'name': 'max_amount'
            },
            {
                'name': 'account_type'
            },
        ]
    },
    '/module/transaction-enrichment/users-GET': {
        'parameters': [
            {
                'name': 'module-id'
            },
            {
                'name': 'user_id_prefix'
            },
            {
                'name': 'page_number'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/health-GET': {
        'parameters': [
        ]
    },
    '/persona-POST': {
        'parameters': [
            {
                'name': 'persona_name'
            },
            {
                'name': 'company_facets'
            },
            {
                'name': 'demographic_facets'
            },
            {
                'name': 'interest_facets'
            },
            {
                'name': 'locations'
            },
            {
                'name': 'pre_defined_personas'
            },
            {
                'name': 'model_version'
            },
        ]
    },
    '/persona/{persona_id}-DELETE': {
        'parameters': [
            {
                'name': 'persona_id'
            },
        ]
    },
    '/batch/user/personas-POST': {
        'parameters': [
            {
                'name': 'user_ids'
            },
            {
                'name': 'module-id'
            },
            {
                'name': 'month'
            },
            {
                'name': 'persona_score_threshold'
            },
        ]
    },
    '/persona/{persona_id}/percentile_score-GET': {
        'parameters': [
            {
                'name': 'persona_id'
            },
            {
                'name': 'percentile'
            },
            {
                'name': 'module-id'
            },
            {
                'name': 'month'
            },
        ]
    },
    '/persona/{persona_id}-GET': {
        'parameters': [
            {
                'name': 'persona_id'
            },
            {
                'name': 'module-id'
            },
            {
                'name': 'month'
            },
            {
                'name': 'persona_score_threshold'
            },
        ]
    },
    '/persona/{persona_id}/users-POST': {
        'parameters': [
            {
                'name': 'blocklist'
            },
            {
                'name': 'branch'
            },
            {
                'name': 'persona_id'
            },
            {
                'name': 'birth_date'
            },
            {
                'name': 'cbo_code'
            },
            {
                'name': 'declared_monthly_income'
            },
            {
                'name': 'job_title'
            },
            {
                'name': 'module-id'
            },
            {
                'name': 'page_number'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'month'
            },
            {
                'name': 'persona_score_threshold'
            },
        ]
    },
    '/persona-GET': {
        'parameters': [
            {
                'name': 'facet_types'
            },
            {
                'name': 'module-id'
            },
            {
                'name': 'page_number'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/users/{user_id}/personas-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'module-id'
            },
            {
                'name': 'month'
            },
            {
                'name': 'persona_score_threshold'
            },
        ]
    },
    '/statistics/latest_month-GET': {
        'parameters': [
        ]
    },
    '/batch/user/personas-POST': {
        'parameters': [
            {
                'name': 'user_ids'
            },
            {
                'name': 'module-id'
            },
            {
                'name': 'month'
            },
            {
                'name': 'persona_score_threshold'
            },
        ]
    },
    '/users/{user_id}/personas-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'module-id'
            },
            {
                'name': 'month'
            },
            {
                'name': 'persona_score_threshold'
            },
        ]
    },
};