__author__ = 'Abduljaleel'
from pymongo import *
import csv

connection = Connection()
db_usa = connection.twit_usa
t_u = db_usa.tu
tw = t_u.find()


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


# for row in tw:
#     print row['data']['user']['location'] + "----->" + row['city'] +' , ' +row ['state']


AL=0; AK=0; AZ=0; AR=0; CA=0; CO=0; CT=0; DE=0; DC=0; FL=0; GA=0; HI=0; ID=0; IL=0; IN=0; IA=0; KS=0; KY=0; LA=0; ME=0;
MD=0; MA=0; MI=0; MN=0; MS=0; MO=0; MT=0; NE=0; NV=0; NH=0; NJ=0; NM=0; NY=0; NC=0; ND=0; OH=0; OK=0; OR=0; PA=0; RI=0;
SC=0; SD=0; TN=0; TX=0; UT=0; VT=0; VA=0; WA=0; WV=0; WI=0; WY=0;

total = 0
n = 0
for row in tw:
    text = row['data']['text']
    txt = text.lower()

    if (is_penumonitis(txt)==True):
        state = row['state'].lower()

        if (state != ''):
            if (state == "alabama"):
                AL += 1
                total +=1
            elif (state == "alaska"):
                AK += 1
                total +=1
            elif (state == "arizona"):
                AZ += 1
                total +=1
            elif (state == "arkansas"):
                AR += 1
                total +=1
            elif (state == "california"):
                CA += 1
                total +=1
            elif (state == "colorado"):
                CO += 1
                total +=1
            elif (state == "connecticut"):
                CT += 1
                total +=1
            elif (state == "delaware"):
                DE += 1
                total +=1
            elif (state == "district of columbia"):
                DC += 1
                total +=1
            elif (state == "florida"):
                FL += 1
                total +=1
            elif (state == "georgia"):
                GA += 1
                total +=1
            elif (state == "hawaii"):
                HI += 1
                total +=1
            elif (state == "idaho"):
                ID += 1
                total +=1
            elif (state == "illinois"):
                IL += 1
                total +=1
            elif (state == "indiana"):
                IN += 1
                total +=1
            elif (state == "iowa"):
                IA += 1
                total +=1
            elif (state == "kansas"):
                KS += 1
                total +=1
            elif (state == "kentucky"):
                KY += 1
                total +=1
            elif (state == "louisiana"):
                LA += 1
                total +=1
            elif (state == "maine"):
                ME += 1
                total +=1
            elif (state == "maryland"):
                MD += 1
                total +=1
            elif (state == "massachusetts"):
                MA += 1
                total +=1
            elif (state == "michigan"):
                MI += 1
                total +=1
            elif (state == "minnesota"):
                MN += 1
                total +=1
            elif (state == "mississippi"):
                MS += 1
                total +=1
            elif (state == "missouri"):
                MO += 1
                total +=1
            elif (state == "montana"):
                MT += 1
                total +=1
            elif (state == "nebraska"):
                NE += 1
                total +=1
            elif (state == "nevada"):
                NV += 1
                total +=1
            elif (state == "new hampshire"):
                NH += 1
                total +=1
            elif (state == "new jersey"):
                NJ += 1
                total +=1
            elif (state == "new mexico"):
                NM += 1
                total +=1
            elif (state == "new york"):
                NY += 1
                total +=1
            elif (state == "north carolina"):
                NC += 1
                total +=1
            elif (state == "north dakota"):
                ND += 1
                total +=1
            elif (state == "ohio"):
                OH += 1
                total +=1
            elif (state == "oklahoma"):
                OK += 1
                total +=1
            elif (state == "oregon"):
                OR += 1
                total +=1
            elif (state == "penna"):
                PA += 1
                total +=1
            elif (state == "rhode island"):
                RI += 1
                total +=1
            elif (state == "south carolina"):
                SC += 1
                total +=1
            elif (state == "south dakota"):
                SD += 1
                total +=1
            elif (state == "tennessee"):
                TN += 1
                total +=1
            elif (state == "texas"):
                TX += 1
                total +=1
            elif (state == "utah"):
                UT += 1
                total +=1
            elif (state == "vermont"):
                VT += 1
                total +=1
            elif (state == "virginia"):
                VA += 1
                total +=1
            elif (state == "washington"):
                WA += 1
                total +=1
            elif (state == "west virginia"):
                WV += 1
                total +=1
            elif (state == "wisconsin"):
                WI += 1
                total +=1
            elif (state == "wyoming"):
                WY += 1
                total +=1
            else:
                id = row['_id']
                db_usa.tu.remove( { '_id': id } )
                print 'removed'
    print n
    n+=1


