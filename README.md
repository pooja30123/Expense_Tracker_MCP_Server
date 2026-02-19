# Expense Tracker MCP Server

This project is an Expense Tracker MCP server. To set up and run locally:

## Setup
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate the virtual environment:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

```bash
python main.py
```

## Deployment
You can deploy this server to FastMCP or any cloud VM. For FastMCP, push your code to GitHub and connect your repo in the FastMCP dashboard.

## Notes
- Do not commit sensitive files (e.g., .env) or your virtual environment folder.
- See .gitignore for ignored files.