import sqlite3
from datetime import datetime

DB_PATH = "db1.db"  # using existing db file as per repo


def execute_and_print(conn, sql, params=None, description=""):
    print("\n" + (description or "SQL"))
    print(sql)

    cur = conn.cursor()
    if params is None:
        cur.execute(sql)
    else:
        cur.execute(sql, params)

    # If it's a SELECT, print rows
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
        # 1) Create 2-3 tables
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
            CREATE TABLE IF NOT EXISTS audit_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                operation TEXT NOT NULL,
                ts TEXT NOT NULL
            );
            """,
            description="2) Create table: audit_log (extra practice table)",
        )

        # (Optional) another small table for variety
        execute_and_print(
            conn,
            """
            CREATE TABLE IF NOT EXISTS contact_tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contact_id INTEGER NOT NULL,
                tag TEXT NOT NULL,
                FOREIGN KEY(contact_id) REFERENCES contacts(id) ON DELETE CASCADE
            );
            """,
            description="3) Create table: contact_tags",
        )

        # 2) Insert some records
        contacts = [
            ("Rahul Sharma", "12 MG Road", "9876543210", "rahul.sharma@example.com"),
            ("Anita Verma", "45 Lake View", "9812345678", "anita.verma@example.com"),
            ("Imran Khan", "78 Park Street", "9123456789", "imran.khan@example.com"),
        ]

        execute_and_print(conn, "DELETE FROM contact_tags", description="Cleanup: clear tags")
        execute_and_print(conn, "DELETE FROM contacts", description="Cleanup: clear contacts")
        execute_and_print(conn, "DELETE FROM audit_log", description="Cleanup: clear audit_log")

        print("\n2) Insert records into contacts")
        for name, address, mobile, email in contacts:
            conn.execute(
                "INSERT INTO contacts(name, address, mobile, email) VALUES (?, ?, ?, ?)",
                (name, address, mobile, email),
            )
        conn.commit()
        print("Inserted 3 contacts")

        # Insert tags
        cur = conn.execute("SELECT id, email FROM contacts")
        email_to_id = {email: cid for cid, email in cur.fetchall()}

        tags = [
            (email_to_id["rahul.sharma@example.com"], "friend"),
            (email_to_id["anita.verma@example.com"], "work"),
            (email_to_id["imran.khan@example.com"], "family"),
        ]
        conn.executemany(
            "INSERT INTO contact_tags(contact_id, tag) VALUES (?, ?)",
            tags,
        )
        conn.commit()
        print("Inserted 3 tags")

        conn.execute(
            "INSERT INTO audit_log(operation, ts) VALUES (?, ?)",
            ("INSERT contacts + tags", datetime.now().isoformat(timespec="seconds")),
        )
        conn.commit()

        # 3) Perform different select operations
        execute_and_print(conn, "SELECT * FROM contacts", description="4) SELECT: all contacts")

        execute_and_print(
            conn,
            "SELECT name, mobile FROM contacts WHERE name LIKE '%Anita%';",
            description="5) SELECT: by name (LIKE)",
        )

        execute_and_print(
            conn,
            "SELECT id, name, email FROM contacts ORDER BY name DESC;",
            description="6) SELECT: order by name desc",
        )

        execute_and_print(
            conn,
            """
            SELECT c.name, c.email, t.tag
            FROM contacts c
            JOIN contact_tags t ON t.contact_id = c.id
            ORDER BY c.name;
            """,
            description="7) SELECT: join contacts with tags",
        )

        # 4) Update some data
        execute_and_print(
            conn,
            """
            UPDATE contacts
            SET address = ?, mobile = ?
            WHERE email = ?;
            """,
            params=("99 New Address Street", "9000000000", "rahul.sharma@example.com"),
            description="8) UPDATE: change address/mobile for Rahul",
        )

        execute_and_print(
            conn,
            "SELECT * FROM contacts WHERE email = 'rahul.sharma@example.com';",
            description="Verify update (SELECT)",
        )

        conn.execute(
            "INSERT INTO audit_log(operation, ts) VALUES (?, ?)",
            ("UPDATE Rahul", datetime.now().isoformat(timespec="seconds")),
        )
        conn.commit()

        # 5) Delete some data
        execute_and_print(
            conn,
            "DELETE FROM contacts WHERE email = ?;",
            params=("imran.khan@example.com",),
            description="9) DELETE: remove Imran",
        )

        # After delete, tags should cascade
        execute_and_print(
            conn,
            "SELECT * FROM contacts",
            description="10) SELECT after delete: all contacts",
        )

        execute_and_print(
            conn,
            "SELECT * FROM contact_tags",
            description="11) SELECT after delete: remaining tags",
        )

        conn.execute(
            "INSERT INTO audit_log(operation, ts) VALUES (?, ?)",
            ("DELETE Imran", datetime.now().isoformat(timespec="seconds")),
        )
        conn.commit()

        execute_and_print(conn, "SELECT * FROM audit_log ORDER BY id", description="12) SELECT: audit log")

        print("\nAll database CRUD steps completed successfully.")

    finally:
        conn.close()


if __name__ == "__main__":
    main()

