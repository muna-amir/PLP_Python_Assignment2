class Car:
    def __init__(self, model):
        self.model = model
        
    def move(self):
        print(f"The {self.model} is Driving down the highway.")

class Plane:
    def __init__(self, model):
        self.model = model
        
    def move(self):
        print(f"The {self.model} is Flying in the sky.")
    
class Boat:
    def __init__(self, model):
        self.model = model
    
    def move(self):
        print(f"The {self.model} is Sailing down the river.")

def perform_movement(vehicles_list):
    print("--- Starting Movement Sequence ---")
    for vehicle in vehicles_list:
        vehicle.move()
    print("--- Movement Sequence Finished ---")
    
if __name__ == "__main__":
    # Create instances of the different classes
    my_car = Car("Sedan")
    my_plane = Plane("Jetliner")
    my_boat = Boat("Yacht")

    # Group all objects into a single list
    fleet = [my_car, my_plane, my_boat]

    # Call the polymorphic function
    perform_movement(fleet)
