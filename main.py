from models import Mashin
from mixins import JsonMixin, CreateMixin, ReadMixin, UpdateMixin, DeleteMixin



class Cars(JsonMixin, CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    _file_name = 'db.json'
    _model = Mashin

    def help(self):
        print("""
        create - создание записи
        list - список записи
        detalis - получение одной записи
        update -обнавление записи
        delete - удаление записи
        help - список команд
        quit - выход
        """)


    def start(self):
        commands = {
            'create': self.create,
            'list': self.list,
            'detalis': self.read_by_model,
            'update': self.update,
            'delete': self.delete,
            'help': self.help
        }
        while True:
            try:
                command = input('Введите команду или help для списка команду: ').lower().strip()
                if command in commands:
                    commands[command]()

                elif command == 'quit':
                    print('Выход из программы.')
                    break
                else:
                    print('Такой команды нет.')
            except:
                print('Некорректные данные, попробуйте ещё раз.')


car = Cars()
# car.create()
# car.read_by_model()
# car.list()
# car.update()
car.start()