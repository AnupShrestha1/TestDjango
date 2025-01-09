import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hazard.settings')
django.setup()

from app.models import User

# Create a new user
user = User.objects.create(
    firstname="John",
    lastname="Doe",
    email="john.doe@example.com",
    password="securepassword"
)

# Print the created user
print(f"Created user: {user}")

# Retrieve all users
users = User.objects.all()
print(f"All users: {list(users)}")
