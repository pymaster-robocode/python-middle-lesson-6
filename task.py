from functools import wraps

class Player:
    mana = 100

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Виконується дія: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def magic_effect(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Магічний ефект {i+1}/{times}:")
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
                print(f"-{self.cost} мани. Залишилось: {Player.mana}")
                return func(*args, **kwargs)
            else:
                print("Недостатньо мани!")
        return wrapper

@log_action
@ManaCost(30)
@magic_effect(2)
def firestorm():
    print("🔥🌪 Вогняний шторм!")

@log_action
@ManaCost(50)
def heal():
    print("💖 Гравець відновив здоров'я!")

# Меню
while True:
    print("\n=== Дії ===")
    print("1. Вогняний шторм")
    print("2. Лікування")
    print("3. Вийти")
    choice = input("Оберіть дію: ")
    if choice == "1":
        firestorm()
    elif choice == "2":
        heal()
    elif choice == "3":
        break
