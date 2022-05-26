class TipoConexion:
    
    @classmethod
    def conexionSSH(cls, ip, usuario , password):
    
        huawei_ssh = {
            'device_type': 'huawei',
            'host': ip,
            'username': usuario,
            'password': password,
            'conn_timeout': 40,
            'port': 22
        }    
        return  huawei_ssh