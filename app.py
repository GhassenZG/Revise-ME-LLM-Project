import streamlit as st
from pdf_scraper import scrape_pdf_info
from summarizer import summarize_text
from web_scraper import scrape_website_info
from yt_scraper import scrape_youtube_transcript
from vector_db import create_chroma_db, get_relevant_passage, add_documents_to_db

def main():
    st.title("ReviseME - LLM Based Revision Tool")

    # Create a new vector database for the session
    db_name = "scraped_content_db"
    db = create_chroma_db(db_name)

    # File uploader for PDFs
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
    if pdf_file and st.button("Scrape and Save PDF"):
        with open(pdf_file.name, "wb") as f:
            f.write(pdf_file.getbuffer())
        scraped_data = scrape_pdf_info(pdf_file.name)
        if scraped_data['content'].startswith('Error'):
            st.error(scraped_data['content'])
        else:
            add_documents_to_db(db, [scraped_data['content']])
            st.success("PDF content scraped and added to the database successfully!")
            print(f"PDF content added: {scraped_data['content']}")  # Log the content added

    # URL input for web scraping
    url = st.text_input("Enter a URL to scrape")
    if url and st.button("Scrape and Save URL"):
        scraped_data = scrape_website_info(url)
        if scraped_data['content'].startswith('Error'):
            st.error(scraped_data['content'])
        else:
            add_documents_to_db(db, [scraped_data['content']])
            st.success("Website content scraped and added to the database successfully!")
            print(f"Website content added: {scraped_data['content']}")  # Log the content added

    # YouTube video input for transcript extraction
    youtube_url = st.text_input("Enter a YouTube URL to scrape")
    if youtube_url and st.button("Scrape and Save YouTube Transcript"):
        scraped_data = scrape_youtube_transcript(youtube_url)
        if scraped_data['content'].startswith('Error'):
            st.error(scraped_data['content'])
        else:
            add_documents_to_db(db, [scraped_data['content']])
            st.success("YouTube transcript scraped and added to the database successfully!")
            print(f"YouTube transcript added: {scraped_data['content']}")  # Log the content added

    # Summarization section
    query = st.text_input("Ask a question about the scraped content")

    if query:
        st.write("Summarizing information...")
        relevant_passage = get_relevant_passage(query, db)
        if not relevant_passage:
            st.write("No relevant passage found in the database.")
        else:
            summary = summarize_text([relevant_passage], query)
            st.write(summary)

if __name__ == "__main__":
    main()
