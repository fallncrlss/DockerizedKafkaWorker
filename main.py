from typing import NoReturn

from src.config.settings import settings
from src.utils import publish_api_response


def main() -> NoReturn:
    endpoint_url: str = settings.API_URL + '/users'
    publish_api_response(endpoint=endpoint_url, topic=settings.VAULT_TOPIC)
    # print(get_info_from_topic(topic=settings.VAULT_TOPIC))


if __name__ == '__main__':
    main()
