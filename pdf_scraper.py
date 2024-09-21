import PyPDF2
import json

def scrape_pdf_info(file_path):
    content = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                content += page.extract_text()
    except Exception as e:
        content = f"Error reading PDF file: {str(e)}"
    
    return {
        'title': file_path.split('/')[-1],
        'content': content
    }

def save_to_json(data, filename='data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    file_path = input("Enter the path to the PDF file: ")
    scraped_data = scrape_pdf_info(file_path)
    save_to_json(scraped_data)
    print(f"Data scraped and saved successfully from {file_path}!")

if __name__ == "__main__":
    main()
