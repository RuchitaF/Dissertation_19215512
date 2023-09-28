import time
import wrapt

@wrapt.patch_function_wrapper(time, 'clock')
def patched_clock(wrapped, instance, args, kwargs):
    return time.perf_counter()

# Import SQLAlchemy after the time function is patched
import sqlalchemy
