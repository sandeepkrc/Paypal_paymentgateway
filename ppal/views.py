from django.shortcuts import render
from .models import Product,Order
from django.http import JsonResponse


def store(request):
	products = Product.objects.all()

	context = {'products':products}
	return render(request,'store.html',context)



def checkout(request,pk):
	product = Product.objects.get(id=pk)
	context = {'product':product}
	return render(request,'checkout.html',context)



# def paymentcomplete(request):
# 	body = json.loads(request.body)
# 	product = Product.objects.get(id=body['productid'])
# 	order.objects.create(
# 		product = product
# 		)
# 	print('BODUY',body)
# 	return JsonResponse('Payment completed!',safe=True)

def paymentcomplete(request):
	return render(request,'suc.html')