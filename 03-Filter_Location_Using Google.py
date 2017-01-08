__author__ = 'Abduljaleel'
from twitter import *
import time
from pymongo import *
from db_sqlite3 import sqlite3
import geopy
import sys
from geopy.geocoders import GoogleV3

reload(sys)
sys.setdefaultencoding("utf8")
geolocator = GoogleV3()

#Access the twitter app
CON_key = 'c2zHl8hyYPcnRcqtjchJZwMb5'
CON_secret = 'u0i3NYcO6nZNn8JjT5cc7PDwEZMMfnRU9jewZ68eqA9qlqHLhw'
ACCESS_key = '61739184-EBxmw8OxMtOKWGXyE2Tvx9mioTOzy5FF22xld0QV6'
ACCESS_secret = '8tuGKkfaJBGsONt8UQrhx37f2RsbwD28UJrCKdRvgaSzw'

# usa,states,cities
usa = ' USA US U.S.A U.S. U.S U.S.A. united states of america '
states = ' AL AK AZ AR CA CO CT DE DC D.C. D.C FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM ' \
         ' NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY ' \
         ' Alabama Alaska Arizona Arkansas California Colorado Connecticut Delaware Florida Georgia Hawaii Idaho Illinois ' \
         ' Indiana Iowa Kansas Kentucky Louisiana Maine Maryland Massachusetts Michigan Minnesota Mississippi Missouri Montana ' \
         ' Nebraska Nevada New Hampshire New Jersey New Mexico New York North Carolina North Dakota Ohio Oklahoma Oregon ' \
         ' Pennsylvania Rhode Island South Carolina South Dakota Tennessee Texas Utah Vermont Virginia Washington West Virginia ' \
         ' Wisconsin Wyoming District of Columbia penna '