td = float(100)/float(total)



ALp=AL*td; AKp=AK*td; AZp=AZ*td; ARp=AR*td; CAp=CA*td; COp=CO*td; CTp=CT*td; DEp=DE*td; DCp=DC*td; FLp=FL*td; GAp=GA*td;
HIp=HI*td; IDp=ID*td; ILp=IL*td; INp=IN*td; IAp=IA*td; KSp=KS*td; KYp=KY*td; LAp=LA*td; MEp=ME*td; MDp=MD*td; MAp=MA*td;
MIp=MI*td; MNp=MN*td; MSp=MS*td; MOp=MO*td; MTp=MT*td; NEp=NE*td; NVp=NV*td; NHp=NH*td; NJp=NJ*td; NMp=NM*td; NYp=NY*td;
NCp=NC*td; NDp=ND*td; OHp=OH*td; OKp=OK*td; ORp=OR*td; PAp=PA*td; RIp=RI*td; SCp=SC*td; SDp=SD*td; TNp=TN*td; TXp=TX*td;
UTp=UT*td; VTp=VT*td; VAp=VA*td; WAp=WA*td; WVp=WV*td; WIp=WI*td; WYp=WY*td;

wd = csv.writer(open("PenumonitisTweets_States.csv", "w"))
wd.writerow(('Postal Code','Penumonitis_Tweets','Percentage'))
wd.writerow(('AL',AL,ALp))
wd.writerow(('AK',AK,AKp))
wd.writerow(('AZ',AZ,AZp))
wd.writerow(('AR',AR,ARp))
wd.writerow(('CA',CA,CAp))
wd.writerow(('CO',CO,COp))
wd.writerow(('CT',CT,CTp))
wd.writerow(('DE',DE,DEp))
wd.writerow(('DC',DC,DCp))
wd.writerow(('FL',FL,FLp))
wd.writerow(('GA',GA,GAp))
wd.writerow(('HI',HI,HIp))
wd.writerow(('ID',ID,IDp))
wd.writerow(('IL',IL,ILp))
wd.writerow(('IN',IN,INp))
wd.writerow(('IA',IA,IAp))
wd.writerow(('KS',KS,KSp))
wd.writerow(('KY',KY,KYp))
wd.writerow(('LA',LA,LAp))
wd.writerow(('ME',ME,MEp))
wd.writerow(('MD',MD,MDp))
wd.writerow(('MA',MA,MAp))
wd.writerow(('MI',MI,MIp))
wd.writerow(('MN',MN,MNp))
wd.writerow(('MS',MS,MSp))
wd.writerow(('MO',MO,MOp))
wd.writerow(('MT',MT,MTp))
wd.writerow(('NE',NE,NEp))
wd.writerow(('NV',NV,NVp))
wd.writerow(('NH',NH,NHp))
wd.writerow(('NJ',NJ,NJp))
wd.writerow(('NM',NM,NMp))
wd.writerow(('NY',NY,NYp))
wd.writerow(('NC',NC,NCp))
wd.writerow(('ND',ND,NDp))
wd.writerow(('OH',OH,OHp))
wd.writerow(('OK',OK,OKp))
wd.writerow(('OR',OR,ORp))
wd.writerow(('PA',PA,PAp))
wd.writerow(('RI',RI,RIp))
wd.writerow(('SC',SC,SCp))
wd.writerow(('SD',SD,SDp))
wd.writerow(('TN',TN,TNp))
wd.writerow(('TX',TX,TXp))
wd.writerow(('UT',UT,UTp))
wd.writerow(('VT',VT,VTp))
wd.writerow(('VA',VA,VAp))
wd.writerow(('WA',WA,WAp))
wd.writerow(('WV',WV,WVp))
wd.writerow(('WI',WI,WIp))
wd.writerow(('WY',WY,WYp))

