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


def ft_plant_growth() -> None:
    plant1 = Plant("Rose", 25.0, 30)
    initial_height = plant1._height
    print("=== Garden Plant Growth ===")
    plant1.show()
    for day in range(7):
        print(f"=== Day {day + 1} ===")
        plant1.grow()
        plant1.age()
        plant1.show()
    growth = plant1._height - initial_height
    print(f"Growth this week: {growth:.1f}cm")


if __name__ == "__main__":
    ft_plant_growth()
