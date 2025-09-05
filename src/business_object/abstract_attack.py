from abc import ABC, abstractmethod


class AbstractAttack(ABC):

    def __init__(self, power, name, description):
        self._power: int = power
        self._name: int = name
        self._description: str = description

    @abstractmethod
    def compute_damage(self, pokemon1, pokemon2) -> int:
        pass
