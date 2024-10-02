import logging
import logging.config

def configure_logging():
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'default': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'formatter': 'default',
            },
            'rotating_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'DEBUG',
                'formatter': 'file',
                'filename': 'pet.log',
                'maxBytes': 1024 * 1024,
                'backupCount': 2,
                'encoding': 'utf8',
            },
        },
        'formatters': {
            'default': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
            'file': {
                'format': '%(asctime)s - %(levelname)s - %(message)s',
            },
        },
        'loggers': {
            'uvicorn': {
                'handlers': ['default', 'rotating_file'],
                'level': 'INFO',
                'propagate': True,
            },
            'main': {
                'handlers': ['default', 'rotating_file'],
                'level': 'INFO',
                'propagate': False,
            },
        },
    }
    
    logging.config.dictConfig(logging_config)
