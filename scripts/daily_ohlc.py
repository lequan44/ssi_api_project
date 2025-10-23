import time
from datetime import date
import pandas as pd
import requests
import get_config

current_date = date.today()
current_date_path = current_date.strftime("%Y%m%d")
print("Current Date:", current_date_path)

url = "https://fc-data.ssi.com.vn/api/v2/Market/DailyOhlc"
headers = {
    "Authorization": f"Bearer {get_config.access_token}",
    "Content-Type": "application/json"
}

df = pd.DataFrame()
data_date = current_date.strftime('%d/%m/%Y')

for index in range(1, 10):
    params = {
            "fromDate": data_date,
            "toDate": data_date,
            "pageIndex": index,
            "pageSize": 1000
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json().get('data', [])
    df_response = pd.DataFrame(data)
    df = pd.concat([df, df_response], ignore_index=True)
    time.sleep(1)
    if len(df_response) == 0:
        break

# Export to csv file
output_dir = '~/ssi_api_data/daily_ohlc'
df.to_csv(f"{output_dir}/ohlc_{current_date_path}.csv", index=False,encoding='utf-8-sig')