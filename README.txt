# ReviseME - LLM Based Revision Tool

## Project Overview
ReviseME is an interactive web application designed to scrape and summarize content from PDFs, web URLs, and YouTube videos. The application leverages the power of Large Language Models (LLMs) and vector databases to provide accurate and relevant summaries based on user queries. The app is built using Streamlit for the web interface, ChromaDB for vector database management, and the Gemini API for text embedding and summarization.

## Features
- **PDF Scraping**: Upload a PDF file to extract and save its content.
- **URL Scraping**: Input a web URL to extract and save its content.
- **YouTube Video Scraping**: Input a YouTube video URL to extract and save its content.
- **Query-Based Summarization**: Input a query to get a summarized response from the scraped content.
- **Session Management**: Each session starts with a fresh database to ensure no data carry-over.

## Getting Started

### Prerequisites
- Python 3.8 or later
- Virtual environment management tool (e.g., `venv` or `virtualenv`)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/reviseme.git
    cd reviseme
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment**:
    - **Windows**:
      ```bash
      .\env\Scripts\activate
      ```
    - **macOS/Linux**:
      ```bash
      source env/bin/activate
      ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up environment variables**:
    - Create a `.env` file in the root directory of the project.
    - Add your Gemini API key to the `.env` file:
      ```
      GEMINI_API_KEY=your_gemini_api_key
      ```

### Running the Application

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Interacting with the App**:
    - Upload a PDF file or input a URL/YouTube video link.
    - Enter a query to get summarized content based on the scraped data.

## Project Structure

- **app.py**: Main application script for the Streamlit interface.
- **pdf_scraper.py**: Contains functions to scrape content from PDF files.
- **url_scraper.py**: Contains functions to scrape content from web URLs.
- **yt_scraper.py**: Contains functions to scrape content from YouTube videos.
- **summarizer.py**: Contains functions to generate summaries based on user queries.
- **vector_db.py**: Manages the vector database using ChromaDB.
- **requirements.txt**: Lists all the dependencies required for the project.

## Detailed Process

1. **Upload/Enter Content**: Users can upload a PDF, input a web URL, or a YouTube video URL.
2. **Scraping**: The appropriate scraper extracts the content and saves it in a list of documents.
3. **Vector Database Creation**: The extracted content is converted to embeddings using the Gemini API and stored in a ChromaDB collection.
4. **Query Input**: Users input a query, which the app uses to search the vector database.
5. **Summarization**: The relevant passage is extracted, and the Gemini API generates a summary based on the query.
6. **Display Result**: The summary is displayed to the user.
7. **Session Management**: At the end of each session, the vector database is cleared to start fresh in the next session.

## Contributing
If you would like to contribute to the project, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or suggestions, please contact [your-email@example.com].
