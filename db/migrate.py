import psycopg2


def migration_initialise():
    connection = psycopg2.connect(user="root", password="root", host="postgres-db", port="5432", database="hp_data")

    cursor = connection.cursor()
    print('Checking if \'migration_history\' tables exists...')
    cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'migration_history');")
    row = cursor.fetchone()

    if row and row[0]:
        print('\'migration_history\' table exists, nothing to do')
    else:
        print('\'migration_history\' table does not exist, creating...')
        cursor.execute("CREATE TABLE migration_history (migration_number CHARACTER(12), migrated_timestamp TIMESTAMP WITH TIME ZONE);")
        connection.commit()
        print('\'migration_history\' table created')

    connection.close()


def migrate():
    print('test')


def main():
    migration_initialise()
    migrate()


if __name__ == '__main__':
    main()
