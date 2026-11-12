class Plant:
    def __init__(
        self,
        name: str = "Unknown plant",
        height: float = 0.0,
        age: int = 0,
    ) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age

        print("Plant created: ", end="")
        self.show()

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def show(self) -> None:
        print(
            f"{self._name.capitalize()}: {self._height:.1f}cm, "
            f"{self._age} days old"
        )


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 15.0, 10)
    print()
    plant1.set_height(25)
    plant1.set_age(30)
    print()
    plant1.set_height(-1)
    plant1.set_age(-1)
    print()
    print("Current state: ", end="")
    plant1.show()


if __name__ == "__main__":
    ft_garden_security()
