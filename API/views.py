from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions, mixins, authentication,status
from rest_framework.decorators import action
from datetime import date
from types import SimpleNamespace



import environ
env = environ.Env()
environ.Env.read_env()


from .helpers import TranzilaAPI,GetTransactions,GetTransactionByID,GetInovation,GetInoviceDoc,VerifyCreditCard
# Create your views here.


class InvoicesViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
        permission_classes = [permissions.AllowAny]

        def list(self,request):
            Terminal = request.query_params.get("terminal","ultranet1a")
            res = GetInoviceDoc(Terminal)
            return Response(res,200)
            

        def retrieve(self,request,pk=None):
             ClientID = pk
             Terminal = request.query_params.get("terminal","ultranet1atok")
             if not ClientID:
                  return Response({"details":"client id is required"},status=status.HTTP_400_BAD_REQUEST)
             
             res = GetInovation(ClientID,Terminal)
             return Response(res,200)
        





class ManualActionsViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
        permission_classes = [permissions.AllowAny]
        #serializer_class = TranzilaTestSerializer


 # GET /api/tranzila/action/
        def list(self, request, *args, **kwargs):
            res = GetTransactions("ultranet1atok")
            return Response(res,200)
        



        # GET /api/tranzila/action/<client_id>/
        def retrieve(self ,request,pk =None):
            ClientID = pk 
            terminal = request.query_params.get("terminal", "ultranet1atok") #if terminal n
            if not ClientID:
                return Response({"details":"client id is required"},status=status.HTTP_400_BAD_REQUEST)
            try:
                res = GetTransactionByID(ClientID, terminal)
                return Response(res,status=status.HTTP_200_OK)
            except Exception as e: 
                return Response({"details":str(e)},status=status.HTTP_502_BAD_GATEWAY)
    


class ClientBillingMethodViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
     permission_classes = [permissions.AllowAny]
     def create(self, request):
          dummy_client = SimpleNamespace(
                    FullName="John Doe",
                    IdNumber="123456789",
                    Email="john.doe@example.com"
                )
          Data = {
                "CardExpDate": date(2026, 12, 1),   # Exp: Dec 2026
                "CardCVV": "123",
                "CardNumber": "4111111111111111",   # Visa test number
                "IdNumber": "123456789",
                "Client": dummy_client
            }
          res = VerifyCreditCard(
            ExpDate=Data["CardExpDate"],
            CVV=Data["CardCVV"],
            CardNumber=Data["CardNumber"],
            ClientInstance=Data["Client"],
            IDNumber=Data["IdNumber"]
        )
          return Response(res)
                
     

