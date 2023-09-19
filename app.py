# Define your function
def my_function():
    # Your function logic here
    return "Hello, World!"

# Expose the function as a REST API endpoint
from flask import Flask
app = Flask(__name__)

@app.route('/get_output', methods=['GET'])
def get_output():
    result = my_function()
    return result

if __name__ == '__main__':
    app.run()