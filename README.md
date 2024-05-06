# Vendor Profile Management

## Project Setup

### Pre-Requirements
- Python Version 3.12
- Poetry 1.7.1

Follow the  steps in order to setup the project and install the project requirements.

Step 1: Clone the repository

`git clone https://github.com/anubhuti24/vendor_hub.git`

Step 2: Setup poetry environment

`poetry shell`

Step 3: Install the project requirements

`poetry install --no-root`

Step 4: Creating migrations for the project

`python manage.py makemigrations`

Step 5: Applying the migrations

`python manage.py migrate`

Step 6: Create a superuser/admin and provide username and password.

`python manage.py createsuperuser`

This will a superuser with provided username and password.


Step 6: Run the django server

`python manage.py runserver`

Login to the django admin route using provided username and password of the superuser.

🚀 Now, you have successfully logged in as an admin and can test the APIs and database interaction.

# Documented APIs

Import the provided JSON link into a tool for API testing, such as Postman. This JSON file contains detailed descriptions of all the API endpoints. You can then thoroughly test each endpoint to ensure its functionality.

Firstly, generate the token using username and password of the superuser using API endpoint `/api-token-auth/`

This token needs to be provided in the Authorization Header.

Run all the apis using auth token.

# Test Suite

## Test the purchase order APIs

`python manage.py test purchase_order.tests`

## Test the vendor APIs

`python manage.py test vendor.tests`