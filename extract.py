from pypdf import PdfReader
reader_obj=PdfReader('new.pdf')
print(len(reader_obj.pages))
page_pdf=reader_obj.pages[0]
text=page_pdf.extract_text()
print(text)
