# FlashyCards

FlashyCards is a browser application that will allow a registered user to create a deck of flashcards and be able to use them to study or review. Use this as a tool to your advantage and you will surely ace the exam!

## Installation
```bash
#Have Homebrew installed on Mac
#Install Ember
brew update
brew upgrade node
brew install node
npm install -g npm
npm install -g ember-cli

#Pull down dependencies for frontend
git clone https://github.com/qadams/flashycards-test.git
cd frontend
npm install

#Make sure to install python
#Install Django
easy_install pip
pip install virtualenv
export PYTHONUSERBASE=$HOME
pip install--user virtualenv
#Setup Virtual Environment
virtualenv -p /usr/bin/python2.7 venv
source venv/bin/activate
#Install Django's core
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install djangorestframework-jsonapi==2.0.0-beta.2
```

## Getting Started
In order to run FlashyCards app,
```bash
#In frontend directory
ember build
ember s 
#In Django project directory
python manage.py runserver
```

# License
Currently, there is no license associated with this project, however, I do believe any person can use my code freely.
