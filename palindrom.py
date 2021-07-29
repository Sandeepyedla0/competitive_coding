import re


def rev(pal):
    pal=pal.lower()
    pal=re.sub('[^a-zA-Z1-9]+', "", pal)
    pal=pal.replace(" ","")
    print("original", pal)
    print("reversed",pal[::-1])
    if(pal[::-1]==pal):
        print(True)
    else:
        print(False)



pal= "A man, a plan, a canal: Panama"
rev(pal)