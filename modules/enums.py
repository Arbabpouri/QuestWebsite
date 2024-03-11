from enum import IntEnum, StrEnum


class ResponseCode(IntEnum):
    OK = 0
    ERROR = 1
    BAD_DATA = 2
    INVALIED_TOKEN = 3


class ResponseMessage(StrEnum):
    OK = "ok"
    ERROR = "Error in process"
    BAD_DATA = "invalied data"
    INVALIED_TOKEN = "Token is invalied"
