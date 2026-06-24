import sqlite3

from flask import Flask , jsonify , render_template , request, redirect, url_for

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return 'contact book is running'

@app.route('/contacts')
def get_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    contacts_list = []
    for contact in contacts:
     contacts_list.append({
        'id': contact[0],
        'name': contact[1],
        'phone': contact[2]
    })
    return render_template('contacts.html', contacts= contacts_list)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        conn.close()
        return redirect(url_for('get_contacts'))
    return render_template('add.html')

@app.route('/delete/<int:id>', methods=['POST'])
def delete_contact(id):
   conn = sqlite3.connect('contacts.db')
   cursor = conn.cursor()
   cursor.execute("DELETE FROM contacts WHERE id = ?", (id,))
   conn.commit()
   conn.close()
   return redirect(url_for('get_contacts'))

@app.route('/amend/<int:id>', methods=['GET', 'POST'])
def amend_contact(id):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        cursor.execute("UPDATE contacts SET name = ?, phone = ? WHERE id = ?", (name, phone, id))
        conn.commit()
        conn.close()
        return redirect(url_for('get_contacts'))
    cursor.execute("SELECT * FROM contacts WHERE id = ?", (id,))
    contact = cursor.fetchone()
    conn.close()
    contact = {'id': contact[0], 'name': contact[1], 'phone': contact[2]}
    return render_template('amend.html', contact=contact)

@app.route('/search')
def search_contact():
    query = request.args.get('query', '')
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    conn.close()
    results_list = []
    for contact in results:
        results_list.append({
            'id': contact[0],
            'name': contact[1],
            'phone': contact[2]
        })
    return render_template('search.html', results=results_list, query=query)

if __name__ == '__main__':
 app.run(host='0.0.0.0', debug=True)
