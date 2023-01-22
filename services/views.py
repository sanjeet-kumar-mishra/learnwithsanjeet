from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests
from pymongo import MongoClient
import pandas as pd

# Creating Client
client = MongoClient("mongodb+srv://sanjityaya:Sanjeet111@cluster0.gbw3x.mongodb.net/?retryWrites=true&w=majority")

def home(request):
    return render(request, 'Home.html')

def ActiveDataEntry(request):
    db = client["EmployeeData"]
    collection = db["ActiveEmployees"]
    data_count = collection.count_documents({})

    if request.method == "POST" and request.FILES['activeEmployees']:
        activeEmployee = request.FILES['activeEmployees']
        excel_data = pd.read_excel(activeEmployee)
        postable_data = excel_data.to_dict('records')

        collection.insert_many(postable_data)

        data_count = collection.count_documents({})

        return render(request, 'ActiveDataEntry.html', {"data_count" : data_count})
    else:
        return render(request, 'ActiveDataEntry.html', {"data_count" : data_count})

def DeleteEntry(request):
    db = client["EmployeeData"]
    collection = db["ActiveEmployees"]
    collection.delete_many({})

    return HttpResponseRedirect(reverse('activedataentry'))

def EmployeeDetails(request):
    db = client["EmployeeData"]
    collection = db["ActiveEmployees"]

    if request.method == "POST":
        checkresult = request.POST["searchemployee"]
        cardno = collection.find({"CARDNO": int(checkresult)})
        empcode = collection.find({"Emp_Code": int(checkresult)})
        esicno = collection.find({"ESINO": int(checkresult)})
        uanno = collection.find({"PF_UAN_NO": int(checkresult)})
        return render(request, 'EmployeeDetails.html', {
            "cardno": cardno,
            "empcode": empcode,
            "esicno": esicno,
            "uanno": uanno,
        })
    else:
        return render(request,'EmployeeDetails.html')

