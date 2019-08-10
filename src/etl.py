import pandas as pd
import numpy  as np
import json
import os
from datetime import datetime as dt

def etl_profiles(json_file):
    df = pd.read_json(json_file,orient='index')
    df.to_json('temp.json',orient='records')
    with open('temp.json') as json_content:
        de_profile = json.load(json_content)
    de_profile = pd.DataFrame(pd.io.json.json_normalize(de_profile))
    os.remove('temp.json')
    de_profile.index = df.index
    return de_profile


def export_profiles(path):
    df = pd.concat([pd.DataFrame(x) for x in de_profile['experiences.jobs']], keys=de_profile.index).reset_index(level=1,drop=True)
    df.index.name = 'linkedin_url'
    df_date_range = df.date_range.str.split('–',expand=True).rename({0:'from',1:'to'},axis=1)
    df = pd.concat([df,df_date_range],axis=1)
    df.drop('date_range',axis=1,inplace=True)
    df['to'] = df.to.str.replace('Present',dt.today().strftime('%b %Y'))
    df['to'] = pd.to_datetime(df.to.str.strip())
    df['from'] = pd.to_datetime(df['from'].str.strip())
    df['experience_years'] = df.to - df['from']
    df['experience_years'] = pd.to_numeric(df.experience_years.apply(lambda x: x.days/365.25),errors='coerce')

    total_exp_year = df.groupby(df.index)['from','to'].agg({'from':'min','to':'max'})
    total_exp_year['total_exp_year'] = total_exp_year.to - total_exp_year['from']
    total_exp_year['total_exp_year'] = total_exp_year.total_exp_year.apply(lambda x: x.days/365.25)
    df = df.merge(total_exp_year.total_exp_year,'left',left_index=True,right_index=True)

    pi = de_profile[['personal_info.name','personal_info.headline','personal_info.summary','personal_info.email','personal_info.phone','personal_info.school']]


    res = pi.merge(df,'right',left_index=True,right_index=True)
    res.to_csv(path)

de_profile = etl_profiles('../data/ea_profiles.json')
export_profiles('../data/ea_profiles.csv')
