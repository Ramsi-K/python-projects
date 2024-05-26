import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world['area']>=3000000) | (world['population']>=25000000)][['name','population','area']]
    # res = []
    # for i, row in world.iterrows():
    #     if row.area >= 3000000 or row.population >= 25000000:
    #         res.append([row["name"], row.population, row.area])
    
    # res = pd.DataFrame(res, columns = ["name", "population", "area"])

    # return res
