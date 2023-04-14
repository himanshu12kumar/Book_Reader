import pyttsx3
import PyPDF2
book = open('quantum.pdf' , 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(1)
text = page.extract_text()
voices = speaker.getProperty('voices')
speaker.setProperty('voice' , voices[1].id)
rate = speaker.getProperty('rate')
speaker.setProperty('rate' , 130)
speaker.say(text)
speaker.runAndWait()


# speaker.save_to_file('Hii Mr. Himanshu how are this is your computer so if any body try to touch this computer I pucnished them' , 'test.mp3')
# speaker.runAndWait()