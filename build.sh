#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

# ตัวนี้แหละที่จะดึง CSS ของ Django Admin มารวมกัน
python manage.py collectstatic --no-input

python manage.py migrate

# สร้าง Superuser อัตโนมัติ
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', '12345678')
    print('Superuser created successfully.')
END