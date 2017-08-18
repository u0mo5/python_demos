import sys, getopt
opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
input_file=""
output_file=""
for op, value in opts:
  if op == "-i":
    input_file = value
    print(input_file)
  elif op == "-o":
    output_file = value
    print(output_file)
  elif op == "-h":
    # usage()
    sys.exit()

import requests
address = '北京市'
url= 'http://api.map.baidu.com/geocoder?output=json&key=f247cdb592eb43ebac6ccd27f796e2d2&address='+str(address)
response = requests.get(url)
answer = response.json()
lon = float(answer['result']['location']['lng'])
lat = float(answer['result']['location']['lat'])
print(lon,lat)