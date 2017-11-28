from django.shortcuts import render
from first_app.models import AccessRecord,Topic,Webpage

# Create your views here.
def index(request):
    Webpage_list = AccessRecord.objects.order_by('date')
    my_con = {'access_records':Webpage_list}
    return render(request,'first_app/index.html',context=my_con)
