import time
from datetime import date,timedelta
import pandas as pd
import requests
import get_config

current_date = date.today()
current_date_path = current_date.strftime("%Y%m%d")
print("Current Date:", current_date_path)

start_date = (date.today() - timedelta(days = 0)).strftime('%d/%m/%Y')
end_date = (date.today() - timedelta(days = 0)).strftime('%d/%m/%Y')

# Get index list
url = "https://fc-data.ssi.com.vn/api/v2/Market/IndexList"
headers = {
    "Authorization": f"Bearer {get_config.access_token}",
    "Content-Type": "application/json"
}
params = {
    "pageIndex": 1,
    "pageSize": 1000
}
# Send the GET request
response = requests.get(url, headers=headers,params=params)
# Extract data from the response JSON
data = response.json().get('data', [])
index_list = [data[i]['IndexCode'] for i in range(len(data))]
df = pd.DataFrame(data)
# print(index_list)
# print(len(index_list))

output_dir = '~/ssi_api_data/index_list'
df.to_csv(f"{output_dir}/index_list_{current_date_path}.csv", index=False,encoding='utf-8-sig')
print(f"File exported successfully to {output_dir}")

