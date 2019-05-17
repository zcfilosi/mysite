from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from .models import todoItem
from .serializers import todoItemSerializer
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

# Create your views here.


def homeView(request):
    return HttpResponse("hello")

# DONE
def todoView(request, par_id = 0):
    #check and see if base object exists, this will not be displayed, but serve as the parent object of all
    if( not todoItem.objects.filter(id = 0).exists()):
        c = todoItem(id = 0, content = '', parent_id = None, description='' )
        c.save()
        parent_item = c
    else:
        parent_item = todoItem.objects.get(id = par_id)

    if par_id is None:
        all_todo_items = list(todoItem.objects.filter(parent_id = parent_item))
        return render(request, 'baselist.html',
        {'all_items': all_todo_items, 'parent_id' : 0}
        )
    else:
        all_todo_items = list(todoItem.objects.filter(parent_id = parent_item))
        return render(request, 'baselist.html',
        {'all_items': all_todo_items, 'parent_id' : par_id}
        )
# need to implement new parent
def addTodoView(request):
    parObj = todoItem.objects.get(id = request.POST['parent_id'])
    new_item = todoItem(content = request.POST['content'], parent_id = parObj, description = request.POST['description'])
    new_item.save()
    return HttpResponseRedirect('/todo/'+ request.POST['parent_id'])

# need to implement new parent
def removeTodoView(request, todo_id):
    deleteItem = todoItem.objects.get(id = todo_id)
    delItemParentId = deleteItem.parent_id.id
    delItemId = deleteItem.id
    deleteItem.delete()
    # cascadeDelete(delItemId) # commented out for now
    return HttpResponseRedirect('/todo/'+ str(delItemParentId))

#@csrf_exempt
def get_data(request, par_id = 0):
    data = None
    baseItem = True

    if( not todoItem.objects.filter(id = 0).exists()):
        c = todoItem(id = 0, content = '', parent_id = None, description='' )
        c.save()
        parent_item = c
    else:
        parent_item = todoItem.objects.get(id = par_id)


    if par_id is None:
        data = list(todoItem.objects.filter(parent_id = parent_item))

    else:
        data = list(todoItem.objects.filter(parent_id = parent_item))
        baseItem = False

    if request.method == 'GET':
        all_items = serializers.serialize('json', data)
        serializer = {
            "data": all_items,
            "par_id": str(parent_item)
        }
        return JsonResponse(serializer, safe=False)
#delete when done with new parent, as cascade delete handled by db
# def cascadeDelete(parent_id):
#     child_list = list(todoItem.objects.filter(parent_id = parent_id))
#     if not child_list:
#         return None
#     else:
#         for item in child_list:
#             this_id = item.id
#             item.delete()
#             cascadeDelete(this_id)