cities = ' Aberdeen Abilene Akron Albany Albuquerque Alexandria Allentown Amarillo Anaheim Anchorage Ann Arbor Antioch Apple Valley ' \
         ' Appleton Arlington Arvada Asheville Athens Atlanta Atlantic City Augusta Aurora Austin Bakersfield Baltimore Barnstable ' \
         ' Baton Rouge Beaumont Bel Air Bellevue Berkeley Bethlehem Billings Birmingham Bloomington Boise City Bonita Springs Boston ' \
         ' Boulder Bradenton Bremerton Bridgeport Brighton Brownsville Bryan Buffalo Burbank Burlington Cambridge Canton Cape Coral ' \
         ' Carrollton Cary Cathedral City Cedar Rapids Champaign Chandler Charleston Charlotte Chattanooga Chesapeake Chicago Chula ' \
         ' Vista Cincinnati Clarke County Clarksville Clearwater Cleveland College Station Colorado Springs Columbia Columbus Concord ' \
         ' Coral Springs Corona Corpus Christi Costa Mesa Dallas Daly City Danbury Davenport Davidson County Dayton Daytona Beach Deltona ' \
         ' Denton Denver Des Moines Detroit Downey Duluth Durham El Monte El Paso Elizabeth Elk Grove Elkhart Erie Escondido Eugene ' \
         ' Evansville Fairfield Fargo Fayetteville Fitchburg Flint Fontana Fort Collins Fort Lauderdale Fort Smith Fort Walton Beach ' \
         ' Fort Wayne Fort Worth Frederick Fremont Fresno Fullerton Gainesville Garden Grove Garland Gastonia Gilbert Glendale Grand ' \
         ' Prairie Grand Rapids Grayslake Green Bay GreenBay Greensboro Greenville Gulfport-Biloxi Hagerstown Hampton Harlingen Harrisburg ' \
         ' Hartford Havre de Grace Hayward Hemet Henderson Hesperia Hialeah Hickory High Point Hollywood Honolulu Houma Houston Howell ' \
         ' Huntington Beach Huntsville Independence Indianapolis Inglewood Irvine Irving Jackson Jacksonville Jefferson Jersey City ' \
         ' Johnson City Joliet Kailua Kalamazoo Kaneohe Kansas City Kennewick Kenosha Killeen Kissimmee Knoxville Lacey Lafayette ' \
         ' Lake Charles Lakeland Lakewood Lancaster Lansing Laredo Las Cruces Las Vegas Layton Leominster Lewisville Lexington Lincoln ' \
         ' Little Rock Long Beach Lorain Los Angeles Louisville Lowell Lubbock Macon Madison Manchester Marina Marysville McAllen McHenry ' \
         ' Medford Melbourne Memphis Merced Mesa Mesquite Miami Milwaukee Minneapolis Miramar Mission Viejo Mobile Modesto Monroe Monterey ' \
         ' Montgomery Moreno Valley Murfreesboro Murrieta Muskegon Myrtle Beach Naperville Naples Nashua Nashville New Bedford New Haven ' \
         ' New London New Orleans New York New York City Newark Newburgh Newport News Norfolk Normal Norman North Charleston North Las Vegas ' \
         ' North Port Norwalk Norwich Oakland Ocala Oceanside Odessa Ogden Oklahoma City Olathe Olympia Omaha Ontario Orange Orem Orlando ' \
         ' Overland Park Oxnard Palm Bay Palm Springs Palmdale Panama City Pasadena Paterson Pembroke Pines Pensacola Peoria Philadelphia ' \
         ' Phoenix Pittsburgh Plano Pomona Pompano Beach Port Arthur Port Orange Port Saint Lucie Port St. Lucie Portland Portsmouth ' \
         ' Poughkeepsie Providence Provo Pueblo Punta Gorda Racine Raleigh Rancho Cucamonga Reading Redding Reno Richland Richmond ' \
         ' Richmond County Riverside Roanoke Rochester Rockford Roseville Round Lake Beach Sacramento Saginaw Saint Louis Saint Paul ' \
         ' Saint Petersburg Salem Salinas Salt Lake City San Antonio San Bernardino San Buenaventura San Diego San Francisco SF San Jose ' \
         ' Santa Ana Santa Barbara Santa Clara Santa Clarita Santa Cruz Santa Maria Santa Rosa Sarasota Savannah Scottsdale Scranton Seaside ' \
         ' Seattle Sebastian Shreveport Simi Valley Sioux City Sioux Falls South end South Lyon Spartanburg Spokane Springdale Springfield ' \
         ' St. Louis St. Paul St. Petersburg Stamford Sterling Heights Stockton Sunnyvale Syracuse Tacoma Tallahassee Tampa Temecula Tempe ' \
         ' Thornton Thousand Oaks Toledo Topeka Torrance Trenton Tucson Tulsa Tuscaloosa Tyler Utica Vallejo Vancouver Vero Beach Victorville ' \
         ' Virginia Beach Visalia Waco Warren Washington Waterbury Waterloo West Covina West Valley City Westminster Wichita Wilmington Winston ' \
         ' Winter Haven Worcester Yakima Yonkers York Youngstown nyc '

#connecting to MongoDB 1
connection = Connection()
database = connection.twit_filtered
t_mongo = database.tdf
twit = t_mongo.find()
print twit.count()


#connecting to MongoDB 2
db_usa = connection.twit_usa
t_u = db_usa.tu
tw = t_u.find()
print tw.count()

#small SQLite DB for the counter
db = sqlite3.connect('counterdb')
c = db.cursor()

# SQLite DB for matching loc and address
db_match = sqlite3.connect('matchdb')
c_m = db_match.cursor()

# Sqlite DB for locstr
db_locstr = sqlite3.connect('locstr')
c_loc = db_locstr.cursor()

