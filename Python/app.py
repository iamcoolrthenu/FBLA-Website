from flask import Flask
import pathlib
import textwrap
import textract
import emailserver
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure Google Generative AI with API key from environment variables
GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

@app.route('/api', methods=['GET'])
def email_applicant():
    try:
        # Extract the text from the applicant's resume
        resume_path = emailserver.application['resume']
        text = textract.process(resume_path).decode('utf-8')

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
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Use 0.0.0.0 to be accessible externally
