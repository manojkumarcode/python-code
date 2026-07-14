class Points(object):
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def print_point(self): 
        print('x=', self.x, ' y=', self.y) 

p1 = Points("A", "B") 
p1.print_point()

items = ["Vase", "Statue", "Mask"]
for index, item in enumerate(items, start=1):
    print(f"Exhibit {index}: {item} - Ancient Greece")

items1 = ["Vase", "Statue", "Mask"]
for index, item in enumerate(items1):
    print(f"Exhibit {index}: {item} - Ancient Greece")

class Points(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print_point(self):
        print('x=', self.x, ' y=', self.y)
p2 = Points('Boston', 'Chicago')
p2.y = 'Denver'
p2.print_point()

total_budget = 1000 
def calculate_remaining(spent): 
    total_budget = 500 
    return total_budget - spent 
print(calculate_remaining(200))