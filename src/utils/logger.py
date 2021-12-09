import os
import logging
import logging.config

LOG_FOLDER = 'logs'
LOG_FILE = 'log.log'
LOG_LEVEL = 'INFO'
LOG_LEVELS = {
    50: 'CRITICAL',
    40: 'ERROR',
    30: 'WARNING',
    20: 'INFO',
    10: 'DEBUG',
    0: 'NOTSET'
}
LOGGER_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file_handler": {
            "class": "logging.FileHandler",
            "formatter": "simple",
            "filename": r"{}\{}".format(LOG_FOLDER, LOG_FILE),
        },
    },
    "formatters": {
        "simple": {
            "format": "[%(levelname)s] %(message)s [%(asctime)s]",
            "datefmt": "%Y:%m:%d - %I:%M:%S"
        }
    },
    "loggers": {
        "": {
            "handlers": ["console", "file_handler"],
            "level": LOG_LEVEL
        }
    }
}


def enable_debug():
    logger.setLevel(logging.DEBUG)


if not os.path.exists(LOG_FOLDER):
    os.mkdir(LOG_FOLDER)

logging.config.dictConfig(LOGGER_CONFIG)  # type: ignore
logger = logging.getLogger()
logger.debug('** LOG LEVEL: {}'.format(LOG_LEVELS[logger.getEffectiveLevel()]))
logger.enable_debug = enable_debug  # type: ignore
