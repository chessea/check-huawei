import openpyxl

class ListaToExcel:
  
    @classmethod
    def datosToExcel(cls,lista):
        book =openpyxl.load_workbook('/home/Python/git-proyect/check-huawei/servicio/store/v5.xlsx')  
        try:
            ott=lista[1]
            cs=lista[0]
            hostname=lista[2]
            marca=lista[3]
            modelo=lista[4]
            versionSNMP=lista[5]
					
            sigla="SIGLA.CLIENTE"
            tipoEnlace='UNICO'
            if ott == None:
                ott="sin datos"
                
            if cs == None:
                cs="sin datos"
            if hostname == None:
                hostname="sin datos"
            if marca == None:
                marca="sin datos"
            if modelo == None:
                modelo="sin datos"            
            if versionSNMP == None:
                versionSNMP="sin datos"            
            sheet = book['encabezado']
            sheet['B3']=ott
            sheet['B4']=cs
            sheet['B14']=hostname
            sheet['B19']=marca
            sheet['B20']=modelo
            sheet['B21']=versionSNMP
            sheet['B25']=lista[9]       
            print('FIN ENCABEZADO')
            
            

            x= range(0,len(lista[8]))
            contador=3
            for todos in x:
                contador=contador+1
                sheet2 = book['interfaces']
                sheet2[f'A{contador}']=lista[8][todos]
            print('FIN BRIEF') 


            y= range(0,len(lista[7]))
	  	
            contador=3
            for todos2 in y:
                contador=contador+1
                sheet3 = book['configuracion']
                sheet3[f'D{contador}']=lista[7][todos2]
            print('FIN VERSION')   

            
            x= range(0,len(lista[6]))
            contador=3
            for todos3 in x:
                contador=contador+1
                sheet3[f'A{contador}']=lista[6][todos3]
            print('FIN SH RUN') 
        except Exception as e:
            print('ERROR Al aguardar datos')               
        book.save(f'/home/Clientes/check_huawei/CHECKPROV_{sigla}_{ott}_{cs}_{tipoEnlace}.xlsx')
