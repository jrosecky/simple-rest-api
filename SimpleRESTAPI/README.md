# Simple REST API

A simple REST API built with Python and FastAPI.

## Features

- CRUD operations for items
- JSON-based communication
- Data validation using Pydantic
- Automated API tests with pytest
- Basic CI workflow using GitHub Actions

## Technologies

- Python
- FastAPI
- Pydantic
- pytest
- GitHub Actions

## Run the application

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

## Run tests

```bash
python -m pytest
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/items` | Get all items |
| POST | `/items` | Create a new item |
| PUT | `/items/{item_id}` | Update an item |
| DELETE | `/items/{item_id}` | Delete an item |