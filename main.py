# 1. Simple Decorator
def my_decorator(func):
   def wrapper():
       print("Before main func")
       func()
       print("After main func")
   return wrapper

@my_decorator
def say_hello():
   print("Hello, Robocode!")

say_hello()

# 2 Decorator with args.
def log_args(func):
   def wrapper(*args, **kwargs):
       print(f"Args: {args}, {kwargs}")
       return func(*args, **kwargs)
   return wrapper

@log_args
def add(a, b):
   return a + b

print(add(2, 3))

# 3 Decorator with custom args.
def repeat(times):
   def decorator(func):
       def wrapper(*args, **kwargs):
           for i in range(times):
               func(*args, **kwargs)
       return wrapper
   return decorator

@repeat(3)
def greet(name):
   print(f"Greetings, {name}!")
greet("Robocat")

# 3.5
def greet(name):
   print(f"Hello {name}")
greet = repeat(3)(greet)

# 4 Saving original function metadata
from functools import wraps

def decorator_with_wraps(func):
   @wraps(func)
   def wrapper(*args, **kwargs):
       return func(*args, **kwargs)
   return wrapper


def decorator_without_wraps(func):
   def wrapper(*args, **kwargs):
       return func(*args, **kwargs)
   return wrapper


def original_function():
   """Dummy docstring."""
   pass

decorated1 = decorator_with_wraps(original_function)
decorated2 = decorator_without_wraps(original_function)

print("With @wraps:")
print("Name:", decorated1.__name__)
print("Docstring:", decorated1.__doc__)

print("\nWithout @wraps:")
print("Name:", decorated2.__name__)
print("Docstring:", decorated2.__doc__)

# 5 Class as Decorator
class MyDecorator:
   def __init__(self, func):
       self.func = func
   def __call__(self, *args, **kwargs):
       print("Before")
       result = self.func(*args, **kwargs)
       print("After")
       return result

@MyDecorator
def say_hi():
   print("Hi!")

say_hi()
