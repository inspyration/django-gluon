What is it?
===========

#) Mainly a Django framework with some tools to glue applications amongst themselves such as:
    #) Some model mixins providing usefull common features usually needed
    #) Some handy view mixins too
    #) Webservice automation features
    #) Rest features for all models
    #) Import / Export automation features
    #) Integration of Bootstrap3, JQuery, Datatables, Chartit, Dhmltx and a bunch of other frameworks
#) A functionnal integrated architecture
    #) Management of users, groups, profiles, applications, security, ...
    #) Management of SAAS: add an customer account, select its applications and configure it.
    #) Integration of all application into a single front-end
    #) Back-office interfaces for administrator and SAAS Manager

Based on PyDanny guidelines found in 2 scoops of "Django: Best practices for Django 1.6."

Summary
=======

#) prerequisites
#) create a virtual environment
#) use the virtual environment
#) install requirements
#) Run the server

prerequisites
=============

This project is based on Python 3 only and uses Django 1.7.1.

    # aptitude install python3 python3-pip

You must install either virtualenv or virtualenvwrapper

Install virtualenv
------------------

Using *pip*

    # pip3 install virtualenv

Install virtualenvwrapper
-------------------------

Using *pip*

    # pip3 install virtualenvwrapper

Then, you must add this 3 lines at the end of ~/.bashrc

    export WORKON_HOME = /.virtualenvs
    mkdir -p $WORKON_HOME
    source ~/.local/bin/virtualenvwrapper.sh

Create a virtual environment
============================

When using virtualenv, you may want to create a virtual environment for each project

Using *virtualenv*

    $ virtualenv -p python3 my_virtualenv_name

Using *virtualenvwrapper*

    $ mkvirtualenv -p python3 my_virtualenv_name

Using virtual environment
=========================

Each time you want to use the project, you must use the virtual environment

Using *virtualenv*

    $ source my_virtualenv_name/bin/activate

Usingh *virtualenvwrapper*

    $ workon your_virtual_env_name

You can check if the virtual environment is active with

    $ which python

Install requirements
====================

In order to use your project for the first time, you must install all requirements

    $ pip install -r requirements/base.txt

How to run the Server
=====================

Now, run the server and enjoy it !

    $ ./manage.py runserver

