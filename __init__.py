class Car(object):
    """blueprint for car"""
    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.model = model
        self.company = company
        self.speed_limit = speed_limit

    def start (self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating...")
        "accelerating functionality here"

    def change_gear(self, gear_type):
        print("gear changed")
        "gear related functionality here"
maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)

print(maruthi_suzuki.color)
