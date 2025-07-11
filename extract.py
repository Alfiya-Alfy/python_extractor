;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;from pypdf import PdfReader
reader_obj=PdfReader('new.pdf')
print(len(reader_obj.pages))
page=reader_obj.pages[0]
text=page.extract_text()
print(text)
