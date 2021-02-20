from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
image = ImageCaptcha()

image_data = image.generate('Sareer Talks')
image.write('Sareer Talks', 'cap.png')

audio = AudioCaptcha()
audio_data = audio.generate('12345')
audio.write('12345', 'audio.mp3')