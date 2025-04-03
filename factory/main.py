from factory.factories import USVehicleFactory, EUVehicleFactory

def main():
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    # Create vehicles using US factory
    us_car = us_factory.create_car("Ford", "Mustang")
    us_bike = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

    # Create vehicles using EU factory
    eu_car = eu_factory.create_car("BMW", "X5")
    eu_bike = eu_factory.create_motorcycle("Yamaha", "MT-07")

    # Start engines
    us_car.start_engine()
    us_bike.start_engine()
    eu_car.start_engine()
    eu_bike.start_engine()

if __name__ == "__main__":
    main()
