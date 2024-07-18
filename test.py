from utils.pdf_reader import read_large_pdf

pdf_file_path = './data/ion-resume.pdf'
full_text = read_large_pdf(pdf_file_path, 128)
print(full_text)
