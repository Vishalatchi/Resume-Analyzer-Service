import time
import uuid
import logging
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint


logger= logging.getLogger(__name__)

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_time=time.time()
        request_id = str(uuid.uuid4())
        response =await call_next(request)
        process_time =time.time()-request_time
        logger.info(
            f"reqeust_id={request_id},"
            f"method={request.method},"
            f"path={request.url.path},"
            f"status={response.status_code},"
            f"time ={process_time}"
        )
        response.headers["X-Request_ID"]=request_id
        return response


