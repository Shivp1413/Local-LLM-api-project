# src/utils/html_formatter.py

import html

def format_to_html(text):
    # Escape any HTML special characters
    escaped_text = html.escape(text)
    
    # Split the text into paragraphs
    paragraphs = escaped_text.split('\n\n')
    
    # Wrap each paragraph in <p> tags
    formatted_paragraphs = [f'<p>{p.strip()}</p>' for p in paragraphs if p.strip()]
    
    # Join the formatted paragraphs and wrap in a div
    html_output = f'<div class="llama-response">{"".join(formatted_paragraphs)}</div>'
    
    return html_output
