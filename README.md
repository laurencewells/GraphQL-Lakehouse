# GraphQL Databricks

A GraphQL abstraction layer for Databricks Apps that provides a modern, type-safe API interface for interacting with Databricks resources.

## Overview

This project provides a GraphQL API that abstracts Databricks functionality, making it easier to interact with Databricks resources through a modern, type-safe interface. It uses FastAPI and Strawberry GraphQL to create a robust and performant API layer.

## Features

- GraphQL API for Databricks resources
- Type-safe query interface
- FastAPI backend with modern async support
- Databricks SQL integration
- Health check endpoint
- CORS support

## Prerequisites

- Python 3.8+
- Databricks account and credentials
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/GraphQL_Databricks.git
cd GraphQL_Databricks
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Set up your Databricks credentials in your environment:
```bash
export DATABRICKS_HOST="your-databricks-host"
export DATABRICKS_TOKEN="your-databricks-token"
```

## Running the Application

Start the FastAPI server:
```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- GraphQL Playground: `http://localhost:8000/graphql`
- OpenAPI Documentation: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/v1/health`

## Project Structure

```
.
├── api/            # API routes and GraphQL schema
├── common/         # Shared utilities and configurations
├── examples/       # Example queries and usage
├── app.py         # Main FastAPI application
├── app.yaml       # Application configuration
└── requirements.txt # Project dependencies
```

## Dependencies

- databricks-sdk: Databricks SDK for Python
- databricks-sql-connector: SQL connector for Databricks
- fastapi: Modern web framework
- strawberry-graphql: GraphQL library
- databricks-sqlalchemy: SQLAlchemy integration for Databricks

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the terms of the license included in the repository.

## Support

For support, please open an issue in the GitHub repository.
