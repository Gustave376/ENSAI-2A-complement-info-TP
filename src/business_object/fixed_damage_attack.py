from business_object.abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):

    def __init__(self, power, name, description):
        super().__init__(power, name, description)

    def compute_damage(self, pokemon1, pokemon2) -> int:
        return self._power
