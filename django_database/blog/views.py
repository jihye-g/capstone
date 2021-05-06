from django.shortcuts import render, get_object_or_404
from .models import Medicine

def MedicineListView(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine_list.html', {'medicines': medicines})

def MedicineDeatilView(request, code):
    medicine = get_object_or_404(Medicine, code=code)
    return render(request, 'medicine_detail.html', {'medicine': medicine})