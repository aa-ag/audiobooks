import pyttsx3
import PyPDF2

'''
## Test 1
voice = pyttsx3.init()
voice.say('Hello World!')
voice.runAndWait()
'''

text = open('Introduction_to_Python_Harvard.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(text)
pages = pdfReader.numPages
print(pages)
voice = pyttsx3.init()
page = pdfReader.getPage(0)
readable = page.extractText()
voice.say(readable)
voice.runAndWait()