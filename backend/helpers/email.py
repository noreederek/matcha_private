from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import request
import config

mailAPIkey = config.sendgrid
sg = SendGridAPIClient(mailAPIkey)

def send_mail(email, subject, body):
    message = Mail(from_email='mayorovyuri7@gmail.com',\
      to_emails=email,\
      subject=subject,\
      html_content=body)
    try:
      response = sg.send(message)
      return response.status_code
    except Exception as e:
      return "Error on mailing service"

def send_validation_email(user, code):

    base = config.frontend_uri
    name = "{0} {1}".format(user.fname, user.lname)
    print("http://localhost:8080/validate?code=" + code)

    html = """
    <div>
      <h3>{name} - Registration</h3>
      <p>Click on the link below: </p>
      <a href="{base}/validate?code={code}">Verify Email</a>
    </div>
    """.format(name=name, base=base, code=code)

    result = send_mail(user.email, "Email Verification", html)
    return result

def send_password_reset_email(user, code):
    base = config.frontend_uri
    name = "{0} {1}".format(user.fname, user.lname)

    html = """
    <div>
      <h3>Reset password - {name}</h3>
      <p>To reset your password click on link</p>
      <a href="{base}/reset-password?code={code}">Reset Password</a>
    </div>
    """.format(name=name, base=base, code=code)

    result = send_mail(user.email, "Password Reset", html)
    return result
