# urshop
### A marketplace web application written in django, where people can both sell and buy.  
## How to install
### Download or clone this repository and navigate inside Urshop directory
```bash
cd urshop/
```
### Provide environment variables
### Create a ```.env``` file
```bash
touch .env
```
### Set those values in the created file
```env
SECRET_KEY
DATABASE_USER = postgres # default
DATABASE_PASSWORD = postgres # default
DATABASE_HOST = db # inside container
DATABASE_PORT = 5432 # default
STRIPE_PUBLIC_KEY 
STRIPE_SECRET_KEY
STRIPE_API_KEY
STRIPE_WEBHOOK_KEY # Only for test
```
### Remove stripe-cli from docker-compose if you don't want to see webhook responses in console

### Running through docker
```bash
docker-compose up --build
```
### Shutdown docker containers and create the postgres database used by the app
### Can follow these steps
```bash
docker-compose down
docker-compose exec db bash
psql -U postgres 
CREATE DATABASE urshop;
\q
exit
docker-compose up
```
### Now you can makemigrations and migrate
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### Running outside docker
```bash
pip install -r requirements.txt
psql -i -u postgres 
CREATE DATABASE urshop;
\q
exit
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## App features
### A registered user is able to add products with :  

    - name  
    - description  
    - categories  
    - brand  
    - price  
    - images  
### He can then edit his own products.
### Any user can browse the app, search for products and add to cart, but only registered user can proceed to checkout.  
### A non registered can leave his cart and resume shopping within an interval of 30 days
### Item quantity can be modified prior to checkout.  
### Payment system : Stripe.  

## Features to be addded
    - [ ] Products recommendation system based on user activity on the app  
    - Possibility to add products from another market place proving url  
    - Products rating by customers  
    - Feedback chat under products
    - Direct real time chat between users  
    - Other payment systems : yoomoney, paypal, PM
    - others

    