from django.contrib.auth import get_user_model

from config.celery_app import app
import subprocess as sp

@app.task()
def get_users_count():
    User = get_user_model()
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()


