import math

def display_menu():
    print(
        """
        1. Enter radius
        2. Display radius
        3. Display diameter
        4. Display area
        5. Display perimeter
        6. Exit
        """
    )

class Circle:
    def __init__(self):
        self.__radius: float

    @property
    def radius(self) -> float:
        try:
            return self.__radius
        except:
            raise Exception("Radius has not been set.")

    @radius.setter
    def set_radius(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius cannot be <= 0.")
        self.__radius = radius

    def get_diameter(self) -> float:
        return self.__radius * 2

    def get_area(self) -> float:
        return math.pi * (self.__radius ** 2)

    def get_perimeter(self) -> float:
        return self.get_diameter() * math.pi


def main():
    circle = Circle()
    running = True
    while running:
        display_menu()
        option: int = int(input("Please select an option: "))
        match option:
            case 1:
                r: float = float(input("Please input a radius: "))
                circle.set_radius = r
            case 2: 
                print(float(circle.radius))
            case 3:
                print(circle.get_diameter())
            case 4:
                print(circle.get_area())
            case 5:
                print(circle.get_perimeter())
            case 6:
                running = False
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()