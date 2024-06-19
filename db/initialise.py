import psycopg2


def main():
    print('Initialising hp_data Database')
    connection = psycopg2.connect(user="root", password="root", host="postgres-db", port="5432", database="hp_data")
    print('Connection opened')

    cursor = connection.cursor()
    cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'migration_history');")
    row = cursor.fetchone()

    if row and row[0]:
        print('Migration history table exists, nothing to do')
    else:
        print('Migration History table does not exist, creating...')
        cursor.execute("CREATE TABLE migration_history (migration_number INT, migrated_timestamp TIMESTAMP WITH TIME ZONE);")
        connection.commit()
        print('Migration History table created')

    connection.close()
    print("Connection closed")


if __name__ == '__main__':
    main()
