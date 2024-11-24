Flask Emissions Calculator Documentation
Overview
This is a simple Flask-based web application that calculates carbon dioxide (CO₂) emissions from diesel fuel and electricity usage. Users can input emission factors and quantities, and the app calculates Scope 1 (direct emissions from fuel) and Scope 2 (indirect emissions from electricity) emissions based on the Greenhouse Gas (GHG) Protocol.
________________________________________
Prerequisites
Before you begin, ensure you have the following installed on your system:
•	Python 3.x
•	Flask library
________________________________________
Installation
1.	Clone the Repository:
git clone <repository_url>
cd <project_directory>
2.	Create a Virtual Environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3.	Install Required Packages:
pip install Flask
________________________________________
Project Structure
project_directory/
│
├── app.py              # Main Flask application
├── templates/
│   ├── index.html      # Main input form template
│   └── result.html     # Results display template
└── static/             # (Optional) For CSS, JS, or image files
________________________________________
Code Explanation
app.py (Main Application File)
1. Import Required Modules:
from flask import Flask, render_template, request
•	Flask: The micro web framework for Python.
•	render_template: Renders HTML templates.
•	request: Accesses form data sent by the user.
2. Initialize the Flask Application:
app = Flask(__name__)
•	Creates an instance of the Flask class.
3. Define the Route and View Function:
@app.route('/', methods=['GET', 'POST'])
def calculate_emissions():
•	Route: Handles both GET and POST requests for the root URL ('/').
•	View Function: calculate_emissions() manages input data, calculations, and template rendering.
4. Default Emission Factors:
default_factors = {
    'diesel': 2.68,         # Default emission factor for diesel (kg CO₂ per liter)
    'electricity': 0.5      # Default emission factor for electricity (kg CO₂ per kWh)
}
5. Handle POST Requests (Form Submission):
if request.method == 'POST':
    try:
        # Retrieve emission factors from the form or use defaults
        factors = {
            'diesel': float(request.form.get('diesel_emission_factor', default_factors['diesel'])),
            'electricity': float(request.form.get('electricity_emission_factor', default_factors['electricity']))
        }
        
        # Retrieve quantities from the form
        quantities = {
            'diesel': float(request.form.get('fuel_quantity', 0)),
            'electricity': float(request.form.get('electricity_quantity', 0))
        }
        
        # Calculate emissions for each scope
        emissions = {key: quantities[key] * factors[key] for key in quantities}
        total_emissions = sum(emissions.values())
        
        # Round results to 2 decimal places
        emissions = {key: round(value, 2) for key, value in emissions.items()}
        total_emissions = round(total_emissions, 2)
        
        # Render result template with calculated values
        return render_template('result.html', scope1=emissions['diesel'], scope2=emissions['electricity'], total=total_emissions)
    
    except ValueError:
        # Handle invalid input and return an error message
        return render_template('index.html', error="Invalid input. Please enter valid numbers.", **default_factors)
6. Handle GET Requests (Initial Page Load):
return render_template('index.html', **default_factors)
•	Displays the form with default emission factors.
7. Run the Application:
if __name__ == '__main__':
    app.run(debug=True)
•	Starts the Flask development server with debug mode enabled.
________________________________________
index.html (Input Form Template)
•	Provides a user-friendly form to enter emission factors and quantities.
Key Features:
•	Input fields for diesel and electricity emission factors.
•	Fields to enter fuel and electricity quantities.
•	Displays errors if invalid data is submitted.-
<form method="POST" action="/">
    <!-- Emission factor inputs -->
    <label>Diesel Emission Factor (kg CO₂/liter):</label>
    <input type="number" step="0.01" name="diesel_emission_factor" value="{{ diesel_emission_factor }}">

    <label>Electricity Emission Factor (kg CO₂/kWh):</label>
    <input type="number" step="0.01" name="electricity_emission_factor" value="{{ electricity_emission_factor }}">

    <!-- Quantity inputs -->
    <label>Fuel Quantity (liters):</label>
    <input type="number" step="0.01" name="fuel_quantity" value="0">

    <label>Electricity Quantity (kWh):</label>
    <input type="number" step="0.01" name="electricity_quantity" value="0">

    <!-- Submit button -->
    <button type="submit">Calculate</button>
</form>
________________________________________
result.html (Result Display Template)
•	Displays calculated emissions for Scope 1 (fuel) and Scope 2 (electricity), along with the total CO₂ emissions.
Example Calculation Display:
<p>Fuel Quantity: {{ scope1 | round(2) }} kg CO₂</p>
<p>Electricity Quantity: {{ scope2 | round(2) }} kg CO₂</p>
<p>Total CO₂ Emissions: {{ total | round(2) }} kg CO₂</p>
<a href="/">Go Back</a>
________________________________________
Running the Application
1.	Open a terminal and navigate to the project directory.
2.	Activate your virtual environment (if used).
3.	Start the Flask application:
4.	Open your web browser and go to http://127.0.0.1:5000.
________________________________________
Conclusion
This documentation provides a comprehensive guide to understanding, installing, and running the Flask-based emissions calculator. The code is modular, clean, and follows best practices for error handling and template rendering.

