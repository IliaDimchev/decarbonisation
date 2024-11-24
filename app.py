from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_emissions():
    # Emission factors for different regions
    regional_factors = {
        'ivory_coast': {'diesel': 2.68, 'electricity': 0.5},
        'ghana': {'diesel': 2.7, 'electricity': 0.55},
        'mali': {'diesel': 2.6, 'electricity': 0.52},
        'burkina_faso': {'diesel': 2.65, 'electricity': 0.54},
        'liberia': {'diesel': 2.75, 'electricity': 0.53},
        'guinea': {'diesel': 2.64, 'electricity': 0.51}
    }

    if request.method == 'POST':
        try:
            # Get the selected region from the form
            region = request.form.get('region', 'ivory_coast')
            factors = regional_factors.get(region, regional_factors['ivory_coast'])
            
            # Get fuel and electricity quantities from user input
            quantities = {
                'diesel': float(request.form.get('fuel_quantity', 0)),
                'electricity': float(request.form.get('electricity_quantity', 0))
            }

            # Calculate emissions for each source
            emissions = {key: quantities[key] * factors[key] for key in quantities}
            # Sum the total emissions
            total_emissions = sum(emissions.values())

            # Round the emissions to two decimal places
            emissions = {key: round(value, 2) for key, value in emissions.items()}
            total_emissions = round(total_emissions, 2)

            # Render the result template with calculated emissions
            return render_template('result.html', scope1=emissions['diesel'], scope2=emissions['electricity'], total=total_emissions)

        except ValueError:
            # Handle invalid input by rendering the input form with an error message
            return render_template('index.html', error="Invalid input. Please enter valid numbers.", regional_factors=regional_factors['ivory_coast'])

    # Render the input form with default regional factors for GET requests
    return render_template('index.html', regional_factors=regional_factors['ivory_coast'])

if __name__ == '__main__':
    app.run(debug=True)
