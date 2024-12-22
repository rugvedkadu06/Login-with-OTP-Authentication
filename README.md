# Login with OTP Authentication Project Documentation


## Introduction

This project demonstrates a **Login with OTP Authentication** system. It allows users to log in using a one-time password (OTP) sent to their registered email. The project uses **ReactJS** for the frontend, **Flask** as the backend, and an **Excel sheet** as the database for simplicity and testing.

---

## Features

- **OTP Generation and Validation**: Generate OTPs and validate them for login.  
- **Email-based Authentication**: Send OTPs to the user's email for secure access.  
- **Frontend-Backend Communication**: Ensure smooth interaction between React and Flask.  
- **Excel Database**: Use an Excel file to store user data for testing purposes.

---

## Technologies Used

1. **Frontend**: ReactJS (JavaScript, JSX)  
2. **Backend**: Flask (Python)  
3. **Database**: Excel file using the `openpyxl` library in Python  
4. **Email Service**: SMTP (e.g., Gmail, Elastic Email, or Mailgun)  

---

## System Architecture

### Components:
1. **Frontend**:
   - Login Form: Accepts user email.  
   - OTP Verification: Field to input and verify OTP.  

2. **Backend**:
   - Flask API for handling user requests, OTP generation, and validation.  
   - Integration with the email service to send OTPs.

3. **Database**:
   - Excel file for storing user emails, OTPs, and other metadata.  

---

## Setup and Installation

### Prerequisites:
- Node.js and npm/yarn (for React)
- Python 3.x
- Flask and necessary Python packages
- Excel file setup for database

###Setup and Installation
**Prerequisites:**
1. Node.js and npm/yarn (for React)
2. Python 3.x
3. Flask and necessary Python packages
4. Excel file setup for database
**Installation Steps:**
**1. Clone the Repository**:
```
git clone https://github.com/rugvedkadu06/Login-with-OTP-Authentication.git
cd Login-with-OTP-Authentication
```
**2. Frontend Setup:**

Navigate to the frontend folder:
```
cd frontend
```
Install dependencies:
```
npm install
```
Start the React development server:
```
npm start
```
**3. Backend Setup:**
Navigate to the backend folder:
```
cd backend
```
Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```
Install dependencies:
```
pip install -r requirements.txt
```
Start the Flask server:
```
flask run
```
**4. Database Setup:**

Create an Excel file (e.g., users.xlsx) with a sheet containing user details:
| Email | OTP | IsVerified |
| :---         |     :---:      |          ---: |
