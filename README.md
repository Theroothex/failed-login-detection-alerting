# 🔐 Failed Login Detection \& Alerting (SOC Project)



A Security Operations Center (SOC) style project that detects \*\*failed login attempts\*\* from \*\*Windows Security Event Logs (Event ID 4625)\*\* and raises \*\*brute-force alerts\*\* using a Django-based dashboard.



---



# 📌 Project Overview



This project monitors Windows failed login events, stores them in a database, and detects potential brute-force attacks based on configurable thresholds.



It simulates how a \*\*SOC Level 1 analyst\*\* monitors authentication failures and escalates suspicious activity.



---



# 🚀 Features



\- 📄 Reads Windows Security Logs (Event ID 4625)

\- ❌ Detects failed login attempts

\- 📊 Dashboard with summary statistics

\- 🚨 Brute-force detection based on IP attempts

\- ⚠️ Severity classification (Low / High)

\- 🗂️ Stores events \& alerts in database

\- 🖥️ Django Admin panel for monitoring

\- 📸 Visual evidence via screenshots



---



# 🧠 Brute Force Detection Logic



```text

Attempts ≤ 2  → Low severity  

Attempts ≥ 3  → High severity (Brute Force)





## 🏗️ Project Architecture

Failed Login Detection \& Alerting

├── detector/               # Core SOC logic

│   ├── log\_reader.py       # Reads Event ID 4625 logs

│   ├── brute\_detector.py  # IP-based brute force detection

│   ├── user\_brute\_detector.py

│   ├── models.py          # Django models

│   ├── views.py           # Dashboard, events, alerts

│   └── urls.py

├── templates/              # HTML UI pages

│   ├── dashboard.html

│   ├── events.html

│   └── alerts.html

├── static/                 # CSS styling

├── screenshots/            # Project screenshots

├── db.sqlite3              # Database

├── manage.py

└── README.md


## 📸 Screenshots

1️⃣ Windows Event Viewer (Event ID 4625)

2️⃣ Dashboard Summary

3️⃣ Failed Login Events Page

4️⃣ Brute Force Alert Detection

5️⃣ Django Admin – SOC Monitoring

6️⃣ Project Structure


## ⚙️ Tech Stack

Python 3

Django

Windows Event Logs

SQLite

HTML / CSS

Git \& GitHub


## ▶️ How to Run the Project

\# Activate virtual environment

venv\\Scripts\\activate

\# Run Django server

python manage.py runserver

Access:

Dashboard → http://127.0.0.1:8000/

Events → /events/

Alerts → /alerts/

Admin → /admin/


# 🎯 SOC Use Case (Real-Life Example)

If an attacker tries multiple passwords for the same system or IP, this tool detects repeated failures and flags it as a brute-force attempt, just like a real SOC environment.


# 👨‍💻 Author

Sandeep Mandal

SOC / Cybersecurity Project

GitHub: https://github.com/Theroothex

