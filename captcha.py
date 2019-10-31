import random
from captcha.image import ImageCaptcha
def main():
    a=random.choice(alpha)
    A=random.choice(ALPHA)
    n1=random.choice(num)
    n2=random.choice(num)
    n3=random.choice(num)
    row_captcha=a+str(n3)+A+str(n2)+A+str(n1)
    row_captcha=list(row_captcha)
    random.shuffle(row_captcha)
    row_captcha=''.join(row_captcha)
    img = ImageCaptcha()
    image = img.generate_image(row_captcha)
    image.show()
    return a,row_captcha
if __name__=="__main__":
    main()
