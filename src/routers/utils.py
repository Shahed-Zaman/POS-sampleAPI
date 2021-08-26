from fastapi import Response
import json
from utils.logger import logger

def setResponse(statusCode: int, message: str=None, returnBodyJson: dict={}):
    if message is not None:
        returnBodyJson["message"] = message
        if statusCode >= 400    :  logger.warning(message)
        elif statusCode >= 500  : logger.error(message)
    return Response(content=json.dumps(returnBodyJson), status_code=statusCode)

