# Problem 1 - Sales Analysis III (https://leetcode.com/problems/sales-analysis-iii/description/)
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.groupby(['product_id'])['sale_date'].agg(['min', 'max']).reset_index()
    res = df[(df['max'] <= '2019-03-31') & (df['min'] >= '2019-01-01')]
    df = product.merge(res, on = 'product_id', how = 'inner')
    return df[['product_id', 'product_name']]