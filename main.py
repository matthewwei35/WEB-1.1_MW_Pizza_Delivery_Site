# Import the flask library for usage
from flask import Flask, request, render_template
import json

# Create an instance of the flask server
# as the root directory within 'main.py'
app = Flask(__name__)

# Create some routes
@app.route('/')
def display_home_page():
  return render_template('index.html') 

@app.route('/form-example')
def first_form():
  return render_template('form.html')

@app.route('/results', methods=['GET'])
def simple_pizza_results():
  
  # A context object contains all of the needed form data for the template
  context = {
    'pizza_flavor' : request.args.get("pizza_flavor"),
    'crust' : request.args.get("crust"),
    'individual_toppings' : ['mushrooms', 'olives', 'garlic']
  }

  return render_template('confirmation_page.html', **context)

with open('example_obj.json') as example_obj_file:
  print("raw file printed = ", example_obj_file)
  json_data = json.load(example_obj_file)
  print("just the JSON data printed = ", json_data)

@app.route('/json-example', methods=['GET'])
def json_route():
  return json_data

# Turn the server on for serving
if __name__ == "__main__":
  app.run(debug=True, port=3000)
