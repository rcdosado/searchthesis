# searchthesis
simple thesis search engine for PSU Computer Studies 

# Installation

1. Install python 3.7, git, virtualenv, pip3 
2. create virtual environment & activate it
	```batch
	>python.exe -m venv env3
	>env3\scripts\activate.bat
	```
3. Clone this repository
	```batch
	>git clone https://github.com/rcdosado/searchthesis
	>cd searchthesis
	```
4.  Install mysql (this version uses it), write the account information, then install the following dependencies
	```batch
	pip3 install -r requirements.txt
	```
	change the information according to your mysql server account information in settings.py, DATABASES dictionary

5.  Assuming all dependencies succeeded, Renew the database (make sure mysql server is running using your account info.)
	```batch
	>python manage.py makemigrations
	>python manage.py migrate
	>python manage.py createsuperuser
	>..
	```
6.  Create superuser account (fill the necessary details)
	```batch	
	>python manage.py createsuperuser	
	```
7.  Run the WSGI server
	```batch
	>python manage.py runserver	
	```
8.  Go to localhost:8000/admin, login, then fill the system with information
9.  Browse localhost:8000 to see public search page

# Reports (requires root access & sql commands knowledge)

This feature enables you to export data as xlsx, csv, json, in any form you want, provided that you know sql
schema can be viewed on this page. 

1. install requirements, run the server
2. go to http://localhost/explorer, show schema, and execute something like `select * from search_thesis`.


# Backing up data

After encoding thesis information, you can back up your database by issuing
```batch
>python manage.py dumpdata search > db.json
```
after which when deploying in another computer, you can restore those information by issuing
```batch
>python manage.py loaddata db.json
```
if you want to restore user information and more, consult the Django official docs.

# Todo
 * landing page
 * refactor
 * adviser profile
