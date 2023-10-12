import pandas as pd
from sqlalchemy import create_engine,text
import os
import openai
def sql_translate(txt):
    openai.api_key = "<give your key>"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"### mysql SQL tables, with their properties:\n#\n# Employee(ID,Experience_Years,Age,Gender,Salary)\n# Supermart(Order ID,Customer Name,Category,Sub Category,City,Order Date,Region,Sales,Discount,Profit,State)\n# BigBasket(ProductName,Brand,Price,DiscountPrice,Image_Url,Quantity,Category,SubCategory,Absolute_Url)\n#\n### A query to answer{txt}\n",
      temperature=0,
      max_tokens=150,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0,
      stop=["#", ";"]
    )
    return response['choices'][0]['text']
text=input()
sql_translate(text)
