import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views[views.author_id == views.viewer_id][["author_id"]].drop_duplicates().sort_values(by="author_id", ignore_index=True).rename(columns={"author_id": "id"})