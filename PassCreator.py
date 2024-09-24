import random
from tqdm import tqdm
def GeneratePass(PASS_LEN):
    LEN = 0
    pswd = ""
    while LEN != PASS_LEN*2:
      KEY_A = random.randint(0,9999)
      KEY_B = random.randint(0,9999)
      random.seed(KEY_A)
      PART_1 = int(random.random() * pow(10,PASS_LEN))
      random.seed(KEY_B)
      PART_2 = int(random.random() * pow(10,PASS_LEN))
      LEN = len(f"{PART_1}{PART_2}")
    print(f"KEY_A: {KEY_A}; KEY_B: {KEY_B}")
    RAW_PASS = f"{PART_1}{PART_2}"
    #print(RAW_PASS)
    MAXi = 125
    MINi = 33
    for i in range(int(LEN/2)):
        num = int(f'{RAW_PASS[i]}{RAW_PASS[i+PASS_LEN]}')
        if num % 2 == 0:
            num *= 3
        if num < MINi :
            num += (MINi-num)+int(RAW_PASS[i+1])
        elif num > MAXi:
            num -= (num-MAXi)
            num -= int(RAW_PASS[i-1])
        pswd += chr(num)
        #print(f"{num} = {chr(num)}")
    print(f"Your password: {pswd}")
    #print(len(pswd))

def GenerateShortPass(PASS_LEN):
    sh_pswd = ""
    MAXi = 125
    MINi = 33
    for i in range(4):
        num = random.randint(MINi,MAXi)
        sh_pswd += chr(num)
        #print(f"{num} = {chr(num)}")
    key_b1 = ""
    key_b2 = ""
    for i in range(4):
        num = ord(sh_pswd[i])
        num = str(num)
        key_b1 += num[0]
        key_b2 += num[1]
    #print(f"KEY_A: {key_b1}; KEY_B: {key_b2}")
    ReversePass(PASS_LEN,int(key_b1),int(key_b2))
    print(f"Shortpass: {sh_pswd}")

def ReversePass(PASS_LEN,KEY_A,KEY_B):
    LEN = 0
    pswd = ""
    while LEN != PASS_LEN*2:
      random.seed(KEY_A)
      PART_1 = int(random.random() * pow(10,PASS_LEN))
      random.seed(KEY_B)
      PART_2 = int(random.random() * pow(10,PASS_LEN))
      LEN = len(f"{PART_1}{PART_2}")
    print(f"KEY_A: {KEY_A}; KEY_B: {KEY_B}")
    RAW_PASS = f"{PART_1}{PART_2}"
    #print(RAW_PASS)
    MAXi = 125
    MINi = 33
    for i in range(int(LEN/2)):
        num = int(f'{RAW_PASS[i]}{RAW_PASS[i+PASS_LEN]}')
        if num % 2 == 0:
            num *= 3
        if num < MINi :
            num += (MINi-num)+int(RAW_PASS[i+1])
        elif num > MAXi:
            num -= (num-MAXi)
            num -= int(RAW_PASS[i-1])
        pswd += chr(num)
        #print(f"{num} = {chr(num)}")
    print(f"Your password: {pswd}")
    #print(len(pswd))

def main():
    inpt = input("Generate(G/g)/Revert(R/r): ")
    if(inpt == "G" or inpt == "g"):
        inpt2 = input("Shortpass(S/s)/Manual keys(M/m  stronger password but harder to remember 8 digits): ")
        if (inpt2 == "S" or inpt2 == "s"):
            GenerateShortPass(int(input("Pass lenght (8,16,32.... IT MUST BE AN EVEN NUMBER):")))
        else:
            GeneratePass(int(input("Pass lenght (8,16,32.... IT MUST BE AN EVEN NUMBER):")))
    elif (inpt == "R" or inpt == "r"):
        pswd_len = int(input("Pass lenght (8,16,32.... IT MUST BE AN EVEN NUMBER):"))
        inpt2 = input("Shortpass(S/s)/Manual keys(M/m): ")
        if (inpt2 == "S" or inpt2 == "s"):
            sh_pswd = input("Password (4 character long): ")
            key_b1 = ""
            key_b2 = ""
            for i in range(4):
                num = ord(sh_pswd[i])
                num = str(num)
                key_b1 += num[0]
                key_b2 += num[1]
            #print(f"KEY_A: {key_b1}; KEY_B: {key_b2}")
            ReversePass(pswd_len,int(key_b1),int(key_b2))
        else:
            K_A = int(input("KEY_A:"))
            K_B = int(input("KEY_B:"))
            ReversePass(pswd_len, K_A, K_B)
main()
