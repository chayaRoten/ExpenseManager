import datetime

def log(log_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                success = True
            except Exception as e:
                result = str(e)
                success = False

            with open(log_file, 'a') as f:
                f.write(f"Function: {func.__name__}, Time: {current_time}, Success: {success}\n")
            return result
        return wrapper
    return decorator

