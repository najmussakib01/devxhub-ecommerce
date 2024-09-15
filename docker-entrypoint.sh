#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create a superuser (optional)
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
    echo "Creating superuser..."
    python manage.py createsuperuser --noinput || true
fi

# Create initial data
echo "Creating initial data..."
python manage.py create_data

#Download static content
echo "Download static content"
python manage.py collectstatic
# Start Django development server
echo "Starting Django server..."
exec "$@"
