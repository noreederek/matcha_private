from mailin import Mailin
from flask import request

import config

m = Mailin("https://api.sendinblue.com/v2.0", config.send_in_blue)

def send_mail(name, email, subject, body):
    data = {
      "to" : {email : name},
      "from" : ["no-reply@matchame.co.za", "🔥 Matcha 🔥"],
      "subject" : subject,
      "html" : body}

    return m.send_email(data)

def send_validation_email(user, code):

    base = config.frontend_uri
    name = "{0} {1}".format(user.fname, user.lname)
    print("http://localhost:8080/validate?code=" + code)

    html = """
    <div>
      <h3>Hello {name}, welcome to Matcha</h3>
      <p>Please validate your email by clicking the link below</p>
      <a href="{base}/validate?code={code}">Verify Email</a>
    </div>
    """.format(name=name, base=base, code=code)

    result = send_mail(name, user.email, "Email Verification", html)

    return result["code"]

def send_password_reset_email(user, code):
    base = config.frontend_uri
    name = "{0} {1}".format(user.fname, user.lname)

    html = """
    <div>
      <h3>Hello {name}</h3>
      <p>To reset your password please use the following wink</p>
      <a href="{base}/reset-password?code={code}">Reset Password</a>
    </div>
    """.format(name=name, base=base, code=code)

    result = send_mail(name, user.email, "Password Reset", html)

    return result["code"]
