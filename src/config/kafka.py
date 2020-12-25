from kafka import KafkaConsumer, KafkaProducer

from src.config.core import deserializer, serializer
from src.config.settings import settings


producer: KafkaProducer = KafkaProducer(
    bootstrap_servers=settings.BOOTSTRAP_SERVERS,
    value_serializer=serializer
)

consumer: KafkaConsumer = KafkaConsumer(
    bootstrap_servers=settings.BOOTSTRAP_SERVERS,
    value_deserializer=deserializer,
    consumer_timeout_ms=10000
)
