# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 13:43:37 2016

@author: haicen
"""

import hashlib
import sys, getopt


def compressor(in_var, out):
    i=0
    j=0
    
    while i<len(in_var):
       
    
        out[j] = (in_var[i] + in_var[i+1]) % 62;
        if (out[j] < 10):
            out[j] += 48
        elif (out[j] < 36):
          out[j] += 55;
        else:
            out[j] += 61        

        i=i+2
        j=j+1
        
def dhash(passw):
    m = hashlib.md5()
    m.update(passw.encode("ascii"))
    
    s=m.digest()
    #print(type(s))
    crypt=[]
    for b in s:
        crypt.append(b)
    
    
    
    
    out2=['']*8
    compressor(crypt,out2)
    result=''.join([chr(a) for a in out2])
    return result

def helpPage():
     print('DahuaHash.py -v <password to hash> or -i <infile> -o <outfile>')
     print("\t infile is a file with one password per line, output will be"+
                    " a csv file like <password>,<hash>")

def main():
    inputfile,outputfile='',''
    try:
        opts,args = getopt.getopt(sys.argv[1:],"hv:i:o:",["help","password=","infile=","outfile="])
    except getopt.GetoptError:
        helpPage()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            helpPage()
            sys.exit()
        elif opt in ("-i", "--infile"):
            inputfile = arg
        elif opt in ("-o", "--outfile"):
            outputfile = arg
        elif opt in("-v" , "--password"):
            print("{} = {}".format(arg,dhash(arg)))
            sys.exit()
            
    if( not (inputfile=='') and not (outputfile=='')):
       with open(inputfile,'r') as fileIn, open(outputfile,'w') as fileOut:
            for line in fileIn:
                line=line.strip('\n')
                fileOut.write("{},{}".format(line,dhash(line)))
    else:
        helpPage()
if __name__=="__main__":
    main()            