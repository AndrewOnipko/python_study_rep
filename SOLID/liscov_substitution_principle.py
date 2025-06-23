# Соответствует LSP
# метод message_sender одинаково хорошо работает с базовым классом и его наследниками

from abc import ABC, abstractmethod

class Message(ABC):
    
    @abstractmethod
    def send(self, message, address):
        pass

class EmailMessage(Message):
    def send(self, message: str, address: str):
        print(f"send {message} to {address}")

class SmsMessage(Message):
    def send(self, message: str, address: str):
        print(f"send {message} to {address}")


def message_sender(sender: Message, message: str, address:str):
    sender.send(message, address)

sms_sender = SmsMessage()
email_sender = EmailMessage()

message_sender(sms_sender, "some_message", "+779856634")
message_sender(email_sender, "some_message", "asde@asd.com")

    
# Не соответствует LSP
# метод message_sender в случае работы с CallMessage работает не так как ожидалось, что принципально является нарушением
# метода согласованности наследников ввиду неверно обозначенной ответственности класса

from abc import ABC, abstractmethod

class Message(ABC):
    
    @abstractmethod
    def send(self, message, address):
        pass


class EmailMessage(Message):
    def send(self, message: str, address: str):
        print(f"send {message} to {address}")


class SmsMessage(Message):
    def send(self, message: str, address: str):
        print(f"send {message} to {address}")


class CallMessage(Message):
    def send(self, message, address):
        return(message+address)
    

def message_sender(sender: Message, message: str, address:str):
    sender.send(message, address)

sms_sender = SmsMessage()
email_sender = EmailMessage()
call_sender = CallMessage()

message_sender(sms_sender, "some_message", "+779856634")
message_sender(email_sender, "some_message", "asde@asd.com")
message_sender(call_sender, "some_message", "+779856634")

    