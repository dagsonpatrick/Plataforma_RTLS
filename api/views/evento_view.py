from rest_framework.views import APIView
from ..services import evento_service
from ..serializers import evento_serializer
from ..serializers import info_evento_serializer
from ..serializers import info_planta_serializer
from rest_framework.response import Response
from rest_framework import status as ev
from ..entidades import evento
from monitor.services import monitor_service


class EventoList(APIView):

    def get(self, request, format=None):
        info_planta = monitor_service.create_info_planta()
        serializer = info_planta_serializer.PlantaInfoSerializer(info_planta, many=True)
        return Response(serializer.data, status=ev.HTTP_200_OK)

    '''def get(self, request, format=None):
        eventos = evento_service.listar_eventos()
        serializer = evento_serializer.EventoSerializer(eventos, many=True)
        return Response(serializer.data, status = ev.HTTP_200_OK )'''

    def post(self, request, format=None):
        serializer = evento_serializer.EventoSerializer(data=request.data)
        if serializer.is_valid():
            idanchor = serializer.validated_data["idanchor"]
            idtag =  serializer.validated_data["idtag"]
            dtInicio =  serializer.validated_data["dtInicio"]
            dtFim =  serializer.validated_data["dtFim"]
            permanencia =  serializer.validated_data["permanencia"]
            status =  serializer.validated_data["status"]
            evento_novo = evento.Evento(idanchor = idanchor,
                                        idtag =  idtag,
                                        dtInicio =  dtInicio,
                                        dtFim =  dtFim,
                                        permanencia =  permanencia,
                                        status=status)
            evento_bd =  evento_service.cadastrar_evento(evento_novo)
            return Response(serializer.data, status=ev.HTTP_201_CREATED)
        return Response(serializer.errors, status=ev.HTTP_400_BAD_REQUEST)

class EventoDetalhes(APIView):

    def get(self, request, id, format=None):
        planoSelecionado = monitor_service.listar_plano_id(id)
        anchorsPlano = monitor_service.buscar_anchors_plano(planoSelecionado)
        eventos = monitor_service.buscar_evento_anchors(anchorsPlano)
        info_eventos = monitor_service.create_info_evento(eventos)
        serializer = info_evento_serializer.EventoInfoSerializer(info_eventos, many=True)
        #serializer = evento_serializer.EventoSerializer(eventos, many=True)
        return Response(serializer.data, status=ev.HTTP_200_OK)

    '''def get(self, request, id, format=None):
        evento = evento_service.listar_evento_id(id)
        serializer = evento_serializer.EventoSerializer(evento)
        return Response(serializer.data, status=ev.HTTP_200_OK)'''

    def put(self, request, id, format=None):
        evento_antigo = evento_service.listar_evento_id(id)
        serializer = evento_serializer.EventoSerializer(evento_antigo, data=request.data)
        if serializer.is_valid():
            idanchor = serializer.validated_data["idanchor"]
            idtag = serializer.validated_data["idtag"]
            dtInicio = serializer.validated_data["dtInicio"]
            dtFim = serializer.validated_data["dtFim"]
            permanencia = serializer.validated_data["permanencia"]
            status = serializer.validated_data["status"]
            evento_novo = evento.Evento(idanchor=idanchor,
                                        idtag=idtag,
                                        dtInicio=dtInicio,
                                        dtFim=dtFim,
                                        permanencia=permanencia,
                                        status=status)
            evento_service.editar_evento(evento_antigo, evento_novo)
            return Response(serializer.data, status=ev.HTTP_200_OK)
        return Response(serializer.errors, status=ev.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        evento = evento_service.listar_evento_id(id)
        evento_service.remover_evento(evento)
        return Response(ev.HTTP_204_NO_CONTENT)




