import os

def move_file(source, destination, extension='.pdf'):
    pdf_files = [file for file in os.listdir(source) if extension in file]

    for pdf in pdf_files:
        src_path = os.path.join(source, pdf)
        dst_path = os.path.join(destination, pdf)

        os.rename(src_path, dst_path)
    return pdf_files
