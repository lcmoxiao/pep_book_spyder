# -- coding: utf-8 --
# 导入PYPDF2库
from PyPDF2 import PdfReader, PdfWriter


def split_single_pdf(read_file, start_page, end_page, pdf_file):
    # 1. 获取原始pdf文件
    fp_read_file = open(read_file, 'rb')
    # 2. 将要分割的PDF内容格式化
    pdf_input = PdfReader(fp_read_file)
    # 3. 实例一个 PDF文件编写器
    pdf_output = PdfWriter()
    # 4. 把3到4页放到PDF文件编写器
    for i in range(start_page, end_page):
        pdf_output.add_page(pdf_input.pages[i])
    # 5. PDF文件输出
    with open(pdf_file, 'wb') as pdf_out:
        pdf_output.write(pdf_out)
    print(f'{read_file}分割{start_page}页-{end_page}页完成，保存为{pdf_file}!')


if __name__ == '__main__':
    # 待切分文件文件名
    in_pdf_name = "E:\温宿县中考精炼资料汇编（七年级上 unit1--unit9）(1).pdf 更新至七下unit3(1).pdf"
    # 切分后文件文件名
    out_pdf_name = '试题.pdf'
    # 切分开始页面
    start = 10
    # 切分结束页面
    end = 20
    split_single_pdf(in_pdf_name, start, end, out_pdf_name)
