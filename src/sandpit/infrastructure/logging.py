import logging

import sandpit

# Grab the uvicorn logger so we can generate logs to the application log
logger = logging.getLogger(f"uvicorn.error.{sandpit.__name__}")
