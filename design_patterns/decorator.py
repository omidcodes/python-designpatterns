"""Decorator Pattern
🔧 Practice: Write a logging decorator

Create a decorator @log_call that logs the name of the function being called.

Apply it to 2–3 different functions (e.g., add, subtract).

Also log execution time using time.time().

🧠 Bonus: Create a @repeat(n) decorator to repeat a function n times."""


def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function named '{func.__name__}' .")
        return func(*args , **kwargs)
    return wrapper

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args , **kwargs)
        end = time.time()
        print(f"Running time in miliseconds= '{(end-start) * 1000}' .")
        return result
    return wrapper


def repeat(n:int):
    def caller(func):
        def wrapper(*args , **kwargs):
            for i in range(n):
                print(f"repeat #{i} : ")
                func(*args , **kwargs)
            return None
        return wrapper
    return caller
    


@log_execution_time
@log_call
def add(a, b):
    print(a+b)

add(2,5)