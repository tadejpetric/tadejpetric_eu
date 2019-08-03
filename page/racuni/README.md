# Project app

## Description of the project

If you have a small company (mostly s.p. in Slovenia), you need to generate receipts of a certain kind to be allowed to receive payment for your work. This app does precisely that: allows you to enter receipts in a user-friendly form with all the required fields listed and supports saving and printing those receipts (on an A4 sized paper). You can choose to generate the receipts anonymously, without an account (however without the ability to save them to a database) or you can create an account and save those receipts to the said account.

In the following section, URL's listed will be relative to the current app; if the URL is mentioned as `login` it would mean `localhost:8080/racuni/login` if following the locally hosted instructions on the main readme. The URLs are in code blocks (making links wouldn't work with every setup).

### accessible sites

The app starts on the login page at `login`. There's an option to register a new account and login. The page also supports some error messages (if you get redirected from an inaccessible page, failed and successful registers and failed logins). Logging in will redirect to `homepage`, registring will reload the site with a status message. Alternatively, you can choose to ignore accounts and enter a receipt anonymously. By clicking that link, you are redirected to `form_input_anonymous`.

Homepage is located on `homepage`. It serves as a site where all previous receipts are displayed. There you can choose to delete them, edit them or print them. The page also serves as a central hub; you can access other pages from it (like statistics of receipts from the past year, settings and input of a new receipt) as well as log out of the site.

You can find settings on `settings`. Here you can set presets for entering receipts since most fields are the same in every receipt (company name, address, full name, etc.). By setting them up, when you attempt to enter a new receipt it will have some fields filled in, making the use of the site much easier.

You can also browse some simple statistics on `statistics`. A simple graph is displayed with height of bars representing the value of receipts made in each month. You are also listed some facts such as amount of receipts filed and their average value.

The core of the project are form inputs at `form_input` and `form_input_anonymous`. Here you can enter the fields which will be rendered in the receipt. You can also leave some fields blank (although printing them in such a state is far from recommended! It helps since you can save it and edit it later). Some simple error checking is performed on some fields (transaction account must start with 2 letters and followed by some digits) although not much more could be done due to inconsistent laws, specailly if companies and customers are not from Slovenia. Another feature is the extensible table so you can dynamically add and delete rows. That way you can add as many rows as you wish. If you are logged in, you can save the receipt. Logged or not, you can print them (however if you do click print, you cannot save them retroactively so logged users should usually choose save).

Directly relating to inputting forms are outputs. Those are found at `result` (although you can only get there by clicking links. Trying to input URL manually will redirect since it doesn't know which receipt). The design of the site is aimed at A4 paper printing which can be done using the builtin browser function (usually obtained by pressing ctrl+P). This allows you to generate a pdf file or print directly.

## Description of the files
- `urls.py` calls the correct function in `views.py` depending on the URI
- `views.py` responsible for calling and setting up templates. Almost no computation, just calling and preparing functions, reading POST/GET data and handling redirects. Functions in it are called by `urls.py`
- `user_manage.py` handling user creation and logins
- `receipt_manage.py` sets up everything related to receipts. Almost all the computation is done here.
- `models.py` defines the database model of the application
