from fastapi.requests import Request
from starlette.responses import JSONResponse


class APIException(Exception):
    def __init__(self, status_code, message: str = '', *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

        self.message = message
        self.status_code = status_code


async def on_api_exception(request: Request, exception: APIException) -> JSONResponse:
    response = {
        "content": {"error": exception.message},
        "status_code": exception.status_code
    }
    return JSONResponse(**response)
