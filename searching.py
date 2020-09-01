

import os
import app

def find(term):
   #term="between"
    list=[]
    for file_n in os.listdir(os.getcwd()):
        if not file_n.endswith(".txt"):
            continue
        f = open(file_n)
        for line in f:
            line.strip().split('/n')
            if term in line:
                
                list.append(os.path.join(os.getcwd(), file_n[:len(file_n)-4]+'.pdf'))
                break

        f.close()
    print(list)
    

       

