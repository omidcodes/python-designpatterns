"""Decorator Pattern
🔧 Practice: Write a logging decorator

Create a decorator @log_call that logs the name of the function being called.

Apply it to 2–3 different functions (e.g., add, subtract).

Also log execution time using time.time().

🧠 Bonus: Create a @repeat(n) decorator to repeat a function n times."""


def repeat(n:int):
    def caller(func):
        def wrapper(*args , **kwargs):
            for i in range(n):
                print(f"repeat #{i} : ")
                func(*args , **kwargs)
            return None
        return wrapper
    return caller
    


@repeat(3)
def add(a, b):
    print(a+b)

add(2,5)