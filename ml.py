import torch
import fitz
import pdfplumber
import re
from pypdf import PdfReader
import PyPDF2 
from transformers import AutoTokenizer, AutoModelWithLMHead
tokenizer=AutoTokenizer.from_pretrained('T5-base')
model=AutoModelWithLMHead.from_pretrained('T5-base', return_dict=True)
pdf_path = r"C:\Users\Sanat\Downloads\testFile.pdf"
#a = PyPDF2.PdfReader(pdf_path)
#reader  = PdfReader(pdf_path)
#reader = PdfReader(pdf_path)
#def extract_text(file_path):
#    text="";
#    with pdfplumber.open(file_path) as pdf:
#        for page in pdf.pages:
#            pgtext = page.extract_text()
#            if pgtext:
#                text += pgtext
#    return text

#sequence = ("Data science is an interdisciplinary field[10] focused on extracting knowledge from typically large data sets and applying the knowledge and insights from that data to solve problems in a wide range of application domains.[11] The field encompasses preparing data for analysis, formulating data science problems, analyzing data, developing data-driven solutions, and presenting findings to inform high-level decisions in a broad range of application domains. As such, it incorporates skills from computer science, statistics, information science, mathematics, data visualization, information visualization, data sonification, data integration, graphic design, complex systems, communication and business.[12][13] Statistician Nathan Yau, drawing on Ben Fry, also links data science to human–computer interaction: users should be able to intuitively control and explore data.[14][15] In 2015, the American Statistical Association identified database management, statistics and machine learning, and distributed and parallel systems as the three emerging foundational professional communities.[16]")
# inputs=tokenizer.encode("sumarize: " +sequence,return_tensors='pt', max_length=512, truncation=True)
# output = model.generate(inputs, min_length=80, max_length=100)
# summary=tokenizer.decode(output[0])
text = ""
#print(len(reader.pages))
#for i in range(len(reader.pages)):
#    page = reader.pages[i]
#    pagetxt = page.extract_text()
#    text+=pagetxt


# Open the PDF file
def extractor(pdf_path):
    txt =""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

    # Open the text file where the extracted text will be stored
        for page in reader.pages:
            tmptext = page.extract_text()
            if tmptext:  # Check if text is not None
                txt+=tmptext
    return txt
def cleaner(text):
    text = re.sub(r'Page \d+ of \d+','',text,flags=re.IGNORECASE)
    text = re.sub(r'\bPage\s+\d+\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'References\b.*', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'\b\d+\b', '', text)
    return text
def summariser(text):
    inputs=tokenizer.encode("sumarize: " +text,return_tensors='pt', max_length=10000, truncation=True)
    output = model.generate(inputs, min_length=80, max_length=200)
    summary=tokenizer.decode(output[0])
    return summary
text = extractor(pdf_path)
text = cleaner(text)
summarisedText = summariser(text)
print(text)