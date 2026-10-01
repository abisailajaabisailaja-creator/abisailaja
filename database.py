import sqlite3


DATABASE = "legalease.db"


def create_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            document_type TEXT NOT NULL,

            name TEXT NOT NULL,

            company TEXT,

            effective_date TEXT,

            role TEXT,

            address TEXT,

            terms TEXT,

            document TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    connection.commit()

    connection.close()


def save_document(
    document_type,
    name,
    company,
    effective_date,
    role,
    address,
    terms,
    document
):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO documents
        (
            document_type,
            name,
            company,
            effective_date,
            role,
            address,
            terms,
            document
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        document_type,
        name,
        company,
        effective_date,
        role,
        address,
        terms,
        document
    ))

    connection.commit()

    connection.close()


def get_documents():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            document_type,
            name,
            created_at
        FROM documents
        ORDER BY id DESC
    """)

    documents = cursor.fetchall()

    connection.close()

    return documents