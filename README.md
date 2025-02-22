# SQL. LEVEL1
***


## Задача Q1. СУБД. Объекты баз данных
Решения упражнений с 1 по 20 в файле `sql-ex tasks/task q1`
***


## Задача Q2. Запросы
Решения упражнений с 21 по 70 (кроме задач на 3 балла) в файле `sql-ex tasks/task q2`
***


## Задача Q3. Запросы 2.0
### Требования к системе
* [Python](https://www.python.org/downloads/) (3.12)  
* [Docker](https://docs.docker.com/get-started/get-docker/) (24.0.5)
* [PostgreSQL](https://hub.docker.com/_/postgres) (16.4)

Все необходимые пакеты Python можно установить с помощью команды:
```commandline
python3 -m pip install -r requirements.txt
```

### Предустановка
1. Создать файл `.env` с основными параметрами, например:
    ```text
    PGSQL_PROJECT_NAME="project_name"
    PGSQL_DATABASE_USER="user_name"
    PGSQL_DATABASE_PASSWORD="secret_password"
    PGSQL_DATABASE_NAME="db_name"
    PGSQL_DATABASE_HOST="0.0.0.0"
    PGSQL_DATABASE_PORT="5432"
    ```

2. Для запуска PostgreSQL Docker контейнера выполнить:
    ```commandline
    run_postgres_container.sh
    ```

### Для демонстрации решения задачи Q3, запустить:
```commandline
run_task_3.sh
```
Пример вывода решения задачи в терминале:
```text
1. Создать в одном из инструментов для работы с БД таблицу User с полями FirstName, LastName
[('User',)]

2. Добавить через запрос данные в таблицу
[{'id': 1, 'uuid': '100bbd152cf544daa0415a2f214e935f', 'firstname': 'Joseph', 'lastname': 'Harris'},
{'id': 2, 'uuid': '3e8858aea8ea407d8828765d4446629f', 'firstname': 'Lauren', 'lastname': 'Ayala'},
{'id': 3, 'uuid': '2a4af6fa0a7845c69353baaaa14a2c1b', 'firstname': 'Brittany', 'lastname': 'Holmes'}, 
{'id': 4, 'uuid': 'd50cda6bb6bf43b7b2ea2ec7d7dcf255', 'firstname': 'Danielle', 'lastname': 'Grant'},
{'id': 5, 'uuid': 'e9af42dcb6e549c3b74bd2b5303f6b2a', 'firstname': 'Nicholas', 'lastname': 'Johnson'}]

3. Отредактировать одну из добавленных записей в таблице
{'id': 3, 'uuid': '2a4af6fa0a7845c69353baaaa14a2c1b', 'firstname': 'Brittany', 'lastname': 'Holmes'}
{'id': 3, 'uuid': '2a4af6fa0a7845c69353baaaa14a2c1b', 'firstname': 'Kathy', 'lastname': 'Nicholson'}

4. Удалить запись в таблице
{'id': 2, 'uuid': '3e8858aea8ea407d8828765d4446629f', 'firstname': 'Lauren', 'lastname': 'Ayala'}

[{'id': 1, 'uuid': '100bbd152cf544daa0415a2f214e935f', 'firstname': 'Joseph', 'lastname': 'Harris'},
{'id': 4, 'uuid': 'd50cda6bb6bf43b7b2ea2ec7d7dcf255', 'firstname': 'Danielle', 'lastname': 'Grant'},
{'id': 5, 'uuid': 'e9af42dcb6e549c3b74bd2b5303f6b2a', 'firstname': 'Nicholas', 'lastname': 'Johnson'},
{'id': 3, 'uuid': '2a4af6fa0a7845c69353baaaa14a2c1b', 'firstname': 'Kathy', 'lastname': 'Nicholson'}]
```
***


### Файлы и директории:
* `sql-ex tasks/` решения упражнений с 1 по 70
* `task_3/` решение задачи Q3
* `requirements.txt` требуемые пакеты Python
* `run_postgres_container.sh` запуск контейнера PostgreSQL
* `run_task_3.sh` скрипт с решением задачи Q3