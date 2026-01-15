import os
import django
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError

def create_superuser():
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

    if not username or not password:
        print("No superuser environment variables found. Skipping...")
        return

    try:
        User = get_user_model()
        if not User.objects.filter(username=username).exists():
            print(f"Creating superuser '{username}'...")
            User.objects.create_superuser(username=username, email=email, password=password)
            print("Superuser created successfully.")
        else:
            print(f"Superuser '{username}' already exists.")
    except OperationalError:
        print("Database not ready, skipping superuser creation.")
    except Exception as e:
        print(f"Error creating superuser: {e}")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    django.setup()
    create_superuser()
