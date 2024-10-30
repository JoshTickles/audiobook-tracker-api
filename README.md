# Audiobook Tracker API

Welcome to the Audiobook Tracker API! This API allows you to manage and track your audiobook listening activities. You can add, update, retrieve, and delete audiobook entries.

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL
- Docker & Docker Compose (for containerization)

### Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd audiobook_tracker
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**

   Ensure PostgreSQL is running and the `uuid-ossp` extension is enabled. Edit your `.env` file to match your database configuration.

5. **Run the Application**

   ```bash
   python src/main.py
   ```

## API Endpoints

### Landing Page

- **GET /**  
  Returns a welcome message.

### Audiobooks

- **GET /audiobooks/**  
  Retrieve all audiobooks.

- **POST /audiobooks/**  
  Add a new audiobook.
  - **Body**: 
    ```json
    {
      "title": "Book Title",
      "author": "Author Name",
      "length": "HH:MM:SS",
      "start_date": "YYYY-MM-DD",
      "end_date": "YYYY-MM-DD" ## This is optional
    }
    ```

- **PUT /audiobooks/{audiobook_id}/end_date**  
  Update the end date for an audiobook.
  - **Path Parameter**: `audiobook_id` (UUID)
  - **Body**: 
    ```json
    {
      "end_date": "YYYY-MM-DD"
    }
    ```

- **DELETE /audiobooks/{audiobook_id}**  
  Delete an audiobook.
  - **Path Parameter**: `audiobook_id` (UUID)

### Health Check

- **GET /health**  
  Check the database connection status.

## Using the API

You can test the API using tools like Postman or Insomnia by importing the OpenAPI schema available at `/openapi.json`.

