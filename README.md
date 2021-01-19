# Supermarket management App (backend)
## App description :
This is the backend of a supermarket management App build using Django 
## Project setup
Firstly, clone this repository to the current directory:
```
git clone https://github.com/HananeOB/DjangoRESTAPISuperMarket .
```
Next, set up a virtual environment and activate it:
Then, install required packages:
````
pip install -r requirements.txt
````
Configure your database then perform migration:
```
python manage.py makemigrations 
```
```
python manage.py migrate
```
The setup is complete. Run a local server with
```
python manage.py runserver 
```
The blog should be available at localhost:8000.
