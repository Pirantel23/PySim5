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
        if json['sms'] is None: return
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
    def __init__(self, target: str, operator: str, country: str, json: dict) -> None:
        self.target: Target = Target(target)
        self.cost: float = json['cost']
        self.count: int = json['count']
        self.operator: str = operator
        self.country: Country = Country(country)

    def __repr__(self) -> str:
        return f"Product(target={self.target}, country={self.country}, cost={self.cost}, count={self.count}, operator={self.operator})"
    
    def __lt__(self, other) -> bool:
        return self.cost < other.cost
    
    def __gt__(self, other) -> bool:
        return self.cost > other.cost


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

    def get_products_by_country(self, country: Country) -> list[Product]:
        products: list[Product] = []
        data = send_request(f"https://{self.domain}/v1/guest/prices?country={country.value}", {"Accept": self._accept_str})[country.value]
        
        for target, other in data.items():
            for operator, info in other.items():
                try:
                    product = Product(target, operator, country, info)
                except ValueError:
                    continue
                if product.count == 0: continue
                products.append(product)
        return products
    
    def get_products_by_target(self, target: Target) -> list[Product]:
        products: list[Product] = []
        data = send_request(f"https://{self.domain}/v1/guest/prices?product={target.value}", {"Accept": self._accept_str})[target.value]
        
        for country, other in data.items():
            for operator, info in other.items():
                try:
                    product = Product(target, operator, country, info)
                except ValueError:
                    continue
                if product.count == 0: continue
                products.append(product)
        return products
    
    def get_products_by_target_and_country(self, target: Target, country: Country) -> list[Product]:
        products: list[Product] = []
        data = send_request(f"https://{self.domain}/v1/guest/prices?product={target.value}&country={country.value}", {"Accept": self._accept_str})[country.value][target.value]
        
        for operator, other in data.items():
            try:
                product = Product(target, operator, country, other)
            except ValueError:
                continue
            if product.count == 0: continue
            products.append(product)
        return products
    
    def buy_number(self, country: Country = Country.Any, target: Target = Target.Any, operator: str = 'any') -> Order:
        return Order(send_request(f'https://{self.domain}/v1/user/buy/activation/{country.value}/{operator}/{target.value}', {"Authorization": self._api_str, "Accept": self._accept_str}))

    def rebuy_number(self, target: Target, number: str) -> None:
        send_request(f'https://{self.domain}/v1/user/reuse/{target.value}/{number[1:]}', {"Authorization": self._api_str, "Accept": self._accept_str})

    def check_order(self, id: int) -> Order:
        return Order(send_request(f'https://{self.domain}/v1/user/check/{id}', {"Authorization": self._api_str, "Accept": self._accept_str}))

    def finish_order(self, id: int) -> Order:
        return Order(send_request(f'https://{self.domain}/v1/user/finish/{id}', {"Authorization": self._api_str, "Accept": self._accept_str}))
    
    def cancel_order(self, id: int) -> Order:
        return Order(send_request(f'https://{self.domain}/v1/user/cancel/{id}', {"Authorization": self._api_str, "Accept": self._accept_str}))
    
    def finish_order(self, id: int) -> Order:
        return Order(send_request(f'https://{self.domain}/v1/user/ban/{id}', {"Authorization": self._api_str, "Accept": self._accept_str}))

    def get_sms(self, id: int) -> list[SMS]:
        return send_request(f'https://{self.domain}/v1/user/sms/inbox/{id}', {"Authorization": self._api_str, "Accept": self._accept_str})


