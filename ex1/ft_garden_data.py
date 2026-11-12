class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


def ft_garden_data() -> None:
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    ft_garden_data()
