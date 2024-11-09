class: Car
    def __init__(self, brand: str = 'TestCar')
        self.Brand = brand
        self.Driver: Person = None
        self.Passengers: list = list()#

    def add_passenger(self, passenger: Person):
        if(isinstance(passenger, Person)
            and self.Passengers is not None
            self.Passengers.append(passenger)



    def add_driver(self, driver: Passenger):
    if (isinstance(passenger, Person)
        and self.Driver is None
        self.Driver = driver

    def __str__(self):
        passengers_str =
        for item in self.Passengers:
            passengers_str = ''
            for item in self.Passenger:
                passengers_str += str(item)
                return (f'Car:\n{self.Brand} f'Driver:\n{self.Driver}\n' f'Passengers:n\{passengers_str}')




