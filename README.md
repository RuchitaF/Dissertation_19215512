
# E-commerce Chatbot
![welcome](https://github.com/RuchitaF/Dissertation_19215512/assets/125932133/ed26e9c7-0d0a-4268-8a03-d646e3e3563e)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Dataset](#dataset)
- [Code](#code)


## Introduction

This is a Django-based E-commerce Chatbot project that provides product recommendations, customer service assistance, and product information and size/fit recommendations to users. The chatbot is trained to answer user queries related to products, returns, orders, and more.

## Features

- Product recommendations based on user queries
- Customer service support and FAQs
- Product information lookup
- User-friendly web interface
- RESTful API for integration with other systems
- Kids' size recommendations

## Technologies Used

- Django
- ChatterBot
- REST framework
- scikit-learn (for product recommendations)
- HTML/CSS for the web interface
- JavaScript (for interactive features)
- PostgreSQL (or any compatible database)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/e-commerce-chatbot.git

1. Install the required Python packages:
   
   pip install -r requirements.txt
2. Set up your database in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your-database-name',
        'USER': 'your-database-user',
        'PASSWORD': 'your-database-password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
3.Run migrations:

python manage.py makemigrations
python manage.py migrate

4. Start the development server:

python manage.py runserver

## Usage
-Visit the web interface and start chatting with the chatbot.
-You can ask for product recommendations, information about products, customer service assistance, and more.
-Explore the different features of the chatbot.

## API Endpoints
/api/categories/: List of product categories.
/api/products/: List of products.
/api/products/<int:pk>/: Product details by ID.
/api/recommendations/: Product recommendations based on user queries.

## Dataset


## Code
views.py
