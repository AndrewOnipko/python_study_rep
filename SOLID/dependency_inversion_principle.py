from abc import ABC, abstractmethod

class DbController(ABC):
    @abstractmethod
    def send_to_db(self, message):
        pass
        
class BidCalculator(ABC):
    @abstractmethod
    def calculate_bid(self, bid):
        pass

class PGController(DbController):

    def send_to_db(self, message: str):
        print(f"Послали сообщение {message} в postgres базу данных")


class MYSQLController(DbController):

    def send_to_db(self, message: str):
        print(f"Послали сообщение {message} в mysql базу данных")


class TargetBidCalculator(BidCalculator):

    def calculate_bid(self, bid: int):
        target_bid = bid - 1
        print(f"Посчитали target_bid {target_bid}")
        return target_bid
    

class BusinessLogicService:
    def __init__(self, db_controller: DbController, bid_calculator: BidCalculator):
        self.db_controller = db_controller
        self.bid_calculator = bid_calculator

    def proccess_bid(self):
        calculated_bid = self.bid_calculator.calculate_bid(100)
        message = f"Итоговая ставка: {calculated_bid}"
        self.db_controller.send_to_db(message)


def main():
    # Создаются конкретные контроллеры-модули нижнего уровня(интерфейс), затем создается модуль верхнего уровня(клиент)
    # и сервис(бизнес логика) не зависит от конкретных реализаций, а только от абстрактных методов
    pg_controller = PGController()
    bid_controller = TargetBidCalculator()
    mysql_controller = MYSQLController()
    bid_calculator = BusinessLogicService(pg_controller, bid_controller)
    bid_calculator.proccess_bid()
    bid_calculator = BusinessLogicService(mysql_controller, bid_controller)
    bid_calculator.proccess_bid()

if __name__ == '__main__':
    main()