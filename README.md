# searchthesis
simple thesis search engine for PSU Computer Studies (internal use only)

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
4.  Install dependencies
	```batch
	pip3 install -r requirements.txt
	```
5.  Assuming all dependencies succeeded, Renew the database 
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
9.  Browse localhost:8000/search/ to see public search page

# Todo
 * export
 * landing page
 * reports
 * refactor
 * etc..
