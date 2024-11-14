class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    # Методы для получения значений атрибутов
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Метод для изменения имени пользователя
    def set_name(self, name):
        self._name = name



class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')

    # Метод для добавления пользователя в список
    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"пользователь удачно добавлен в список.")


    # Метод для удаления пользователя из списка
    def remove_user(self, user_list, user):
        user_list.remove(user)
        print(f"пользователь удачно удален из списока.")

users = []


# Создаем обычного пользователя и администратора

admin = Admin(2, "Bob")
user1 = User(1, "Alice")
# Администратор добавляет пользователя в список

print(user1.get_name())
admin.add_user(users, user1)
