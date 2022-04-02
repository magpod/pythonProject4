class ExchangeRateTable:
    def __init__(self,name, effective_date, rates):
        self.name=name
        self.effective_date=effective_date
        self.rates=rates

class ExchangeRate:
    def __init__(self, currency, code, ask_rate, bid_rate):
        self.currency=currency
        self.code=code
        self.ask_rate=ask_rate
        self.bid_rate=bid_rate