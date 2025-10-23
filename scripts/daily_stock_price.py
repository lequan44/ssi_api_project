from datetime import date
import pandas as pd
import requests
import get_config

current_date = date.today()
current_date_path = current_date.strftime("%Y%m%d")
print("Current Date:", current_date_path)

data_date = date.today().strftime('%d/%m/%Y')

url = " https://fc-data.ssi.com.vn/api/v2/Market/DailyStockPrice"
headers = {
    "Authorization": f"Bearer {get_config.access_token}",
    "Content-Type": "application/json"
}

# df = pd.DataFrame()
params = {
    "fromDate": data_date,
    "toDate": data_date,
    "pageIndex": 1,
    "pageSize": 1000,
}

# Send the GET request
response = requests.get(url, headers=headers,params=params)
# Extract data from the response JSON
data = response.json().get('data', [])
# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Export to csv file
output_dir = '~/ssi_api_data/daily_stock_price'
df.to_csv(f"{output_dir}/stock_price_{current_date_path}.csv", index=False,encoding='utf-8-sig')