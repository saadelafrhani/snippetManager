import sqlite3

def create_database():
    """Create the SQLite database and snippets table if not exists."""
    conn = sqlite3.connect("snippets.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS snippets (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            code TEXT NOT NULL,
            language TEXT,
            tags TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_snippet(title, code, language, tags):
    """Add a new snippet to the database."""
    conn = sqlite3.connect("snippets.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO snippets (title, code, language, tags) VALUES (?, ?, ?, ?)",
                   (title, code, language, tags))
    conn.commit()
    conn.close()

def get_snippets():
    """Retrieve all snippets from the database."""
    conn = sqlite3.connect("snippets.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM snippets")
    results = cursor.fetchall()
    conn.close()
    return results

def delete_snippet(snippet_id):
    """Delete a snippet from the database by its ID."""
    conn = sqlite3.connect("snippets.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM snippets WHERE id = ?", (snippet_id,))
    conn.commit()
    conn.close()
