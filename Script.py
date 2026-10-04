import requests
import pandas as pd
all_dfs = []
for i in range(1, 501):
    url = f'https://api.themoviedb.org/3/trending/movie/day?api_key=/Enter Your API Here/&language=en-US&page={i}'.format(i)
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZWNmZjgwYTJjODRjYzBlODliYzFiNTZjZDNhMGE4ZCIsIm5iZiI6MTc4MTMyODk3MS41NzQwMDAxLCJzdWIiOiI2YTJjZWM0YmZmNjQ3NjkwZmZmZjE3N2UiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.wXOI83sFE8Fc2yuaqteh-4PGVPZjbqtq3kbaBY4BRao"
    }

    response = requests.get(url=url, headers=headers)
    results = response.json().get('results', [])
    df = pd.DataFrame(results)
    df = df[['id', 'title', 'original_title', 'overview', 'adult', 'original_language', 'popularity', 'release_date', 'vote_average', 'vote_count']]
    all_dfs.append(df)
    Final_Data = pd.concat(all_dfs, ignore_index=True)
Final_Data.to_csv('Trending_Movies_2026.csv',index=False)