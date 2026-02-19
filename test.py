from fastmcp import FastMCP
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "expenses.db")

mcp = FastMCP(name="Expense Tracker")

def init_db():
    with sqlite3.connect(DB_PATH) as c:
        c.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                subcategory TEXT DEFAULT '',
                notes TEXT DEFAULT ''
            )
        """)
        
    init_db()

@mcp.tool
def add_expense(date: str, amount: float, category: str, subcategory: str = "", notes: str = "") -> str:
    """Add a new expense to the database."""
    with sqlite3.connect(DB_PATH) as c:
        c.execute("""
            INSERT INTO expenses (date, amount, category, subcategory, notes)
            VALUES (?, ?, ?, ?, ?)
            """, (date, amount, category, subcategory, notes))
    return {"status": "success", "id": c.lastrowid}
    
@mcp.tool
def list_expenses():
    """List all expenses in the database."""
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute("SELECT id, date, amount, category, subcategory, notes FROM expenses ORDER BY id ASC")
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, row)) for row in cur.fetchall()]
        

if __name__ == "__main__":
    mcp.run()