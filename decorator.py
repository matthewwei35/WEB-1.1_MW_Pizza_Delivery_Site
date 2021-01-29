class Car:
  wheels = 4

  def __init__(self, arg1):
    self.color = arg1

  def __call__(self, func):
    self.color = func()

  def paint_car(self, arg1):
    self.color = arg1

  def details(self):
    print(f"color = {self.color}")

# Init a car
car1 = Car("red")
car1.paint_car("blue")

@car1
def change_color_with_semantic():
  return "yellow"

car1.details()
