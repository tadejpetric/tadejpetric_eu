My personal webpage registered to tadejpetric.eu

visit /racun receipt generator (in Slovenian)

instruction notes:
you need postgresql
on arch linux instructions:
```
sudo pacman -S postgresql
pip install psycopg2

sudo -iu postgres
initdb -D /var/lib/postgres/data

CREATE DATABASE page
CREATE USER pageuser WITH PASSWORD 'password'; -- set password to something secure
ALTER ROLE pageuser SET client_encoding TO 'utf8';
ALTER ROLE pageuser SET timezone TO 'UTC';
ALTER ROLE pageuser SET default_transaction_isolation TO 'read committed';
GRANT all PRIVILEGES ON DATABASE page TO pageuser;
\q
exit

systemctl enable postgresql.service
systemctl start postgresql service

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0:8080
```
