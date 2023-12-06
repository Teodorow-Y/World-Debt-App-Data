import shimoku_api_python as Shimoku 
import pandas as pd

def page_header(shimoku_client: Shimoku.Client, order: int):

    shimoku_client.plt.html(
        order = 0, 
        html=shimoku_client.html_components.box_with_button(
            title='Country Debt - App Data',
            line='Analitycs about countries debt',
            background="https://media.discordapp.net/attachments/856397268193116180/1181864048342609971/8033685_12232.jpg?ex=65829bab&is=657026ab&hm=260edc91aa18dcd6e36b4fe73d22ee1c7aa2a1f59bbcded0821f491f5f6668ba&=&format=webp&width=1302&height=651",
            href='https://shimoku.com',
            button_text='Visit Shimoku',
        ),
    )
 

def distribution_header(shimoku_client: Shimoku.Client, order: int):
    prediction_header = (
    "<head>"
    "<style>"  # Styles title
    ".component-title{height:auto; width:100%; "
    "border-radius:16px; padding:16px;"
    "display:flex; align-items:center;"
    "background-color: var(--chart-C1); color:var(--color-white);}"
    "</style>"
    # Start icons style
    "<style>.big-icon-banner"
    "{width:58px; height: 58px; display: flex;"
    "margin-right: 16px;"
    "justify-content: center;"
    "align-items: center;"
    "background-size: contain;"
    "background-position: center;"
    "background-repeat: no-repeat;"
    # Logo        
    "background-image: url('https://cdn.pixabay.com/photo/2015/08/26/18/20/world-908894_1280.png');}"
    "</style>"
    # End icons style
    "<style>.base-white{color:var(--color-white);}</style>"
    "</head>"  # Styles subtitle
    "<div class='component-title'>"
    "<div class='big-icon-banner'></div>"
    "<div class='text-block'>"
    "<h1>Country Debt</h1>"
    "<p class='base-white'>"
    "This Data App explains the debt of countries, as well as the risk of paying the bonds issued by their central banks. (Without Argentina because it plans to eliminate its Central Bank)</p>"
    "</div>"
    "</div>"
)
   
    shimoku_client.plt.html(html=prediction_header, order=order)
    
    


def tree_world(shimoku_client: Shimoku.Client, order: int):
    tree_table_html = (
        '<div style="width:100%; height:90px; "><h4>Country Tree distribution according to the % of debt / PIB</h4>'
        '<p>List of countries according to the percentage of debt from PIB</p></div>'
    )
    shimoku_client.plt.html(html=tree_table_html, order=order)


def world_table(shimoku_client: Shimoku.Client, order: int):
    world_table_html = (
        '<div style="width:100%; height:90px; "><h4>Country table distribution according to the % of debt</h4>'
        '<p>List of countries according to the percentage of debt from PIB</p></div>'
    )
    shimoku_client.plt.html(html=world_table_html, order=order)


def next_best_product_header(shimoku_client: Shimoku.Client, order: int):
    next_best_product_header_html = (
        '<div style="width:100%; height:90px; "><h4>Next best product prediction</h4>'
        '<p>Products with a high probability of conversion for each lead</p></div>'
    )
    shimoku_client.plt.html(html=next_best_product_header_html, order=order)

def next_best_product_indicators(
    shimoku_client: Shimoku.Client,  order: int, product_recommendation_indicators: pd.DataFrame
):
    shimoku_client.plt.indicator(
        data=product_recommendation_indicators, order=order,
        value='value', header='title', align='align', color='color',
        variant='variant', background_image='backgroundImage',
    )

def next_best_product_table(
    shimoku_client: Shimoku.Client, order: int, product_recommendation_table: pd.DataFrame
):
    shimoku_client.plt.table(
        data=product_recommendation_table[:200], order=order,
        categorical_columns=['Lead Scoring'],
        columns_options={
            'Lead ID': {'width': 360},
            'Lead Scoring': {'width': 360},
            'Probability': {'width': 360},
            'Next Best Product': {'width': 360},
        }
    )