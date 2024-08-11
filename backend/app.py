# app.py

from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
import secrets


app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'  
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'mkico2010@yahoo.in'
app.config['MAIL_PASSWORD'] = 'qwfztyxlwjnfohym'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/send-otp', methods=['POST'])
def send_otp():
    data = request.json
    email = data.get('email')
    genkey = secrets.token_hex(8)
    api_key = "rugveddevapi@" + genkey

    msg = Message('Your OTP Code', sender='mkico2010@yahoo.in', recipients=[email])
    msg.body = f"""
    Dear User,

    Your API Key for verification is: 

    **{api_key}**

    Please use this API Key to complete your verification process. This code will expire in 10 minutes.

    If you did not request this code, please ignore this email or contact support if you have any concerns.

    Best regards,
    Rugveddev
    """
    mail.send(msg)
    
    return jsonify({'message': 'API Key sent', 'otp': api_key}), 200

if __name__ == '__main__':
    app.run(debug=True)
