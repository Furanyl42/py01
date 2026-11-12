class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age_in_days: int = age

    def show(self) -> None:
        print(
            f"{self._name.capitalize()}: {self._height:.1f}cm, "
            f"{self._age_in_days} days old"
        )

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age_in_days += 1


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    plants: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
