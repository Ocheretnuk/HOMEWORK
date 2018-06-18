import json

def http_headers_to_json(txt_file_path, json_file_path):


    with open(txt_file_path) as k:
        string = k.readline()
        string = string.split()
        d = {}

        if string[1] == '200'
                d['protocol'] = string[0]
                d['status_code'] = string[1]
                d['status_message'] = string[2]

        elif string[1] == '301':
                d['protocol'] = string[0]
                d['status_code'] = string[1]
                d['status_message'] = string[2] + ' ' + string[3]

        elif string[0] == 'GET':
                d['method'] = string[0]
                d['uri'] = string[1]
                d['protocol'] = string[2]


        with open(txt_file_path) as k:
            k.readline()
            for i in k:
                if i != '\n':
                    i = i.replace('\n','')
                    i = i.split(': ')
                    d.update({i[0]:i[1]})


        with open(json_file_path, 'w') as k:
                json.dump(d, k, indent=4)