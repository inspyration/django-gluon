What is it?
===========

1. Mainly a Django framework with some tools to glue applications amongst themselves such as:
    1. Some model mixins providing usefull common features usually needed
    1. Some handy view mixins too
    1. Webservice automation features
    1. Rest features for all models
    1. Import / Export automation features
    1. Integration of Bootstrap3, JQuery, Datatables, Chartit, Dhmltx and a bunch of other frameworks
1. A functionnal integrated architecture
    1. Management of users, groups, profiles, applications, security, ...
    1. Management of SAAS: add an customer account, select its applications and configure it.
    1. Integration of all application into a single front-end
    1. Back-office interfaces for administrator and SAAS Manager

Based on PyDanny guidelines found in 2 scoops of "Django: Best practices for Django 1.6."

Summary
=======

1. prerequisites
1. create a virtual environment
1. use the virtual environment
1. install requirements
1. Run the server

prerequisites
=============

This tutorial is based on python3.

    # aptitude install python3

You must install either virtualenv or virtualenvwrapper

Install virtualenv
------------------

- install virtualenv

    # pip install virtualenv

Install virtualenvwrapper
-------------------------

- install virtualenvwrapper

    # pip install virtualenvwrapper

- Add this 3 lines at the end of ~/.bashrc

    export WORKON_HOME = /.virtualenvs
    mkdir -p $WORKON_HOME
    source ~/.local/bin/virtualenvwrapper.sh

Create a virtual environment
============================

When using virtualenv, you may want to create a virtual environment for each project

- with virtualenv

    $ virtualenv -p python3 my_virtualenv_name

- with virtualenvwrapper

    $ mkvirtualenv -p python3 my_virtualenv_name

Using virtual environment
=========================

Each time you want to use the project, you must use the virtual environment

- with virtualenv

    $ source my_virtualenv_name/bin/activate

- with virtualenvwrapper

    $ workon your_virtual_env_name

Install requirements
====================

In order to use your project for the first time, you must install all requirements

    $ pip install -r requirements/base.txt

How to run the Server
=====================

Now, run the server and enjoy it !

    $ ./manage.py runserver
