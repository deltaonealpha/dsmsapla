import os
import time
import getpass
if os.path.exists(r'userblock.txt'):
    os.remove(r'userblock.txt')
print("      []         [] []               ")
print("      []         [] []]]]]] software ")
print("[======] [=====] [] [] [======]  CLI ")
print("[]====[] []---[] [] [] []====[]      ")
print("[======] []____  [] [] [======]]]]   ")
time.sleep(1)
print(" ")
print(" ")
print("DeltaStoreManager")
print("Welcome to the deltaSTOREMANAGER")
time.sleep(1)
print("The program shall NOT elevate and exit without a succesfull OAuth.")
print(" ")
time.sleep(1)
userid = input("Please enter your identification key: ")
towrite = "User identified from login process: " + userid
time.sleep(1)
print("Welcome, " + userid)
print(" ")
print(" ")
time.sleep(0.5)
passw = getpass.getpass(prompt='Enter main password: ', stream=None)
if passw == "root":
    userblock = open(r"userblock.txt","a+") #Opening / creating (if it doesn't exist already) the .txt record file
    userblock.write(towrite)
    userblock.close()
    time.sleep(1) #for a seamless experience
    print("OAuth success!")
    time.sleep(0.8)
    print("Decrypting main program.......")
    time.sleep(1.4) #for a seamless experience
    os.startfile(r'C:\Users\balaj\OneDrive\Desktop\dsmsapl-master\hms1.py')
    exit()
else:
    print(" ")
    if os.path.exists(r'userblock.txt'):
        os.remove(r'userblock.txt')
    print("OAuth failure! Re-run to retry authenication.")
    time.sleep(1)
    print("This program shall now exit.")
    print()
    print("      []         [] []               ")
    print("      []         [] []]]]]] software ")
    print("[======] [=====] [] [] [======]  CLI ")
    print("[]====[] []---[] [] [] []====[]      ")
    print("[======] []____  [] [] [======]]]]   ")
    print()
    print("--------------------------------------------")
    time.sleep(3)
    exit()
