import streamlit as st
import requests
import pandas as pd

url = "https://investidor10.com.br/api/historico-indicadores/18/10"


headers = {
    "accept": "*/*",
    "referer": "https://investidor10.com.br/acoes/vale3/",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36",
    "x-csrf-token": "Nb1lpOfCPfB0PA9z4gg4VY0WL0FRM6dpyUYNdKaq",
    "x-requested-with": "XMLHttpRequest"
}

st.set_page_config(page_title="Vale3", page_icon=":chart_with_upwards_trend:", layout="wide")

response = requests.get(url, headers=headers)
if response.status_code == 200:
    try:
        data = response.json()
        df = pd.DataFrame([item for sublist in data.values() for item in sublist])
        df_pivot = df.pivot(index="key", columns="year", values="value")
        anos = ["Atual", 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2014]
        df_pivot = df_pivot.loc[:, anos]
        st.title("HISTÓRICO DE INDICADORES FUNDAMENTALISTAS VALE3")
        st.write(df_pivot)
       
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
else:
    print(f"Request failed with status code {response.status_code}")
