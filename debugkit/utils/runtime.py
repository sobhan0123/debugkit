import inspect
import time
import os
import psutil


def get_caller_info():
    frame = inspect.stack()[2]

    file = frame.filename
    line = frame.lineno
    code = frame.code_context[0].strip()

    process = psutil.Process(os.getpid())
    memory = process.memory_info().rss / (1024 * 1024)

    return {
        "file": file,
        "line": line,
        "code": code,
        "time": time.strftime("%H:%M:%S"),
        "memory": memory,
    }
