from PyPDF2 import PdfReader
import pyttsx3
from tika import parser
import os


def read_epub(path):
    """Read an epub file and return the plain text."""
    epub = path
    parsed = parser.from_file(epub, service="text")
    content = parsed["content"]
    return content


def read_pdf(path):
    """Read the pdf file, save, and return it as plain text."""
    reader = PdfReader(path)
    pages = reader.pages
    with open("text.txt", "w", encoding="utf-8") as txt:
        for page in pages:
            txt.write(page.extract_text())

    with open("text.txt", "r", encoding="utf-8") as texto:
        h = texto.read()
    return h[0:100000]


def text_to_speech(function):
    """Convert text(str) into speech using pyttsx3 technology."""
    engine = pyttsx3.init()
    engine.setProperty("rate", 130)
    engine.say(function)
    engine.runAndWait()


on = True
while on:

    user_path = input(
        "Please type the route for the file to convert to text to speech. Example: C:/epubs/The lord of the "
        "rings.epub // or type exit to leave:\n")

    if user_path.endswith(".epub") and os.path.isfile(user_path):
        text_to_speech(read_epub(user_path))
    elif user_path.endswith(".pdf") and os.path.isfile(user_path):
        text_to_speech(read_pdf(user_path))
    elif user_path.lower() == "exit":
        on = False
    else:
        print("\nSorry, your path or file is wrong. Try again.")
