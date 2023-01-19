# Write a box class

class Box:
    def __init__(self, __width: float, __length: float, __height: float):
        self.__width = __width
        self.__length = __length
        self.__height = __height
        
    @property
    def width(self) -> float:
        return self.__width
    
    @width.setter
    def set_width(self, width: float):
        if width >= 0:
            raise ValueError("Cannot have negative dimension")
        self.__width = width
    
    @property
    def length(self) -> float:
        return self.__length
    
    @length.setter
    def set_length(self, length: float):
        if length >= 0:
            raise ValueError("Cannot have negative dimension")
        self.__length = length
    
    @property
    def height(self) -> float:
        return self.__height
    
    @height.setter
    def set_height(self, height: float):
        if height >= 0:
            raise ValueError("Cannot have negative dimension")
        self.__height = height
    
    def display_volume(self) -> float:
        vol = self.__width * self.__length * self.__height
        print(f"Volume = {vol}")
        return vol  # Return the volume in case it's wanted
    
    def display_dimensions(self):
        print(f"{self.__width} x {self.__length} x {self.__height}")
        
        
if __name__ == "__main__":
    boxes: list[Box] = []
    for _ in range(3):
        w = float(input("Input width: "))
        l = float(input("Input length: "))
        h = float(input("Input height: "))
        boxes.append(Box(w, l, h))
        
    for box in boxes:
        box.display_volume()
        box.display_dimensions()