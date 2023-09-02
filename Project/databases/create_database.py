import sqlite3

def create_database():
    try:
        # Connect to the database (or create if not exists)
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        # Create a table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')

        # Commit changes and close the connection
        conn.commit()
        conn.close()
        print("Table 'users' created successfully.")
    except sqlite3.Error as e:
        print("Error creating table:", e)

if __name__ == '__main__':
    create_database()
