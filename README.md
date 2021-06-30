# CBC-MAC - Django App for an SE Course [![Build Status](https://travis-ci.com/agarwalchaitanya/ISS-4.svg?token=dMtVNw6oKpsnbfaS7i8n&branch=master)](https://travis-ci.com/agarwalchaitanya/ISS-4) [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
> In cryptography, a cipher block chaining message authentication code (CBC-MAC) is a technique for constructing a message authentication code from a block cipher. The message is encrypted with some block cipher algorithm in CBC mode to create a chain of blocks such that each block depends on the proper encryption of the previous block. This interdependence ensures that a change to any of the plaintext bits will cause the final encrypted block to change in a way that cannot be predicted or counteracted without knowing the key to the block cipher. 

Project aims at building a playground to understand the cryptographic technique. Or at the very least, to redevelop this [webpage](http://cse29-iiith.vlabs.ac.in/exp5/index.php).
Currently, it is deployed on [heroku](https://pacific-inlet-80187.herokuapp.com/).

<!-- ## ToDo
- [ ] Code the playground
- [ ] Follow design and architectural patterns :shipit: 
- [x] Write tests, add CI
- [ ] Document
- [x] Auto Deploy
- [ ] Containerize
- [ ] Integrate CodeCov -->

## Getting Started
> This assumes you have pip3, python3(>3.6) installed in a virtual environment(recommended) running in the clone of [this repository](https://github.com/agarwalchaitanya/ISS-4)

```bash
$ pip3 install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py runserver $PORT
```
Run the unit tests:
```bash
$ python3 manage.py test
```
## Deployment
The project is configured to be deployed to heroku and has a [running web instance](https://pacific-inlet-80187.herokuapp.com/). Once you have the heroku cli set up, follow these steps to create and deploy. Make sure you're on your latest commit.
```bash
$ heroku create
$ git push heroku master
$ heroku ps:scale web=1
$ heroku open
```
## Built With
- Django 2.1.5
- Python 3.6
- Gunicorn

## Acknowledgements
@karandeepSJ for mentoring during the development stage! :penguin:
