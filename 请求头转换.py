import re 
import json

def header_to_dict(header):
    dic = {}
    pattern = re.compile(r'(.*?):(.*?)\n')
    result = pattern.findall(header)
    for i in result:
        key = i[0].strip()
        value = i[1].strip()
        dic[key] = value
    print(json.dumps(dic,indent=1))
    return dic

if __name__ == "__main__":

    header = '''
vmid: 546195
pn: 1
ps: 20
order: desc
jsonp: jsonp
callback: __jp22

    '''
    header_to_dict(header)