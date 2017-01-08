__author__ = 'Abduljaleel'
from pymongo import *
import csv

connection = Connection()

database = connection.twit_usa
t_mongo = database.tu
twit = t_mongo.find()



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

def is_flu(txt):
    if ("influenza" in txt) or ("flu" in txt) or ("h1n1" in txt) or ("h5n1" in txt):
        return True
    else:
        return False

def is_pne(txt):
    if ("pneumonia" in txt):
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


heart = 0
cancer = 0
clrd = 0
stroke = 0
alz = 0
diabetes = 0
flupn = 0
kidney = 0
septicemia = 0
liver = 0
hyper = 0
parkinson = 0
penumonitis = 0
n = 0
ss=0
nn=0

for row in twit:
    # state = row['state'].strip()
    text = row['data']['text']
    c = 0
    # text = row['text']
    txt = text.lower()

    if (is_heart(txt)):
        heart +=1
        c+=1
    if (is_cancer(txt)):
        cancer +=1
        c+=1
    if (is_clrd(txt)):
        clrd +=1
        c+=1
    if (is_stroke(txt)):
        stroke +=1
        c+=1
    if (is_alzheimer(txt)):
        alz +=1
        c+=1
    if (is_diabetes(txt)):
        diabetes +=1
        c+=1
    if (is_flu_or_pneumonia(txt)):
        flupn +=1
        c+=1
    if (is_kidney(txt)):
        kidney +=1
        c+=1
    if (is_septicemia(txt)):
        septicemia +=1
        c+=1
    if (is_liver(txt)):
        liver +=1
        c+=1
    if (is_hyper(txt)):
        hyper +=1
        c+=1
    if (is_parkinson(txt)):
        parkinson +=1
        c+=1
    if (is_penumonitis(txt)):
        penumonitis +=1
        c+=1

    if c>1 :
        ss +=1
    if c==0:
        nn +=1
    n+=1
    print n


total = twit.count()
print 'more than 1 diseases : ' + str(ss)
print 'equal to zero        : ' + str(nn)
print '-------------------------'
print 'total                : ' + str(total-nn)
# print '-------------------------'
# print 'total' + str(twit.count())
# print 'heart : ' + str(heart)
# print 'cancer : ' + str(cancer)
# print 'clrd : ' + str(clrd)
# print 'stroke : ' + str(stroke)
# print 'alz : ' + str(alz)
# print 'diabetes : ' + str(diabetes)
# print 'flupne : ' + str(flupn)
# print 'kidney : ' + str(kidney)
# print 'septicemia : ' + str(septicemia)
# print 'liver : ' + str(liver)
# print 'hyper : ' + str(hyper)
# print 'parkinson : ' + str(parkinson)
# print 'penumonitis : ' + str(penumonitis)


