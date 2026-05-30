# DBMS Project

A Flask-based car and bike rental web application with Supabase PostgreSQL for data storage and Vercel deployment support.

## Features

- User registration and login
- Vehicle browsing and filtering
- Booking flow with booking management
- Admin dashboard for users, vehicles, and bookings
- Supabase-ready PostgreSQL schema and seed data
- Vercel-friendly Flask deployment setup

## Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- PostgreSQL on Supabase
- Vercel for hosting

## Project Files

- [app.py](app.py) - main Flask application
- [db_setup.py](db_setup.py) - database setup script for local use
- [supabase_schema.sql](supabase_schema.sql) - SQL file for Supabase tables and demo data
- [vercel.json](vercel.json) - Vercel routing configuration
- [api/index.py](api/index.py) - Vercel Python entrypoint
- [.env.exp](.env.exp) - example environment variables

## Local Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a local `.env` file or set environment variables.
4. Run the app:

```bash
python app.py
```

## Environment Variables

Use these variables in Vercel and local development:

- `SECRET_KEY` - random secret for Flask sessions
- `DATABASE_URL` - Supabase PostgreSQL connection string
- `VERCEL` - set to `1` on Vercel

See [.env.exp](.env.exp) for the expected format.

## Supabase Database Setup

1. Create a Supabase project.
2. Open the SQL editor.
3. Run [supabase_schema.sql](supabase_schema.sql).
4. Copy your Supabase connection string into `DATABASE_URL`.

The demo data uses plain-text passwords by design for this project:

- `admin@example.com` / `admin123`
- `user@example.com` / `user123`

## Deploying to Vercel

1. Push this repository to GitHub.
2. Import the repository into Vercel.
3. Set the environment variables listed above.
4. Deploy the project.

Vercel uses [api/index.py](api/index.py) as the Python entrypoint and [vercel.json](vercel.json) for routing.

## Notes

- This project is configured for Supabase, not a local PostgreSQL server.
- If you change the database schema, update both the Flask models and [supabase_schema.sql](supabase_schema.sql).