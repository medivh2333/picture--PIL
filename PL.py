from PIL import Image

codeLib="@B%8&WM#*oahkbdpqwmZOOQLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!1I;:,~"
count=len(codeLib)

def transform(image_file):
    codePic=''
    imode=list(image_file.getbands())
    print(imode)
    print(imode[-1])
    for h in range(0,image_file.size[1]):
        for w in range(0,image_file.size[0]):
            if imode[-1]=="A":
                r,g,b,a=image_file.getpixel((w,h))
            elif imode[-1]=="B":
                r,g,b,a=image_file.getpixel((w,h))
            gray=int(r*0.299+g*0.587+b*0.114)
            codePic=codePic+codeLib[int(((count-1)*gray)/256)]
        codePic=codePic+'\r\n'
    return codePic

fp=open("/home/tarena/aid1907/phase3/day01-day05/img02-3.png",'rb')
image_file=Image.open(fp)
image_file=image_file.resize((int(image_file.size[0]*0.35),int(image_file.size[1]*0.175)))
print('Info:',image_file.size[0],'',image_file.size[1],'',count)

tmp=open("/home/tarena/aid1907/phase3/day01-day05/img02-3.txt",'w')
tmp.write(transform(image_file))
tmp.close()

https://github.com/medivh2333/-.git
