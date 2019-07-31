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

### Create Django project   
1. cd <project folder>   
2. django-admin startproject mysite   
  
### Start Django test server   
1. python manage.py runserver   

### git
1. if we don't check in the file, put it in .gitignore

### left over
https://docs.djangoproject.com/en/2.2/topics/http/urls/#naming-url-patterns

### Reference   
1. LDAP https://technowhisp.com/django-access-control-using-ldap/   
2. https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/   
3. https://www.dev2qa.com/django-custom-login-page-use-login_required-decorator/
4. https://medium.com/@himanshuxd/how-to-create-registration-login-webapp-with-django-2-0-fd33dc7a6c67
