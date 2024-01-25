import aiohttp
import pandas as pd

async def get_ts(series_list, api_key=None):
    if not api_key:
        raise ValueError("API key is required")

    all_series_data = []
    for series in series_list:
        url = f'https://api.eia.gov/v2/seriesid/{series}?api_key={api_key}'

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise Exception(f"Error fetching data for series {series}: {response.status}")
                json_response = await response.json()

        series_name = json_response.get('response').get('data')[0].get('series-description')
        series_data = pd.DataFrame(json_response.get('response').get('data'), columns=['period', 'value'])
        series_data.rename(columns={'value': series_name}, inplace=True)
        all_series_data.append(series_data)

    # Combine all series data into a single DataFrame
    combined_df = pd.concat(all_series_data, axis=1)
    return combined_df

# import aiohttp
# import pandas as pd

# async def get_ts(series, api_key=None):
#     if not api_key:
#         raise ValueError("API key is required")

#     url = f'https://api.eia.gov/v2/seriesid/{series}?api_key={api_key}'
    
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             if response.status != 200:
#                 raise Exception(f"Error fetching data: {response.status}")
#             json_response = await response.json()

#     # Process the JSON response
#     nome = json_response.get('response').get('data')[0].get('series-description')
#     df = pd.DataFrame(json_response.get('response').get('data'), columns=['period', 'value'])

#     #df_ts = df[['period', 'value']].copy()
#     #df_ts = df_ts.set_index('period')
#     df_ts.columns = [period,nome]
#     return df
    