from django.views import View
from .models import Tarea
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


class Tareavista(View):
    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self,request, id = 0):
        if (id > 0):
            works = list(Tarea.objects.filter(id=id).values())
            if len(works) > 0 :
                works = works[0]
                datos = {'message':"aprobado", 'tareas': works}
                return JsonResponse(datos)
            else: 
                 datos = {'message':"error",}
            return JsonResponse(datos)
        else:
            works = list(Tarea.objects.values())
            if len(works)>0 :
                datos = {'message':"ok", 'tareas': works}

            else:
                datos = {'message':"not found"}
            return JsonResponse(datos)
        pass    
    def put(self,request, id):
        jd = json.loads(request.body)
        works = list(Tarea.objects.filter(id=id).values())
        if len(works) > 0 :
            works = Tarea.objects.get(id=id)
            works.title = jd['title']
            works.description = jd['description']
            works.fechaDesde = jd['fechaDesde']
            works.fechaHasta = jd['fechaHasta']
            works.save()
            datos = {'message':"Se ha editado correctamente la tarea"}
            return JsonResponse(datos)
        else:
            datos = {'message':"No se han podido guardar los cambios"}
        return JsonResponse(datos)
        pass   
    def post(self,request):
        jd = json.loads(request.body)
        Tarea.objects.create(title=jd['title'], description=jd['description'], fechaDesde=jd['fechaDesde'], fechaHasta=jd['fechaHasta'] )
        datos = {'message':"Tarea creada con exito"}
        return JsonResponse(datos)
        pass   
    def delete(self,request,id):
        works = list(Tarea.objects.filter(id=id).values())
        if len(works) > 0:
            Tarea.objects.filter(id=id).delete()
            datos = {'message':"Tarea eliminada con exito"}

        else : 
            datos = {'message':"error en la eliminacion"}
        return JsonResponse(datos)
        pass  

    