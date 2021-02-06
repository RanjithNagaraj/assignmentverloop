from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import geocoder
import xml.etree.ElementTree as et




KEY = "q60JQBb4IN6OmIhJxArpp8lz2oyVY0Z7"
# Create your views here.
@csrf_exempt
def latnlng(request):
    global KEY
    if request.method == 'POST':
        try:
            address = request.POST['address']
            output_format = request.POST['output_format']                                    
            if(len(address)>0):               
                g = geocoder.mapquest(address, key=KEY)              
                if(output_format.lower() == 'xml'):                                           
                    root = et.Element("root")
                    addrs = et.SubElement(root, "address")
                    addrs.text = address  
                    coordinates = et.SubElement(root,"coordinates")
                    lat = et.SubElement(coordinates,"lat")
                    lat.text = str(g.lat)
                    lng = et.SubElement(coordinates,"lng")
                    lng.text = str(g.lng)
                    return HttpResponse(et.tostring(root), content_type='application/xml')                
                elif(output_format.lower() == 'json'):                    
                    data = {"coordinates": {"lat":g.lat,"lng":g.lng},"address": address}
                    return JsonResponse(data) 
        except Exception as e:
            return JsonResponse({"Exception": str(type(e))})                                      
        return JsonResponse({"Exception": "Exception in reading inputs"})
    else:
        return HttpResponse("<h1>Other methods are not supported</h1>") 



#Reverse geocoding
@csrf_exempt
def reverse(request):
    global KEY
    if request.method == 'POST':
        lat = request.POST['lat']
        lng = request.POST['lng']
        g = geocoder.mapquest([12.97912, 77.5913], method='reverse', key=KEY)        
        return JsonResponse({"address":g.address,"city":g.city,"country":g.country,"lat":g.lat,"lng":g.lng})
    else:
        return HttpResponse("<h1>Other methods are not supported</h1>") 


