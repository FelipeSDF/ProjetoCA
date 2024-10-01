from django.shortcuts import render
from  .models import Report
import PIL.Image
import os
from django.conf import settings

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PIL import Image
import os
from django.conf import settings
# Create your views here.

def add_report_to_database(**kargs):

    number = kargs['number']
    data = kargs['data']
    local = kargs['local']
    bairro = kargs['bairro']
    unidade = kargs['unidade']
    obs = kargs['obs']
    pavimentation = kargs['pavimentation']
    eletricity = kargs['eletricity']
    ilumination = kargs['ilumination']
    quantity_houses = kargs['quantity_houses']
    photos = kargs['photos']
    Reports = kargs['Reports']
    
    
    report = Report(number = number,
    data = data,
    local = local,
    bairro = bairro,
    unidade = unidade,
    obs = obs,
    pavimentation = pavimentation,
    eletricity = eletricity,
    ilumination = ilumination,
    quantity_houses = quantity_houses,
    photos = photos,
    Reports = Reports)
    report.save()
    

def reportpage(request):
    if request.method == 'GET':
        
        report_status='unposted'
        
        return render(request, 'reports/reportpage.html', {'status':report_status})
    
    elif request.method == 'POST':
        
        report_status='posted'
        
        Number = request.POST.get('Numero') 
        Data = request.POST.get('Date') 
        Local = request.POST.get('Local') 
        Bairro = request.POST.get('Bairro') 
        Unidade = request.POST.get('Unidade') 
        Obs = request.POST.get('Obs') 
        Pavimento = request.POST.get('Pavimento') 
        Eletricidade = request.POST.get('Eletricidade') 
        Iluminação = request.POST.get('Iluminação') 
        Casas = request.POST.get('Casas') 
        Fotos = request.FILES.get('Fotos')
        Files= request.FILES.getlist('Fotos')
        
        imagens = []
        
        pdf = canvas.Canvas(os.path.join(settings.BASE_DIR, f"media/report/documents/fotos_{Number}.pdf"), pagesize=A4)#f'{os.path.join(settings.BASE_DIR, 'media/Fotos.pdf')}', pagesize=A4,  )
        pag_width = A4[0]
        pag_height= A4[1]
        paths = []
        
        for file in Files:
            img = Image.open(file)
            path = os.path.join(settings.BASE_DIR, f'media/report/temp_images/{file}')
            paths.append(path)
            img = img.save(path)

            pdf.setPageRotation(90)
            pdf.drawImage(path, 0,0,pag_height,pag_width)
            pdf.showPage()
            imagens.append(path)
            
        pdf.save()
        
        data = '/'.join(list(reversed(Data.split('-')))) 
        
        
        Relatorio = f'''A Secretatia da Cidade Sustentável realizou vistoria no dia {data} no endereço {Local} no bairro {Bairro} com o intuito de analisar condições ambientais para emissão da certidão ambiental para fornecimento de energia elétrica!
        No decorrer da vistoria, observou-se que a propriedade se encontra em via {Pavimento}, {Eletricidade}, {Iluminação} e {Casas}'''
        
        if Unidade != '' and Obs == '':
            Relatorio = f'''A Secretatia da Cidade Sustentável realizou vistoria no dia {Data} no endereço {Local} no bairro {Bairro} com o intuito de analisar condições ambientais para emissão da certidão ambiental para fornecimento de energia elétrica!
            
            No decorrer da vistoria, observou-se que a propriedade se encontra próximo ao(a) {Unidade}, {Pavimento}, {Eletricidade}, {Iluminação} e {Casas}'''
         
        if Obs != '' and Unidade == '':
            Relatorio = f'''A Secretatia da Cidade Sustentável realizou vistoria no dia {Data} no endereço {Local} no bairro {Bairro} com o intuito de analisar condições ambientais para emissão da certidão ambiental para fornecimento de energia elétrica!
            
            No decorrer da vistoria, foi observado que {Obs}, se encontra em via {Pavimento}, {Eletricidade}, {Iluminação} e {Casas}'''
        
        if Obs != '' and Unidade != '':
            Relatorio = f'''A Secretatia da Cidade Sustentável realizou vistoria no dia {Data} no endereço {Local} no bairro {Bairro} com o intuito de analisar condições ambientais para emissão da certidão ambiental para fornecimento de energia elétrica!
            
            No decorrer da vistoria, foi observado que {Obs}, próximo ao (a) {Unidade}, {Pavimento}, {Eletricidade}, {Iluminação} e {Casas}'''
        
        context = {
        'Number':Number,
        'Data':Data,
        'Local':Local,
        'Bairro':Bairro,
        'Unidade':Unidade,
        'Obs':Obs,
        'Pavimento':Pavimento,
        'Eletricidade':Eletricidade,
        'Iluminação':Iluminação,
        'Casas':Casas,
        'Fotos':Fotos,
        'Relatorio':Relatorio,}
        
        
        add_report_to_database(
            number = Number,
            data = Data,
            local = Local,
            bairro = Bairro,
            unidade = Unidade,
            obs = Obs,
            pavimentation = Pavimento,
            eletricity = Eletricidade,
            ilumination = Iluminação,
            quantity_houses = Casas,
            photos = Fotos,
            Reports = Relatorio
         )
        
        return render(request, 'reports/reportpage.html', {'status':report_status, 'context': context})