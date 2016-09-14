python manage.py migrate
python manage.py loaddata fixtures/rocketitems.json
echo "from rockettrade.models import User; import os; User.objects.create_superuser('admin', '', os.environ.get('ADMIN_PASS'))" | python manage.py shell
python manage.py runserver 0.0.0.0:8000