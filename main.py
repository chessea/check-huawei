import time
import asyncio
from servicio.netmiko.comando import Comando
from servicio.filtro.funcionesFiltro import  FuncionesFiltro
from servicio.toExcel.listaToExcel import ListaToExcel

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
    
listaDatos= [] 
for ip in lista:
        
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
    snmpVersion=asyncio(FuncionesFiltro.filtroSnmpVersion(snmpcomando))
    
    
    listaDatos.append(cs)
    listaDatos.append(ott)
    listaDatos.append(hostname)
    listaDatos.append(marca)
    listaDatos.append(model)
    listaDatos.append(snmpVersion)
    listaDatos.append(disCur)
    listaDatos.append(disVer)
    listaDatos.append(brief)
    listaDatos.append(ip) 

    time.sleep(1)
    ListaToExcel.datosToExcel(listaDatos)
