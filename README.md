This is my first web blog
Do the following in order to run this code:

1. Create a top level folder "foldername"
2. Change into the directory in 1. and Create a virtual environment and activate
   $ pip install pipenv
   $ mkdir .venv
   $ pipenv install flask
   $ .venv\Scripts\activate (Windows)
   $ .venv/bin/activate (Linux)

3. Create the directory tree as shown below. The instance folder will be
   created see below

├───.venv
├───blog
│ ├───static
| | └───style.css
| | └───vendingmachine.png
│ └───templates
│ | └───auth
| | | └───login.html
| | | └───register.html
│ | └───blog
| | | └───create.html
| | | └───index.html
| | | └───update.html
| | └───base.html
| └─── --init--.py
| └─── auth.py
| └─── blog.py
| └─── db.py
| └─── schema.sql
├───instance
└───tests

4. Dump the code for the git repo into it or just clone the repo
   git clone
5. set the environment variable
   # $env:FLASK_APP=".\blog\ (Windows)
   # $env:FLASK_ENV="Development" (Windows)
   # export FLASK_APP=".\blog\ (Linux)
   # export FLASK_ENV="Development" (Linux)
   # flask run
