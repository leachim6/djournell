Djournell
=========

### What's up with the name ###
Djournell combines 3 different words,
* Cornell , as in the note taking strategy
* Django  , as in the web framework used to build it
* Journal , as something used to take notes

### How do I say it ? ###
Djournell is pronounced as "Journal"


Grabbing the Dependencies
=========================
Djournell itself has only two dependencies

### Django ###
Get the latest svn version of django by doing

  	 svn co http://code.djangoproject.com/svn/django/trunk/

### Database ###
you will need the python module for the database you choose to use (you only need one of these)
(You can get them from http://pypi.python.org) __Sqlite is the default__

* Mysql      : mysql-python
* Sqlite     : Pysqlite
* PostgreSQL : python-pgsql

Installing Djournell
====================
### Configuring settings ###
In the root of the project there will be a file called settings.py.example,
This file is extremely well commented , just follow the comments and change
the relevant information to your specific settings , after you're done with that

### Running the App ###
Now all you have to do is run this from the project root

	    python ./manage.py syncdb

then fill in all the information it asks for , when it asks you about an admin user
say yes and fill in the relevant information
after that , all you have to do is run

	    python ./manage.py runserver

then go to http://localhost:8000 in your web browser and you're off to the races
