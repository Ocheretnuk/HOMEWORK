import time

def pause(arg1=2):
    def d(func):
        def wrapper(*args, **kwargs):
            time.sleep(arg1)
            return func(*args, **kwargs)
        return wrapper
    return d