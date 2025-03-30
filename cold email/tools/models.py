import sqlite3
import re

def setup_database():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipients (
            recipient_email TEXT NOT NULL UNIQUE,
            entity TEXT NOT NULL,
            representative TEXT NOT NULL,
            email_status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def connect_db():
    return sqlite3.connect("email_tracking.db")

def add_recipient(recipient_email, representative):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO recipients (recipient_email, entity, representative)
        VALUES (?, ?, ?)
    """, (recipient_email, entity, representative))

    conn.commit()
    conn.close()

def fetch_recipients():
    def match_email(*domain_patterns):
        custom_domain = [rf'^[a-zA-Z0-9._%+-]+@{domain}$' for domain in domain_patterns]
        return custom_domain

    conn = sqlite3.connect("email_tracking.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipients")
    data = cursor.fetchall()
    conn.close()

    verfiy_regex = match_email(r'gmail\.com', r'yahoo\.com', r'outlook\.com')
    print("verifying recipients before sending...")
    clean_data = []
    for entry in data:
        recipient_email = entry[1].strip().lower()  
        entity = entry[2].strip()
        representative = entry[3].strip()
        status = entry[4].strip()
        if not re.search(verify_regex, recipient_email):
            print(f"Skipping invalid email: {recipient_email}")
            continue  
        
        clean_data.append((recipient_email, entity, representative, status))

    return clean_data


def update_email_status(recipient_email, status):
    conn = sqlite3.connect('email_tracking.db')
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE recipients
        SET email_status = ?,WHERE recipient_email = ?
    """, (status, recipient, recipient_email))
    
    conn.commit()
    conn.close()