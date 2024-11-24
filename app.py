from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_emissions():
    default_factors = {
        'diesel': 2.68,
        'electricity': 0.5
    }

    if request.method == 'POST':
        try:
            factors = {
                'diesel': float(request.form.get('diesel_emission_factor', default_factors['diesel'])),
                'electricity': float(request.form.get('electricity_emission_factor', default_factors['electricity']))
            }
            
            quantities = {
                'diesel': float(request.form.get('fuel_quantity', 0)),
                'electricity': float(request.form.get('electricity_quantity', 0))
            }

            emissions = {key: quantities[key] * factors[key] for key in quantities}
            total_emissions = sum(emissions.values())

            emissions = {key: round(value, 2) for key, value in emissions.items()}
            total_emissions = round(total_emissions, 2)

            return render_template('result.html', scope1=emissions['diesel'], scope2=emissions['electricity'], total=total_emissions)

        except ValueError:
            return render_template('index.html', error="Invalid input. Please enter valid numbers.", **default_factors)

    return render_template('index.html', **default_factors)

if __name__ == '__main__':
    app.run(debug=True)
