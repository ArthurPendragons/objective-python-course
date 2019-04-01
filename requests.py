import requests

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#badResponse = requests.get('https://automatetheboringstuff.com/noFileFound')
# print(len(response.text))
# print(response.text[:500])
#badResponse.raise_for_status()
playFile = open('romeoandjuliet.txt','wb')
for chunk in response.iter_content(100000):
	playFile.write(chunk)

playFile.close()

