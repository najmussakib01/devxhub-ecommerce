# devxhub-ecommerce
admin user = admin
pass: Admin123

paypal user = monirulslm7@outlook.com
pass: Monir@786


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [project details](#project-details)


## General info
# Django E-commerce Site with Payment Gateway and REST API. An E-commerce site where users can browse products, add them to their shopping cart,
and make purchases. Implement an API to expose the platform's functionality to other services.
	
## Technologies
Project is created with:
* Python version: 3.8.10
* Django version: 4.1.1
* Django Rest Framework version: 3.14.0
* Database Sqlite3
* Java Script
* Bootstrap
* fontawesome
	
## Setup
To run this project, install it locally using pip:

```
$ git clone  https://github.com/monir07/devxhub-ecommerce.git
$ virtualenv venv
$ source venv/bin/activate
$ cd devxhub-ecommerce
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py create_data
$ python manage.py runserver
```

## Project Details

* User Authentication:
User can Registration, Login, and Logout functionality. When an user register, user profile automatically created. After login User can update their profile by clicking update profile.

* Product Management:
Product Database Create with fields: name, description, price, image, and stock status. user can visit all product by clicking shop button at home page. product list page have product search option and pagination.

* Shopping Cart:
User can add product in shopping cart by clicking add to cart button. Authenticate and UnAuthenticate user also add product in cart. Shopping Cart functionality design with django session. After added product in cart user can increase or decrease product quantity. user can get product discount by using coupon code. 

* Purchases and Payment Integration:
After added product in shopping cart user can checkout for payment. after clicking checkout button user see his basic information with shipping address then clock continue user PayPal payment button.