# Start project

1. You need to create your own .env file in envs folder like it was written in .env_example file
2. Than run command 'export $(grep -v '^#' envs/.env | xargs)'
3. Create virtual environment and activate it
4. pip install -r requirements.txt
5. After that run 'python manage.py migrate'
6. And now you can run 'python manage.py runserver'

# Problem with tests
With some troubles 'python manage.py test .' command is not working. This command just don't see tests. 
To run tests you should it manually. 
1. Test api test run 'python manage.py test apps.main.tests.test_api'
2. To test serializers run 'python manage.py test apps.main.tests.test_serializer'
