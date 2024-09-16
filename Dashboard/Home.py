import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import psycopg2
from sqlalchemy import create_engine

# Establish connection
conn = psycopg2.connect(
    dbname="telecom",
    user="postgres",
    password="1q2w3e4r",
    host="172.16.1.16",
    port="5432"
)

# Create a SQLAlchemy engine from psycopg2 connection
engine = create_engine('postgresql+psycopg2://postgres:1q2w3e4r@172.16.1.16:5432/telecom')

# Load data from PostgreSQL using pandas
df = pd.read_sql_query("SELECT * FROM xdr_data", engine)

def display():
    st.title("Exploratory Data Analysis")
    st.write("This is the Exploratory Data Analysis.")
    st.line_chart([1, 2, 3, 4, 5,6,7,8,9,10,11,12])

# Set page title
st.title("Telecom Data - Exploratory Data Analysis")

# Show first few rows of the dataset
st.subheader("Initial Data")
st.write(df.head())

# Option to drop or fill missing values
st.subheader("Handle Missing Values")
missing_columns = df.columns[df.isnull().any()]
missing_column = st.selectbox("Choose a column to fill missing values", missing_columns)
fill_method = st.radio("Fill method", ["Fill with Mean", "Fill with Median", "Drop Rows"])

if st.button("Apply Fill"):
    if fill_method == "Fill with Mean":
        df[missing_column] = df[missing_column].fillna(df[missing_column].mean())
    elif fill_method == "Fill with Median":
        df[missing_column] = df[missing_column].fillna(df[missing_column].median())
    else:
        df = df.dropna(subset=[missing_column])
    st.success(f"{missing_column} cleaned successfully")

# ---- 2. Descriptive Statistics ----
st.subheader("Descriptive Statistics")
st.write(df.describe())

# ---- 3. Visualizations ----

# Handset Type Distribution
st.subheader("Handset Type Distribution")
handset_counts = df['Handset Type'].value_counts()
st.bar_chart(handset_counts)

# Comparing Handset Type with another feature, e.g., Total DL (Bytes)
st.subheader("Comparison: Handset Type vs. Total DL (Bytes)")
df_clean = df.dropna(subset=["Handset Type", "Total DL (Bytes)"])  # Clean data

fig, ax = plt.subplots()
sns.boxplot(x="Handset Type", y="Total DL (Bytes)", data=df_clean, ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)

# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import psycopg2
# from sqlalchemy import create_engine

# # Function to load data
# def load_data():
#     # Establish connection
#     conn = psycopg2.connect(
#         dbname="telecom",
#         user="postgres",
#         password="1q2w3e4r",
#         host="172.16.1.16",
#         port="5432"
#     )

#     # Create a SQLAlchemy engine from psycopg2 connection
#     engine = create_engine('postgresql+psycopg2://postgres:1q2w3e4r@172.16.1.16:5432/telecom')

#     # Load data from PostgreSQL using pandas
#     df = pd.read_sql_query("SELECT * FROM xdr_data", engine)
#     return df
# def display():
#    st.title("Exploratory Data Analysis")
#    st.write("This is the Exploratory Data Analysis.")
# #    st.line_chart([1, 2, 3, 4, 5,6,7,8,9,10,11,12])

# # Main function to display the Streamlit app
# def main():
#     st.set_page_config(page_title="Telecom Data - Exploratory Data Analysis", layout="wide")
    
#     # Load the data
#     df = load_data()

#     # Page title
#     st.title("Telecom Data - Exploratory Data Analysis")

#     # Show first few rows of the dataset
#     st.subheader("Initial Data")
#     st.write(df.head())

#     # Option to drop or fill missing values
#     st.subheader("Handle Missing Values")
#     missing_columns = df.columns[df.isnull().any()]
#     if missing_columns.size > 0:
#         missing_column = st.selectbox("Choose a column to fill missing values", missing_columns)
#         fill_method = st.radio("Fill method", ["Fill with Mean", "Fill with Median", "Drop Rows"])

#         if st.button("Apply Fill"):
#             if fill_method == "Fill with Mean":
#                 df[missing_column] = df[missing_column].fillna(df[missing_column].mean())
#             elif fill_method == "Fill with Median":
#                 df[missing_column] = df[missing_column].fillna(df[missing_column].median())
#             else:
#                 df = df.dropna(subset=[missing_column])
#             st.success(f"{missing_column} cleaned successfully")

#     # Descriptive Statistics
#     st.subheader("Descriptive Statistics")
#     st.write(df.describe())

#     # Handset Type Distribution
#     st.subheader("Handset Type Distribution")
#     if 'Handset Type' in df.columns:
#         handset_counts = df['Handset Type'].value_counts()
#         st.bar_chart(handset_counts)
#     else:
#         st.write("Column 'Handset Type' not found in the dataset.")

#     # Comparison: Handset Type vs. Total DL (Bytes)
#     st.subheader("Comparison: Handset Type vs. Total DL (Bytes)")
#     if 'Handset Type' in df.columns and 'Total DL (Bytes)' in df.columns:
#         df_clean = df.dropna(subset=["Handset Type", "Total DL (Bytes)"])  # Clean data

#         fig, ax = plt.subplots()
#         sns.boxplot(x="Handset Type", y="Total DL (Bytes)", data=df_clean, ax=ax)
#         plt.xticks(rotation=90)
#         st.pyplot(fig)
#     else:
#         st.write("Columns 'Handset Type' or 'Total DL (Bytes)' not found in the dataset.")

# if __name__ == "__main__":
#     main()
