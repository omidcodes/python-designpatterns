"""
1️⃣ Singleton Pattern
🔧 Practice: Create a Logger class

Ensure only one instance of the logger is ever created.

Use __new__ to enforce the singleton.

Add a method log(message) to print or store log entries.

🧠 Bonus: Make it thread-safe using threading.Lock.
"""


import threading

class Logger:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                print("Creating New object")
                cls._instance = super().__new__(cls)
        else:
            print("Object (instance) already exists, returning the current object.")
        return cls._instance

    def log(self, message):
        print(f"[{threading.current_thread().name}] -> {message}")


logger_obj = Logger()
logger_obj.log("Hello 1")


logger_obj = Logger()
logger_obj.log("Hello 2")