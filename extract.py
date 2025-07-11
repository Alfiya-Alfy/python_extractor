from pypdf import PdfReader
reader_obj=PdfReader('new.pdf')
print(len(reader_obj.pages))
page_pdf=reader_obj.pages[0]
text_pdf=page_pdf.extract_text()
print(text_pdf)
