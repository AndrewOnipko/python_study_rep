# Хорошо - соответствуем SRP
class User:
    def __init__(self, name: str, email:str, number: int):
        self.name = name
        self.email = email
        self.number = number

    def save_email_in_db(self):
        print(f"Емейл {self.email} для {self.name} сохранен")
    
    def say_hello_to_user(self):
        print(f"Hello, {self.name}")
        
    
# А далее, при необходимости, классы для взаимодействия с базой данных, какими либо рассчетами т.д.

# Плохо - нарушаем SRP
class User:
    def __init__(self, name: str, email:str, number: int):
        self.name = name
        self.email = email
        self.number = number

    def save_email_in_db(self):
        print(f"Емейл {self.email} для {self.name} сохранен")
    
    def say_hello_to_user(self):
        print(f"Hello, {self.name}")
    
    def call(self):
        pass

    def calculate_trager_share(self, target_share):
        pass


