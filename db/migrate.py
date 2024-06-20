import pg8000
from os import listdir


def migration_initialise(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'migration_history');")
    row = cursor.fetchone()

    if row[0]:
        print('Table \'migration_history\': exists')
    else:
        cursor.execute('CREATE TABLE migration_history (migration_number CHARACTER(12), migrated_timestamp TIMESTAMP WITH TIME ZONE);')
        connection.commit()
        print('Table \'migration_history\': created')

    cursor.close()


def migrate(connection):
    cursor = connection.cursor()
    migration_files = listdir('./migrations')

    for file_name in migration_files:
        migration_number = file_name[:12]
        cursor.execute("SELECT COUNT(*) FROM migration_history WHERE migration_number = %(migration_number)s", {'migration_number': migration_number})
        row = cursor.fetchone()

        if row[0] == 0:
            file = open(f'./migrations/{file_name}')
            cursor.execute(file.read())
            cursor.execute("INSERT INTO migration_history(migration_number, migrated_timestamp) VALUES (%(migration_number)s, NOW())", {'migration_number': migration_number})
            connection.commit()
            print(f'Migration \'{migration_number}\': ran')
        else:
            print(f'Migration \'{migration_number}\': already run')

    cursor.close()


def main():
    connection = pg8000.connect(user='root', password='root', host='postgres-db', port='5432', database='hp_data')
    migration_initialise(connection)
    migrate(connection)
    connection.close()


if __name__ == '__main__':
    main()
