# import random
# from fastmcp import FastMCP

# #Create a FastMCP server instance
# mcp = FastMCP(name = "Demo server")

# @mcp.tool
# def roll_dice(n_dice: int = 1) -> list[int]:
#     """Roll n_dice 6-sided dice and return the results."""
#     return [random.randint(1, 6) for _ in range(n_dice)]

# @mcp.tool
# def add_numbers(a: float, b: float) -> float:
#     """Add two numbers and return the result."""
#     return a + b

# if __name__ == "__main__":
#     mcp.run()


from fastmcp import FastMCP
import os
import sqlite3
import tempfile

DB_PATH = os.environ.get("EXPENSES_DB_PATH")
if not DB_PATH:
    # Use a writable temp directory if not set
    DB_PATH = os.path.join(tempfile.gettempdir(), "expenses.db")
CATEGORIES_PATH = os.path.join(os.path.dirname(__file__), "categories.json")

mcp = FastMCP(name="ExpenseTracker")

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
def add_expense(date, amount, category, subcategory = "", notes = ""):
    """Add a new expense to the database."""
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute("""
            INSERT INTO expenses (date, amount, category, subcategory, notes) VALUES (?, ?, ?, ?, ?)""",
            (date, amount, category, subcategory, notes))
    return {"status": "success", "id": cur.lastrowid}
    
@mcp.tool
def list_expenses(start_date, end_date):
    """List all expenses in the database between start_date and end_date."""
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute("""
            SELECT id, date, amount, category, subcategory, notes
            FROM expenses
            WHERE date BETWEEN ? AND ?
            ORDER BY id ASC
            """, 
            (start_date, end_date)
        )
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, row)) for row in cur.fetchall()]


@mcp.tool
def summarize_expenses(start_date, end_date, category = None):
    """Summarize total expenses by category between start_date and end_date."""
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute("""
            SELECT category, SUM(amount) as total
            FROM expenses
            WHERE date BETWEEN ? AND ?
            """
        )
        params = [start_date, end_date]

        if category:
            query += " AND category = ?"
            params.append(category)

        query += " GROUP BY category ORDER BY category ASC"

        cur = c.execute(query, params)
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, row)) for row in cur.fetchall()]
 
@mcp.resource("expense://categories", mime_type="application/json")
def categories():
    # Read fresh each time so you can edit the file without restarting
    with open(CATEGORIES_PATH, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    mcp.run()