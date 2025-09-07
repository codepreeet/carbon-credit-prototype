from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    co2 = credits = prediction = None
    if request.method == 'POST':
        kwh = float(request.form['kwh'])
        co2 = kwh * 0.82  # grid emission factor kg CO2/kWh
        credits = co2 / 1000  # 1 credit per tonne CO2
        prediction = kwh  # placeholder prediction
    return render_template('index.html', co2=co2, credits=credits, prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
