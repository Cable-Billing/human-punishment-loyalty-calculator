import pg8000
from os import listdir


def migration_initialise(connection):
    row = connection.run("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'migration_history')")[0]

    if row[0]:
        print('Table \'migration_history\': exists')
    else:
        connection.run('CREATE TABLE migration_history (migration_number CHARACTER(12), migrated_timestamp TIMESTAMP WITH TIME ZONE)')
        print('Table \'migration_history\': created')


def migrate(connection):
    migration_files = listdir('./migrations')

    for file_name in migration_files:
        migration_number = file_name[:12]
        row = connection.run("SELECT EXISTS (SELECT FROM migration_history WHERE migration_number = :migration_number)", migration_number=migration_number)[0]

        if row[0]:
            print(f'Migration \'{migration_number}\': already run')
        else:
            file = open(f'./migrations/{file_name}')
            connection.run(file.read())
            connection.run("INSERT INTO migration_history(migration_number, migrated_timestamp) VALUES (:migration_number, NOW())", migration_number=migration_number)
            print(f'Migration \'{migration_number}\': ran')


def main():
    connection = pg8000.connect(user='root', password='root', host='postgres-db', port='5432', database='hp_data')

    try:
        migration_initialise(connection)
        migrate(connection)
        connection.commit()
    except:
        connection.rollback()
    finally:
        connection.close()


if __name__ == '__main__':
    main()
