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
    print(RAW_PASS)
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
        print(f"{num} = {chr(num)}")
    print(pswd)
    print(len(pswd))
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
    print(RAW_PASS)
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
        print(f"{num} = {chr(num)}")
    print(pswd)
    print(len(pswd))

def main():
    inpt = input("Generate(G/g)/Revert(R/r)/Decript(de):")
    if(inpt == "G" or inpt == "g"):
        GeneratePass(int(input("Pass lenght (8,16,32.... IT MUST BE AN EVEN NUMBER):")))
    elif (inpt == "R" or inpt == "r"):
        pswd_len = int(input("Pass lenght (8,16,32.... IT MUST BE AN EVEN NUMBER):"))
        K_A = int(input("KEY_A:"))
        K_B = int(input("KEY_B:"))
        ReversePass(pswd_len, K_A, K_B)
    elif (inpt == "de"):
        pass
main()
