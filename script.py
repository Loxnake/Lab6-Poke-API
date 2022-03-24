import requests
from sys import argv

def main():

    pokeInfo = retrieveMon(argv[1])
    if retrieveMon:
        pastingStrings = pasteBinStrings(pokeInfo)
        pasteBinURL = pasteBinPOST(pastingStrings[0], pastingStrings[1])

        print(pasteBinURL)

def retrieveMon(pokeName):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pokeName))
    print('Getting Pokemon Information...', end = '')
    if response.status_code == 200:
     print('Success!')
     return response.json()
    else:
     print('Fialed, Response code:',response.status_code)
     return
    
def pasteBinStrings(pokeDict):

    body = ""
    for i in range(len(pokeDict['abilities'])):
        body += "-" + pokeDict['abilities'][i]['ability']['name'] + '\n'


    title = pokeDict['name'] + "'s Abilities"

    #body += " " + pokeDict['address']['geo']['lat']+ "\n"
    #body += "Longitude: "+ pokeDict['address']['geo']['lng']

    return (title, body)

def pasteBinPOST(title, body):

    
    params = {
        'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option': 'paste',
        'api_paste_code': body,
        'api_paste_name': title
    }
    response = requests.post('https://pastebin.com/api/api_post.php', data=params)

    print('Posting to PasteBin...', end = '')

    if response.status_code == 200:
     print('Success!')
     return response.text
    else:
     print('Failed, Response code:',response.status_code)
     return response.status_code



main()