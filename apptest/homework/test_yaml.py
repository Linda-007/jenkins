import yaml


def test_yaml():
    with open("data.yml") as f:
        all_datas = yaml.safe_load(f)
    #return all_datas['datas']
    print(all_datas)