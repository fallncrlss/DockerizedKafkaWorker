from loguru import logger


logger.add(sink='kafka.log', format='{time} - {level}: {message}',
           level='INFO', rotation='5MB')
