import time, logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        start = time.perf_counter()

        request.request_id = request.headers.get("X-Request-ID")

        response = self.get_response(request)

        time_spent = (time.perf_counter() - start) * 1000
        logger.info(
            f'method={request.method} path={request.path} status={response.status_code} time spent={time_spent}'
        )
        print(f'method={request.method} path={request.path} status={response.status_code} time spent={time_spent}')
        return response


