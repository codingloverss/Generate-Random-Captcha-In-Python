import random
from captcha.image import ImageCaptcha
def main():
    alpha = []
    ALPHA=[]
    num=[]
    for i in range(65,91):
        ALPHA.append(chr(i))
        alpha.append(chr(i).lower())
    for i in range(0,10):
        num.append(i)
    s_alpha = random.choice(alpha)
    c_alpha = random.choice(ALPHA)
    c_alpha1 = random.choice(ALPHA)
    num1 = random.choice(num)
    num2 = random.choice(num)
    num3 = random.choice(num)
    row_captcha = s_alpha+str(num3)+c_alpha+str(num2)+c_alpha1+str(num1)
    row_captcha = list(row_captcha)
    random.shuffle(row_captcha)
    row_captcha = ''.join(row_captcha)
    img = ImageCaptcha()
    image = img.generate_image(row_captcha)
    image.show()
    return row_captcha
if __name__=="__main__":
    main()
    
    
