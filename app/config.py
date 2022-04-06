from pydantic import BaseModel


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "servodroid-logger"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "servodroid.log"
    LOG_FILE_PATH: str = "./logs/"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "file": {
            "formatter": "default",
            "class": "logging.handlers.RotatingFileHandler",
            "level": LOG_LEVEL,
            "filename": LOG_FILE_PATH + LOG_FILE,
            "maxBytes": 10485760,
            "backupCount": 10,
            "encoding": "utf-8",
            "mode": "a",
        },
    }
    loggers = {
        "mycoolapp": {"handlers": ["default"], "level": LOG_LEVEL},
    }
