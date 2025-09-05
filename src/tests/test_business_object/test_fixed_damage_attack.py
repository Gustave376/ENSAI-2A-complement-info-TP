from business_object.fixed_damage_attack import FixedDamageAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon


class TestFixedDamageAttack:

    def test_compute_damage(self):

        # GIVEN
        pokemon1 = AttackerPokemon()
        pokemon2 = AttackerPokemon()
        attack = FixedDamageAttack(
            power=0, name="trempette", description="Le pokemon fait trempette"
        )

        # WHEN
        damage = attack.compute_damage(pokemon1, pokemon2)

        # THEN
        assert damage == 0


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
