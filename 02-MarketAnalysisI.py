# Problem 2 - Market Analysis I (https://leetcode.com/problems/market-analysis-i/description/)
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Filter orders made in 2019
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    orders_2019 = orders[orders['order_date'].dt.year == 2019]

    # Step 2: Count orders in 2019 per buyer
    buyer_counts = orders_2019.groupby('buyer_id').size().reset_index(name='orders_in_2019')

    # Step 3: Merge with users
    result = users.merge(buyer_counts, how='left', left_on='user_id', right_on='buyer_id')

    # Step 4: Fill NaN with 0 and cast to int
    result['orders_in_2019'] = result['orders_in_2019'].fillna(0).astype(int)

    # Step 5: Select final columns and rename
    return result[['user_id', 'join_date', 'orders_in_2019']].rename(columns={'user_id': 'buyer_id'})