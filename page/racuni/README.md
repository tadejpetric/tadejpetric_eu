# Project app

Description of the files
- `urls.py` calls the correct function in `views.py` depending on the URI
- `views.py` responsible for calling and setting up templates. Almost no computation, just calling and preparing functions, reading POST/GET data and handling redirects. Functions in it are called by `urls.py`
- `user_manage.py` handling user creation and logins
- `receipt_manage.py` sets up everything related to receipts. Almost all the computation is done here.
- `models.py` defines the database model of the application
