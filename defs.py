#DeEFS 1.6
from random import choice as rch
from os import system as sy
def buffmc(mac):
  if any(cha in ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f",":"] for cha in mac) or len(mac) != 17:return True
  else:return False
def randma():
  def randc():
    v=[]
    for i in range(2):v.append(str(rch(["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e"])))
    else:return "".join(v)
  v=[]
  for i in range(6):v.append(randc())
  else:return ":".join(v)
def dwlan(mac):
  if mac == "rand":
    ma=randma();sy("svc wifi disable");sy("su -c echo "+ma+" > /efs/wifi/.mac.cob && echo "+ma+" > /efs/wifi/.mac.info");sy("svc wifi enable");return ma
  else:
    buffmc(mac) == False if None else sy("svc wifi disable");sy("su -c echo "+mac+" > /efs/wifi/.mac.cob && echo "+mac+" > /efs/wifi/.mac.info");sy("svc wifi enable");return(0)
def dbt(mac):
  if mac == "rand":
    mab=randma();sy("svc bluetooth disable");sy("su -c echo "+mab+" > /efs/bluetooth/bt_addr");sy("svc bluetooth enable");return mab
  else:
    buffmc(mac) == False if None else sy("svc bluetooth disable");sy("su -c echo "+mac+" > /efs/bluetooth/bt_addr");sy("svc bluetooth enable");return(0)
def adwlan(reg,out=False):
  for i in range(reg):mac1=dwlan("rand");sy("dumpsys wifi scan "+(("> /dev/null") if out == False else ""));print("\u001b[32m["+str(i)+","+mac1+"] wlan packet send")
def adbt(reg,out=False):
  for i in range(reg):mac1=dbt("rand");sy("dumpsys bluetooth_manager >"+(("> /dev/null") if out == False else ""));print("\u001b[32m["+str(i)+","+mac1+"] bt packet send")
def cusefs(dict,value):sy("su -c echo "+value+" > /efs/"+dict)
#jump_out
