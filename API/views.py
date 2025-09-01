from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions, mixins, authentication,status


import environ
env = environ.Env()
environ.Env.read_env()


from .helpers import TranzilaTransactionAPI,GetTransactions
# Create your views here.


class ManualActionsViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
        permission_classes = [permissions.AllowAny]
        #serializer_class = TranzilaTestSerializer


 # GET /api/tranzila/action/
        def list(self, request, *args, **kwargs):

            res = GetTransactions("ultranet1atok")
            return Response(res,200)
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
   


      
