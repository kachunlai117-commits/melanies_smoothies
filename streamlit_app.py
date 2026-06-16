# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests 
import pandas as pd

# Write directly to the app
st.title(f"Customize Your Smoothie :cup_with_straw:")
st.write(
  """Choose the fruits you want in your custom Smoothie!"""
)

name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be:', name_on_order)

cnx = st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'), col('SEARCH_ON'))
pd_df = my_dataframe.to_pandas()

ingredients_list = st.multiselect('Choose up to 5 ingredients:', my_dataframe, 
                                  max_selections = 5)

if ingredients_list:
    ingredients_string = ''
    
    for fruits_chosen in ingredients_list:
        ingredients_string += fruits_chosen + ' '
        search_on = pd_df['SEARCH_ON'][pd_df['FRUIT_NAME'] == fruit_chosen].iloc[0]
        st.write('The Search Value for ', fruit_chosen, ' is ', search_on, '.')
        sf_df = st.dataframe(data = smoothiefroot_response.json(), use_container_width = True)
        st.subheader(fruit_chosen + ' Nutrition Information ')
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit" + search_on)
      
    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(name_on_order, ingredients)
    values ('""" + name_on_order + """','""" + ingredients_string + """') """
    
    time_to_insert = st.button("Submit Order")

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success(f'Your Smoothie is ordered, {name_on_order}!')

    

    

