import json
from pprint import pprint



class JsonMixin:
    def get_db_content(self):
        try:
            with open(self._file_name, 'r') as file:
                return json.load(file)
        except json.decoder.JSONDecodeError:
            return {'users': []}

    def write_db_json(self, data):
        with open(self._file_name, 'w') as file:
            json.dump(data, file, indent=4)
        


class CreateMixin:
    def create(self):
        marka = input('Введите марку автомобиля: ')
        model = input('Введите модель автомобиля: ')
        age_birth = input('Введите год выпуска: ')
        engine = input('Введите объём двигателя: ')
        color = input('Введите цвет мишины: ')
        body = input('Введите тип кузова: ')
        mileage = input('Введите пробег автомобиля: ')
        price = input('Введите цену: ')
        next_1 = self._model(marka = marka, model = model, 
        age_birth = age_birth, engine = engine, color = color, body = body, mileage = mileage, price = price)

        data = self.get_db_content()
        data['users'].append(next_1.as_dict)
        self.write_db_json(data)
        print('готово.')

class ReadMixin:
    def list(self):
        data = self.get_db_content()
        pprint(data)

    def read_by_model(self):
        price_car = input('Введите цену машины: ')
        data = self.get_db_content()
        user = data['users']
        res = list(filter(lambda x: x['price'] == price_car, user))
        pprint(res[0] if res else 'Не найдено')
        return res[0] if res else None

class UpdateMixin:
    def update(self):
        models = self._model

        soup = self.get_db_content()
        user = self.read_by_model()
        if user is not None:
            soup['users'].remove(user)
            marka = input('Введите марку автомобиля: ') or user['marka']
            model = input('Введите модель автомобиля: ') or user['model']
            age_birth = input('Введите год выпуска: ') or user['age_birth']
            engine = input('Введите объём двигателя: ') or user['engine']
            color = input('Введите цвет мишины: ') or user['color']
            body = input('Введите тип кузова: ') or user['body']
            mileage = input('Введите пробег автомобиля: ') or user['mileage']
            price = input('Введите цену: ') or user['price']

            new_user = models(marka = marka, model = model, age_birth = age_birth, engine = engine, 
            color = color, body = body, mileage = mileage, price = price)
            
            new_user.__dict__['price'] = user['price']
            soup['users'].append(new_user.as_dict)
            self.write_db_json(soup)
            print('Готово.')
        else:
            print('Не найдено.')

class DeleteMixin:
    def delete(self):
        next_price = self.get_db_content()
        user_w = self.read_by_model()
        if user_w is not None:
            next_price['users'].remove(user_w)
            self.write_db_json(next_price)
            print('Готово.')
        else:
            print('Не найдено.')

