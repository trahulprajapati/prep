
from abc import ABC, abstractmethod

class Donation(ABC):
    @abstractmethod
    def quantity(self):
        pass

class DonateFactory:
    def donatetype(self, type):
        if type == 'cash':
            return MoneyDonation(1000)
        elif type == 'saman':
            return SamanDonation('Reti')

class MoneyDonation(Donation):
    def __init__(self, quant):
        self.quant = quant
    def quantity(self):
        return self.quant

class SamanDonation(Donation):
    def __init__(self, item):
        self.item = item
    def quantity(self):
        return self.item

ob = DonateFactory().donatetype('cash')
print(ob.__class__)
print(ob.quantity())