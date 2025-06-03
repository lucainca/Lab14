import dataclasses


@dataclasses.dataclass

class Store:
    store_id: int
    store_name: str
    phone:str
    email:str
    street:str
    city:str
    state:str
    zip_code:int

    def __hash__(self):
        return hash(self.store_id)