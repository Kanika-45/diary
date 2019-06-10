from django.shortcuts import render
from .models import Log
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

# Create your views here.
def log_list(request):
    logs = Log.objects.all()
    return render(request, 'diary/log_list.html',{'logs':logs})


def log_detail(request, primary_key):
   # log = get_object_or_404(Log, pk=pk)
   try:
       log = Log.objects.get(pk=primary_key)
   except Log.DoesNotExist:
       raise Http404
   return render(request, 'diary/log_detail.html', {'log': log})

def log_new(request):
    form = PostForm()
    return render(request, 'diary/log_new.html',{'form': form})
