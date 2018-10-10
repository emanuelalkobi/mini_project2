import sys
import os
import os.path
import google_vision_api as google_vision_api

if (len(sys.argv)!=2):
    print("Please insert a file name only")
    sys.exit(1)
file_name= (sys.argv[1])

if not os.path.isfile(file_name)  and not os.access(file_name, os.R_OK):
    print("The file is missing or not readable")
    sys.exit(1)

print("Soccer ball image detector")
print("Please choose with witch which classifier you want to predict your image")
print("1.Google cloud AutoML Vision")
print("2.")
nb = input('Choose a classifier: ')
if (int(nb)==1):
    print("google classifier is running")
    with open(file_name, 'rb') as ff:
        content = ff.read()
    print(google_vision_api.get_prediction(content, 'clas-219000',  'ICN7228006044013306359'))
