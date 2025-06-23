# Хорошо, соответствует ISP, класс наследник включает в себя оба интерфейса, но, при необходимости он может включать только один и
# не нужно будет реализовывать неподдерживаемые методы (как у Олега), метод demonstrate_skills также можно вынести в отдельный интерфейс
# чтобы сегрегировать ответственность и соблюсти принцип наследования Интерфейс - Клиент 

from abc import ABC, abstractmethod

class Student(ABC):
    @abstractmethod
    def study(self):
        pass

class Singer(ABC):
    @abstractmethod
    def sing(self):
        pass

class Stepan(Student, Singer):
    def __init__(self, study_object: str, song_name: str):
        self.study_object = study_object
        self.song_name = song_name
        
    def study(self):
        print(f"Степан изучает {self.study_object}")

    def sing(self):
        print(f"Степан поет {self.song_name}")

    def demonstrate_skills(self):
        self.study()
        self.sing()


class Oleg(Singer):
    def __init__(self, song_name: str):
        self.song_name = song_name
        
    def sing(self):
        print(f"Олег поет {self.song_name}")

    def demonstrate_skills(self):
        self.sing()


first_student = Stepan("История", "Песня")
second_student = Oleg("Песня2")

first_student.demonstrate_skills()
second_student.demonstrate_skills()