
from PIL import Image
from tkinter import filedialog

lst = []


def def_file():
    filename = filedialog.askopenfile(title='open')
    return filename.name


def convert_img():
    img = Image.open(def_file())
    img = img.resize((640, 480))

    for i in img.getdata():
        lst.append((i[0] * 222 + i[1] * 707 + i[2] * 71) / 1000)

    new_img = Image.new("L", img.size)
    new_img.putdata(lst)
    return new_img


def main():
    result = convert_img()
    result.show()
    # new_im.show()
    # im.show()


if __name__ == "__main__":
    main()
