from app import create_app

# Create an instance of the Flask application
app = create_app()

if __name__ == "__main__":
    # Run the application on localhost and allow access from any IP address
    app.run(host='0.0.0.0', port=5000, debug=True)

