from math import cos, pi

from bettercaptcha import CaptchaImage, Background


def test_basic_captcha():
    captcha = CaptchaImage()
    captcha.create()
    captcha.image.show()


def test_color_captcha():
    captcha = CaptchaImage(color=(255, 0, 0))
    captcha.create()
    captcha.image.show()


def test_text_captcha():
    captcha = CaptchaImage(text="MagicaFreak")
    captcha.create()
    captcha.image.show()


def test_generated_text_captcha():
    captcha = CaptchaImage(char_amount=6)
    captcha.create()
    captcha.image.show()


def test_background_random_captcha():
    captcha = CaptchaImage(background=Background.RANDOM)
    captcha.create()
    captcha.image.show()


def test_background_color_captcha():
    captcha = CaptchaImage(background=Background.COLOR)
    captcha.create()
    captcha.image.show()


def test_background_custom_color_captcha():
    captcha = CaptchaImage(background=Background.COLOR, color=(128, 0, 64))
    captcha.create()
    captcha.image.show()


def test_distortion_captcha():
    captcha = CaptchaImage(distortion=True, font_size=50)
    captcha.create()
    captcha.image.show()


def test_lines_captcha():
    captcha = CaptchaImage(lines=4)
    captcha.create()
    captcha.image.show()


def test_points_captcha():
    captcha = CaptchaImage(points=4)
    captcha.create()
    captcha.image.show()


def test_frame_captcha():
    captcha = CaptchaImage(frame=True)
    captcha.create()
    captcha.image.show()


def test_everything_captcha():
    captcha = CaptchaImage(font_size=50, color=(255, 0, 128), text="MagicaFreak",
                           background=Background.RANDOM, distortion=True, lines=10,
                           points=15, frame=True)
    captcha.create()
    captcha.image.show()


def test_overwrite_distortion_captcha():
    captcha = CaptchaImage(distortion=True)
    captcha.distortion = lambda x, a, w: a * cos(5 * pi * x * w + 400)
    captcha.create()
    captcha.image.show()

    captcha.distortion_factor = (0.5, 16)
    captcha.create()
    captcha.image.show()


def test_overwrite_random_colors_captcha():
    captcha = CaptchaImage(background=Background.RANDOM)
    captcha.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    captcha.create()
    captcha.image.show()


def test_default_random_chars():
    chars = CaptchaImage.rand_chars()
    print(chars)


def test_random_chars_amount():
    chars = CaptchaImage.rand_chars(amount=6)
    print(chars)
    chars = CaptchaImage.rand_chars(amount=6)
    print(chars)
    chars = CaptchaImage.rand_chars(amount=6)
    print(chars)


def test_random_chars_list():
    chars = CaptchaImage.rand_chars(chars=["!", ":", ";", "#", '*', "+", "~", "'", '"', '-', '_', '.', ','])
    print(chars)


def test_random_chars_both():
    chars = CaptchaImage.rand_chars(amount=4, chars=["!", ":", ";", "#"])
    print(chars)


if __name__ == '__main__':
    test_basic_captcha()
    test_color_captcha()
    test_text_captcha()
    test_generated_text_captcha()
    test_background_random_captcha()
    test_background_color_captcha()
    test_background_custom_color_captcha()
    test_distortion_captcha()
    test_lines_captcha()
    test_points_captcha()
    test_frame_captcha()
    test_everything_captcha()
    test_overwrite_distortion_captcha()
    test_overwrite_random_colors_captcha()
    test_default_random_chars()
    test_random_chars_list()
    test_random_chars_amount()
    test_random_chars_both()
