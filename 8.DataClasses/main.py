from cars import Nine
from planes import Tu154
from ships import Titanik


def main():
    sport_car = Nine(80000, 69, 900, 500)
    sport_plane = Tu154(120000, 75, 1100, 850)
    sport_ship = Titanik(160000, 77, 1400, 1000)

    print(sport_car.type_model, sport_car)
    sport_car.moving(sport_car.get_type_model(sport_car.type_model), 11)
    print(sport_plane.type_model, sport_plane)
    print(sport_ship.type_model, sport_ship)


if __name__ == "__main__":
    main()
