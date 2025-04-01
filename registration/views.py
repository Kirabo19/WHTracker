from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Vehicle
from django.db import IntegrityError

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})

def vehicle_create(request):
    if request.method == 'POST':
        voucher_no = request.POST.get('voucher_no')
        registration_plate = request.POST.get('registration_plate')
        contact_no = request.POST.get('contact_no')
        
        # Ensure all fields are provided
        if not voucher_no or not registration_plate or not contact_no:
            return JsonResponse({'error': 'All fields are required!'}, status=400)
        
        try:
            vehicle = Vehicle.objects.create(
                voucher_no=voucher_no,
                registration_plate=registration_plate,
                contact_no=contact_no
            )
            return JsonResponse({'message': 'Vehicle added successfully!'}, status=201)

        except IntegrityError:
            return JsonResponse({'error': 'Registration plate already exists!'}, status=400)
       
    return JsonResponse({'error': 'Invalid request'}, status=400)

def vehicle_update(request, pk):
    if request.method == 'POST':
        vehicle = get_object_or_404(Vehicle, pk=pk)
        vehicle.voucher_no = request.POST.get('voucher_no')
        vehicle.registration_plate = request.POST.get('registration_plate')
        vehicle.contact_no = request.POST.get('contact_no')
        
        try:    
            vehicle.save()
            return JsonResponse({'message': 'Vehicle updated successfully!'}, status=200)
        except IntegrityError:
            return JsonResponse({'error': 'Registration plate already exists!'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def vehicle_delete(request, pk):
    if request.method == 'POST':
        try:
            vehicle = get_object_or_404(Vehicle, pk=pk)
            vehicle.delete()
            return JsonResponse({'message': 'Vehicle deleted successfully!'}, status=200)
        except Exception as e:
            return JsonResponse({'error': 'Failed to delete vehicle!'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)
