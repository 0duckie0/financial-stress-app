import os
from flask import Flask, request, render_template

app = Flask(__name__)

def calculate_stress(monthly_income, monthly_expenses, total_emi, current_savings):

    if monthly_income == 0:
        return 100

    emi_ratio = total_emi / monthly_income
    expense_ratio = monthly_expenses / monthly_income

    if monthly_expenses == 0:
        savings_ratio = 1
    else:
        savings_ratio = current_savings / monthly_expenses

    stress_score = (
        (emi_ratio * 40) +
        (expense_ratio * 30) +
        ((1 - savings_ratio) * 30)
    )

    stress_score = max(0, min(100, stress_score))

    return round(stress_score, 2)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():

    monthly_income = float(request.form['income'])
    monthly_expenses = float(request.form['expenses'])
    total_emi = float(request.form['emi'])
    current_savings = float(request.form['savings'])

    stress_score = calculate_stress(
        monthly_income,
        monthly_expenses,
        total_emi,
        current_savings
    )

    if stress_score <= 40:
        risk_level = "Low Risk"
    elif stress_score <= 70:
        risk_level = "Moderate Risk"
    else:
        risk_level = "High Risk"

    return render_template(
        'index.html',
        score=stress_score,
        risk=risk_level
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
