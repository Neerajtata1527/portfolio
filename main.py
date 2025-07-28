from flask import Flask, request, redirect, render_template, flash
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Needed for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    # Your Gmail credentials (use environment variables in production)
    sender_email = "neerajtata1527@gmail.com"
    app_password = "pith lvmg egvk ekmx"
    receiver_email = "neerajtata1527@gmail.com"  # Where you want to receive contact messages

    # Form data from user
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Compose email content
    msg_body = f"""
    You have a new message from your portfolio contact form:

    Name: {name}
    Email: {email}

    Message:
    {message}
    """

    msg = MIMEText(msg_body)
    msg['Subject'] = f"New Contact Form Message from {name}"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
        flash("Message sent successfully!", "success")
    except Exception as e:
        flash(f"Failed to send email: {e}", "danger")

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
