

## Python-Meme-Generator

Meme Generator from the Udacity Python Nanodegree

## Overview:


The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote:
-   Interact with a variety of complex filetypes. This emulates the kind of data you’ll encounter in a data engineering role.
-   Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
-   Load, manipulate, and save images.
-   Accept dynamic user input through a command-line tool and a web service. This emulates the kind of work you’ll encounter as a full stack developer.
-   Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
-   DRY (don’t repeat yourself) principles of class and method design.
-   Working with modules and packages in Python.
- Code, docstrings, and comments adhere to  [PEP 8 Standards](https://www.python.org/dev/peps/pep-0008/).

## Instructions for Running the Application

Running mem.py -p [path to the image] -b [meme text] -a [author of the meme text] from the command line will return the meme path. 
For running the web application start app.py and open the given web address with a web browser. Initially a random meme will be created, for user defined meme follow the commands under "create".

## Dependencies

**xpdf:**  This project uses xpdf as a submodule to parse pdf text files for the quotes. xpdf must be installed on the system

**Python Packages:**  The full list of modules for this project is given in the  requirement.txt file to be used in a virtual python environment. The most important are:

- pandas
- python
- Pillow
- Flask
- requests

**Fonts:**  The meme engine uses a free ttf font, which is located in the _font directory. So there should be no problems when using the script on different operating system. Feel free to change the font type, size and color in MemeEngine.py file.

## Submodules

**MemeEngine:** creates the meme
**QuoteEngine:** reads the meme text from pdf, txt, csv and docx files using strategic object design pattern and returns a list of objects as containers for the meme text & author
