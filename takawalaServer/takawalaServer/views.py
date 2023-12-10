from django.http import HttpResponse,JsonResponse
from .models import LoanApplication
from .serializers import LoanApplicationSerializers
def home(request):
    return HttpResponse("Hi, welcome to talawala API v1.0")

def application_list(request):
    
    # get all application
    # serialize them 
    # return json 
    laonaAplications = LoanApplication.objects.all()
    serializer = LoanApplicationSerializers(laonaAplications, many=True)
    return JsonResponse({ 'application' : serializer.data}, safe=False)

def about(request):
    return HttpResponse("He there this is my about page")

def contact(request):
    return HttpResponse("He there this is my contact page")

def help(request):
    return HttpResponse("He there this is my help page")