
import logging
from logtail import LogtailHandler
import sys


logger = logging.getLogger()


formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s -%(message)s",
)


stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("brain-api.log")

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


logtail_handler = LogtailHandler(source_token="JkbmGMBfcocxLqFDCGhmZZfK")


logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.addHandler(logtail_handler)

logger.setLevel(logging.INFO)

