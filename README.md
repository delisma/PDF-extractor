# Project Title

## Description
This project is designed to extract structured information from PDF documents and send the data to a specified webhook. It uses several libraries including pytesseract for OCR, pypdfium2 for PDF to image conversion, and OpenAI's GPT-3 model for structured data extraction.

## Setup
1. Clone the repository.
2. Install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```
3. Set up the environment variables in the `.env` file. You will need to provide your OpenAI API key.

## Usage
Run the `app.py` script to start the application:
```
python app.py
```
The application is a Streamlit app, so it will open in your default web browser. You can upload PDF files and specify the data points you want to extract. The extracted data will be displayed in the app, and you can choose to send it to the webhook.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
