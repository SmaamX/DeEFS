#SamHammer 1.0
from random import choice as rch
from os import system as sy
print("\u001b[34mSam\u001b[31mHammer 1.0")
user_input=input("\n\u001b[37m[1] Random Spoof\n[2] BT set\n[3] WLAN set\n[0] Exit\n\u001b[0m")
if user_input == "1":
  def randma():
    def randc():
      v=[]
      for i in range(2):v.append(str(rch(["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e"])))
      else:return "".join(v)
    v=[]
    for i in range(6):v.append(randc())
    else:return ":".join(v)
  ma=randma();print("\n\u001b[0m\u001b[37mwlan random mac",ma);sy("svc wifi disable");sy("su -c echo "+ma+" > /efs/wifi/.mac.cob && echo "+ma+" > /efs/wifi/.mac.info");sy("svc wifi enable")
  mab=randma();print("\n\u001b[0m\u001b[37mbt random mac",mab);sy("svc bluetooth disable");sy("su -c echo "+mab+" > /efs/bluetooth/bt_addr");sy("svc bluetooth enable)
elif user_input == "2":user_inputb=input("\n\u001b[37mBT set -> ");["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f",":"] in user_inputb == False or len(user_inputb) != 17 if exit(1) else sy("svc Bluetooth disable");sy("su -c echo "+mab+" > /efs/bluetooth/bt_addr");
elif user_input == "3":user_inputb=input("\n\u001b[37mWLAN set -> ");["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f",":"] in user_inputb == False or len(user_inputw) != 17 if exit(1) else sy("svc wifi disable");sy("su -c echo "+user_inputw+" > /efs/wifi/.mac.cob && echo "+user_inputw+" > /efs/wifi/.mac.info");sy("svc wifi enable")
elif user_input == "0":exit(0)
else:exit(1)
