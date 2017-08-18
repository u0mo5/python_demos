import os
url = "http://sample.sample/sample.jpg"
os.chdir("C:\\Program Files (x86)\\Thunder Network\\Thunder\\Program\\")
os.system("Thunder.exe -StartType:DesktopIcon \"%s\""%url)

