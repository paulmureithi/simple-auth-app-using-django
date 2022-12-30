# Simple Registration and Login Web App 

This app allows users to create an account on the app and login.
Will later add an profile page that alows users to edit their personal details after succesfull registration.


## Setup

The first thing to do is to clone the repository:

```sh
$ mkdir auth_project && cd auth_project
$ git clone https://github.com/paulmureithi/user-authentication-using-Django.git
```

Create folder for the project and a virtual environment to install the packages in and activate it:

```sh
$ python3 -m venv venv
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/register/`.
