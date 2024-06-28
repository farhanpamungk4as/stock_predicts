# Stock Project

A Django-based web application for managing and predicting company stock prices.

## Features

- Add and view monthly stock prices.
- Predict future stock prices using historical data.
- User-friendly interface with Bootstrap styling.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or later
- MySQL (for database)

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/stock_project.git
    cd stock_project
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    - Create a MySQL database:
        ```sql
        CREATE DATABASE stock_database;
        ```
    - Create a `.env` file in the project root and add the following configurations:
        ```ini
        DEBUG=True
        SECRET_KEY=your-secret-key
        DB_ENGINE=django.db.backends.mysql
        DB_NAME=stock_database
        DB_USER=root
        DB_PASSWORD=your-password
        DB_HOST=localhost
        DB_PORT=3306
        ```

5. Run migrations to set up the database schema:
    ```bash
    python manage.py migrate
    ```

6. Collect static files:
    ```bash
    python manage.py collectstatic
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

8. Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Add Monthly Stock Prices**: Navigate to `/add_monthly_stock_price` and fill out the form.
- **Predict Stock Prices**: Navigate to `/predict/<company_id>/<days_ahead>` to view future stock price predictions.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Your other dependencies and acknowledgements]


