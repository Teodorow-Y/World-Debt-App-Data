from os import getenv
import shimoku_api_python as Shimoku
import web_panel as html
import funtions 


def main():
    #----------------- CLIENT INITIALIZATION ----------------#   

    s = Shimoku.Client(
        local_port=8040,
        verbosity='INFO',
        async_execution=True
    )
    # WorkSpace is empty to work in LOCAL SERVER
    s.set_workspace('World App Data')
    s.set_menu_path('Country Debt')

    #--------------- CREATE DASHBOARD TASKS ----------------#
    #Header
    html.page_header(                 s, 0)

    #Distribution
    html.distribution_header(         s, 2)

    #Tree Country Map
    html.tree_world(                  s,3)
    funtions.tree_world_table(        s,5)

    #Table Country
    html.world_table(                 s,8)
    funtions.world_list_table(        s,10)
    
    html.next_best_product_header(    s, 12)


    #------------------ EXECUTE ALL TASKS -----------------#
    s.run()


if __name__ == '__main__':
    main()