import dataclasses
import datetime


@dataclasses.dataclass
class Ordine:
    order_id: int
    customer_id: int
    order_status: int
    order_date: datetime.date
    required_date: datetime.date
    shipped_date:datetime.date
    store_id: int
    staff_id: int



    def __hash__(self):
        return hash(self.order_id)
    def __eq__(self, other):
        return self.order_id== other.order_id

    def __str__(self):
        return self.order_id
