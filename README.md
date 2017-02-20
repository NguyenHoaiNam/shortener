# Shortener
============================

### About

Here is a simple tool to reduce your link when you want to send a link to someone

### Install

Using `virtualenv` as highly recommended to run this project for testing:

- Create a virtualenv
```
virtualenv create shortener-test
source shortener-test/bin/activate
```
- Clone this project
```
git clone https://github.com/NguyenHoaiNam/shortener.git
```
- Install required packages
```
pip install -r shortener/requirements.txt
```
- Install deverlop enviroment for this project
```
cd shortener
python setup.py develop
```
- Running APP
```
pecan serve config.py
```

### Demo

- After running app. Access the app folows link: http://localhost:3007/ 

- Copy a link to square and submit, after that we will receive a short link.

- Now, we can access the link with a short link received.
