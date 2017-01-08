__author__ = 'Abduljaleel'
from pymongo import *
import csv
connection = Connection()

database = connection.twit_usa
t_mongo = database.tu
twit = t_mongo.find()
p = twit.count()
tc = csv.writer(open("/Users/Abduljaleel/Desktop/project/pneumonitis.csv", "a"))
tc.writerow((str(217),str(218),str(219),str(220),str(221),str(222),str(223),str(224),str(225),str(226),str(227),str(228),
            str(301),str(302),str(303),str(304),str(305),str(306),str(307),str(308),str(309),str(310),str(311),str(312),
            str(313),str(314),str(315),str(316),str(317),str(318),str(319),str(320),str(321),str(322),str(323),str(324),
            str(325),str(326),str(327),str(328),str(329),str(330),str(331),str(401),str(402),str(403),str(404),str(405),
            str(406),str(407),str(408),str(409),str(410),str(411),str(412),str(413),str(414),str(415),str(416)))

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

d217 = 0; d218 = 0; d219=0; d220=0; d221=0; d222=0; d223=0; d224=0; d225=0; d226=0; d227=0; d228=0
d301 = 0; d302 = 0; d303=0; d304=0; d305=0; d306=0; d307=0; d308=0; d309=0; d310=0; d311=0; d312=0
d313 = 0; d314 = 0; d315=0; d316=0; d317=0; d318=0; d319=0; d320=0; d321=0; d322=0; d323=0; d324=0
d325 = 0; d326 = 0; d327=0; d328=0; d329=0; d330=0; d331=0; d401=0; d402=0; d403=0; d404=0; d405=0
d406 = 0; d407 = 0; d408=0; d409=0; d410=0; d411=0; d412=0; d413=0; d414=0; d415=0; d416=0; d417=0
n=0
k=0; kk=0;kkk=0;
for row in twit:
    txt = (row['data']['text']).lower()
    if (is_penumonitis(txt)):
        k+=1
        if 'created_at' in row['data']:
            kk+=1
            if 'None' not in str(row['data']['created_at']):
                kkk+=1
                # print row['data']['text']
                Time = row['data']['created_at']
                # print Time
                mm = Time[4:7]
                # print mm
                if mm == 'Feb':
                    m = 2
                elif mm == 'Mar':
                    m = 3
                elif mm == 'Apr':
                    m = 4
                day = Time[8:10]
                ee = str(m)+str(day)

                if str(ee) == '217':
                    d217 +=1
                elif str(ee) == '218':
                    d218 +=1
                elif str(ee) == '219':
                    d219 +=1
                elif str(ee) == '220':
                    d220 +=1
                elif str(ee) == '221':
                    d221 +=1
                elif str(ee) == '222':
                    d222 +=1
                elif str(ee) == '223':
                    d223 +=1
                elif str(ee) == '224':
                    d224 +=1
                elif str(ee) == '225':
                    d225 +=1
                elif str(ee) == '226':
                    d226 +=1
                elif str(ee) == '227':
                    d227 +=1
                elif str(ee) == '228':
                    d228 +=1
                elif str(ee) == '301':
                    d301 +=1
                elif str(ee) == '302':
                    d302 +=1
                elif str(ee) == '303':
                    d303 +=1
                elif str(ee) == '304':
                    d304 +=1
                elif str(ee) == '305':
                    d305 +=1
                elif str(ee) == '306':
                    d306 +=1
                elif str(ee) == '307':
                    d307 +=1
                elif str(ee) == '308':
                    d308 +=1
                elif str(ee) == '309':
                    d309 +=1
                elif str(ee) == '310':
                    d310 +=1
                elif str(ee) == '311':
                    d311 +=1
                elif str(ee) == '312':
                    d312 +=1
                elif str(ee) == '313':
                    d313 +=1
                elif str(ee) == '314':
                    d314 +=1
                elif str(ee) == '315':
                    d315 +=1
                elif str(ee) == '316':
                    d316 +=1
                elif str(ee) == '317':
                    d317 +=1
                elif str(ee) == '318':
                    d318 +=1
                elif str(ee) == '319':
                    d319 +=1
                elif str(ee) == '320':
                    d320 +=1
                elif str(ee) == '321':
                    d321 +=1
                elif str(ee) == '322':
                    d322 +=1
                elif str(ee) == '323':
                    d323 +=1
                elif str(ee) == '324':
                    d324 +=1
                elif str(ee) == '325':
                    d325 +=1
                elif str(ee) == '326':
                    d326 +=1
                elif str(ee) == '327':
                    d327 +=1
                elif str(ee) == '328':
                    d328 +=1
                elif str(ee) == '329':
                    d329 +=1
                elif str(ee) == '330':
                    d330 +=1
                elif str(ee) == '331':
                    d331 +=1
                elif str(ee) == '401':
                    d401 +=1
                elif str(ee) == '402':
                    d402 +=1
                elif str(ee) == '403':
                    d403 +=1
                elif str(ee) == '404':
                    d404 +=1
                elif str(ee) == '405':
                    d405 +=1
                elif str(ee) == '406':
                    d406 +=1
                elif str(ee) == '407':
                    d407 +=1
                elif str(ee) == '408':
                    d408 +=1
                elif str(ee) == '409':
                    d409 +=1
                elif str(ee) == '410':
                    d410 +=1
                elif str(ee) == '411':
                    d411 +=1
                elif str(ee) == '412':
                    d412 +=1
                elif str(ee) == '413':
                    d413 +=1
                elif str(ee) == '414':
                    d414 +=1
                elif str(ee) == '415':
                    d415 +=1
                elif str(ee) == '416':
                    d416 +=1
    n+=1
    print n

print k
print kk
print kkk

tc.writerow((str(d217),str(d218),str(d219),str(d220),str(d221),str(d222),str(d223),str(d224),str(d225),str(d226),str(d227),str(d228),
            str(d301),str(d302),str(d303),str(d304),str(d305),str(d306),str(d307),str(d308),str(d309),str(d310),str(d311),str(d312),
            str(d313),str(d314),str(d315),str(d316),str(d317),str(d318),str(d319),str(d320),str(d321),str(d322),str(d323),str(d324),
            str(d325),str(d326),str(d327),str(d328),str(d329),str(d330),str(d331),str(d401),str(d402),str(d403),str(d404),str(d405),
            str(d406),str(d407),str(d408),str(d409),str(d410),str(d411),str(d412),str(d413),str(d414),str(d415),str(d416)))
