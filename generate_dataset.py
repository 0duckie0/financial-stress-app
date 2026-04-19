import random
import pandas as pd

data = []

for _ in range(3000):

    income = random.randint(15000, 150000)
    expenses = random.randint(5000, income)
    emi = random.randint(0, int(income * 0.6))
    savings = random.randint(0, income * 6)

    # same logic as phase 1 (label generation)
    if income == 0:
        stress = 100
    else:
        er = expenses / income
        ebr = emi / income
        ssr = min(savings / income, 5)

        stress = (er * 50) + (ebr * 40) - (ssr * 5)
        stress = max(0, min(100, stress))

    data.append([income, expenses, emi, savings, stress])

df = pd.DataFrame(data, columns=[
    "income", "expenses", "emi", "savings", "stress_score"
])

df.to_csv("dataset.csv", index=False)

print("Dataset created!")