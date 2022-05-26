import netmiko
from servicio.netmiko.tipoConexion import TipoConexion

class Comando:
    def enviarComando(cls,comando,ip, usuario , password ):
        lista= []
        try:
            huewei_ssh=TipoConexion.conexionSSH(ip, usuario ,password)
            ssh = netmiko.ConnectHandler(**huewei_ssh)
            ssh.enable()
            
            shRun = ssh.send_command(comando[0], delay_factor=2)
            comandoListShRun=shRun.split('\n')
            shbrief = ssh.send_command(comando[1], delay_factor=2)
            comandoListBrief=shbrief.split('\n')
            shVer = ssh.send_command(comando[2], delay_factor=2)
            comandoListVer=shVer.split('\n')
            disVer2 = ssh.send_command(comando[3], delay_factor=2)
            disHostname = ssh.send_command(comando[4], delay_factor=2)
            disSnmp = ssh.send_command(comando[5], delay_factor=2)
           
 
            
            ssh.exit_enable_mode()
            print(f"CONEXION SSH OK {ip}")
            lista.append(comandoListShRun)
            lista.append(comandoListBrief)
            lista.append(comandoListVer)
            lista.append(disVer2)
            lista.append(disHostname)
            lista.append(disSnmp)

            
            return lista
        except Exception as e:  
            print(f"ERROR SSH {ip}") 