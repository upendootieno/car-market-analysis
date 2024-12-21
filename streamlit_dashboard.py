import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import save_to_json
 
st.write("""Advanced Vehicle Sales Analytics""")
 
df = pd.read_csv("all-vehicles-model.csv", sep=";")
# st.line_chart(df)


# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# st.pyplot(fig1)
