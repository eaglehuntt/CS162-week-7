
"""

Pick a generic object where something could cause exception in its state (example: parts breaking on a vehicle),

Object: consumer electronic

Describe a generic exception that could happen in your object (example: BrokenVehiclePartError),

exception: battery died

Describe two subclasses of the object (examples: car and truck, boat and starship, boat and bike),

subclasses: smart phone, laptop

Describe two subclasses of the exception (examples: flat tire, busted hitch, reactor coolant leak)

exception: call dropped, blue screen of death

Draw an inheritance diagram that shows the relationships between the various classes and the exceptions.

                            consumer electronic
                                   /\
                                  /  \
                                 /    \
                                /      \
                        smart phone      laptop
 
Design a program that uses your classes and inheritance diagram showing how inheritance can work.
(this could be something like a car sales lot, a mechanics shop, or a racing “game”, allowing you to interact with the objects or components, causing exceptions to occur, and handling those exceptions)

program: backpack

"""


class ConsumerElectronics:
    def __init__(self, name, battery_percentage, display_size, processor):
        self.name = name
        self.battery_percentage = battery_percentage
        self.display_size = display_size
        self.processor = processor
        
    def __str__(self):
        return self.name
    

class SmartPhone(ConsumerElectronics):
    def __init__(self, name, battery_percentage, display_size, processor, camera_resolution, phone_carrier):

        super().__init__(name, battery_percentage, display_size, processor)

        self.camera_resolution = camera_resolution
        self.phone_carrier = phone_carrier
        
    def __str__(self):
        return f"{self.name}"
    
    def call(self, number):

        try:
            if self.battery_percentage < 20:
                raise Exception("Battery died")
                
            else:
                print(f"Calling {number}...")
                self.battery_percentage -= 20
                print("Called!")
                print(f"Battery percentage: {self.battery_percentage}%")
                return number
        except Exception as e:
            print("Oh no! Phone battery died!")


class Laptop(ConsumerElectronics):
    def __init__(self, name, battery_percentage, display_size, processor, operating_system, keyboard_layout):

        super().__init__(name, battery_percentage, display_size, processor)

        self.operating_system = operating_system
        self.keyboard_layout = keyboard_layout
        
    def __str__(self):
        return f"{self.name}"
    

    def browse_internet(self, url):

        try:
            if self.battery_percentage < 20:
                raise Exception("Battery died")
            else:
                print(f"Browsing {url}...")
                self.battery_percentage -= 20
                print("Browsed!")
                print(f"Battery percentage: {self.battery_percentage}%")
                return url
            
        except Exception as e:
            print("Oh no! Laptop battery died!")
    
class Backpack:
    def __init__(self, *args) -> None:
        self.devices = {}
        self.add_devices(args)

    def add_devices(self, devices):
        for device in devices:

            if device["name"] == "Laptop":
                laptop = Laptop(device["name"], device["battery_percentage"], device["display_size"], device["processor"], device["operating_system"], device["keyboard_layout"])
                self.devices["Laptop"] = laptop
                
            elif device["name"] == "SmartPhone":
                smartphone = SmartPhone(device["name"], device["battery_percentage"], device["display_size"], device["processor"], device["camera_resolution"], device["phone_carrier"])
                self.devices["SmartPhone"] = smartphone

            else: 
                print("You don't own that device!")
            
    def __str__(self) -> str:
        device_names = [str(device) for device in self.devices]
        return f"Backpack devices: {', '.join(device_names)}"
        


if __name__ == "__main__":

    my_laptop = {
        "name" : "Laptop",
        "battery_percentage": 10,
        "display_size" : 15.6,
        "processor" : "i5",
        "operating_system" : "Windows",
        "keyboard_layout" : "English"
    }

    my_phone = {
        "name" : "SmartPhone",
        "battery_percentage": 80,
        "display_size" : 6.5,
        "processor" : "A14",
        "camera_resolution" : "12MP",
        "phone_carrier" : "T-Mobile"
    }

    my_backpack = Backpack(my_laptop, my_phone)
    
    def make_call(phone):
        phone.call("555-5555")

    def watch_youtube(laptop):
        laptop.browse_internet("https://www.youtube.com")

    make_call(my_backpack.devices[my_phone["name"]])
    watch_youtube(my_backpack.devices[my_laptop["name"]])
