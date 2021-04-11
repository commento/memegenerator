"""Generate a Meme from Flask WebApp."""
import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from MemeEngine import MemeGenerator

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for quote_file in quote_files:
        quotes += Ingestor.parse(quote_file)

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    try:
        for file in os.listdir('./static'):
            os.remove(os.path.join('./static', file))
            print(file, " removed")
    except OSError:
        print("Deleting the image failed")
    else:
        print("Successfully deleted the image")

    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    response = requests.get(image_url)
    file = open("./tmp/img.jpg", "wb")
    file.write(response.content)
    file.close()

    path = meme.make_meme("./tmp/img.jpg", body, author)
    if path == False:
        return abort(400)

    try:
        os.remove("./tmp/img.jpg")
    except OSError:
        print("Deleting the image failed")
    else:
        print("Successfully deleted the image")

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
