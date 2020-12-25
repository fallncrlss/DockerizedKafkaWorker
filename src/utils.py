from typing import Any, List, Optional

from requests import Response
from loguru import logger
import requests

from src.config.kafka import consumer, producer


def fetch(url: str) -> Optional[Response]:
    """Fetch response from requested URL.

    :param url: requested string.
    :returns: response from request or None.
    """
    response: Response = requests.get(url=url)
    if not response.ok:
        return logger.error(f'{response.url} - {response.status_code} - '
                            f'{response.reason}')
    return response


def publish_api_response(endpoint: str, topic: str) -> None:
    """Send api endpoint response data to Kafka topic.

    :param endpoint: API endpoint of API_URL. See src/config/settings.toml
    :param topic: Kafka topic name.
    :returns: None
    """
    api_response: Optional[Response] = fetch(endpoint)
    if api_response:
        try:
            data_response: dict = api_response.json()
        except ValueError:
            error_message: str = f'Invalid response data from ' \
                                 f'{api_response.url}. Abort'
            return logger.error(error_message)

        try:
            producer.send(topic=topic, value=data_response)
            # producer.flush()
        except Exception as error:
            return logger.error(error)
        else:
            info_message: str = f'Successfully added response ' \
                                f'from {api_response.url} ' \
                                f'to topic {topic} ' \
                                f'with code {api_response.status_code} ' \
                                f'and response data: {data_response}'
            logger.info(info_message)


def get_info_from_topic(topic: str) -> List[Any]:
    """Get info from Kafka topic.

    :param topic: kafka topic name to extract data.
    :returns: data list from topic.
    """
    consumer.subscribe([topic])
    info: List[Any] = [event.value for event in consumer]
    consumer.unsubscribe()
    return info
