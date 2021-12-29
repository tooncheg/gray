from PIL import Image
from tkinter import filedialog


def main():
    lst = []

    def def_file():
        filename = filedialog.askopenfile(title='open')
        return filename.name

    im = Image.open(def_file())
    im = im.resize((640, 480))

    for i in im.getdata():
        lst.append((i[0] * 222 + i[1] * 707 + i[2] * 71) / 1000)

    new_im = Image.new("L", im.size)
    new_im.putdata(lst)

    new_im.show()
    im.show()


if __name__ == "__main__":
    main()
