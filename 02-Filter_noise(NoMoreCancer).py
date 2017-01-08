__author__ = 'Abduljaleel'

from twitter import *
import time
from pymongo import *
from db_sqlite3 import sqlite3
import geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim()
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

#Access the twitter app
CON_key = 'c2zHl8hyYPcnRcqtjchJZwMb5'
CON_secret = 'u0i3NYcO6nZNn8JjT5cc7PDwEZMMfnRU9jewZ68eqA9qlqHLhw'
ACCESS_key = '61739184-EBxmw8OxMtOKWGXyE2Tvx9mioTOzy5FF22xld0QV6'
ACCESS_secret = '8tuGKkfaJBGsONt8UQrhx37f2RsbwD28UJrCKdRvgaSzw'

# us,states,cities
usa = ' USA US U.S.A U.S. U.S U.S.A. united states of america '

states = ' AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM ' \
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
         ' Winter Haven Worcester Yakima Yonkers York Youngstown nyc'

#connecting to MongoDB 1
connection = Connection()
database = connection.twitterdatas8
t_mongo = database.twitterdb8

#connecting to MongoDB 2
db_filtered28 = connection.twit_filtered8
t_f = db_filtered28.tdf8

twit = t_mongo.find()
print twit.count()
#
tw = t_f.find()
print tw.count()

n=0
for row in twit:
    if 'text' in row:
        if "more for cancer" not in row['text'].lower():
            print row['created_at']
            n+=1
            t_f.insert(row)



