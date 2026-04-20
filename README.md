🚀 Financial Stress Analyzer (AI-Based)
📌 Overview

The Financial Stress Analyzer is a web-based application that evaluates an individual's financial condition and predicts their financial stress level using both rule-based logic and machine learning.

The system takes basic financial inputs and generates a Stress Score (0–100) along with a risk classification to help users understand their financial stability.

🎯 Features
📊 Financial Stress Score (0–100)
⚠️ Risk Classification (Low / Moderate / High)
🤖 Machine Learning Prediction (Phase 2)
🔁 Rule-Based Fallback System
🎨 Modern UI with progress bar and visual indicators
🔒 No data storage (privacy-friendly)
🧠 How It Works
🔹 Input Parameters
Monthly Income
Monthly Expenses
EMI (Equated Monthly Installment)
Current Savings
🔹 Output
Stress Score (0–100)
Risk Level
Model Used (ML Model / Rule-Based)
🧱 Project Architecture
User Input (Frontend)
        ↓
Flask Backend (API)
        ↓
ML Model / Rule-Based Logic
        ↓
Stress Score Calculation
        ↓
Risk Classification
        ↓
Frontend Display
⚙️ Tech Stack
💻 Frontend
HTML
CSS
JavaScript
🧠 Backend
Python (Flask)
🤖 Machine Learning
Scikit-learn
Random Forest Regressor
NumPy
Pandas
Joblib
🔄 Project Phases
🟢 Phase 1 — Rule-Based System
Used financial ratios:
Expense-to-Income ratio
EMI-to-Income ratio
Savings factor
Applied weighted formula to calculate stress score
Fast and simple but not adaptive
🔵 Phase 2 — Machine Learning Integration
Generated synthetic dataset (~3000 entries)
Trained model using Random Forest Regressor
Learned complex financial patterns
Replaced fixed formula with predictive model
Added fallback mechanism for reliability
📊 Machine Learning Details
Model: Random Forest Regressor
Input Features:
Income
Expenses
EMI
Savings
Output:
Predicted Stress Score

👉 The model captures non-linear relationships between financial variables.

📁 Project Structure
financial-stress-app/
│
├── app.py                # Flask backend
├── model.pkl             # Trained ML model
├── dataset.csv           # Generated dataset
├── generate_dataset.py   # Dataset generation script
├── train_model.py        # Model training script
├── requirements.txt      # Dependencies
│
├── templates/
│   └── index.html        # Frontend UI
│
└── static/               # (optional CSS/JS)
🚀 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/financial-stress-app.git
cd financial-stress-app
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the application
python app.py
4️⃣ Open in browser
http://127.0.0.1:5000
🧪 Model Training (Optional)
Generate dataset
python generate_dataset.py
Train model
python train_model.py
🔒 Privacy Note
No user data is stored
No database integration
All processing happens in real-time
⚠️ Limitations
Uses synthetic dataset (not real-world data)
Predictions depend on generated patterns
No personalized financial advice yet
🚀 Future Scope
📊 Real-world financial dataset integration
📈 Personalized financial recommendations
☁️ Cloud deployment with APIs
🔐 User authentication system
📱 Mobile app version
🎓 Academic Value

This project demonstrates:

Feature engineering using financial indicators
Transition from rule-based to ML-based system
Supervised learning implementation
Full-stack development (Frontend + Backend + ML)
👨‍💻 Author
Developed as part of academic project
Focus: Machine Learning + Web Integration
⭐ Final Note

This project showcases how financial data can be transformed into meaningful insights using machine learning, helping users better understand and manage their financial stress.


Make it portfolio-ready
Write LinkedIn post for this project
Convert into research paper

Just tell me 🚀
