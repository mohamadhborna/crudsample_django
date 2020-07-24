from rest_framework.response import Response

# Create your views here.
from rest_framework.viewsets import ViewSet


#
# def retrieve(self,*args,**kwargs):
#     class CompanyView(ViewSet):
#         pass
class CompaniesView(ViewSet):
    def retrieve(self, *args, **kwargs):
        print("args", args)
        print("kwargs", kwargs)
        return Response(403)
    def getById(self,*args,**kwargs):
        company_pk = 
