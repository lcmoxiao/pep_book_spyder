from download_jpg import Book
import os
from PyPDF2 import PdfWriter
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def numerical_sort(value):
    # 提取文件名中的数字部分进行排序
    return int(''.join(filter(str.isdigit, value)))


def convert_images_to_pdf(images_folder, output_file):
    pdf_writer = PdfWriter()

    # 获取目录下所有jpg文件
    image_files = sorted([f for f in os.listdir(images_folder) if f.endswith('.jpg')], key=numerical_sort)

    print(image_files)

    # 创建一个空白的PDF文件
    c = canvas.Canvas(output_file, pagesize=letter)

    for image_file in image_files:
        image_path = os.path.join(images_folder, image_file)

        # 打开图像文件
        image = Image.open(image_path)

        # 调整图像大小以适应PDF页面
        image.thumbnail((letter[0], letter[1]))

        # 将图像添加到PDF中
        c.drawImage(image_path, 0, 0, letter[0], letter[1])
        c.showPage()

    # 保存PDF文件
    c.save()


if __name__ == '__main__':

    names = [
        Book("地理", "七上", "114", "1338001101121"),
        Book("地理", "七下", "112", "1338001102121"),
        Book("地理", "八上", "122", "1338001201131"),
        Book("地理", "八下", "116", "1338001202131"),

        Book("地理", "必1", "134", "1438001121191"),
        Book("地理", "必2", "134", "1438001122191"),
        Book("地理", "选1", "106", "1438001131201"),
        Book("地理", "选2", "102", "1438001132201"),
        Book("地理", "选3", "128", "1438001133201"),
    ]

    # run
    for name in names:
        name = name.subject + "/" + name.level
        convert_images_to_pdf(name, name + ".pdf")
