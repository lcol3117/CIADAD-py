def dist(a,b):
  d1d,d2d,d3d = ldelta(0,a,b),ldelta(1,a,b),ldelta(2,a,b) #1d distances
  return max([d1d,d2d,d3d]) #largest distance
  
def ldelta(i,l1,l2):
  raw = l1[i]-l2[i] #1d delta
  return abs(raw) #absolute value

inv = lambda l : [(not i) for i in l]

median = lambda l : sorted(l)[int(len(l)/2)]

def CIADAD_detect(data,do):
  if do == "anomalies": 
    return CIADAD_detect_INTERNAL(data)
  elif do == "usual":
    return inv(list(CIADAD_detect_INTERNAL(data)))

def CIADAD_detect_INTERNAL(data):
  vals = list(map(lambda x:getD(x,data),data))
  thresh = median(vals) #median of vals
  return list(map(lambda x:x>thresh, vals))

def getD(i,data):
  options = map(lambda x:distNotSelf(i,x),data)
  return min(options)

def distNotSelf(a,b):
  raw = dist(a,b)
  if not raw == 0:
    return raw
  else:
    return float("inf")

mydata = [[3,3,1],[2,3,1],[3,2,1],[4,3,1],[2,2,1],[5,5,1],[5,6,1],[6,5,1],[10,1,1]]
print(CIADAD_detect(mydata,"usual"))
