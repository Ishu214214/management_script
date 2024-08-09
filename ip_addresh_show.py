from flask import Flask ,request ,jsonify
import requests
from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/')
def index():
    # for ip address
    ip_addr1 = request.remote_addr                                                                
    ip_addr2 = request.environ['REMOTE_ADDR']                                                
    ip_addr3 = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)  

    #   for page no
    page_name = request.path
    query_string = request.query_string.decode('utf-8')
    current_page = page_name + "?" + query_string

    # IP geolocation
    api_key = "your_api_key"
    url = f"http://api.ipinfodb.com/v3/ip-city/?key={api_key}&ip={ip_addr1}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        location_data = response.json()
        country = location_data.get('countryName')
        city = location_data.get('cityName')
        region = location_data.get('regionName')
        latitude = location_data.get('latitude')
        longitude = location_data.get('longitude')
    else:
        country, city, region, latitude, longitude = "", "", "", "", ""

    print(ip_addr1 , ip_addr2 ,ip_addr3)
    current_time = datetime.now(timezone.utc)
    return jsonify({'<h1> Your IP address is:<h1>': [ip_addr1 , ip_addr2 ,ip_addr3],
                        "user_agent": ip_addr3,
                        "ip_address": ip_addr1,
                        "page_name": page_name,
                        "query_string": query_string,
                        "current_page": current_page,
                        "country": country,
                        "city": city,
                        "region": region,
                        "latitude": latitude,
                        "longitude": longitude,
                        "current_time": current_time  
                    }) 

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)







