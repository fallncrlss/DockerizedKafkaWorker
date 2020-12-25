import json

from src.config.settings import settings


serializer = lambda value: json.dumps(value).encode(settings.ENCODING)
deserializer = lambda value: json.loads(value.decode(settings.ENCODING))
