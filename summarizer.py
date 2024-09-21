import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

def summarize_text(texts, query):
    api_key = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=api_key)
    
    combined_text = "\n\n".join(texts)
    
    prompt = f"""
    Here are some texts from various sources:
    {combined_text}

    Based on these texts, please answer the following question as accurately as possible:
    '{query}'
    If the texts do not provide information relevant to the question, say "Impossible to answer your question based on the provided texts."
    """
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    summary = response.text.strip()
    
    if "impossible to answer" in summary.lower():
        return "Impossible to answer your question based on the provided texts."
    
    return summary
