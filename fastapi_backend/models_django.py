import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "veva.settings")
django.setup()

from admin_app.models import add_product