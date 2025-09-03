#  Account Management Web App

A simple **Python + Flask web application** for managing bank accounts.  
You can **select users, view balance, deposit, and withdraw money** using a browser interface.

---

## 📂 Project Structure
```
acc-mgmt-live/
│── account_mgmt.py      # Flask backend with Account class
│── f-end/
│    └── index.html      # Frontend template (HTML + CSS)
│── README.md            # Documentation
```

---

## ⚙️ Requirements

Make sure you have the following installed:

- **Python 3.8+**
- **pip (Python package manager)**
- **Flask** web framework

---

## 📥 Installation Steps

### 1️⃣ Clone the Project
```bash
git clone <your-repo-url>
cd acc-mgmt-live
```

### 2️⃣ Create Virtual Environment (When using WSL)
```bash
python -m venv venv
```
Activate it:
- On Linux/Mac:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  venv\Scripts\activate
  ```

### 3️⃣ Install Dependencies
```bash
pip install flask
```

---

## 🚀 Run the Application

Start the Flask server:
```bash
python account_mgmt.py
```

By default, it runs on **http://0.0.0.0:5000** (or **http://localhost:5000**).

---

## 🖥️ Usage

1. Open your browser → go to: [http://localhost:5000](http://localhost:5000)  
2. Select an account from the dropdown.  
3. View account details:
   - **Account Number**
   - **Holder Name**
   - **Current Balance**
4. Perform actions:
   - **Deposit money**
   - **Withdraw money**
5. Messages will show success/failure (e.g., "✅ Deposited" or "❌ Insufficient balance").

---

##  Features
- Multiple accounts stored in backend (Python dictionary).
- Easy account selection via dropdown.
- Deposit and withdraw operations update balance dynamically.
- Clean HTML interface with basic styling.

---

##  Example Accounts (Preloaded)
- **19104910 – Krishna – ₹230,025**
- **19104915 – Jatin – ₹1,500,000**
- **19104920 – Aditi – ₹50,000**

---

##  Future Improvements
- Load accounts from **JSON or database** instead of hardcoding.
- Add **login/authentication** for users.
- Show **transaction history**.
- REST API endpoints for mobile apps.

---

That’s it! You now have a **working Python + Flask bank account management web app**.
