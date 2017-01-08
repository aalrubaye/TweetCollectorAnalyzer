__author__ = 'Abduljaleel'

from pymongo import *
import igraph

gx = igraph.Graph()

#connecting to MongoDB 1 (THE MAIN DB - USA)
connection = Connection()
db = connection.florida
t_u = db.fl
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



Diseases_Array=[[0 for j in range(13)] for i in range(13)]

for i in range(0,13):
    print Diseases_Array[i]


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
                print str(current)+','+str(nextt)



# GX.add_node(1, label='Diseases of heart', color="heart")
# GX.add_node(2, label='Malignant neoplasms', color="cancer")
# GX.add_node(3, label='CLRD', color="clrd")
# GX.add_node(4, label='Cerebrovascular diseases', color="stroke")
# GX.add_node(5, label='Alzheimer\'s disease', color="clrd")
# GX.add_node(6, label='Diabetes mellitus', color="diabetes")
# GX.add_node(7, label='Influenza or Pneumonia', color="flupne")
# GX.add_node(8, label='Nephritis, Nephrotic syndrome', color="kidney")
# GX.add_node(9, label='Septicemia', color="septicemia")
# GX.add_node(10, label='CLD', color="cld")
# GX.add_node(11, label='Hypertension', color="hypertension")
# GX.add_node(12, label='Parkinson\'s disease', color="parkinson")
# GX.add_node(13, label='Pneumonitis', color="pneumonitis")


gx.add_vertex('heart', label='Diseases of heart', disease=1)
gx.add_vertex('cancer', label='Malignant neoplasms', disease=2)
gx.add_vertex('clrd', label='CLRD', disease=3)
gx.add_vertex('stroke', label='Cerebrovascular diseases', disease=4)
gx.add_vertex('alz', label='Alzheimer\'s disease', disease=5)
gx.add_vertex('diabetes', label='Diabetes mellitus', disease=6)
gx.add_vertex('flupne', label='Influenza or Pneumonia', disease=7)
gx.add_vertex('kidney', label='Nephritis, Nephrotic syndrome', disease=8)
gx.add_vertex('septicemia', label='Septicemia', disease=9)
gx.add_vertex('cld', label='CLD', disease=10)
gx.add_vertex('hypertension', label='Hypertension', disease=11)
gx.add_vertex('parkinson', label='Parkinson\'s disease', disease=12)
gx.add_vertex('pneumonitis', label='Pneumonitis', disease=13)

gx.vs[0]['type'] = 'heart'
gx.vs[1]['type'] = 'cancer'
gx.vs[2]['type'] = 'clrd'
gx.vs[3]['type'] = 'stroke'
gx.vs[4]['type'] = 'alz'
gx.vs[5]['type'] = 'diabetes'
gx.vs[6]['type'] = 'flupne'
gx.vs[7]['type'] = 'kidney'
gx.vs[8]['type'] = 'septicemia'
gx.vs[9]['type'] = 'cld'
gx.vs[10]['type'] = 'hypertension'
gx.vs[11]['type'] = 'parkinson'
gx.vs[12]['type'] = 'pneumonitis'





for i in range (0,13):
    for j in range (i+1,13):
        if Diseases_Array[i][j] != 0:
            x = i+1
            y = j+1
            F = ""
            T= ""
            if x == 1:
                F = "heart"
            elif x==2:
                F = "cancer"
            elif x==3:
                F="clrd"
            elif x==4:
                F = "stroke"
            elif x==5:
                F="alz"
            elif x==6:
                F = "diabetes"
            elif x==7:
                F="flupne"
            elif x==8:
                F = "kidney"
            elif x==9:
                F="septicemia"
            elif x==10:
                F = "cld"
            elif x==11:
                F="hypertension"
            elif x==12:
                F = "parkinson"
            elif x==13:
                F="pneumonitis"

            if y == 1:
                T = "heart"
            elif y==2:
                T = "cancer"
            elif y==3:
                T="clrd"
            elif y==4:
                T = "stroke"
            elif y==5:
                T="alz"
            elif y==6:
                T = "diabetes"
            elif y==7:
                T="flupne"
            elif y==8:
                T = "kidney"
            elif y==9:
                T="septicemia"
            elif y==10:
                T = "cld"
            elif y==11:
                T="hypertension"
            elif y==12:
                T = "parkinson"
            elif y==13:
                T="pneumonitis"

            gx.add_edge(F,T,weight=Diseases_Array[i][j])

gx.write_graphml("/Users/Abduljaleel/Desktop/DN_Florida.graphml")
