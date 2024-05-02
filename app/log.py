
from app.models.budget_management import Budget_Management as Budget

def log(original_func):  # the outer function that gets a function as parameter
    def wrapper(*args):  # inner function that uses the original function but wraps it
        print(f'Running function {original_func.__name__} with args {args}')  # print func name and its params
        original_func(*args)  # original function execution
        print(f'{original_func.__name__} is Done')  # printing that function is done
    return wrapper  # return edited function that logs
