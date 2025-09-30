# Flask Products Site

This project is a simple Flask web application that displays a list of products. Each product has a title, price, description, and an image. The application is structured to allow easy expansion and modification.

## Project Structure

```
flask-products-site
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── templates
│   │   ├── index.html
│   │   └── product.html
│   └── static
│       ├── css
│       │   └── styles.css
│       └── images
├── data
│   └── products.json
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-products-site
   ```

2. **Install dependencies:**
   You can install the required Python packages using pip. It is recommended to use a virtual environment.
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the application:**
   You can run the Flask application locally by executing:
   ```
   flask run
   ```

4. **Using Docker:**
   To build and run the application using Docker, use the following commands:
   ```
   docker-compose up --build
   ```

## Usage

- Navigate to `http://localhost:5000` in your web browser to view the application.
- The main page displays a list of products, and clicking on a product will take you to its detail page.

## License

This project is licensed under the MIT License.