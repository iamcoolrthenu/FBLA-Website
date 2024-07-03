from flask import Flask
import pathlib
import textwrap
import textract
import emailserver
import google.generativeai as genai

import config

app = Flask(__name__)

# Configure Google Generative AI with API key from config
GOOGLE_API_KEY = config.gemini_key
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

@app.route('/api', methods=['GET'])
def email_applicant():
    # Extract the text from the applicant's resume
    text = textract.process(emailserver.application['resume'])

    # Generate email content using the generative model
    prompt = textwrap.dedent(f"""
    Write me an email about whether or not the applicant should be accepted. Do not write the subject. The position is a software engineer.: {text}
    """)
    response = model.generate_content(prompt)

    # Send the generated email to the applicant
    emailserver.application_received()
    emailserver.send_email(
        subject='Application Status',
        body=response.text,
        receiver_email=emailserver.application["email"]
    )
    
    return "Email sent successfully", 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