def abv_to_state(kk):
    if kk == "al":
        return "Alabama"
    if kk == "ak":
        return "Alaska"
    if kk == "az":
        return "Arizona"
    if kk == "ar":
        return "Arkansas"
    if kk == "ca":
        return "California"
    if kk == "co":
        return "Colorado"
    if kk == "ct":
        return "Connecticut"
    if kk == "de":
        return "Delaware"
    if kk == "fl":
        return "Florida"
    if kk == "ga":
        return "Georgia"
    if kk == "hi":
        return "Hawaii"
    if kk == "id":
        return "Idaho"
    if kk == "il":
        return "Illinois"
    if kk == "in":
        return "Indiana"
    if kk == "ia":
        return "Iowa"
    if kk == "ks":
        return "Kansas"
    if kk == "ky":
        return "Kentucky"
    if kk == "la":
        return "Louisiana"
    if kk == "me":
        return "Maine"
    if kk == "md":
        return "Maryland"
    if kk == "ma":
        return "Massachusetts"
    if kk == "mi":
        return "Michigan"
    if kk == "mn":
        return "Minnesota"
    if kk == "ms":
        return "Mississippi"
    if kk == "mo":
        return "Missouri"
    if kk == "mt":
        return "Montana"
    if kk == "ne":
        return "Nebraska"
    if kk == "nv":
        return "Nevada"
    if kk == "nh":
        return "New Hampshire"
    if kk == "nj":
        return "New Jersey"
    if kk == "nm":
        return "New Mexico"
    if kk == "ny":
        return "New York"
    if kk == "nc":
        return "North Carolina"
    if kk == "nd":
        return "North Dakota"
    if kk == "oh":
        return "Ohio"
    if kk == "ok":
        return "Oklahoma"
    if kk == "or":
        return "Oregon"
    if kk == "pa":
        return "Pennsylvania"
    if kk == "ri":
        return "Rhode Island"
    if kk == "sc":
        return "South Carolina"
    if kk == "sd":
        return "South Dakota"
    if kk == "tn":
        return "Tennessee"
    if kk == "tx":
        return "Texas"
    if kk == "ut":
        return "Utah"
    if kk == "vt":
        return "Vermont"
    if kk == "va":
        return "Virginia"
    if kk == "wa":
        return "Washington"
    if kk == "wv":
        return "West Virginia"
    if kk == "wi":
        return "Wisconsin"
    if kk == "wy":
        return "Wyoming"
    if kk == "dc":
        return "District of Columbia"
    else:
        return kk

def pars_address(usadd):

    spli = usadd.split(',')
    g_len = len(spli)

    state = ''
    city = ''
    if spli[g_len-1] == " United States of America":
        for x in range(0,g_len-1):
            if spli[x].lower() in states.lower():
                state = spli[x]
                if (x!=0):
                    if 'County' in spli[x-1]:
                        if (x-1!=0):
                            city = spli[x-2]
                            break
                    else:
                        city = spli[x-1]
                        break

    ddd = [city,state]
    return ddd

def pars_address2(loc):
    spli = loc.split(',')
    l = len(spli)
    city = ''
    state = ''
    if l != 0:
        if l-1 != 0:
            spli2 = spli[l-2].split(' ')
            l2 = len(spli2)
            if (spli2[l2-1].isdigit() == False):
                state = spli[l-2]
            else:
                for i in range (0,l2-1):
                    state += spli2[i] +' '
            if (l-2) > 0:
                city = spli[l-3]
    dd=[city,state]
    return dd

def update(n):
    sql = "UPDATE COUNTER SET COUNT ="+str(n)+" WHERE ID ="+str(1)

    try:
        c.execute(sql)
        db.commit()
    except:
        db.rollback()

def counter():
    sql = "SELECT * FROM COUNTER WHERE ID ="+str(1)

    try:
        c.execute(sql)
        db.commit()
    except:
        db.rollback()

    results = c.fetchall()
    for res in results:
        uu = res[1]
        break
    return uu

def update2(n):
    sql = "UPDATE COUNTER SET COUNT ="+str(n)+" WHERE ID ="+str(2)

    try:
        c.execute(sql)
        db.commit()
    except:
        db.rollback()

def update3(n):
    sql = "UPDATE COUNTER SET COUNT ="+str(n)+" WHERE ID ="+str(3)

    try:
        c.execute(sql)
        db.commit()
    except:
        db.rollback()

def counter2():
    sql = "SELECT * FROM COUNTER WHERE ID ="+str(2)

    try:
        c.execute(sql)
        db.commit()
    except:
        db.rollback()

    results = c.fetchall()

    for res in results:
        uu = res[1]
        break
    return uu

