import pathlib
import textwrap
import textract
import emailserver
import google.generativeai as genai

import config
text = textract.process("TolibSanni-Resume-03-25-24.docx")

GOOGLE_API_KEY = config.gemini_key

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')


response = model.generate_content(f'Write me an email about where or not the applicant should be accepted. Do not write the subject. The position is a software engineer.: {text}')
emailserver.application_received()
emailserver.send_email(subject='Application Status', body=response.text, receiver_email='***REMOVED***')
