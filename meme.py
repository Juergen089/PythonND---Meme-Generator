import os
import random
import argparse
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine import Ingestor
from MemeEngine.MemeEngine import MemeEngine
from pathlib import Path


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='add a meme to an image')
    parser.add_argument('-p', '--path', type=str, default=None, help="Path to image file")
    parser.add_argument('-b', '--body', type=str, default=None, help="Text written to the image")
    parser.add_argument('-a', '--author', type=str, default=None, help="Author of the text, written to the image")
    args = parser.parse_args()
    generated = generate_meme(args.path, args.body, args.author)
    if (generated != None):
        print(f"generated meme: {generated}")
    else:
        print("No meme generated due to error")