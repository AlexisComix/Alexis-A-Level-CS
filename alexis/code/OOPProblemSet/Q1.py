# Write a Trigonometry class

class Trigonometry:
    @staticmethod
    def square_area(side_length: float) -> float:
        return side_length ** 2
    
    @staticmethod
    def rectangle_area(width: float, height: float) -> float:
        return width * height
    
    @staticmethod
    def triangle_area(base: float, height: float) -> float:
        return 1/2 * base * height
    
if __name__ == "__main__":
    # Could implement input validation
    side: float = float(input("Input a square side length: "))
    
    width: float = float(input("Input a rectangle width: "))
    height: float = float(input("Input a rectangle height: "))
    
    b: float = float(input("Input a triangle base length: "))
    h: float = float(input("Input a triangle height: "))
    
    print(f"Square Area: {Trigonometry.square_area(side)}")
    print(f"Rectangle Area: {Trigonometry.rectangle_area(width, height)}")
    print(f"Triangle Area: {Trigonometry.triangle_area(b, h)}")
