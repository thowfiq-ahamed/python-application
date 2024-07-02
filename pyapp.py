from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = calculate_bmi(weight, height)
        return render_template('index.html', bmi=bmi)
    return render_template('index.html')

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

if __name__ == '__main__':
    app.run(debug=True)