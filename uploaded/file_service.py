import yaml
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def readYamlFile(location):
    return yaml.safe_load(location)

def readRemoteFile(location, token):
    headers = {'Authorization': 'token ' + token}
    file = requests.get(location, headers=headers, verify=False)
    return readYamlFile(file.text)

def writeYamlFile(content, fileName) :
    with open(fileName, 'w') as file:
        yaml.dump(content, file)
#########################