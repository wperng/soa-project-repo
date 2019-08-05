# soaproject

### Setup Virtual Environment  
1. pip install virtualenv  
2. python -m pip install --upgrade pip  
3. python -m venv env  
4. To active: mypthon\Scripts\activate (Mac/Linux: "source mypython/bin/activate")  
5. (optional) pip install virtualenvwrapper-win
6. (optional) mkvirtualenv myproject
7. (optional) workon myproject

### Install Django   
1. pip install Django   

### Install LDAP module   
1. django-python3-ldap (django-auth-ldap is not good as it is pure python solution)

### Create Django project & application
1. cd <project folder>   
2. django-admin startproject mysite ("django-admin startproject myproj ." will create in the current directory)   
3. python manage.py startapp polls
  
### Create Super user
1. python manage.py createsuperuser
  
### Modal creation
1. python manage.py makemigrations polls (Generate Script file)
2. python manage.py sqlmigrate polls 0001 (Generate SQL Command)
3. python manage.py migrate (create scheam in database)
  
### Start Django test server   
1. python manage.py runserver   

### Deployment
1. pip install -r requirements.txt
2. pip freeze > requirements.txt
3. pip show <packagename>

### git
1. if we don't check in the file, put it in .gitignore

### left over
https://docs.djangoproject.com/en/2.2/topics/http/urls/#naming-url-patterns

### Reference   
1. LDAP https://technowhisp.com/django-access-control-using-ldap/   
2. https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/   
3. https://www.dev2qa.com/django-custom-login-page-use-login_required-decorator/
4. https://medium.com/@himanshuxd/how-to-create-registration-login-webapp-with-django-2-0-fd33dc7a6c67
5. https://carolhsu.gitbooks.io/django-girls-tutorial-traditional-chiness/content/django_models/README.html (Chinese)
