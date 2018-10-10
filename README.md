# mini_project2 build classifier
In this mini project I will build a machine learning classifier for soccer balls.
as our main project is to detect an offside and the main diffuclty is to detect the soccer ball ,i hope that this classifier will give up better results.
My data set consitst of photots with soocer balls and with photos with no soccer ball.
the output of the classifier should be a result that will represent the chance that there is a soccer ball in the input image.

my data set consist of 144 images with soccer ball and with 160 images with no soccer ball.


I will implement 2 image classifires:
1.I will train  The 1st classifier using the Google cloud AutoML Vision interface.




1.in order to run google cloud run the next commands:

export GOOGLE_APPLICATION_CREDENTIALS="/Users/emanuelalkobi/Desktop/ec601/mini_project2/mini_project2/1.json"

gcloud auth application-default print-access-token

  
gcloud auth login





export PROJECT_ID="clas-219000"

export REGION_NAME="us-central1"

gsutil mb -p $PROJECT_ID -c regional -l $REGION_NAME gs://$PROJECT_ID-vcm/
