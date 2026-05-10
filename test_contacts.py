from Contact_Book_CLI import contacts, add_contact, delete_contact, search_contact,view_contacts

def test_add_valid_contact():
    contacts.clear()
    add_contact("Alice", "07123456789")
    assert "Alice" in contacts

def test_duplicate_contact():
    contacts.clear()
    add_contact("bob", "01234567890")
    add_contact("bob", "01234567890")
    assert len(contacts) == 1

def test_invalid_phone():
    contacts.clear()
    add_contact("charlie", "09876")
    assert "charlie" not in contacts

def test_delete_contact():
    contacts.clear()
    add_contact("delta", "01234567890")
    delete_contact("delta")
    assert "delta" not in contacts

def test_search_missing_contact():
    contacts.clear()
    add_contact("echo", "01234567890")
    search_contact("foxtrot")
    assert "foxtrot" not in contacts