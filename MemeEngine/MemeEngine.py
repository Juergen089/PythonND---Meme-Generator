"""
Meme generator module, which includes  class MemeEngine 
which generates memes with the image,body and author provided.
"""

from PIL import Image
from PIL import UnidentifiedImageError
from PIL import ImageDraw
from PIL import ImageFont
import random
from pathlib import Path
import os

class MemeEngine:
    """class to generate Meme
    """

    def __init__(self, path:str):
        self._path = path


    def check_dir(self, path:str):
        """Method checks if the path exist and
        creates it, if needed
        Arguments:
        path: string to the path to be checked
        """
        _path = Path(path).resolve()
        if not (os.path.exists(_path)):
            os.mkdir(_path)
        return

    def make_meme(self, img_path:str, text:str, author:str, width:int=500) ->str:
        """ method to rezize and add the meme text to an image
        
        Arguments:
        img_path: path of the original image
        text: meme text
        author: meme author
        width: new with of the resized image

        Return:
        path to the new image as string
        """ 
        act_ext = img_path.split('.')[-1]
        outfile = random.randint(1000, 2000000)
        outfile_path = f"{self._path}/{outfile}.{act_ext}"
        self.check_dir(self._path)
        try:
            with Image.open(img_path) as img:
                img.convert('RGB')
                ratio = width/img.width
                new_height = int(img.height*ratio)
                img = img.resize((width, new_height))

                pos1 = random.randint(10, 20)
                pos2 = random.randint(30, 60)
                message = text + ',\n' +'said ' + author
                try:
                    font = ImageFont.truetype("Georgia.ttf", 25)
                except Exception as e:
                    print(f"Font not found on system, {e}")
                draw = ImageDraw.Draw(img)
                draw.text((pos1, pos2), message, font=font, fill='white')
                img.save(outfile_path)
        except FileNotFoundError:
            print(f"Error: image file not found")
            outfile_path=None
        except Exception as error:
            print(error)
            outfile_path = None

        return outfile_path
    