def counter3():
    sql = "SELECT * FROM COUNTER WHERE ID ="+str(3)

    try:
        c.execute(sql)
        db.commit()
    except:
        db.rollback()

    results = c.fetchall()

    for res in results:
        uu = res[1]
        break
    return uu

def insert_into_match(loc1,loc2):
    sql = "INSERT INTO MATCH VALUES ('"+str(loc1)+"','"+str(loc2)+"')"
    try:
        c_m.execute(sql)
        db_match.commit()
    except:
        db_match.rollback()

def find_in_match(loc_find):
    uu = ''
    sql = "SELECT * FROM MATCH WHERE LOC = '"+str(loc_find)+"'"
    try:
        c_m.execute(sql)
        db_match.commit()
    except:
        db_match.rollback()

    results = c_m.fetchall()
    for res in results:
        uu = res[1]
    return uu

def update_loc(loc):
    sql = "UPDATE LOCSTRING SET LOCS = '"+str(loc)+"' WHERE ID ="+str(1)
    try:
        c_loc.execute(sql)
        db_locstr.commit()
    except:
        db_locstr.rollback()

def read_loc():
    sql = "SELECT * FROM LOCSTRING WHERE ID ="+str(1)
    try:
        c_loc.execute(sql)
        db_locstr.commit()
    except:
        db_locstr.rollback()

    results = c_loc.fetchall()
    for res in results:
        uu = res[1]
        break
    return uu


# WHEN YOU START WITH A NEW IP SET GOOGLE_USAGE WITH ZERO
# update3(0)

google_usage = counter3()
count = counter()
mm = counter2()
print "initial count (n) = "+ str(count)
print "geo_loc count (mm) = "+ str(mm)
print "---------------------------------"


