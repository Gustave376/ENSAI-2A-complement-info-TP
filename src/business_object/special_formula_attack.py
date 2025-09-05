from business_object.abstract_formula_attack import AbstractAttack


class SpecialFormulaAttack(AbstractAttack):

    def __init__(self, power, name, description):
        super().__init__(power, name, description)

    def get_attack_stat(self, pokemon1):
        return pokemon1.sp_atk_current()

    def get_defense_stat(self, pokemon2):
        return pokemon2.sp_def_current()
