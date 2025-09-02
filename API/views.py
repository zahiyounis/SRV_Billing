from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions, mixins, authentication,status
from rest_framework.decorators import action


import environ
env = environ.Env()
environ.Env.read_env()


from .helpers import TranzilaAPI,GetTransactions,GetTransactionByID,GetInovation,GetInoviceDoc
# Create your views here.


class InvoicesViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
        permission_classes = [permissions.AllowAny]

        def list(self,request):
            Terminal = request.query_params.get("terminal","ultranet1a")
            print("valueee",Terminal)
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
    


        
        #@action(detail=False, methods=["get"], url_path="client-transactions")
        # def client_transactions(self, request, *args, **kwargs):
        #       res = GetTransactionByID("037404225","ultranet1atok")
        #       return Response(res,200)
            #return Response({"status": "ok", "hint": "POST to this endpoint with Tranzila payload to test."})
        # # create manual 
        # def create(self, request, *args, **kwargs):
        #     s = self.get_serializer(data=request.data)
        #     s.is_valid(raise_exception=True)
        #     payload = s.validated_data

        #     # Uncomment when ready to call Tranzila
        #     # resp = TranzilaTransactionAPI(payload)
        #     # return Response({"ok": True, "tranzila_response": resp}, status=status.HTTP_201_CREATED)

        #     return Response({"ok": True, "received": payload}, status=status.HTTP_201_CREATED)
   


      
