import dataclasses

from model.ordine import Ordine


@dataclasses.dataclass

class Arco:
    o1 : Ordine
    o2 : Ordine
    peso : int

