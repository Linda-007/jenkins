import yaml

with open("../datas/caps.yaml") as f:
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']
    print(datas['desirecaps'])