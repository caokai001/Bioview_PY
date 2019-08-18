import sys
import os
import json

args=sys.argv
biotype=args[1]
file=args[2]
#file="C:/Users/hp/Desktop/152/BioView_PY/example/example_dna.fa"

path_dir=os.path.abspath(".")
Ty=biotype
#print(path_dir)



# load 读入json文件
with open(os.path.join(path_dir,"theme","emoji.json")) as f:
    json_text=json.load(f)
    theme_body=json_text["base_color"]
    
def colored(Ty,theme_body):
    fg=theme_body[Ty]["fg"]
    bg=theme_body[Ty]["bg"]
    print('\x1b[0;{0};{1}m'.format(fg,bg) + Ty + '\x1b[0m',end="")

    
    
    
if biotype=="fa":
    #print("fa model")
    
    with open(file) as f:
        for line in f.readlines():
            line=line.rstrip("\n")
            if line.startswith(">"):
                print(line)
                #print("-"*20)
                continue
            else:
                for i in line:
                    colored(i.upper(),theme_body)
                print()
                    
                
            
        
