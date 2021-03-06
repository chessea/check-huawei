import openpyxl

class ListaToExcel:
  
    @classmethod
    def datosToExcel(cls,lista):
        try:
            book =openpyxl.load_workbook('/home/Python/git-proyect/check-huawei/servicio/store/v5.xlsx')  
   
					
            sigla="SIGLA.CLIENTE"
            tipoEnlace='UNICO'
        
            sheet = book['encabezado']
            sheet['B3']=lista[1]
            sheet['B4']=lista[0]
            sheet['B14']=lista[2]
            sheet['B19']=lista[3]
            sheet['B20']=lista[4]
            sheet['B21']=lista[5]
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
            book.save(f'/home/Clientes/check_huawei/CHECKPROV_{sigla}_{lista[1]}_{lista[0]}_{tipoEnlace}.xlsx')
            print('FIN SH RUN') 
        except Exception as e:
            print('ERROR Al aguardar datos')               

