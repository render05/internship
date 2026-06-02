import sqlite3
from datetime import datetime

DB_PATH = "db1.db"  # matches existing db file in this repo


def execute_and_print(conn: sqlite3.Connection, sql: str, params=None, description: str = ""):
    print("\n" + (description or "SQL"))
    print(sql.strip())

    cur = conn.cursor()
    if params is None:
        cur.execute(sql)
    else:
        cur.execute(sql, params)

    if sql.lstrip().lower().startswith("select"):
        rows = cur.fetchall()
        for r in rows:
            print(r)
        if not rows:
            print("(no rows)")
    else:
        conn.commit()
        print(f"Done. Rows affected: {cur.rowcount}")


def main():
    conn = sqlite3.connect(DB_PATH)
    try:
        # 1) Create tables (2-3 tables)
        execute_and_print(
            conn,
            """
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                mobile TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
            """,
            description="1) Create table: contacts",
        )

        execute_and_print(
            conn,
            """
            CREATE TABLE IF NOT EXISTS contact_notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contact_id INTEGER NOT NULL,
                note TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY(contact_id) REFERENCES contacts(id) ON DELETE CASCADE
            );
            """,
            description="2) Create table: contact_notes",
        )

        execute_and_print(
            conn,
            """
            CREATE TABLE IF NOT EXISTS audit_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                operation TEXT NOT NULL,
                ts TEXT NOT NULL
            );
            """,
            description="3) Create table: audit_log",
        )

        # Ensure fresh run (so results are visible)
        execute_and_print(conn, "DELETE FROM audit_log", description="Cleanup: clear audit_log")
        execute_and_print(conn, "DELETE FROM contact_notes", description="Cleanup: clear contact_notes")
        execute_and_print(conn, "DELETE FROM contacts", description="Cleanup: clear contacts")

        # 2) Insert records
        contacts = [
            ("Rahul Sharma", "12 MG Road", "9876543210", "rahul.sharma@example.com"),
            ("Anita Verma", "45 Lake View", "9812345678", "anita.verma@example.com"),
            ("Imran Khan", "78 Park Street", "9123456789", "imran.khan@example.com"),
        ]

        for name, address, mobile, email in contacts:
            conn.execute(
                "INSERT INTO contacts(name, address, mobile, email) VALUES (?, ?, ?, ?)",
                (name, address, mobile, email),
            )
        conn.commit()
        print("Inserted 3 contacts")

        # Insert notes for each contact
        cur = conn.execute("SELECT id, email FROM contacts")
        email_to_id = {email: cid for cid, email in cur.fetchall()}

        notes = [
            (email_to_id["rahul.sharma@example.com"], "Met at college fest",),
            (email_to_id["anita.verma@example.com"], "Important client",),
            (email_to_id["imran.khan@example.com"], "Friend from gym",),
        ]

        for contact_id, note in notes:
            conn.execute(
                "INSERT INTO contact_notes(contact_id, note, created_at) VALUES (?, ?, ?)",
                (contact_id, note, datetime.now().isoformat(timespec="seconds")),
            )
        conn.commit()
        print("Inserted notes")

        conn.execute(
            "INSERT INTO audit_log(operation, ts) VALUES (?, ?)",
            ("INSERT contacts + contact_notes", datetime.now().isoformat(timespec="seconds")),
        )
        conn.commit()

        # 4) Select operations (different queries)
        execute_and_print(conn, "SELECT * FROM contacts", description="4) SELECT all contacts")

        execute_and_print(
            conn,
            "SELECT name, mobile FROM contacts WHERE name LIKE '%Anita%';",
            description="5) SELECT filter using LIKE",
        )

        execute_and_print(
            conn,
            "SELECT c.name, c.email, n.note FROM contacts c JOIN contact_notes n ON n.contact_id = c.id ORDER BY c.name;",
            description="6) SELECT join contacts + notes",
        )

        # 5) Update some data
        execute_and_print(
            conn,
            """
            UPDATE contacts
            SET address = ?, mobile = ?
            WHERE email = ?;
            """,
            params=("99 New Address Street", "9000000000", "rahul.sharma@example.com"),
            description="7) UPDATE Rahul address/mobile",
        )

        execute_and_print(
            conn,
            "SELECT * FROM contacts WHERE email = 'rahul.sharma@example.com';",
            description="Verify UPDATE with SELECT",
        )

        conn.execute(
            "INSERT INTO audit_log(operation, ts) VALUES (?, ?)",
            ("UPDATE Rahul", datetime.now().isoformat(timespec="seconds")),
        )
        conn.commit()

        # 6) Delete some data
        execute_and_print(
            conn,
            "DELETE FROM contacts WHERE email = ?;",
            params=("imran.khan@example.com",),
            description="8) DELETE Imran contact (notes will cascade)",
        )

        execute_and_print(conn, "SELECT * FROM contacts", description="After DELETE: contacts")
        execute_and_print(conn, "SELECT * FROM contact_notes", description="After DELETE: contact_notes (should be less)")

        conn.execute(
            "INSERT INTO audit_log(operation, ts) VALUES (?, ?)",
            ("DELETE Imran", datetime.now().isoformat(timespec="seconds")),
        )
        conn.commit()

        execute_and_print(conn, "SELECT * FROM audit_log ORDER BY id", description="Final audit_log")

        print("\nAssignment 5 DB CRUD completed successfully.")

    finally:
        conn.close()


if __name__ == "__main__":
    main()

