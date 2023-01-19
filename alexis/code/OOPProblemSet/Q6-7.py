# Write a cube class

class Cube:
    def __init__(self, __edge: float):
        self.__edge = __edge
        
    @property
    def edge(self) -> float:
        return self.__edge
    
    @edge.setter
    def set_edge(self, edge: float):
        if edge <= 0:
            raise ValueError("Edge must be positive length")
        self.__edge = edge
    
    def display_volume(self):
        vol = self.__edge ** 3
        print(f"Volume: {vol}")
        return vol
    
    def display_one_surface(self):
        area = self.__edge ** 2
        print(f"Face area: {area}")
        return area
    
    def display_total_surface(self):
        surface_area = self.__edge**2 * 6
        print(f"Surface area: {surface_area}")
        return surface_area
    
if __name__ == "__main__":
    side = float(input("Input a side length: "))
    cube = Cube(side)
    
    cube.display_volume()
    cube.display_one_surface()
    cube.display_total_surface()