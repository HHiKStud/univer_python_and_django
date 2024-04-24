class Wallet:
    def __init__(self, currency: str = "Rub", name: str = "МойКошелёк", paying_system: str ="MIR", balance: int =0):
        self.currency = currency
        self.name = name
        self.paying_system = paying_system
        self.balance = balance

#    def _protected(self):  # с protected не получилось, надо было на лекции рассмотреть, как это использовать
#        self.balance = 0

    def add_money(self, amount) -> str:
        self.balance += amount
        print(f"На баланс начислено: {amount} {self.currency}")

    def withdraw_money(self, amount):
        if self.balance < amount:
            print("Недостаточно средств")
        else:
            self.balance -= amount
            print(f"Снято с баланса: {amount} {self.currency}")

    def print_balance(self):
        print(f"Баланс: {self.balance} {self.currency}")

    def delete(self):
        print(f"Кошелёк {self.name} удалён") 
        self.balance = 0
        self.currency = "Отсутствует"
        self.name = "Отсутствует"
        self.paying_system = "Отсутствует"

wallet = Wallet("Rub", "СтимКошелек", "MIR")
wallet.add_money(1000)
wallet.print_balance()
wallet.withdraw_money(500)
wallet.print_balance()
wallet.withdraw_money(1000)
wallet.delete()
wallet.print_balance()