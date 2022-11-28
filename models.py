class Mashin:
    def __init__(self, marka: str, model: str, age_birth: str, engine: str, color: str, body: str, mileage: str, price: str) -> None:
        self.marka = marka,
        self.model = model,
        self.age_birth = age_birth,
        self.engine = engine,
        self.color = color,
        self.body = body,
        self.mileage = mileage,
        self.price = price

    @property
    def as_dict(self):
        self.__dict__['marka'] = str(self.__dict__['marka'])
        self.__dict__['model'] = str(self.__dict__['model'])
        self.__dict__['age_birth'] = str(self.__dict__['age_birth'])
        self.__dict__['engine'] = str(self.__dict__['engine'])
        self.__dict__['color'] = str(self.__dict__['color'])
        self.__dict__['body'] = str(self.__dict__['body'])
        self.__dict__['mileage'] = str(self.__dict__['mileage'])
        self.__dict__['price'] = str(self.__dict__['price'])
        return self.__dict__ 