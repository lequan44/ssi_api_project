import time
from datetime import date
import pandas as pd
import requests
import get_config

current_date = date.today()
current_date_path = current_date.strftime("%Y%m%d")
print("Current Date:", current_date_path)

url = "https://fc-data.ssi.com.vn/api/v2/Market/SecuritiesDetails"
headers = {
    "Authorization": f"Bearer {get_config.access_token}",
    "Content-Type": "application/json"
}

df = pd.DataFrame()

for index in range(1, 10):
    params = {
        "pageIndex": index,
        "pageSize": 1000
        }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()['data'][0]['RepeatedInfo']
    df_response = pd.DataFrame(data)
    df = pd.concat([df, df_response], ignore_index=True)
    time.sleep(1)
    if len(df_response) == 0:
        break

output_dir = '~/ssi_api_data/securities_details'
df.to_csv(f"{output_dir}/securities_{current_date_path}.csv", index=False,encoding='utf-8-sig')
print(f"File exported successfully to {output_dir}")
