# Captcha

Captcha illustrator with Pillow and Numpy for Python 3.6 or higher

### Installation

Install without distortion setting:

```
pip install captcha-MagicaFreak
```

Install with distortion setting:

```
pip install bettercaptcha[distortion]
```

or

```
pip install bettercaptcha
pip install numpy
```

## Captcha Class

All the possile CAPTCHA variants

### CaptchaImage

The class `CaptchaImage` generates an Image with given Text or generated Text. The look of the CAPTCHA can be changed
through the [default Arguments](#default-arguments:), [setting Arguments](#setting-arguments:) and diffrent
[overwrites](#overwrites).

The most basic usage of this class looks like this:

```python
from bettercaptcha import CaptchaImage

captcha = CaptchaImage()

image = captcha.create()
text = captcha.text
```

Here is the ``image`` a `PIL.Image` instance and `text` the text what is written in the CAPTCHA

#### Default Arguments:

Name | Type | Description | Default
--- | --- | --- | ---
font | str | path to the font file | arial.ttf
font_size | int | size of the font | 24
color | tuple | text color of the CAPTCHA | (0, 0, 0) => black
text | str | text on the captcha | random generated string
char_amount | int | length of the random generated string | 12

#### Setting Arguments:

Name | Type | Description | Default
--- | --- | --- | ---
background | Background | sets a background on the captcha (see more under [Background](#background)) | None
distortion | bool | distorts the text (Needs the numpy package) | False
lines | int | adds the amount of lines between random Points | None
points | int | adds the amount of points on random Points | None
frame | bool | adds a frame around the CAPTCHA | False

#### Background

The class `Background` has all modes for the setting `background`.

The first mode is `Background.RANDOM`. It generates a random color in every Pixel of the background. The color is
choosen from the list `CaptchaImage.colors` that can be [overwritten](#overwrites).

The second mode is `Background.COLOR`. It colors the background with the text color with only 50% alpha.

#### Overwrites

Overwrites can be used in many diffrent cases, but the 2 biggest would be if the captcha is generated with some
flexibiltiy, or you generate another captcha with diffrent look but same text.

The default argumnets can't be overwritten except color The overwrites for color would look like this:

```python
captcha = CaptchaImage()
captcha.color = (52, 52, 52)
```

Important to notice that `captcha.color` can only be a rgb value!

All the setting arguments can be overwritten, this would look like this:

```python
captcha = CaptchaImage()
captcha.settings['distortion'] = True
captcha.settings['background'] = Background.RANDOM
```

The third kind of overwrites are things that are normaly contstaned. Under this counts `CaptchaImage.colors`,
`CaptchaImage.distortion` and `CaptchaImage.distortion_factor`.

`CaptchaImage.colors` is a list or RGB colors for the background setting `Background.RANDOM`, it can be overwritten with
another list of RGB colors, like so:

```python
captcha = CaptchaImage(background=Background.RANDOM)
captcha.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
```

`CaptchaImage.distortion` is a mathematical function. To overwrite it you need to create another function with the
values `x`, `a` and `w`. It can be overwritten like this:

```python
from math import sin, pi

captcha = CaptchaImage(distrotion=True)


def distortion(x, a, w):
    return a * sin(2 * pi * x * w)
# or
distortion = lambda x, a, w: a * sin(2 * pi * x * w)

captcha.distortion = distortion
```

`CaptchaImage.distortion_factor` is the last overwrite it is a tuple of ints that are influencing the values `a` and `w`
. The calculation of `a` and `w` looks like this:

```python
a = image_height / distortion_factor[1]
w = distortion_factor[0] / image_width
```

To overwrite the complete distortion factor you would do this:

```python
captcha = CaptchaImage(distrotion=True)
captcha.distortion_factor = (0.59, 17.0)
```

#### CaptchaImage.rand_chars(amount, chars)

This function generates a random string with the length of the amount, but it only usese every character one time out of
the list. Important to notice that if you give a chars list smaller than the amount it will not work! 

```python
text = CaptchaImage.rand_chars(12)
```

Arguments:

Name | Type | Description | Default
--- | --- | --- | --- 
amount | int | length of the string | 12
chars | list | list of used characters | all ascii letters and digits