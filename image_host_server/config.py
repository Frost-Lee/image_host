import os

ACCEPTED_FORMATS = [
    'jpeg',
    'png',
    'jpg',
    'gif'
]

COMPRESSIBLE_FORMATS = [
    'jpeg',
    'jpg',
    'png'
]

def get_required_env(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Required environment variable {key} is not set")
    return value

CONTAINER_PATH = get_required_env('IMAGE_HOST_CONTAINER_PATH')
DEPLOY_PORT = int(get_required_env('IMAGE_HOST_PORT'))
ACCEPTED_TOKENS = get_required_env('IMAGE_HOST_TOKENS').split(',')
