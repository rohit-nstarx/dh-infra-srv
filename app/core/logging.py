# logger.py
import os
import logging
import json


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, "%Y-%m-%d %H:%M:%S"),
            "level": record.levelname,
            "name": record.name,
            "filename": record.filename,
            "line": record.lineno,
            "function": record.funcName,
            "message": record.getMessage(),
        }
        return json.dumps(log_record)


def setup_logging():
    formatter = JsonFormatter()

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    # Your app logger
    app_logger = logging.getLogger("app")
    app_logger.setLevel(level=os.environ.get("LOG_LEVEL", "INFO"))
    app_logger.addHandler(handler)
    app_logger.propagate = False

    # # Uvicorn loggers
    # for name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
    #     uvicorn_logger = logging.getLogger(name)
    #     uvicorn_logger.handlers = []  # remove default handler
    #     uvicorn_logger.setLevel(logging.INFO)
    #     uvicorn_logger.addHandler(handler)


logger = logging.getLogger("app")
