import sys
import os
import os.path
import google_vision_api as google_vision_api
import label_image as label_image
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
print("2.TensorFlow classifier")
print("3.Run both")
nb = input('Choose a classifier: ')
if (int(nb)==1 or int(nb)==3):
    print("---------------------------------------------------------------------------------")
    print("google classifier is running")
    print("---------------------------------------------------------------------------------")
    with open(file_name, 'rb') as ff:
        content = ff.read()
    response=(google_vision_api.get_prediction(content, 'clas-219000',  'ICN7228006044013306359'))
    print("---------------------------------------------------------------------------------")
    print("Google cloud AutoML vision results")
    print("---------------------------------------------------------------------------------")
    for result in response.payload:
        print("Predicted class name: {}".format(result.display_name))
        print("Predicted class score: {}".format(result.classification.score))
if (int(nb)==2 or int(nb)==3):
    print("---------------------------------------------------------------------------------")
    print("TensorFlow classifier is running")
    print("---------------------------------------------------------------------------------")
    os.system('python label_image.py --graph=output_graph.pb --labels=output_labels.txt --input_layer=Placeholder  --output_layer=final_result --image='+file_name )
else:
    print("Please type a number between 1 to 3")
    sys.exit(1)

