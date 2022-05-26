import openpyxl

class ListaToExcel:
  
    @classmethod
    def datosToExcel(cls,lista):
        try:
            book =openpyxl.load_workbook('/home/fr/Documentos/huawei-check/servicio/store/v5.xlsx')
            
            ott=lista[0]
            cs=lista[1]
            hostname=lista[2]
            marca=lista[3]
            modelo=lista[4]
            versionSNMP=lista[5]
            sigla="SIGLA.CLIENTE"
            tipoEnlace='UNICO'
            
            sheet = book['encabezado']
            sheet['B3']=ott
            sheet['B4']=cs
            sheet['B14']=hostname
            sheet['B19']=marca
            sheet['B20']=modelo
            sheet['B19']=versionSNMP
       
            print('FIN ENCABEZADO')
            
            


            x= range(0,len(lista[6]))
            contador=3
            for todos in x:
                contador=contador+1
                sheet2 = book['interfaces']
                sheet2[f'A{contador}']=lista[7][todos]
            print('FIN BRIEF') 


            y= range(0,len(lista[7]))
            contador=3
            for todos2 in y:
                contador=contador+1
                sheet3 = book['configuracion']
                sheet3[f'I{contador}']=lista[8][todos2]
            print('FIN VERSION')   


            x= range(0,len(lista[8]))
            contador=3
            for todos3 in x:
                contador=contador+1
                sheet3[f'A{contador}']=lista[8][todos3]
            book.save(f'/home/fr/Documentos/huawei-check/servicio/store/CHECKPROV_{sigla}_{ott}_{cs}_{tipoEnlace}.xlsx')
            print('FIN SH RUN') 
        except Exception as e:
            print('ERROR Al aguardar datos')               