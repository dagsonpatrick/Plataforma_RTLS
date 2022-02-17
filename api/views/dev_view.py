from rest_framework.decorators import api_view
from rest_framework.views import APIView
from ..services import dev_service
from ..serializers import dev_serializer
from rest_framework.response import Response
from rest_framework import status
from ..entidades import dev
from ..entidades.event_dev_aws import EventDevAws


class DevList(APIView):

    def get(self, request, format=None):
        devs = dev_service.listar_devs()
        serializer = dev_serializer.DevSerializer(devs, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK )

    def post(self, request, format=None):
        serializer = dev_serializer.DevSerializer(data=request.data)
        if serializer.is_valid():
            address = serializer.validated_data["address"]
            place_id = serializer.validated_data["place_id"]
            place_name= serializer.validated_data["place_name"]
            utcdate = serializer.validated_data["utcdate"]
            connector_utcdate = serializer.validated_data["connector_utcdate"]
            dev_novo = dev.Dev(address=address,
                               place_id=place_id,
                               place_name=place_name,
                               utcdate=utcdate,
                               connector_utcdate=connector_utcdate)

            dev_bd = dev_service.cadastrar_dev(dev_novo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DevDetalhes(APIView):

    def get(self, request, id, format=None):
        dev = dev_service.listar_dev_id(id)
        serializer = dev_serializer.DevSerializer(dev)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        dev_antigo = dev_service.listar_dev_id(id)
        serializer = dev_serializer.DevSerializer(dev_antigo, data=request.data)
        if serializer.is_valid():
            address  = serializer.validated_data["address"]
            place_id= serializer.validated_data["place_id"]
            place_name  = serializer.validated_data["place_name"]
            utcdate = serializer.validated_data["utcdate"]
            connector_utcdate = serializer.validated_data["connector_utcdate"]

            dev_novo = dev.Dev(address=address,
                               place_id=place_id,
                               place_name =place_name,
                               utcdate=utcdate,
                               connector_utcdate=connector_utcdate)

            dev_service.editar_dev(dev_antigo, dev_novo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        dev = dev_service.listar_dev_id(id)
        dev_service.remover_dev(dev)
        return Response(status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        serializer = dev_serializer.DevSerializer(data=request.data)
        if serializer.is_valid():

            name = serializer.validated_data["name"]
            place_name = serializer.validated_data["place_name"]
            distance = serializer.validated_data["distance"]
            last_seen = serializer.validated_data["last_seen"]
            utcdate = serializer.validated_data["utcdate"]

            dev_novo = EventDevAws(name=name,
                                   place_name=place_name,
                                   distance=distance,
                                   last_seen=last_seen,
                                   utcdate=utcdate)

            dev_service.verifique_dado(dev_novo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, format=None):
        #serializer = dev_serializer.DevSerializer(data=request.data)
        #if serializer.is_valid():
            #address = serializer.validated_data["address"]
            #place_id = serializer.validated_data["place_id"]
            #place_name = serializer.validated_data["place_name"]
            #utcdate = serializer.validated_data["utcdate"]
            #connector_utcdate = serializer.validated_data["connector_utcdate"]
            #dev_novo = dev.Dev(address=address,
                               #place_id=place_id,
                               #place_name=place_name,
                               #utcdate=utcdate,
                               #connector_utcdate=connector_utcdate)
            #dev_service.verifique_dado(dev_novo)
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)''''''
