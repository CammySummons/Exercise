class Bus:
    bus_list = []

    def __init__(self, number, route, driver):
        self.number = number
        self.route = route
        self.driver = driver
        Bus.bus_list.append(self)

    def display_info(self):
        for bus in Bus.bus_list:
            if bus == self:
                print(f"Bus number: {bus.number}  "
                      f"Bus route: {bus.route}  "
                      f"Bus driver: {bus.driver}")


bus1 = Bus(2020, "Y", "Jono")
bus2 = Bus(1045, "P", "John")
bus3 = Bus(4200, "130", "Patrick")

for bus in range(len(Bus.bus_list)):
    Bus.display_info(Bus.bus_list[bus])
