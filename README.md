My personal webpage registered to tadejpetric.eu

The `page` folder contains the application and implementation (as well as further README files); `website` contains the settings.

instruction notes:

Create a python virtual environment with `python -m venv tadejpetric_eu` and activate it with `source bin/activate.sh` (or the supported scripting language of your choice)

Clone the repository in the venv (using `git clone git@github.com:tadejpetric/tadejpetric_eu.git`)

Install the python requirements with pip. This is done using `pip install -r requirements.txt`

Lastly, you will need to set up the database. The project uses the postgres because of its array attributes (and simply because it's a great database). The following instructions are based on Arch Linux
```
sudo pacman -S postgresql

sudo -iu postgres
initdb -D /var/lib/postgres/data

exit

systemctl enable postgresql.service
systemctl start postgresql.service

sudo -iu postgres

psql
CREATE DATABASE page
CREATE USER pageuser WITH PASSWORD 'password'; -- set password to something secure
ALTER ROLE pageuser SET client_encoding TO 'utf8';
ALTER ROLE pageuser SET timezone TO 'UTC';
ALTER ROLE pageuser SET default_transaction_isolation TO 'read committed';
GRANT all PRIVILEGES ON DATABASE page TO pageuser;
\q
exit

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0:8080
```

This should get the server up and running. You can reach it on <http://localhost:8080> but the relevant content is currently on <http://localhost:8080/racuni>
