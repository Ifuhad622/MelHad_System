# wsgi.py

from myapp import create_app  # Replace 'myapp' with your actual Flask application package

app = create_app()

if __name__ == "__main__":
    app.run()
