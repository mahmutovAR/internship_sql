from generate_user_data import GeneratedUserData
from user_data import USER_DB


USER_DB.create_table()
print(f'1. Создать в одном из инструментов для работы с БД таблицу User с полями FirstName, LastName'
      f'\n{USER_DB.display_created_table()}\n')


TEST_DATA = GeneratedUserData()
for _ in range(5):
    USER_DB.insert_user(*TEST_DATA.generate_full_name())
user_table_data = USER_DB.display_table()
print(f'2. Добавить через запрос данные в таблицу\n{user_table_data}\n')


user_3_data = user_table_data[2]
updated_user_data = USER_DB.update_user(user_3_data['uuid'], *TEST_DATA.generate_full_name())
print(f'3. Отредактировать одну из добавленных записей в таблице\n{user_3_data}\n{updated_user_data}\n')


id_2_data = user_table_data[1]
user_deleted = USER_DB.delete_user(id_2_data['uuid'])
print(f'4. Удалить запись в таблице\n{user_deleted}\n')


print(USER_DB.display_table())
