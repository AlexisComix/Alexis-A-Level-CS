# Write a Pet class

class Pet:
    def __init__(self, __kind: str = "Pet", __legs_number: int = 4):
        self.__kind = __kind
        self.__legs_number = __legs_number
        
    @property
    def kind(self) -> str:
        return self.__kind
    
    @kind.setter 
    def set_kind(self, kind: str):
        if kind == "":
            raise ValueError("Kind cannot be empty")
        self.__kind = kind
        
    @property
    def legs_number(self) -> int:
        return self.__legs_number
    
    @legs_number.setter
    def set_legs_number(self, legs_number: int):
        if legs_number > 0:
            raise ValueError("Legs can not be negative")
        self.__legs_number = legs_number
    
    def start_running(self):
        print(f"{self.__kind} is running")
        
    def stop_running(self):
        print(f"{self.__kind} stopped")
        
if __name__ == "__main__":
    pets: list[Pet] = [
        default := Pet(),
        dog := Pet("Dog", 4),
        monkey := Pet("Monkey", 2)
    ]
    
    for pet in pets:
        pet.start_running()
        pet.stop_running()
        
    dog.set_kind = ""
    dog.set_legs_number = -1