import pandas as pd
from scrape_linkedin import ProfileScraper, scrape_in_parallel

profiles = pd.read_csv('ea_list.csv',names=['link'])

profiles['short_cut'] = profiles.link.apply(lambda x: x.split('/in/')[-1])

# df = []
# for i in range(len(profiles)):
#         try:
#             profile = scraper.scrape(user=profiles.iloc[i,1])
#             profile_dict  = profile.to_dict()
#             df.append(profile_dict)
#         except:
#             pass
#
# df = pd.io.json.json_normalize(df)

if __name__ == '__main__':

    scrape_in_parallel(
        scraper_type=ProfileScraper,
        items=profiles.short_cut.tolist(),
        output_file="../data/ea_profiles.json",
        num_instances=20
    )
