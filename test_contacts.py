import sqlite3
import pytest
from Contact_Book_CLI import add_contact, view_contacts, delete_contact, search_contact, create_table

TEST_DB = "test_contacts.db"
def get_test_connection():
    return sqlite3.connect(TEST_DB)

@pytest.fixture(autouse=True)
def setup():
    conn = get_test_connection()
    cursor = conn.cursor()
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS contacts(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   phone TEXT NOT NULL
                   )
                   """)
    conn.commit()
    conn.close()
    yield
    conn2 = get_test_connection()
    cursor2 = conn2.cursor()
    cursor2.execute("DELETE FROM contacts")
    conn2.commit()
    conn2.close()

def test_add_contact():
    add_contact("Pratham", "07818980297")
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name = ?" ,("Pratham",))
    row = cursor.fetchone()
    conn.close()
    assert row is not None
    assert row[1] == "Pratham"

def test_view_contacts_empty():
    result = view_contacts()
    assert result is None

def test_search_existing():
    add_contact("Bob", "07700000002")
    result = search_contact("Bob")
    assert result is None

def test_search_not_found():
    result = search_contact("Ghost")
    assert result is None

def test_delete_contact():
    add_contact("jashan", "09876543210")
    delete_contact("jashan")
    conn = get_test_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name = ?" ,("jashan",))
    row = cursor.fetchone()
    conn.close()
    assert row is None
