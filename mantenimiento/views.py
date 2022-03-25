from rest_framework import viewsets
from mantenimiento.models import Notificacion, ParteTrabajo, Tarea, Especialidad, TipoPeriodo, TipoTarea, LineaParteTrabajo, EstadoLineasTareas
from mantenimiento.serializers import NotificacionSerializer, TareaSerializer, EspecialidadSerializer, TipoTareaSerializer, TipoPeriodoSerializer, TareaNuevaSerializer, ParteTrabajoSerializer, ParteTrabajoDetalleSerializer, LineaParteTrabajoSerializer, LineaParteTrabajoNuevaSerializer, LineaParteTrabajoMovSerializer, ListadoLineasPartesSerializer, EstadoLineasTareasSerializer
from django_filters import rest_framework as filters
from django.db.models import Count, F, Value

class NotificacionFilter(filters.FilterSet):
    class Meta:
        model = Notificacion
        fields = {
            'empresa': ['exact'],
            'que': ['icontains'],
            'revisado': ['exact'],
            'descartado': ['exact'],
            'finalizado': ['exact'],
            
        }
class TareaFilter(filters.FilterSet):
    class Meta:
        model = Tarea
        fields = {
            'nombre': ['icontains'],
            'especialidad': ['exact'],
            'prioridad': ['lte', 'gte'],            
        }

class LineasFilter(filters.FilterSet):
    class Meta:
        model = LineaParteTrabajo
        fields = {
            'parte': ['exact'],
            'tarea': ['exact'],            
            'tarea__nombre': ['icontains'],
            'tarea__especialidad': ['exact'],
            'tarea__prioridad': ['lte', 'gte'],
            'parte__tipo': ['exact'],
            'parte__empresa__id' : ['exact'],
            'parte__zona__id': ['exact'],
            'parte__seccion__id': ['exact'],
            'parte__equipo__id': ['exact'],
            'parte__nombre': ['icontains'],
            'fecha_inicio': ['lte', 'gte'],
            'fecha_fin': ['lte', 'gte'],
            'fecha_plan': ['lte', 'gte'],
            'estado': ['exact'],

        }

class EspecialidadFilter(filters.FilterSet):
    class Meta:
        model = Especialidad
        fields = {
            'nombre': ['icontains'],
        }

class PartesFilter(filters.FilterSet):
    class Meta:
        model = ParteTrabajo
        fields = {
            'nombre': ['icontains'],
            'tipo': ['exact'],
            'creado_por':['exact'],
            'observaciones': ['icontains'],
            'finalizado': ['exact'],
            'empresa__id' : ['exact'],
            'zona__id': ['exact'],
            'seccion__id': ['exact'],
            'equipo__id': ['exact'],
            'fecha_prevista_inicio': ['lte', 'gte'],
        }

class EstadoLineasTareasFilter(filters.FilterSet):
    class Meta:
        model = EstadoLineasTareas
        fields = {
            'nombre': ['exact'],
        }

class NotificacionViewSet(viewsets.ModelViewSet):
    serializer_class = NotificacionSerializer
    queryset = Notificacion.objects.all()
    filterset_class = NotificacionFilter

class EspecialidadViewSet(viewsets.ModelViewSet):
    serializer_class = EspecialidadSerializer
    queryset = Especialidad.objects.all()
    filterset_class = EspecialidadFilter

class EstadoLineasTareasViewSet(viewsets.ModelViewSet):
    serializer_class = EstadoLineasTareasSerializer
    queryset = EstadoLineasTareas.objects.all()
    filterset_class = EstadoLineasTareasFilter

class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all().distinct()
    filterset_class = TareaFilter

class TareaNuevaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaNuevaSerializer
    queryset = Tarea.objects.all()
    filterset_class = TareaFilter

class TipoTareaViewSet(viewsets.ModelViewSet):
    serializer_class = TipoTareaSerializer
    queryset = TipoTarea.objects.all()

class TipoPeriodoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoPeriodoSerializer
    queryset = TipoPeriodo.objects.all()

class LineaParteTrabajoViewSet(viewsets.ModelViewSet):
    serializer_class = LineaParteTrabajoSerializer
    queryset = LineaParteTrabajo.objects.all()
    filterset_class = LineasFilter

class LineaParteTrabajoMovViewSet(viewsets.ModelViewSet):
    serializer_class = LineaParteTrabajoMovSerializer
    queryset = LineaParteTrabajo.objects.all()
    filterset_class = LineasFilter

class LineaParteTrabajoNuevaViewSet(viewsets.ModelViewSet):
    serializer_class = LineaParteTrabajoNuevaSerializer
    queryset = LineaParteTrabajo.objects.all()
    filterset_class = LineasFilter

class ListadoLineaParteViewSet(viewsets.ModelViewSet):
    serializer_class = ListadoLineasPartesSerializer
    queryset = LineaParteTrabajo.objects.all()
    filterset_class = LineasFilter

class ParteTrabajoViewSet(viewsets.ModelViewSet):
    serializer_class = ParteTrabajoSerializer
    #queryset = ParteTrabajo.objects.filter(tareas__gt=0)
    queryset = ParteTrabajo.objects.all()
    filterset_class = PartesFilter

class ParteTrabajoDetalleViewSet(viewsets.ModelViewSet):
    serializer_class = ParteTrabajoDetalleSerializer
    queryset = ParteTrabajo.objects.all()
    filterset_class = PartesFilter