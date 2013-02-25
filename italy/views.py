from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from italy.models import Regioni, Provincie, Comuni

def index(request):
    regioni_list = Regioni.objects.all().order_by('name')
    return render_to_response('italy/index.html', {'regioni_list': regioni_list})
    
def detail_regione(request,regione_name):
    regione=  Regioni.objects.all().filter(slug=regione_name).values('codice_regione_istat')
    regione_istat= regione[0]['codice_regione_istat']
    prov_list= Provincie.objects.all().order_by('name').filter(codice_regione_istat=regione_istat)
    return render_to_response('italy/detail_regione.html', {'prov_list': prov_list})



