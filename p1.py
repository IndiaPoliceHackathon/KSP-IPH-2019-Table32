

# firebase=firebase
from firebase import firebase
firebase = firebase.FirebaseApplication('https://new1-4ded7.firebaseio.com/police')
acc=firebase.put('/','login info',{'chat':{'message':'hi','message2':'bye'},'id':'12345',})
a1=firebase.put('/','12345',{'lat':2,'lon':1,'firstname':'ashok','last name':'kumar','adhaar number':'84123456789456','phone no':1234567890,'blood group':'A+'})
a2=firebase.put('/','12346',{'lat':2.001,'lon':1.001})
result = firebase.get('/','')
print(result)
from math import radians,sin,cos,acos
print (result)
def dis(id1,id2)  :
    p1_id=str(id1)
    p2_id=str(id2)
    lat1 = firebase.get(p1_id,'lat')
    lon1 = firebase.get( p1_id, 'lon')
    lat2 = firebase.get(p2_id, 'lat')
    lon2 = firebase.get( p2_id, 'lon')

    d=6371.01*acos(sin(lat1)*sin(lat2)+cos(lat2)*cos(lat1)*cos(lon1-lon2))
    return(d)

print(firebase.get('/',''))
list=[4,5]
print(result.keys())
m=str(result.keys())
ls_id=[]
id=0
for i in range(len(m)):
    if m[i] in ['1','2','3','4','5','6','7','8','9','0']:
        id=id*10+int(m[i])
        if 9999<id<99999:
            ls_id.append(id)
            id=0
print(ls_id)

m=dict.fromkeys(ls_id)
class ID :

    def __init__(self,a):
        self.nearby=a

print(m)
list2=[]
for i in range(len(ls_id)):
    ls_nearby=[]
    for m in range(len(ls_id)):
        if(0.10<dis(ls_id[i],ls_id[m])<10):
            ls_nearby.append(str(ls_id[m]))
    print('near to',ls_id[i],'is',ls_nearby)
    list2.append(ls_nearby)
for i in range(2):
    am=firebase.put('/',ls_id[i]+100000, {'nearby police':list2[i]})
result = firebase.get('/','')


print(result)


