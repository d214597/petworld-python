import logging
import time
from fastapi import Request

logger = logging.getLogger("main")

# Декоратор для вимірювання часу виконання функцій
def measure_time(func):
    async def wrapper(request: Request, *args, **kwargs):
        start_time = time.time()
        response = await func(request, *args, **kwargs)
        process_time = time.time() - start_time
        logging.info(f"Completed in {process_time:.2f}s | status_code: {response.status_code}")
        return response
    return wrapper

# Middleware для логування запитів
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    formatted_process_time = f"{process_time:.4f}"
    
    log_details = f"{request.method} {request.url} {response.status_code} Time: {formatted_process_time}s"
    logging.info(log_details)
    
    return response
