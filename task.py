from functools import wraps


class Player:
   mana = 100


def log_action(func):
   @wraps(func)
   def wrapper(*args, **kwargs):
       print(f"Performing action: {func.__name__}")
       return func(*args, **kwargs)
   return wrapper


def magic_effect(times):
   def decorator(func):
       @wraps(func)
       def wrapper(*args, **kwargs):
           for i in range(times):
               print(f"Magic effect {i+1}/{times}:")
               func(*args, **kwargs)
       return wrapper
   return decorator


class ManaCost:
   def __init__(self, cost):
       self.cost = cost
   def __call__(self, func):
       @wraps(func)
       def wrapper(*args, **kwargs):
           if Player.mana >= self.cost:
               Player.mana -= self.cost
               print(f"-{self.cost} mana. Remaining: {Player.mana}")
               return func(*args, **kwargs)
           else:
               print("Not enough mana!")
       return wrapper
@log_action
@ManaCost(30)
@magic_effect(2)
def firestorm():
   print("🔥🌪 Firestorm!")


@log_action
@ManaCost(50)
def heal():
   print("💖 Player healed!")
while True:
   print("\n=== Actions ===")
   print("1. Firestorm")
   print("2. Heal")
   print("3. Exit")
   choice = input("Choose an action: ")
   if choice == "1":
       firestorm()
   elif choice == "2":
       heal()
   elif choice == "3":
       break