n=0
outloop = 0
for row in twit:
    if n < count:
        n+=1
    else:
        loc = row['user']['location']
        sep = loc.split(',')
        sl = len(sep)
        if loc != "":
            if (sl == 1):
                if ' '+sep[0].lower()+' ' in usa.lower():
                    t_u.insert({'city': "", 'state': "", 'data': row})
                    mm+=1
                    print str(mm)+' - (USA) / ('+ str(row['created_at']) +') ** MY'
                else:
                    if (' ' + sep[0].lower()+' ' in states.lower()):
                        st_name = abv_to_state(sep[0].lower())
                        t_u.insert({'city': "", 'state': st_name, 'data': row})
                        mm+=1
                        print str(mm)+' - (state = '+st_name+') / ('+ str(row['created_at']) +') ** MY'
                    else:
                        g = ''
                        g = find_in_match(loc)
                        if g != '':
                            if " America" in g:
                                ctst = pars_address(g)
                                t_u.insert({'city': ctst[0], 'state': ctst[1], 'data': row})
                                mm+=1
                                print str(mm)+' - ( city = '+ctst[0]+', state = '+ctst[1]+') / ('+ str(row['created_at']) +') -- Found in Match'
                            else:
                                if " USA" in g:
                                    ctst = pars_address2(g)
                                    t_u.insert({'city': ctst[0], 'state': ctst[1], 'data': row})
                                    mm+=1
                                    print str(mm)+' - ( city = '+ctst[0]+', state = '+ctst[1]+') / ('+ str(row['created_at']) +') -- Found in Match'
                        else:
                            LIMIT = False

                            if (google_usage >2495):
                                LIMIT = True
                                update3(0)
                                break
                            try:
                                google_usage +=1
                                geoloc = geolocator.geocode(loc)
                                time.sleep(0.5)
                                if " America" in geoloc.address:
                                    ctst = pars_address(geoloc.address)
                                    t_u.insert({'city': ctst[0], 'state': ctst[1], 'data': row})
                                    mm+=1
                                    print str(mm)+' - ( city = '+ctst[0]+', state = '+ctst[1]+' ) / ('+ str(row['created_at']) +') -- Using Google'
                                if " USA" in geoloc.address:
                                    ctst = pars_address2(geoloc.address)
                                    t_u.insert({'city': ctst[0], 'state': ctst[1], 'data': row})
                                    mm+=1
                                    print str(mm)+' - ( city = '+ctst[0]+', state = '+ctst[1]+' ) / ('+ str(row['created_at']) +') -- Using Google'
                                insert_into_match(loc,geoloc.address)

                            except geopy.exc.GeocoderQueryError as badRequest:
                                print '.................................ERROR2:',badRequest
                                insert_into_match(loc,"-")

                            except Exception as ex:
                                print '.................................ERROR3:',ex
                                if str(ex) == "<urlopen error [Errno 65] No route to host>":
                                    print "Check the Connection"
                                    break
                                print loc
                                insert_into_match(loc,"-")

                            except geopy.exc.GeocoderTimedOut as timeout:
                                print '.................................ERROR1:',timeout
                                if str(ex) == "<urlopen error [Errno 65] No route to host>":
                                    print "Check the Connection"
                                    break
                                print loc
                                insert_into_match(loc,"-")


                            if (LIMIT == True):
                                update(n)
                                update2(mm)
                                break

            else:
                if (sep[0].lower() in cities.lower()) and (sep[1].lower() in states.lower()):
                    t_u.insert({'city': sep[0], 'state': sep[1], 'data': row})
                    mm+=1
                    print str(mm)+' - ( city = '+sep[0]+', state = '+sep[1]+') / ('+ str(row['created_at']) +') ** MY'
                else:
                    g = ''
                    g = find_in_match(loc)
                    if g != '':
                        if " America" in g:
                            ctst = pars_address(g)
                            t_u.insert({'city': ctst[0], 'state': ctst[1], 'data': row})
                            mm+=1
                            print str(mm)+' - ( city = '+ctst[0]+', state = '+ctst[1]+') / ('+ str(row['created_at']) +') -- found in Match'
                        if " USA" in g:
                            ctst = pars_address2(g)
                            t_u.insert({'city': ctst[0], 'state': ctst[1], 'data': row})
                            mm+=1
                            print str(mm)+' - ( city = '+ctst[0]+', state = '+ctst[1]+') / ('+ str(row['created_at']) +') -- Found in Match'
                    else:
                        # Use google reverse geocoding when the location's length is One
                        LIMIT = False
                        if (google_usage >2495):
                            LIMIT = True
                            update3(0)
                            break
                        try:
                            google_usage +=1
                            geoloc = geolocator.geocode(loc)
                            time.sleep(0.5)
                            if " America" in geoloc.address:
                                ctst = pars_address(geoloc.address)
                                t_u.insert({'city': ctst[0], 'state': ctst[1], 'data': row})
                                mm+=1
                                print str(mm)+' - ( city = '+ctst[0]+', state = '+ctst[1]+') / ('+ str(row['created_at']) +') -- Using Google'
                            if " USA" in geoloc.address:
                                ctst = pars_address2(geoloc.address)
                                t_u.insert({'city': ctst[0], 'state': ctst[1], 'data': row})
                                mm+=1
                                print str(mm)+' - ( city = '+ctst[0]+', state = '+ctst[1]+' ) / ('+ str(row['created_at']) +') -- Using Google'
                            insert_into_match(loc,geoloc.address)

                        except geopy.exc.GeocoderQueryError as badRequest:
                            print '.................................ERROR2:',badRequest
                            insert_into_match(loc,"-")
                        except Exception as ex:
                            print '.................................ERROR3:',ex
                            if str(ex) == "<urlopen error [Errno 65] No route to host>":
                                print "Check the Connection"
                                break
                            print loc
                            insert_into_match(loc,"-")

                        except geopy.exc.GeocoderTimedOut as timeout:
                            print '.................................ERROR1:',timeout
                            if str(ex) == "<urlopen error [Errno 65] No route to host>":
                                print "Check the Connection"
                                break
                            print loc

                            # end of while
                        if (LIMIT == True):
                            update(n)
                            update2(mm)
                            break
        n+=1
        update(n)
        update2(mm)
        update3(google_usage)
        # if (n==200):
        #     break




# If break, we will be here
# All inside us loc out of all without geocode 449550