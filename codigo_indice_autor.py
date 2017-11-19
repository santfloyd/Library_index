#libraries to read from a DB and encode a dictionary to perform an index for a library catalog
import pandas as pd
import collections
import codecs

#Excel file
df=pd.read_excel('BaseSO_sutatenza_retrial.xlsx', 'Hoja1', na_values=[' '])
#select the targeted columns for index
df=df[["No", "Nombre_autor", "Lugar_elaboracion", "Tema_1"]]

#slice even more, just the number and the name
s1=df[["No", "Nombre_autor"]]
#format the type of column data for index from int to object
s1["No"] = df["No"].astype(object)


print s1
#order names alphabetically
s1.sort_values(["Nombre_autor"], ascending=False)

#Group by name, topic, topology or whatever. Name in this case
for name, group in s1.groupby("Nombre_autor"):
    # print the name, topic, topology or whatever
    print(name)
    # print the group of No. 
    print(group)
#ask for type to ensure it`s object  
print s1.dtypes
#Generate a Dic with the names as keys and numbers of column No. as values 

mydict = {}
for x in range(len(s1)):
    currentid = s1.iloc[x,1]
    currentvalue = s1.iloc[x,0]
    mydict.setdefault(currentid, [])
    mydict[currentid].append(currentvalue)
    mydict=collections.OrderedDict(sorted(mydict.items()))
print mydict
#write the output on a blank file and allows any character with accent encoded as utf-8
with codecs.open ("indices.autor.txt.doc", 'w', 'utf-8') as f:
    #mydict = {k: unicode(v).encode("utf-8") for k,v in mydict.iteritems()}
    for key, value in mydict.items():
        f.write('%s:%s\n' % (key, value))
        