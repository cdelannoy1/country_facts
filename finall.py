import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
import plotly.graph_objects as go

from PIL import Image


def main():

	menu = ["Home", "Exploratory Data Analysis Section", "SQL Playground", "About"]

	choice = st.sidebar.selectbox("Menu", menu)

	if choice=="Home":

		st.header("CIA Country Informations")

		img = Image.open("heart.jpg")
		st.image(img)

		st.write("### App content")

		st.write ("- This app has four sections :")
		st.write ("1) Home Page")
		st.write ("2) Exploratory Data Analysis - Data Analysis, Visualization Parts and insights")
		st.write ("3) SQL Playground")
		st.write ("4) About")

		st.write("The dataset I'm using is the CIA country facts one. It contains informations like population, area, GDP and much more !")

		st.markdown("---")


 
	elif choice=="Exploratory Data Analysis Section":
		
		st.write("The dataset I'm using is the CIA country facts one. It contains informations like population, area, GDP and much more !")

		st.write("Here is the complete dataset :")

		df = pd.read_csv("CIA_Country_Facts.csv")

		st.dataframe(df)

		st.write("Variables types :")

		st.dataframe(df.dtypes)

		st.write("Statistical value of the columns :")

		st.dataframe(df.describe())

# Creating Dataframe only with the Numerical values to create heatmap

		dt = df.drop(columns=['Region', 'Country'])

		st.markdown("---")

		st.write("### Here is the correlation between the different variables :")

		fig, ax = plt.subplots()
		sns.heatmap(dt.corr(), ax=ax)
		st.write(fig)

		st.write("There is a high negative correlation between Infant Mortality and Phones per 1000, Literacy, GDP per capita.")
		st.write("High correlation between Infant Mortality and Agriculture (meaning that the country living mostly from agriculture have a higher infant mortality).")
		st.write("We can identify a high correlation between Service and Phones per 1000, Literacy, GDP per capita.")
		st.write("Finally, we can see that a low birthrate is correlated with a high literacy and a high GDP per capita.")

		st.markdown("---")

		st.write("### General informations (grouped by Regions) :")

		st.write("I did not include Literacy and Climate. A stacked chart with many percentages and scores didn't make any sense and displayed uninterpretable informations.")

		with st.container():
			choose = st.selectbox("Choose the plot you want to view", ["Population", "Area", 
				"Population Density", "Infant Mortality", "Net Migration", "GDP", "Phones", "Birthrate", "Deathrate", "Agriculture", "Industry", "Service"])

			if choose == "Population":
				a = px.bar(df, x = "Region", y = "Population", color = "Country")
				a.update_xaxes(categoryorder='total ascending')
				st.plotly_chart(a)

			elif choose == "Area":
				b = px.bar(df, x = "Region", y = "Area (sq. mi.)", color = "Country")
				b.update_xaxes(categoryorder='total ascending')
				st.plotly_chart(b)

			elif choose == "Population Density":
				c = px.bar(df, x = "Region", y = "Pop. Density (per sq. mi.)", color = "Country")
				c.update_xaxes(categoryorder='total ascending')
				st.plotly_chart(c)

			elif choose == "Infant Mortality":
				d = px.bar(df, x = "Region", y = "Infant mortality (per 1000 births)", color = "Country")
				d.update_xaxes(categoryorder='total ascending')
				st.plotly_chart(d)

			elif choose == "Net Migration":
				e = px.bar(df, x = "Region", y = "Net migration", color = "Country")
				e.update_xaxes(categoryorder='total ascending')
				st.plotly_chart(e)

			elif choose == "GDP":
				f = px.bar(df, x = "Region", y = "GDP ($ per capita)", color = "Country")
				f.update_xaxes(categoryorder='total ascending')
				st.plotly_chart(f)


			elif choose == "Phones":
				h = px.bar(df, x = "Region", y = "Phones (per 1000)", color = "Country")
				h.update_xaxes(categoryorder='total ascending')
				st.plotly_chart(h)


			elif choose == "Birthrate":
				j = px.bar(df, x = "Region", y = "Birthrate", color = "Country")
				j.update_xaxes(categoryorder='total ascending')
				st.plotly_chart(j)

			elif choose == "Deathrate":
				k = px.bar(df, x = "Region", y = "Deathrate", color = "Country")
				k.update_xaxes(categoryorder='total ascending')
				st.plotly_chart(k)

			elif choose == "Agriculture":
				l = px.bar(df, x = "Region", y = "Agriculture", color = "Country")
				l.update_xaxes(categoryorder='total ascending')
				st.plotly_chart(l)

			elif choose == "Industry":
				m = px.bar(df, x = "Region", y = "Industry", color = "Country")
				m.update_xaxes(categoryorder='total ascending')
				st.plotly_chart(m)

			elif choose == "Service":
				n = px.bar(df, x = "Region", y = "Service", color = "Country")
				n.update_xaxes(categoryorder='total ascending')
				st.plotly_chart(n)

		st.write("Asia has (by far) the highest population and the highest population density (followed by Western Europe).")
		st.write("Infant mortality is extremely high in the sub-saharan Africa region")

		st.markdown("---")

		st.write("### Bubble chart representing Birthrate on GDP per Capita :")

		fig = px.scatter(df, x="Birthrate", y="GDP ($ per capita)",
			 size="Population", color="Region",
				 hover_name="Country")
		st.plotly_chart(fig)

		st.write("Birthrate and GDP are highly correlated. Nevertheless, we can see that a Low birthrate doesn’t necesarly mean a high GDP per Capita (example : Russia, Ukraine, Bosnia, Belarus and pretty much all Eastern Europe countries) but none of the country with a High birthrate have a high GDP per Capita. ")
		st.write("Countries with a medium GDP per Capita and a medium Birthrate are all located in the middle-east (UAE, Saudi Arabia, Qatar, Kuwait and Israel).")
		st.write("Finally, we can clearly see that the countries located in the Sub-saharan Africa region have the highest birthrate.")


		st.markdown("---")

		st.write("### Scatter plots :")

		z = px.scatter(df, x = "GDP ($ per capita)", y = "Literacy (%)", color = "Country")
		st.plotly_chart(z)

		st.write("This scatter plot clearly displays that the higher the GDP per Capita the higher the Literacy except for a couple of outliers located in the Middle East (Qatar, Kuwait and UAE). ")

		zi = px.scatter(df, x = "GDP ($ per capita)", y = "Phones (per 1000)", color = "Country")
		st.plotly_chart(zi)

		st.write("As expected, the higher the GDP per Capita the higher the number of Phones (except for two outliers : Luxembourg and Norway).")

		zx = px.scatter(df, x = "GDP ($ per capita)", y = "Infant mortality (per 1000 births)", color = "Country")
		st.plotly_chart(zx)

		st.write("Confirming what we mentionned before, the higher the GDP per Capita the lower the Infant Mortality.")

		st.markdown("---")

	 
	elif choice == "SQL Playground": 
		 import sqlite3 
		 conn = sqlite3.connect('data.sqlite')
		 c = conn.cursor()



		# Fxn Make Execution
		 def sql_executor(raw_code):
		  c.execute(raw_code)
		  data = c.fetchall()
		  return data 


		 CIA_Country_Facts = ['Country', 'Region', 'Population', 'Area (sq. mi.)', 'Pop. Density (per sq. mi.)', 'Coastline (coast/area ratio)', 'Net migration', 'Infant mortality (per 1000 births)', 'GDP ($ per capita)', 'Literacy (%)', 'Phones (per 100)', 'Arable (%)', 'Crops (%)', 'Other (%)', 'Birthrate', 'Agriculture', 'Industry', 'Service']

		 def m():
		  st.title("SQL Playground")

		  st.write("### For the queries to work the CAST() function needs to be applied on Numerical Variables")
			
# Columns/Layout
		  col1,col2 = st.columns(2)

		  with col1:
		  	with st.form(key='query_form'):
		  		raw_code = st.text_area("SQL Code Here")
		  		submit_code = st.form_submit_button("Execute")

		  	with st.expander("Table Info"):
		  		table_info = {'city':CIA_Country_Facts}
		  		st.json(table_info)
			
		# Results Layouts
		  with col2:
		  	if submit_code:
		  		st.info("Query Submitted")
		  		st.code(raw_code)

		  		query_results = sql_executor(raw_code)
		  		with st.expander("Results"):
		  			st.write(query_results)

		  		with st.expander("Pretty Table"):
		  			query_df = pd.DataFrame(query_results)
		  			st.dataframe(query_df)

		 m()

		 st.markdown("---")



	elif choice=="About":
		st.write("""

	## About

	Camille Delannoy. Student at IE university. This app was created for the Python II individual project. 

	Conchita, I hope you like it :smile:

	Linkedin : https://www.linkedin.com/in/camille-delannoy-6548bb177/""")

		st.markdown("---")

main()
   



