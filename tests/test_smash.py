import pytest

from smash import CHARACTERS, calculate_damage, create_fighter, fighter_sprite, health_bar


def test_every_fighter_has_required_stats_and_moves():
    required_moves = {"neutral", "side", "up", "down", "final"}

    assert CHARACTERS

    for name, data in CHARACTERS.items():
        assert data["hp"] > 0
        assert data["speed"] > 0
        assert required_moves.issubset(data["moves"])
        assert data["description"]


def test_create_fighter_starts_correctly():
    fighter = create_fighter("Cloud")

    assert fighter == {
        "name": "Cloud",
        "hp": 100,
        "final_meter": 0,
        "limit": 0,
        "ko_meter": 0,
        "used_final": False,
    }


def test_health_bar_is_full_at_max_hp():
    fighter = create_fighter("Mario")

    assert health_bar(fighter) == "[####################]"


def test_fighter_sprite_exists_for_every_character():
    for name in CHARACTERS:
        sprite = fighter_sprite(name)
        assert isinstance(sprite, list)
        assert len(sprite) == 4


def test_damage_uses_base_damage_when_random_bonus_is_zero(monkeypatch):
    monkeypatch.setattr("smash.random.randint", lambda a, b: 0)

    fighter = create_fighter("Mario")
    move_name, damage, critical = calculate_damage(fighter, "neutral")

    assert move_name == "Fireball"
    assert damage == 8
    assert critical is False


def test_cloud_limit_break_adds_damage_and_resets_limit(monkeypatch):
    monkeypatch.setattr("smash.random.randint", lambda a, b: 0)

    fighter = create_fighter("Cloud")
    fighter["limit"] = 100

    move_name, damage, critical = calculate_damage(fighter, "down")

    assert move_name == "Limit Break"
    assert damage == 28
    assert fighter["limit"] == 0
    assert critical is False


def test_little_mac_ko_punch(monkeypatch):
    monkeypatch.setattr("smash.random.randint", lambda a, b: 0)

    fighter = create_fighter("Little Mac")
    fighter["ko_meter"] = 100

    move_name, damage, critical = calculate_damage(fighter, "neutral")

    assert move_name == "KO Punch"
    assert damage == 32
    assert fighter["ko_meter"] == 0
    assert critical is False


def test_ness_magnet_deals_no_damage(monkeypatch):
    monkeypatch.setattr("smash.random.randint", lambda a, b: 0)

    fighter = create_fighter("Ness")

    move_name, damage, critical = calculate_damage(fighter, "down")

    assert move_name == "Magnet"
    assert damage == 0
    assert critical is False


def test_terry_go_moves_are_available(monkeypatch):
    monkeypatch.setattr("smash.random.randint", lambda a, b: 0)

    fighter = create_fighter("Terry")

    geyser_name, geyser_damage, _ = calculate_damage(
        fighter, "power_geyser"
    )
    wolf_name, wolf_damage, _ = calculate_damage(
        fighter, "buster_wolf"
    )

    assert geyser_name == "Power Geyser"
    assert geyser_damage == 40
    assert wolf_name == "Buster Wolf"
    assert wolf_damage == 48
