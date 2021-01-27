import numpy as np
import pandas as pd

# build a dataframe for each Dynamics export table

products = pd.read_csv('product-order.csv')

print(products)

# build a dataframe for each Salesforce object

# build the mapping list

# for each Salesforce object,
#   run its mapping to get data from Dynamics df into Salesforce df, then
#   for each df, clean each series to put into Salesforce shape