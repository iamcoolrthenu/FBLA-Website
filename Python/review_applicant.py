import os
import pathlib
import textwrap
import textract
import google.generativeai as genai
from dotenv import load_dotenv
import emailserver as emailserver

# Load environment variables from .env file
load_dotenv()

# Extract text from the resume
text = textract.process("TolibSanni-Resume-03-25-24.docx")

# Configure Google Generative AI with API key from .env file
GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

# Generate email content
prompt = textwrap.dedent(f"""
Write me an email about whether or not the applicant should be accepted. Do not write the subject. The position is a software engineer.: {text}
""")
response = model.generate_content(prompt)

# Send email
emailserver.application_received()
emailserver.send_email(
    subject='Application Status',
    body=response.text,
    receiver_email='***REMOVED***'
)
