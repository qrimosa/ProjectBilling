from django.shortcuts import render 
from .models import Tenant
# Create your views here.
def tenant_view(request):
    if request.method == 'POST':
        # print(request.POST)
        mall = request.POST.get('mall')
        contract_num = request.POST.get('contract_num')
        contract_start = request.POST.get('contract_start')
        contract_end = request.POST.get('contract_end')
        contract_date = request.POST.get('contract_date')
        landlord = request.POST.get('landlord')
        tenant = request.POST.get('tenant')
        landlord_r_s = request.POST.get('landlord_r_s')
        type_of_contract = request.POST.get('type_of_contract')
        tax = request.POST.get('tax')
        work = request.POST.get('work')
        close = request.POST.get('close')
        commentary = request.POST.get('commentary')
        contract_num_bill = request.POST.get('contract_num_bill')
        main_contract = request.POST.get('main_contract')
        main_lot = request.POST.get('main_lot')
        Tenant.objects.create(complex = mall, number_contract=contract_num, 
                              end_contract=contract_end, start_contract = contract_start,
                                date_contract = contract_date, tenant_name=landlord, owner_name = tenant,
                                tenant_r_s=landlord_r_s, type_of_contract=type_of_contract, tax_on_ad=tax, in_work=work, close=close, 
                                comment= commentary, number_contract_in_check=contract_num_bill, main_contract = main_contract, main_lot = main_lot)
    return render(request, 'new_tenant/tenant.html')