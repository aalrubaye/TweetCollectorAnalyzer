__author__ = 'Abduljaleel'

from pymongo import *
import networkx as nx
from igraph import *

GX=nx.Graph()

g = Graph()


# connecting to MongoDB 1 (THE MAIN DB - USA)
connection = Connection()
db = connection.twit_usa
t_u = db.tu
SS= 'DC'
tw = t_u.find()
print tw.count()


def is_heart(txt):
    if ("heart disease" in txt) or ("diseases of heart" in txt) or ("coronary artery" in txt) or \
            ("heart failure" in txt) or ("heart attack" in txt) or ("acute coronary" in txt) or ("angina" in txt) or \
            ("atrial fib" in txt) or ("arrhythmias" in txt) or ("atherosclerotic cardiovascular" in txt) or \
            ("congenital heart" in txt) or ("peripheral arterial disease" in txt) or ("pericardial" in txt) or \
            ("myocardial infarction" in txt) or ("endocarditis" in txt) or ("pericardium" in txt) or \
            ("myocarditis" in txt) or ("cardiac arrest" in txt) or ("congestive heart" in txt) or \
            ("heart block" in txt) or ("chd" in txt) or ("ihd" in txt) or ("cad" in txt):
                return True
    else:
        return False

def is_cancer(txt):
    if ("malignant" in txt) or ("cancer" in txt) or ("tumor" in txt) or ("malignancy" in txt):
        return True
    else:
        return False

def is_clrd(txt):
    if ("lower respiratory" in txt) or ("chronic obstructive pulmonary" in txt) or ("copd" in txt) or \
            ("asthma" in txt) or ("bronchitis" in txt) or ("emphysema" in txt):
                return True
    else:
        return False

def is_stroke(txt):
    if ("stroke" in txt) or ("brain attack" in txt) or ("cerebrovascular" in txt):
        return True
    else:
        return False

def is_alzheimer(txt):
    if ("alzheimer" in txt):
        return True
    else:
        return False

def is_diabetes(txt):
    if ("diabetes" in txt) or ("diabetic" in txt):
        return True
    else:
        return False

def is_flu_or_pneumonia(txt):
    if ("influenza" in txt) or ("pneumonia" in txt) or ("flu" in txt) or ("h1n1" in txt) or ("h5n1" in txt):
        return True
    else:
        return False

def is_kidney(txt):
    if ("nephritis" in txt) or ("nephrotic" in txt) or ("nephrosis" in txt) or ("nephritic" in txt) or \
            ("renal failure" in txt) or ("kidney disorder" in txt) or ("disorders of kidney" in txt) or \
            ("kidney failure" in txt) or ("kidney disease" in txt) or ("esrd" in txt) or \
            ("end stage renal" in txt) or ("dialysis" in txt):
                return True
    else:
        return False

def is_septicemia(txt):
    if ("septicemia" in txt) or ("blood poisoning" in txt) or ("bacteraemia" in txt) or \
            ("bacteremia" in txt) or ("sepsis" in txt):
                return True
    else:
        return False

def is_liver(txt):
    if ("chronic liver" in txt) or ("liver disease" in txt) or ("cirrhosis" in txt) or ("liver cirrhosis" in txt):
                return True
    else:
        return False

def is_hyper(txt):
    if ("hypertension" in txt) or ("hypertensive" in txt) or ("blood pressure" in txt):
        return True
    else:
        return False

def is_parkinson(txt):
    if ("parkinson" in txt) or ("paralysis agitans" in txt) or ("shaking palsy" in txt):
        return True
    else:
        return False

def is_penumonitis(txt):
    if ("aspiration pneumonia" in txt) or ("pulmonary aspiration" in txt) or ("inhalation pneumonia" in txt) or ("endotracheal aspiration" in txt):
        return True
    else:
        return False

def dod(SSS):

    Diseases_Array=[[0 for j in range(13)] for i in range(13)]

    for i in range(0,13):
        print Diseases_Array[i]

    nnn = 0
    for row in tw:
        nums = []
        tweet = row['data']['text'].lower()
        if (is_heart(tweet)):
            nums.append(0)
        if (is_cancer(tweet)):
            nums.append(1)
        if (is_clrd(tweet)):
            nums.append(2)
        if (is_stroke(tweet)):
            nums.append(3)
        if (is_alzheimer(tweet)):
            nums.append(4)
        if (is_diabetes(tweet)):
            nums.append(5)
        if (is_flu_or_pneumonia(tweet)):
            nums.append(6)
        if (is_kidney(tweet)):
            nums.append(7)
        if (is_septicemia(tweet)):
            nums.append(8)
        if (is_liver(tweet)):
            nums.append(9)
        if (is_hyper(tweet)):
            nums.append(10)
        if (is_parkinson(tweet)):
            nums.append(11)
        if (is_penumonitis(tweet)):
            nums.append(12)

        if len(nums) > 1:
            for i in range(0, len(nums)):
                current = nums[i]
                for j in range (i+1,len(nums)):
                    nextt = nums[j]
                    Diseases_Array[current][nextt] += 1
                    # print str(current)+','+str(nextt)

        nnn+=1
        print nnn
        #
    GX.add_node(0, nn="Heart Diseases")
    GX.add_node(1, nn= "Cancer")
    GX.add_node(2, nn="CLRD")
    GX.add_node(3, nn="Stroke")
    GX.add_node(4, nn="Alzheimer")
    GX.add_node(5, nn="Diabetes")
    GX.add_node(6, nn="Flu_Pneumonia")
    GX.add_node(7, nn= "Kidney Diseases")
    GX.add_node(8, nn="Septicemia")
    GX.add_node(9, nn="Liver Diseases")
    GX.add_node(10, nn="Hypertension")
    GX.add_node(11, nn="Parkinson")
    GX.add_node(12, nn="Pneymonitis")

    for i in range (0,13):
        for j in range (i+1,13):
            if Diseases_Array[i][j] != 0:
                GX.add_edge(i,j,weight=Diseases_Array[i][j])

    nx.write_graphml(GX,"/Users/Abduljaleel/Desktop/project/ND_"+SSS+".graphml")


# dod(SS)




# GX.add_node(0,ii='cancer')
# GX.add_node(1,ii='heart')
# GX.add_node(2,ii='diabetes')
#
# GX.add_edge(1,2)
# GX.add_edge(1,0)
#
# nx.write_graphml(GX,"/Users/Abduljaleel/Desktop/project/ND_usa.graphml")


for row in tw:
    if is_cancer(row['data']['text'].lower()):
        print '@'+row['data']['user']['screen_name'] + '....' + row['data']['text']