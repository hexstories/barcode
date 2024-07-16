# Django Barcode Generator

This is a simple Django project for generating and storing barcodes. It includes a Django app to generate barcodes, save them to the database, and manage them through the Django admin interface.

## Features

- Generate barcodes using the `python-barcode` library.
- Save generated barcodes as images in the database.
- Manage barcodes via the Django admin interface.
- Simple form interface to generate barcodes.

## Requirements

- Python 3.x
- Django 3.x or later
- Pillow
- python-barcode

## Installation

1. **Clone the repository:**

    ```sh
    git clone  https://github.com/hexstories/barcode.git
    cd django-barcode-generator
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Usage

1. **Access the Django admin interface:**

    Navigate to `http://127.0.0.1:8000/admin/` and log in with your superuser account. You can add, edit, and delete barcodes through the admin interface.

2. **Generate a barcode:**

    Navigate to `http://127.0.0.1:8000/generate/` to input a code and generate a barcode.

3. **View a generated barcode:**

    Navigate to `http://127.0.0.1:8000/barcode/<code>/` to view the barcode image for the given code.

## Project Structure

