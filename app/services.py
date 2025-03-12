from app.models import Event


class Account:
    def __init__(self):
        self.balances = {}

    def reset(self):
        self.balances = {}
        return True

    def get_account(self, account_id: str):
        if account_id in self.balances:
            return self.balances[account_id]

    def get_balance(self, account_id: str):
        return self.balances.get(account_id, 0)

    def deposit(self, account_id: str, amount: int):
        self.balances[account_id] = self.get_balance(account_id) + amount

    def withdraw(self, account_id: str, amount: int) -> bool:
        if self.get_balance(account_id) >= amount:
            self.balances[account_id] -= amount
            return True
        return False

    def process_event(self, event: Event):
        if event.type == "deposit":
            self.deposit(event.destination, event.amount)
            return {"destination": {"id": event.destination,
                                    "balance": self.get_balance(event.destination)}}

        elif event.type == "withdraw":
            if self.withdraw(event.origin, event.amount):
                return {"origin": {"id": event.origin, "balance": self.get_balance(event.origin)}}
            return None

        elif event.type == "transfer":
            if self.get_balance(event.origin) >= event.amount:
                self.withdraw(event.origin, event.amount)
                self.deposit(event.destination, event.amount)
                return {
                    "origin": {"id": event.origin, "balance": self.get_balance(event.origin)},
                    "destination": {"id": event.destination, "balance": self.get_balance(event.destination)}
                }
            return None

        return None


account = Account()