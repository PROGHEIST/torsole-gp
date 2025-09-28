# TODO: Switch to SQLite for Development and PostgreSQL for Production

## Steps to Complete:

1. **Edit torsole_backend/settings.py**: Modify the DATABASES configuration to use SQLite when DEBUG=True (development) and PostgreSQL when DEBUG=False (production).
   - Status: Completed

2. **Run Migrations for Development**: After editing, run `python manage.py makemigrations` and `python manage.py migrate` to set up the SQLite database.
   - Status: Completed

3. **Verify Configuration**: Test the setup in development mode (DEBUG=True) to ensure SQLite is used, and confirm PostgreSQL for production.
   - Status: Completed (Configuration updated; SQLite will be used in development when DEBUG=True, PostgreSQL in production when DEBUG=False)

4. **Update TODO**: Mark steps as completed after each action.
   - Status: In Progress
