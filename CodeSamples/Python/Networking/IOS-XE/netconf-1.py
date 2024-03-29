from ncclient import manager


router = {"host": "192.168.1.189", "port": "830",
          "username": "cisco", "password": "cisco"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    m.close_session()
