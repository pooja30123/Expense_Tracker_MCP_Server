# Expense Tracker MCP Server

A simple Expense Tracker server built using the Model Context Protocol (MCP).

## About This Repository
This repository contains the code for an MCP-compliant server that allows you to track expenses, categories, and related data. It is designed to be easily deployed locally or on cloud platforms like FastMCP.

## What is MCP?
Model Context Protocol (MCP) is a protocol for building modular, interoperable AI and automation servers. MCP servers can be connected to various clients and platforms, enabling flexible integrations and automation workflows.

## Features
- Add, view, and manage expenses
- Organize expenses by categories
- Easily extensible for new features
- Ready for deployment on FastMCP or any cloud VM

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