from pypdf import PdfReader


def read_pdf(file_path, chunk_size=512):
    with open(file_path, 'rb') as f:
        pdf_reader = PdfReader(f)
        total_pages = pdf_reader.get_num_pages()
        full_text = ''
        
        for current_page in range(total_pages):
            pdf = PdfReader(f)
            page = pdf.get_page(current_page)
            text = page.extract_text()
            full_text += text
            
            # Move the file pointer to the next page
            f.seek(f.tell() + chunk_size)
        
        return full_text