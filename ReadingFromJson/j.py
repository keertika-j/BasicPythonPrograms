import requests
import csv
r=requests.get('https://frdemoobddata.firebaseio.com/ImageData_iOS/16-04-2019.json')
resp=r.json()
# print(resp['Arun-down']['Auth']['3n4mkutwSZ']['Rx,Ry'])
# print(type(resp))
f=open('sheet4.csv','w')
with f:
	fnames=['username','XcallID','signature']
	writer=csv.DictWriter(f,fieldnames=fnames)
	for s in resp:
		print(s)
		username=s
		writer.writerow({'username':username})
		for k in resp[s]:
			for l in resp[s][k]:
				# print(l)
				# print(resp[s][k][l])
				for m in resp[s][k][l]:
					# print(m)
					if(m=="Rx,Ry"):
						# global RxRy
						RxRy=resp[s][k][l][m]
						# writer.writerow({'RxRy': RxRy})
						print(RxRy)
					elif(m=="XcallID"):
						# global XcallID
						XcallID=resp[s][k][l][m]
						writer.writerow({'XcallID': XcallID})
						print(XcallID)
					else:
						signature=resp[s][k][l][m]
						writer.writerow({'signature':signature})
					
					


	
  
    		