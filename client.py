from request_handler import send_request
from enums import PaymentType, Target, Country, Status
from datetime import datetime


class Profile:
    def __init__(self, json: dict) -> None:
        self.id: int = json['id']
        self.email: str = json['email']
        self.balance: float = json['balance']
        self.rating: float = json['rating']
        self.country: Country = Country(json['default_country']['name'])

    def __repr__(self) -> str:
        return f"Profile(id={self.id}, email={self.email}, balance={self.balance}, rating={self.rating}, country={self.country})"
    

class Order:
    def __init__(self, json) -> None:
        self.id: int = json['id']
        self.phone: str = json['phone']
        self.operator: str = json['operator']
        self.product: Target = Target(json['product'])
        self.price: float = json['price']
        self.status: Status = Status(json['status'])
        self.expires: datetime = datetime.strptime(json['expires'], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.country: Country = Country(json['country'])
        self.sms_list: list[SMS] = [SMS(sms) for sms in json['sms']]

    def __repr__(self) -> str:
        return f"Order(id={self.id}, phone={self.phone}, operator={self.operator}, product={self.product}, " \
               f"price={self.price}, status={self.status}, expires={self.expires}, country={self.country}, sms={self.sms_list})"


class SMS:
    def __init__(self, json) -> None:
        self.date: datetime = datetime.strptime(json['date'], "%Y-%m-%dT%H:%M:%SZ")
        self.sender: str = json['sender']
        self.text: str = json['text']
        self.code: str = json['code']
    
    def __repr__(self) -> str:
        return f"SMS(date={self.date}, sender={self.sender}, text={self.text}, code={self.code})"


class Payment:
    def __init__(self, json) -> None:
        self.id: int = json['ID']
        self.type: PaymentType = PaymentType(json['TypeName'])
        self.provider: str = json['ProviderName']
        self.amount: float = json['Amount']
        self.balance: float = json['Balance']
        self.date: datetime = datetime.strptime(json['CreatedAt'], "%Y-%m-%dT%H:%M:%S.%fZ")

    def __repr__(self) -> str:
        return f"Payment(id={self.id}, type={self.type}, provider={self.provider}, amount={self.amount}, balance={self.balance}, date={self.date})"


class Product:
    def __init__(self, target: str, operator: str, json: dict) -> None:
        self.target: Target = Target(target)
        self.cost: float = json['cost']
        self.count: int = json['count']
        self.operator: str = operator

    def __repr__(self) -> str:
        return f"Product(target={self.target}, cost={self.cost}, count={self.count}, operator={self.operator})"


class Client:
    def __init__(self, api_key: str, domain: str = '5sim.biz'):
        self.api_key: str = api_key
        self.domain: str = domain
        self._api_str: str = f"Bearer {self.api_key}"
        self._accept_str: str = "application/json"

    def get_profile(self) -> Profile:
        return Profile(send_request(f'https://{self.domain}/v1/user/profile', {"Authorization": self._api_str, "Accept": self._accept_str}))
    
    def get_order_history(self) -> list[Order]:
        return [Order(order) for order in send_request(f"https://{self.domain}/v1/user/orders?category=activation", {"Authorization": self._api_str, "Accept": self._accept_str})['Data']]

    def get_payment_history(self) -> list[Payment]:
        return [Payment(payment) for payment in send_request(f"https://{self.domain}/v1/user/payments", {"Authorization": self._api_str, "Accept": self._accept_str})['Data']]

    def get_products(self, country: Country) -> list[Product]:
        products: list[Product] = []
        data = send_request(f"https://{self.domain}/v1/guest/prices?country={country.value}", {"Accept": self._accept_str})[country.value]
        for target, other in data.items():
            for operator, info in other.items():
                try:
                    product = Product(target, operator, info)
                except ValueError:
                    continue
                products.append(product)
        return products

    
cl = Client("eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTk4MjIzMzAsImlhdCI6MTY4ODI4NjMzMCwicmF5IjoiMWViNzIwODAxMjM1ZTc0NTc1YzI2ZDQwMDFlM2VlZDQiLCJzdWIiOjEyNDI2MDl9.COD7sYIAS4zokp2lMizjdEbA6Yqm33qFZXifNDoSJL7H7piRYLONu5qW7nBROX9z2VhPSbn6XGidnLFadPrYXmR5F1_PHJReE8RyIxNk1-85YA4DUnbBSFCaojuzLgdyCjjc-FmsqlUUwnKp1yZJxOxERkhrk1_WUE0EPynugmYFzuamx1WdK1YZKm0Z-rSXfphMuMzK600JxodAlFrnhrz6oaP-m2xca1VzFFUXyRD0MgDHIxCFtGqBUQKKs4rwMJWXnNxNvObsOFuC3EmUf3Ysof5Iu6ydF1GC3w2ehVbnnG-hemCkc6ax3QrMyw_rSO6IQxMr9drySFGTtPAC1A")
data = cl.get_products(Country.Zimbabwe)
print(data)