#constitutive exons
# this code take gtf file and search for constitutive exons
#constitutive exons : exon exist only once in all isoforms
#open file and create a a hash using the trnscript id as a key and teh exon start
# and end as tuple in alist as a value (list of tuples) 
fileName = input("Input gtf file")
GTF = open (fileName, 'r')
trans =[]
count = 0
header = GTF.readline()
header = GTF.readline()
gene = {}
for line in GTF:
    if count % 1 == 0:
        line = line.strip()
        mylist = line.split()
        if mylist[2] == "transcript":
            mylist[11] =   mylist[11].rstrip(';')
            mylist[11] = mylist[11].strip('"')
            trans.append(mylist[11])
            tmp = mylist[11]
            gene[mylist[11]] = []
            #print(tmp)
            tmp =[]
            #print(tmp)
        if mylist[2] == "exon":
            tmp.append((mylist[3],mylist[4]))
            mylist[11] =   mylist[11].rstrip(';')
            mylist[11] = mylist[11].strip('"')
            gene[mylist[11]].append((mylist[3],mylist[4]))
            
            
           # print(mylist[11],tmp)
 
    count+=1
# iterate over the hash tabl and create a list for each transcript by combining all the tuples into one list
# itereate over the list and check for constitutive exons
flag = 0
for key in gene:
    mykey = key.split('.')
    if flag == 0:
        tmpkey = mykey[0]+'.'+mykey[1]
        tr=[]
        flag = 1
        prevkey = tmpkey
        #print(tmpkey)
    if len(mykey) > 1 and tmpkey == (mykey[0]+'.'+mykey[1]):
        #print(key, gene[key], end="###")
        tr.append(gene[key])
        
    else:
        #print('\n')
        count = 0
        final = []
        dup =[]
        for item in tr:
            for i in item:
                if i not in final:
                    count += 1
                    final.append(i)
                else:
                    if i not in dup:
                        dup.append(i)
                        count -=1
        print(f'{prevkey},{count}')
                #print(i, end= '...')
        #print('\n\n')
        tr=[]
        tr.append(gene[key])
        #print(key, gene[key], end="###")
        if len(mykey) > 1 :
            tmpkey = mykey[0]+'.'+mykey[1]
        else:
            tmpkey = mykey[0]+'.' 
        prevkey = tmpkey
        #print(tmpkey)
#print('\n')
count = 0
final = []
dup =[]
for item in tr:
    for i in item:
        if i not in final:
            count += 1
            final.append(i)
        else:
            if i not in dup:
                dup.append(i)
                count -=1
print(f'{prevkey},{count}')   
        
#for item in trans:
#    print(item)
GTF.close()
