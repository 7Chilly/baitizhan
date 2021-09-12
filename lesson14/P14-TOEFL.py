import docx

filePath = "托福口语-万能理由和答案.docx"
doc = docx.Document(filePath)
for para in doc.paragraphs:
    styleName = para.style.name
    if styleName in ["Title", "Heading 1", "Heading 2"]:
        print(para.text)
