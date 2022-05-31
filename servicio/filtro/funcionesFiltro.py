import asyncio


class FuncionesFiltro:
   
    @classmethod    
    def filtroCodigo(cls,comandoShRun):
        busquedaCS =  ["10000","100000","7880","7879","66678"]
        for litadoBusqueda in busquedaCS:
            filtroCS = [s for s in comandoShRun if litadoBusqueda in s]

            if len(filtroCS)>0:
                filtroListaCS=filtroCS[0].split(' ')
                filtroCS = [s for s in filtroListaCS if litadoBusqueda in s]
                if len(filtroCS)<10:
                    filtroListaCS=filtroCS[0].split(':')
                    filtroCS = [s for s in filtroListaCS if litadoBusqueda in s]  
                if len(filtroCS)<10:
                    filtroListaCS=filtroCS[0].split('_')
                    filtroCS = [s for s in filtroListaCS if litadoBusqueda in s] 
                else:
                    datos=filtroCS
                    return datos
                return  filtroCS[0]

            
    @classmethod
    def filtroOTT(cls,comandoShRun):

        busquedaOTT = ["71701","712008","7200","7210","7180","7190", "7170", "7160" ,"7150"]
        for litadoBusqueda in busquedaOTT:
            filtroOTT = [s for s in comandoShRun if litadoBusqueda in s]

            if len(filtroOTT)>0:
                filtroListaOTT=filtroOTT[0].split(' ')
                filtroOTT = [s for s in filtroListaOTT if litadoBusqueda in s]
                if len(filtroOTT)<10:
                    filtroListaOTT=filtroOTT[0].split(':')
                    filtroOTT = [s for s in filtroListaOTT if litadoBusqueda in s]  
                if len(filtroOTT)<10:
                    filtroListaOTT=filtroOTT[0].split('_')
                    filtroOTT = [s for s in filtroListaOTT if litadoBusqueda in s] 
                else:
                    datos=filtroOTT
                    return datos

                return  filtroOTT[0]
   
    @classmethod
    async def filtroModel(cls, comandoModel):
        list_versions = ['CE6800 V200R005C10SPC607B607','AR3200 V200R003C00','S5735-L24P4S-A1']
        for software_ver in list_versions:
            int_version= 0
            int_version = comandoModel.find(software_ver) 
            await asyncio.sleep(1)
            if int_version > 0:
		
                return software_ver
            else:
                pass
      
    @classmethod
    async def filtroMarca(cls, comandoMarca):
        list_versions = ['Huawei','cisco','Foriner']
        for software_marca in list_versions:
            int_version= 0
            int_version = comandoMarca.find(software_marca)
            await asyncio.sleep(1) 
            if int_version > 0:
                return software_marca
            else:
                pass   
            
                       
    @classmethod
    async def filtroSnmpVersion(cls, comandoSnmpVersion):
        list_versions = ['SNMPv2c:enable',
                 'SNMPv3:enable',
                 ]
        for snmp_version in list_versions:
            int_version= 0
            int_version = comandoSnmpVersion.find(snmp_version) 
            if int_version > 0:
                if int_version == 'SNMPv3:enable':
                    return 'V3'
                else:
                    return 'V2'
            else:
                pass     
        await asyncio.sleep(1)

    @classmethod
    async def filtroHostname(cls, comandoHostname):
        dato=comandoHostname.split(' ')
        await asyncio.sleep(1)
        if len(dato[1]) > 10:
            return dato[1]
        else:
            return 'sin datos'
            

 

if __name__ == '__main__':
    datos=open("hostname.txt", "r")  
    comando=datos.read()
       
    print(FuncionesFiltro.filtroHostname(comando))    
