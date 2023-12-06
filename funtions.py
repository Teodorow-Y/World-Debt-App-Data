from os import getenv
import shimoku_api_python as Shimoku
import pandas as pd
import source.scraping as scraping 


#----------------- DATA INITIALIZATION ----------------# 
data_countries = scraping.adding_to_dict()
date = [scraping.nd] 


#----------------- TREE MAP ----------------# 
def tree_world_table(s: Shimoku, order: int) -> int:

    s.plt.treemap(
    data=date, order=order,
    title='Total Debt from each country - World',
    rows_size=8, 
    cols_size=15, padding='0,0,0,0',    
)
    return order+1

#----------------- WORLD TABLE ----------------# 
def world_list_table(s: Shimoku, order: int) -> int: 
    table = data_countries
    color_dict = {
        'Low': 'active',
        'Medium': 'caution',
        'Critical': 'error',
    }
    s.plt.table(
            title = 'Country Table',
            data=table,
            initial_sort_column='Country', sort_descending=True,
            order=order+1,
            page_size_options=[3, 5,10],
            cols_size=22,
            label_columns={
                'level': color_dict,
            },
            columns_options={
            'Country': {'width': 180},
            'Deuda_total': {'width': 180},
            'Deuda_Per_Capita': {'width': 260},            
            'Deuda_PIB': {'width': 200},
            'level': {'width': 250}
        }
        )
    return order+2


