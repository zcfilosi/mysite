from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import todoItem
# Create your views here.



def todoView(request, par_id = None):
    if par_id is None:
        all_todo_items = list(todoItem.objects.filter(parent_id = 0))
        return render(request, 'baselist.html',
        {'all_items': all_todo_items, 'parent_id' : 0}
        )
    else:
        all_todo_items = list(todoItem.objects.filter(parent_id = par_id))
        return render(request, 'baselist.html',
        {'all_items': all_todo_items, 'parent_id' : par_id}
        )

def addTodoView(request):
    new_item = todoItem(content = request.POST['content'], parent_id = request.POST['parent_id'], description = request.POST['description'])
    new_item.save()
    return HttpResponseRedirect('/todo/'+ request.POST['parent_id'])

def removeTodoView(request, todo_id):
    deleteItem = todoItem.objects.get(id = todo_id)
    delItemParentId = deleteItem.parent_id
    delItemId = deleteItem.id
    deleteItem.delete()
    cascadeDelete(delItemId)
    return HttpResponseRedirect('/todo/'+ str(delItemParentId))


def cascadeDelete(parent_id):
    child_list = list(todoItem.objects.filter(parent_id = parent_id))
    if not child_list:
        return None
    else:
        for item in child_list:
            this_id = item.id
            item.delete()
            cascadeDelete(this_id)
