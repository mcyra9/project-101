import os
import shutil

fromdir = 'C:/Users/michael/downloads'
todir = 'C:/Users/michael/documents'
listof = os.listdir(fromdir)

for filename in listof:
    name, ext = os.path.splitext(filename)
    if ext == "":
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = fromdir + '/' + filename
        path2 = todir + '/' + 'Document_Files'
        path3 = todir + '/' + 'Document_Files' + '/' + filename
        if os.path.exists(path2):
            print('Moving' + filename + '.....')
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print('Moving' + filename + '.....')
            shutil.move(path1, path3)