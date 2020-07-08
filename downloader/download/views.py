from django.shortcuts import render
from django.contrib import messages
from .forms import ImageCreateForm

def image_create(request):
    form = ImageCreateForm()

    if request.method == 'POST':
        form = ImageCreateForm(data = request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit = False)
            
            #assign current user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request,'Image added successfully')

            #redirect to new created item
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    
    return render(request,'create/create.html',{'section':'images','form':form})
