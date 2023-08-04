from langchain.chat_models import ChatOpenAi
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from pytesseract import image_to_string
from PIL import Image
from io import BytesIO
import pypdfium2 as pdfium
import streamlit import st
import multiprocessing
from tempfile import NamedTemporaryFile
import pandas as pd
import json
import requests

# Load environment variables from .env file
load_dotenv()

import pypdfium2 as pdfium
from io import BytesIO

# 1 Convert a PDF file into images using PyPDFium2.
def convert_pdf_to_images(pdf_path, scale=300/72):
    # Load the PDF
    pdf = pdfium.PdfDocument(pdf_path)
    
    # Convert each page to an image
    images = []
    for page in range(pdf.page_count):
        bitmap = pdf.render_page(page, scale=scale)
        image = Image.frombuffer('RGBA', (bitmap.width, bitmap.height), bitmap.buffer, 'raw', 'RGBA', 0, 1)
        
        # Save the image to a BytesIO object
        image_data = BytesIO()
        image.save(image_data, format='PNG')
        image_data.seek(0)
        
        images.append(image_data)
    
from pytesseract import image_to_string

# 2 Extract text from the images using PyTesseract.
def extract_text_from_image(images):
    # Initialize an empty list to store the text from each image
    texts = []
    
    # Iterate over the list of images
    for image in images:
        # Convert the image to text and append it to the list
        texts.append(pytesseract.image_to_string(image))
    
    # Join the list of texts into a single string and return it
    return ' '.join(texts)

# 3 Extract structured information from the text using the Langchain library to access the OpenAI API.
def extract_info_from_text(text):
    # TODO: Extract structured information from the text


# 4 Send the extracted data to make.com via a webhook.
def send_data_to_webhook(data):
    # TODO: Send the data to make.com via a webhook
from requests import get

from urllib.parse import urlparse

def extract_content_from_url(url_or_path):
    # Check if the input is a URL or a local file path
    parsed = urlparse(url_or_path)
    if parsed.scheme in ('http', 'https'):
        # It's a URL, download the file
        response = get(url_or_path)
        with NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
            temp_pdf.write(response.content)
        file_path = temp_pdf.name
    else:
        # It's a local file path, no need to download
        file_path = url_or_path

    # Convert the PDF into images
    images = convert_pdf_to_images(file_path)
    
    # Extract the text from the images
    text = extract_text_from_image(images)
    
    # Return the extracted text
    return text

def main():
    # TODO: Main function to tie all the steps together

if __name__ == "__main__":
    main()
