class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def increment_grow(self) -> None:
            self._grow_calls += 1

        def increment_age(self) -> None:
            self._age_calls += 1

        def increment_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self._stats = self.Statistics()

    def get_name(self) -> str:
        return self._name

    def grow(self, amount: float) -> None:
        self._height += amount
        self._stats.increment_grow()

    def age(self, days: int) -> None:
        self._age += days
        self._stats.increment_age()

    def show(self) -> None:
        self._stats.increment_show()
        print(
            f"{self._name}: {self._height:.1f}cm, {self._age} days old"
        )

    def show_statistics(self) -> None:
        self._stats.display()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.is_bloomed: bool = False

    def bloom(self) -> None:
        self.is_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self._num_seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        if self._num_seeds == 0:
            self._num_seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._num_seeds}")


class Tree(Plant):
    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._produce_shade_calls: int = 0

        def increment_shade(self) -> None:
            self._produce_shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._produce_shade_calls} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter
        self._tree_stats = self.TreeStatistics()
        self._stats = self._tree_stats

    def produce_shade(self) -> None:
        self._tree_stats.increment_shade()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: float = 0.0,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: float = nutritional_value

    def age(self, days: int) -> None:
        super().age(days)
        self.nutritional_value += days * 0.5

    def grow(self, amount: float) -> None:
        super().grow(amount)
        self.nutritional_value += amount * (10 / 42)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {round(self.nutritional_value)}")


def display_plant_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.show_statistics()


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")

    print("\n=== Check year-old")
    print(
        "Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        "Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_statistics(rose)
    print("\n[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_statistics(oak)
    print("\n[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("\n[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_statistics(sunflower)

    print("\n=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    display_plant_statistics(anonymous)


if __name__ == "__main__":
    ft_garden_analytics()
