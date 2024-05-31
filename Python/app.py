from flask import Flask
import pathlib
import textwrap
import textract
import Python.emailserver as emailserver
import google.generativeai as genai

import Python.config as config

app = Flask(__name__)
text = textract.process(emailserver.application['resume'])
GOOGLE_API_KEY = config.gemini_key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
@app.route('/api')
def email_applicant():
    response = model.generate_content(f'Write me an email about where or not the applicant should be accepted. Do not write the subject. The position is a software engineer.: {text}')
    emailserver.application_received()
    emailserver.send_email(subject='Application Status', body=response.text, receiver_email=f'emailserver.application["email"]')



if __name__ == '__main__':
    exec(open("build_databases.py").read())
    app.run(host='localhost', port=5000)