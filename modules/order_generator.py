import json
import random
import uuid
from datetime import datetime, timedelta


class Order:
    def __init__(self):
        merchant = random.choice(["lungolini", "merchantX", "merchantY"])
        self.id = str(uuid.uuid4())
        self.number = str(random.randint(1000000, 9999999))
        self.date = datetime.now().isoformat() + "Z"
        self.status = random.choice(["paid", "unpaid", "processing"])
        self.orderState = random.choice(["Cancelled", "Completed", "Pending"])
        self.customerName = random.choice(["John Doe", "Jane Smith", "Raeli Desnel"])
        self.items = [
            {
                "productId": str(uuid.uuid4()),
                "productName": random.choice(["Shoes", "Bag", "Shirt"]),
                "sizeValue": random.choice(["M", "L", "XL", "XXL"]),
                "price": round(random.uniform(200, 900), 2),
                "currency": "USD",
                "merchant": merchant,
                "merchantProductId": f"{merchant}_" + str(random.randint(1000, 9999)),
                "merchantSkuId": f"{merchant}_" + str(random.randint(1000, 9999)),
                "fulfilmentReference": "FR_" + str(random.randint(1000, 9999)),
                "isSourceRequest": random.choice([True, False]),
                "merchantPriceCurrencyCode": "EUR",
                "merchantPrice": round(random.uniform(10, 200), 2),
            }
        ]
        self.totalBeforeDiscounts = round(random.uniform(250, 900), 2)
        self.discounts = round(random.uniform(10, 50), 2)
        self.total = self.totalBeforeDiscounts - self.discounts
        self.currency = "USD"
        self.charges = [
            {
                "id": str(uuid.uuid4()),
                "amount": self.total,
                "currency": "USD",
                "payment": {
                    "date": (datetime.now() - timedelta(days=1)).isoformat() + "Z",
                    "amount": self.total,
                    "currency": "USD",
                    "paymentService": random.choice(["stripe", "paypal"]),
                    "paymentReference": str(uuid.uuid4()),
                },
            }
        ]
        self.isRefunded = random.choice([True, False])
        self.amountRefunded = round(random.uniform(0, self.total), 2) if self.isRefunded else 0
        self.refundedDate = datetime.now().isoformat() + "Z" if self.isRefunded else None
        self.fees = 0.0
        self.promoCodeActivationToken = random.choice(["DISCOUNT10", "SUMMER2024", "LAST10"])
        self.shippingFees = 0
        self.email = f"user{random.randint(1, 1000)}@mail.com"
        self.source = random.choice(["WebPortal", "MobileApp", "POS"])
        self.externalOrderId = ""

    def to_json(self):
        return json.dumps(self.__dict__)