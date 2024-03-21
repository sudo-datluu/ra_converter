# RA Converter Project

## Overview

The RA Converter project is an tool designed to analyze CSV and Excel files. It efficiently identifies column types within these files and matches them with their corresponding Pandas data types.

## Workflow

The RA Converter operates through a straightforward workflow:

1. **User Upload**: Users upload their CSV or Excel files via the frontend interface.
2. **Backend Processing**: The backend system processes the uploaded file, inferring the column types.
3. **View Details**: Users can view detailed information about the inferred column types, directly from the frontend interface.

## Technology Stack

- **Frontend**: Built with React, offering a dynamic and responsive user interface.
- **Backend**: Utilizes Django for server-side logic, Pandas for data processing, and a combination of Redis and Celery for efficient task queuing and asynchronous processing.

## Installation Instructions

Follow these steps to set up and run the RA Converter project:

### Prerequisites

Ensure Python, Redis, and Node.js are installed on your system.

### Setting Up the Python Environment

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # On Windows
   .\\venv\\Scripts\\activate
   # On macOS/Linux
   source venv/bin/activate
   ```
2. Install the requirements

   ```bash
   pip install -r requirements.txt
   ```

### Setting Up the Redis

1.  Install Redis following the instructions on the [official Redis website](https://redis.io/docs/install/install-redis/).

2.  Start the Redis server

   ```bash
   redis-server
   ```

### Setting Up Celery

Within your project directory, run the Celery worker:

   ```bash
   python -m celery -A ra_converter worker -l info
   ```

### Running the backend services

   ```bash
   python manage.py runserver
   ```

### Install dependencies and running the frontend services

   ```bash
   cd frontend
   npm install
   npm start
   ```