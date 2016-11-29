import subprocess
import json
import os

# commands
extractor = 'extractor'
list_test = 'list_test'
server = '-server'
url = 'http://106.125.51.125'
download = 'download'
type_of_download = 'dump'

list_test_file = open('list_test.json', 'w')

limit_of_test_data = '200'

subprocess.call([extractor, server, url, 'list_test', '-limit', limit_of_test_data], stdout=list_test_file)

with open('list_test.json') as json_file:
    json_data = json.load(json_file)

names = list(json_data.keys())

for name in names:
    if not os.path.exists(name):
        os.makedirs(name)
    file_name = name + "/" + name + ".txt"
    temp_file = open(file_name, 'w')
    temp_query= '.' + str(name) +'[].sha256'
    temp_file = open(file_name, 'r+')
    subprocess.call(['jq', temp_query, 'list_test.json'], stdout=temp_file)
    temp_file.close()


    work_directory = '/home/vbaranov/PycharmProjects/parseJson/' + name

    download_file = open(file_name, 'r')
    for line in download_file:
        hash_dump =line[1:-2]
        subprocess.call([extractor, server, url, download, type_of_download, hash_dump], cwd=work_directory)