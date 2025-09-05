from abc import ABC, abstractmethod
from business_object.abstract_attack import AbstractAttack
import random


class AbstractFormulaAttack(AbstractAttack, ABC):

    def __init__(self, power, name, description):
        super().__init__(power, name, description)

    def compute_damage(self, pokemon1, pokemon2) -> int:
        damage = (
            ((2 + 2 * pokemon1.level()/5) * self._power * self.get_attack_stat(pokemon1))
            / (self.get_defense_stat(pokemon2) * 50)
            + 2
        ) * random.uniform(0.58, 1)
        return damage

    @abstractmethod
    def get_attack_stat(pokemon1) -> float:
        pass

    @abstractmethod
    def get_defense_stat(pokemon2) -> float:
        pass
