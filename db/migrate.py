import psycopg2
from os import listdir


def migration_initialise(connection):
    cursor = connection.cursor()
    print('Checking if \'migration_history\' tables exists...')
    cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'migration_history');")
    row = cursor.fetchone()

    if row and row[0]:
        print('\'migration_history\' table exists, nothing to do')
    else:
        print('\'migration_history\' table does not exist, creating...')
        cursor.execute('CREATE TABLE migration_history (migration_number CHARACTER(12), migrated_timestamp TIMESTAMP WITH TIME ZONE);')
        connection.commit()
        print('\'migration_history\' table created')

    cursor.close()


def migrate(connection):
    cursor = connection.cursor()
    migration_files = listdir('./migrations')

    for file_name in migration_files:
        migration_number = file_name[:12]
        cursor.execute("SELECT COUNT(*) FROM migration_history WHERE migration_number = %(migration_number)s", {'migration_number': migration_number})
        row = cursor.fetchone()

        if row and row[0] == 0:
            print()

    cursor.close()


def main():
    connection = psycopg2.connect(user='root', password='root', host='postgres-db', port='5432', database='hp_data')
    migration_initialise(connection)
    migrate(connection)
    connection.close()


if __name__ == '__main__':
    main()
