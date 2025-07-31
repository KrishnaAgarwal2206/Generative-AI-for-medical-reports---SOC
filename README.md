# Generative-AI-for-medical-reports---SOC 
Mid term report --> https://docs.google.com/document/d/181u7m950cRvn9-HlWzXJSy5wNLKjxsxtpkJaBHJAUSM/edit?usp=sharing


This project is a generative AI chatbot for creating structured medical reports based on user symptoms and context from medical PDFs.

## Features

- Chatbot interface for entering symptoms
- Generates structured medical reports
- Uses Gemini and Pinecone for retrieval-augmented generation
- Loads and indexes medical PDFs from the `Data/` folder

## Setup Instructions

### 1. Clone the repository

```sh
git clone <repo-url>
cd Generative-AI-for-medical-reports---SOC
```

### 2. Install dependencies

It is recommended to use a virtual environment.

```sh
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3. Set API Keys

Create a `.env` file in the project root with your API keys:

```
PINECONE_API_KEY = "<your-pinecone-api-key>"
GEMINI_API_KEY = "<your-gemini-api-key>"
```


### 4. Build the Pinecone Index

Run the following script to load, chunk, embed, and index the documents:

```sh
python save_index.py
```

### 5. Start the Web Application

```sh
python app.py
```

The chatbot will be available at [http://localhost:8080](http://localhost:8080).

## Usage

- Open the web interface.
- Enter your symptoms in the chat.
- The bot will generate a structured medical report based on the indexed documents.

## Project Structure

- `app.py` — Flask web app and chatbot logic
- `save_index.py` — Loads PDFs, creates embeddings, and builds Pinecone index
- `src/helper.py` — Data loading and embedding helpers
- `src/prompt.py` — System prompt for the chatbot
- `templates/chat.html` — Chatbot UI
- `static/style.css` — UI styling
- `Data/` — Place your medical PDFs here

## Notes

- Ensure your API keys have sufficient quota and access.

