import random
import string
from math import sin, pi
from PIL import Image, ImageDraw, ImageFont


class MissingPackage(Exception):
    """
    Exception raised for errors where a package is missing but needed for a specific setting

    Attributes:
        :param package: The missing Package
        :type package: str
        :param setting: The setting where it got raised
        :type setting: str
    """

    def __init__(self, package: str, setting: str):
        self.package = package
        self.setting = setting
        self.message = f"The Python Package {self.package} is missing for {self.setting} Captchas!"
        super().__init__(self.message)


class Background:
    """
    Diffrent modes for the setting Background:

    Mode:
        :cvar RANDOM: generates every background Pixel in a random color
        :cvar COLOR: colors the background in a brighter text color
    """
    RANDOM = 'random'
    COLOR = 'color'


class CaptchaImage:
    """
    Generates a Captcha from the given Attriutes and Settings

    Attriutes:
        :param font: path to the font file (default: arial.ttf)
        :param font_size: size of the font (default: 24)
        :param color: main color of the CAPTCHA
        :param text: text on the bettercaptcha, if not given generates a random string in the length of char_amount
        :param char_amount: length of the random generated string (default: 12)
        
    Settings:
        :param background: sets a background on the bettercaptcha (see modes under `help(bettercaptcha.Background)`)
        :param distortion: distorts the text
        :param lines: adds the amount of lines between random Points
        :param points: adds the amount of points on random Points
        :param frame: adds a frame around the CAPTCHA
    """

    def __init__(self, font: str = None, font_size: int = 24, color: tuple = (0, 0, 0), text: str = None,
                 char_amount: int = 12, background: str = None, distortion: bool = None, lines: int = None,
                 points: int = None, frame: bool = None):

        self.text = text or self.rand_chars(char_amount)
        try:
            self.font: ImageFont = ImageFont.truetype(font or "arial.ttf", font_size)
        except OSError:
            self.font: ImageFont = ImageFont.load_default()
        self.color = color
        self.__textsize = self.font.getsize(self.text)
        self.size = (int(self.__textsize[0] * 1.2), int(self.__textsize[1] * 1.75))
        self.image = Image.new("RGB", self.size, (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)
        self.settings = {"background": background or False, "distortion": distortion or False,
                         "lines": lines or False, "points": points or False, "frame": frame or False}

        self.colors = [(255, 153, 255), (153, 255, 102), (255, 153, 102), (102, 255, 255), (153, 102, 255)]
        self.distortion = lambda x, a, w: a * sin(5 * pi * x * w + 400)
        self.distortion_factor = (0.6, 18.0)

    def create(self):
        """Draws the CAPTCHA"""
        if self.settings["background"]:

            if self.settings["background"] == Background.RANDOM:
                for x in range(self.size[0]):
                    for y in range(self.size[1]):
                        self.draw.point([x, y], fill=random.choice(self.colors))

            elif self.settings["background"] == Background.COLOR:
                img = Image.new("RGBA", self.size, (*self.color, 128))
                self.image.paste(img, (0, 0), mask=img)

        text_offset = [(self.size[0] - self.__textsize[0]) / 2, (self.size[1] - self.__textsize[1]) / 2]
        if self.settings["distortion"]:
            try:
                import numpy as np
                text_image = Image.new("RGB", self.size, (255, 255, 255))
                text_draw = ImageDraw.Draw(text_image)
                text_draw.text(text_offset, self.text, font=self.font, fill=self.color)

                m = np.array(text_image)
                a = m.shape[1] / self.distortion_factor[1]
                w = self.distortion_factor[0] / m.shape[0]
                for i in range(m.shape[0]):
                    m[i] = np.roll(m[i], int(self.distortion(i, a, w)))

                text_image = Image.fromarray(np.uint8(m)).convert("RGBA")
                new_data = [(255, 255, 255, 0) if item == (255, 255, 255, 255) else (*self.color, 255) for item in
                            text_image.getdata()]
                text_image.putdata(new_data)

                self.image.paste(text_image, (0, 0), mask=text_image)

            except ImportError:
                raise MissingPackage("Numpy", "distorted")
        else:
            self.draw.text(text_offset, self.text, font=self.font, fill=self.color)

        if self.settings["lines"]:
            for _ in range(self.settings["lines"]):
                self.draw.line([random.randint(0, self.size[0]), random.randint(0, self.size[1]),
                                random.randint(0, self.size[0]), random.randint(0, self.size[1])],
                               fill=self.color)

        if self.settings["points"]:
            for _ in range(self.settings["points"]):
                cords = (random.randint(0, self.size[0]), random.randint(0, self.size[1]))
                self.draw.ellipse([cords, (cords[0] + 3, cords[1] + 3)], fill=self.color)

        if self.settings["frame"]:
            self.draw.rectangle([(0, 0), (self.size[0] - 1, self.size[1] - 1)], outline=self.color, width=3)

        return self.image

    @staticmethod
    def rand_chars(amount=12, chars=None):
        """
        Generates a random string with the length of the amount (default 12 and with every ascii letter and digit)
        
        Attributes:
            :param amount: length of the string
            :param chars: list of characters
        """
        chars = chars or string.digits + string.ascii_letters
        return ''.join(random.sample(chars, amount))
