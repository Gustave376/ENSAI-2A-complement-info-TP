from business_object.pokemon.attackerPokemon import AttackerPokemon
from business_object.statistic import Statistic

class TestAttackerPokemon:

    def test_get_pokemon_attack_coef(self):
        # GIVEN
        snorlax = AttackerPokemon(stat_current=Statistic(speed=2000, attack=100))

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 11.5

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
