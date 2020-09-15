from django.shortcuts import render, redirect

from . import models

def index(req):
    if req.POST:
        models.Task.objects.create(name=req.POST['name'])

    tasks = models.Task.objects.all()
    return render(req, 'hal1/index.html', {
        'data': tasks,
    })

def detail(req, id):
    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/detail.html', {
        'data': task,
    })

def delete(req, id):
    task = models.Task.objects.filter(pk=id).delete()
    return redirect('/')

def edit(req, id):
    if req.POST:
        task = models.Task.objects.filter(pk=id).update(name=req.POST['name'])
        return redirect('/')  

    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/edit.html', {
        'data': task,
    })

def buying(req):
    return render(req, 'hal2/buying.html')

def selling(req):
    return render(req, 'hal2/selling.html')

def customer(req):
    if req.POST:
        models.customer.objects.create(customername=req.POST['customername'], customeraddress=req.POST['customeraddress'], customercontact=req.POST['customercontact'])
    customers = models.customer.objects.all()
    return render(req, 'hal3customer/customer.html', {
        'data': customers,
    })

def customerdetail(req, id):
    customers = models.customer.objects.filter(pk=id).first()
    return render(req, 'hal3customer/customerdetail.html', {
        'data': customers,
    })

def customeredit(req, id):
    if req.POST:
        models.customer.objects.filter(pk=id).update(customername=req.POST['customername'], customeraddress=req.POST['customeraddress'], customercontact=req.POST['customercontact'])
        return redirect('/customer')  

    customers = models.customer.objects.filter(pk=id).first()
    return render(req, 'hal3customer/customeredit.html', {
        'data': customers,
    })

def customerdelete(req, id):
    customer = models.customer.objects.filter(pk=id).delete()
    return redirect('/customer')

def supplier(req):
    if req.POST:
        models.supplier.objects.create(suppliername=req.POST['suppliername'], supplieraddress=req.POST['supplieraddress'], suppliercontact=req.POST['suppliercontact'])
    suppliers = models.supplier.objects.all()
    return render(req, 'hal3supplier/supplier.html', {
        'data': suppliers,
    })

def supplierdetail(req, id):
    suppliers = models.supplier.objects.filter(pk=id).first()
    return render(req, 'hal3supplier/supplierdetail.html', {
        'data': suppliers,
    })

def supplieredit(req, id):
    if req.POST:
        models.supplier.objects.filter(pk=id).update(suppliername=req.POST['suppliername'], supplieraddress=req.POST['supplieraddress'], suppliercontact=req.POST['suppliercontact'])
        return redirect('/supplier')  

    suppliers = models.supplier.objects.filter(pk=id).first()
    return render(req, 'hal3supplier/supplieredit.html', {
        'data': suppliers,
    })

def supplierdelete(req, id):
    supplier = models.supplier.objects.filter(pk=id).delete()
    return redirect('/supplier')

def item(req):
    if req.POST:
        models.item.objects.create(itemname=req.POST['itemname'], itemprice=req.POST['itemprice'], itemsaleprice=req.POST['itemsaleprice'])
    items = models.item.objects.all()
    return render(req, 'hal3item/item.html', {
        'data': items,
    })    

def itemdetail(req, id):
    items = models.item.objects.filter(pk=id).first()
    return render(req, 'hal3item/itemdetail.html', {
        'data': items,
    })

def itemedit(req, id):
    if req.POST:
        models.item.objects.filter(pk=id).update(itemname=req.POST['itemname'], itemprice=req.POST['itemprice'], itemsaleprice=req.POST['itemsaleprice'])
        return redirect('/item')  

    items = models.item.objects.filter(pk=id).first()
    return render(req, 'hal3item/itemedit.html', {
        'data': items,
    })     

def itemdelete(req, id):
    items = models.item.objects.filter(pk=id).delete()
    return redirect('/item')

 