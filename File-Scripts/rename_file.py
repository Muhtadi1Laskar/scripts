import os

def rename_file(directory, name, extension='.pdf'):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            new_name = 'prefix' + filename
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            