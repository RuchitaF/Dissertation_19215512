[requirements.txt](https://github.com/RuchitaF/Dissertation_19215512/files/12755637/requirements.txt)
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
- [Requirements.txt](#requirements)


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
https://www.kaggle.com/datasets/cclark/product-item-data

## Code
views.py
## Requirements.txt
[Uploadiabsl-py==1.4.0
aio-pika==6.8.2
aiofiles==23.1.0
aiogram==2.25.1
aiohttp==3.7.4
aiormq==3.3.1
APScheduler==3.7.0
asgiref==3.7.2
astunparse==1.6.3
async-generator==1.10
async-timeout==3.0.1
attrs==21.2.0
Babel==2.9.1
bidict==0.22.1
blis==0.7.10
boto3==1.28.11
botocore==1.31.11
CacheControl==0.12.14
cachetools==4.2.4
catalogue==2.0.9
certifi==2023.7.22
cffi==1.15.1
chardet==3.0.4
charset-normalizer==3.2.0
ChatterBot==1.0.4
chatterbot-corpus==1.2.0
click==8.1.6
cloudpickle==1.6.0
cmake==3.27.1
colorama==0.4.6
colorclass==2.2.2
coloredlogs==15.0.1
colorhash==1.0.4
confection==0.1.1
confluent-kafka==1.9.2
cryptography==41.0.2
cycler==0.11.0
cymem==2.0.7
dask==2022.2.0
distlib==0.3.7
Django==3.2.20
django-bootstrap5==23.3
djangorestframework==3.14.0
dnspython==1.16.0
docopt==0.6.2
fastjsonschema==2.18.0
fbmessenger==6.0.0
filelock==3.12.2
fire==0.5.0
flatbuffers==2.0.7
fsspec==2023.1.0
future==0.18.3
gast==0.4.0
google-auth==1.35.0
google-auth-oauthlib==0.4.6
google-pasta==0.2.0
greenlet==2.0.2
grpcio==1.56.2
h5py==3.8.0
httptools==0.6.0
huggingface-hub==0.16.4
humanfriendly==10.0
idna==3.4
importlib-metadata==6.7.0
install==1.3.5
Jinja2==3.1.2
jmespath==1.0.1
joblib==1.0.1
jsonpickle==2.0.0
jsonschema==3.2.0
jupyter_core==4.12.0
kafka-python==2.0.2
keras==2.11.0
Keras-Preprocessing==1.1.2
kiwisolver==1.4.4
langcodes==3.3.0
libclang==16.0.6
locket==1.0.0
magic-filter==1.0.10
Markdown==3.4.4
MarkupSafe==2.1.3
mathparse==0.1.2
matplotlib==3.3.4
mattermostwrapper==2.2
msgpack==1.0.5
multidict==5.2.0
murmurhash==1.0.9
nbformat==5.8.0
networkx==2.6.3
nltk==3.8.1
numpy==1.21.6
oauthlib==3.2.2
opt-einsum==3.3.0
packaging==20.9
pamqp==2.3.0
pandas==1.3.5
partd==1.4.0
pathy==0.10.2
Pillow==9.5.0
Pint==0.18
platformdirs==3.10.0
pluggy==1.2.0
portalocker==2.7.0
preshed==3.0.8
prompt-toolkit==3.0.28
protobuf==3.19.6
psycopg2-binary==2.9.6
pyasn1==0.5.0
pyasn1-modules==0.3.0
pycparser==2.21
pydantic==1.10.2
pydot==1.4.2
PyJWT==2.8.0
pykwalify==1.8.0
pymongo==3.10.1
pyparsing==3.1.0
pyreadline==2.1
pyrsistent==0.19.3
pyTelegramBotAPI==3.8.3
python-crfsuite==0.9.9
python-dateutil==2.8.2
python-engineio==4.5.1
python-socketio==5.8.0
pytz==2021.3
pywin32==306
PyYAML==6.0.1
questionary==1.10.0
randomname==0.1.5
rasa==3.5.15
rasa-sdk==3.5.1
redis==4.6.0
regex==2021.8.28
requests==2.31.0
requests-oauthlib==1.3.1
requests-toolbelt==1.0.0
rocketchat-API==1.16.0
rsa==4.9
ruamel.yaml==0.17.10
ruamel.yaml.clib==0.2.7
s3transfer==0.6.1
safetensors==0.3.2
sanic==21.12.2
Sanic-Cors==2.0.1
sanic-jwt==1.8.0
sanic-routing==0.7.2
scikit-learn==0.24.2
scipy==1.7.3
sentry-sdk==1.3.1
six==1.16.0
sklearn-crfsuite==0.3.6
slack-sdk==3.21.3
slackclient==2.9.4
smart-open==6.3.0
spacy-legacy==3.0.12
spacy-loggers==1.0.4
SQLAlchemy==1.2.19
sqlparse==0.4.4
srsly==2.4.7
tabulate==0.9.0
tarsafe==0.0.3
tensorboard==2.11.2
tensorboard-data-server==0.6.1
tensorboard-plugin-wit==1.8.1
tensorflow==2.11.0
tensorflow-addons==0.19.0
tensorflow-estimator==2.11.0
tensorflow-hub==0.12.0
tensorflow-intel==2.11.0
tensorflow-io-gcs-filesystem==0.31.0
termcolor==2.3.0
terminaltables==3.1.10
thinc==8.1.12
threadpoolctl==3.1.0
tokenizers==0.13.3
toolz==0.12.0
torch==1.13.1
tqdm==4.65.0
traitlets==5.9.0
transformers==4.30.2
twilio==6.50.1
typeguard==4.0.0
typer==0.9.0
typing-utils==0.1.0
typing_extensions==4.4.0
tzlocal==2.1
ujson==4.3.0
urllib3==1.25.4
virtualenv==20.24.2
wasabi==1.1.2
wcwidth==0.2.6
webexteamssdk==1.6.1
websockets==10.0
Werkzeug==2.2.3
wrapt==1.15.0
yarl==1.9.2
zipp==3.15.0
ng requirements.txt…]()
