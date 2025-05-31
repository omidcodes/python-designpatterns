from abc import ABC, abstractmethod

# ----------------------------
# 1. The Product: House
# ----------------------------
class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.doors = None
        self.windows = None

    def __str__(self):
        parts = [
            f"Walls: {self.walls}",
            f"Roof: {self.roof}",
            f"Doors: {self.doors}",
            f"Windows: {self.windows}",
        ]
        return "\n".join(parts)


# ---------------------------------------
# 2. The Builder Interface: HouseBuilder
# ---------------------------------------
class HouseBuilder(ABC):
    """Abstract Builder that defines the steps to build a House."""

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def get_result(self) -> House:
        pass


# ---------------------------------------------
# 3. Concrete Builder: ConcreteHouseBuilder
# ---------------------------------------------
class ConcreteHouseBuilder(HouseBuilder):
    """Concrete implementation of HouseBuilder that actually constructs a House."""

    def __init__(self):
        self.reset()

    def reset(self):
        self._house = House()

    def build_walls(self):
        self._house.walls = "Brick Walls"

    def build_roof(self):
        self._house.roof = "Concrete Roof"

    def build_doors(self):
        self._house.doors = "Wooden Doors"

    def build_windows(self):
        self._house.windows = "Glass Windows"

    def get_result(self) -> House:
        finished_house = self._house
        self.reset()
        return finished_house


# ---------------------------------------
# 4. (Optional) Director: HouseDirector
# ---------------------------------------
class HouseDirector:
    """Director that defines the order of building steps for a House."""

    def __init__(self, builder: HouseBuilder):
        self._builder = builder

    def construct_small_house(self):
        """Defines the build sequence for a small house."""
        self._builder.build_walls()
        self._builder.build_roof()
        self._builder.build_doors()
        self._builder.build_windows()

    def construct_vacation_house(self):
        """Defines a different sequence for a vacation house."""
        self._builder.build_walls()
        self._builder.build_doors()
        self._builder.build_windows()
        self._builder.build_roof()


# ---------------------------------------
# 5. Client Code: Putting It All Together
# ---------------------------------------
if __name__ == "__main__":
    # Create a concrete builder
    builder = ConcreteHouseBuilder()

    # Option A: Use a director for predefined house types
    director = HouseDirector(builder)

    # Build a small house
    director.construct_small_house()
    small_house = builder.get_result()
    print("Small House built:")
    print(small_house)
    print("\n" + "-" * 30 + "\n")

    # Build a vacation house
    director.construct_vacation_house()
    vacation_house = builder.get_result()
    print("Vacation House built:")
    print(vacation_house)
    print("\n" + "-" * 30 + "\n")

    # Option B: Skip the director and call builder methods directly
    # Build a quick cabin (no doors or windows)
    builder.build_walls()
    builder.build_roof()
    quick_cabin = builder.get_result()
    print("Quick Cabin built:")
    print(quick_cabin)
