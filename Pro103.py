import pandas as pd
import plotly.express as px

# To read data
df = pd.read_csv('covid_data.csv')

# Data Properties
graph = px.scatter(df,x='date',y='cases',size='cases',color='country')
# To show Scattered Data
graph.show()