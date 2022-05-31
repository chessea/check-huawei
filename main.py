import time
import asyncio
from servicio.netmiko.comando import Comando
from servicio.filtro.funcionesFiltro import  FuncionesFiltro
from servicio.toExcel.listaToExcel import ListaToExcel
import openpyxl
from bullet import VerticalPrompt, Input, Password

print("Inicio")
cli= VerticalPrompt([
    Input(prompt="Ingrese usuario: "),
    Password(prompt="Ingrese password : ", hidden="*")],spacing=0)
result=cli.launch()

usuario=result[0][1]
password=result[1][1] 

with open("/home/Python/git-proyect/check-huawei/servicio/store/listado.txt", "r") as datos:
    lista = [linea.rstrip() for linea in datos] 
    

book =openpyxl.load_workbook('/home/Python/git-proyect/check-huawei/servicio/store/v5.xlsx')  
sigla="SIGLA.CLIENTE"
tipoEnlace='UNICO'
sheet = book['encabezado']
for ip in lista:
    try:     
        listaComandos=['dis cur', 
                       'dis ip int brief',
                       'dis version', 
                       'dis version', 
                       'dis cur | i sysname',
                       'dis snmp-agent sys-info version']

        comandos=asyncio.run(Comando.enviarComando(listaComandos,ip,usuario,password))
        disCur, brief, disVer, disVer2 ,disRunHost, snmpcomando = comandos

        cs=asyncio.run(FuncionesFiltro.filtroCodigo(disCur))
        ott=asyncio.run(FuncionesFiltro.filtroOTT(disCur))
        marca=asyncio.run(FuncionesFiltro.filtroMarca(disVer2))
        model=asyncio.run(FuncionesFiltro.filtroModel(disVer2))
        hostname=asyncio.run(FuncionesFiltro.filtroHostname(disRunHost))
        snmpVersion=asyncio.run(FuncionesFiltro.filtroSnmpVersion(snmpcomando))


    
        sheet['B3']=ott
        sheet['B4']=cs
        sheet['B14']=hostname
        sheet['B19']=marca
        sheet['B20']=model
        sheet['B21']=snmpVersion
        sheet['B25']=ip

        x= range(0,len(brief))
        contador=3
        for todos in x:
            contador=contador+1
            sheet2 = book['interfaces']
            sheet2[f'A{contador}']=brief[todos]
        print('FIN BRIEF')  
        y= range(0,len(disVer))
        contador=3
        for todos2 in y:
            contador=contador+1
            sheet3 = book['configuracion']
            sheet3[f'D{contador}']=disVer[todos2]
        print('FIN VERSION')    
        x= range(0,len(disCur))
        contador=3
        for todos3 in x:
            contador=contador+1
            sheet3[f'A{contador}']=disCur[todos3]
        book.save(f'/home/Clientes/check_huawei/CHECKPROV_{sigla}_{ott}_{cs}_{tipoEnlace}.xlsx')
        print('FIN SH RUN') 
    except Exception as e:
        print('ERROR')    
     
