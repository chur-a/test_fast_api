PROJECT_NAME: str = 'TestSearcher'
VERSION: str = '1.0.0'

POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '5432'
POSTGRES_DB = 'test_fast_api'
POSTGRES_USER = 'username'
POSTGRES_PASSWORD = 'password'

DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

ELASTICSEARCH_HOST = 'localhost'
ELASTICSEARCH_PORT = '9200'
ELASTICSEARCH_USERNAME = 'username'
ELASTICSEARCH_PASSWORD = 'password'

ELASTICSEARCH_PATH_TO_CERTIFICATE = 'C:\Program Files (x86)\elasticsearch-8.5.0\config\certs\http_ca.crt'

ELASTICSEARCH_NAME_OF_INDEX = 'documents'

ELASTICSEARCH_URL: str = \
    f'https://{ELASTICSEARCH_USERNAME}:{ELASTICSEARCH_PASSWORD}@{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}'
