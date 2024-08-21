import streamlit as st
import pandas as pd
import mysql.connector as db

# Establish connection to MySQL
connection = db.connect(
    host="localhost",
    user="root",
    port="3306",
    password="root",
    database="project"
)
writer = connection.cursor()

# Execute initial query and fetch data
writer.execute('SELECT * FROM bus_routes')
data = writer.fetchall()

# Create DataFrame with explicit column names
df = pd.DataFrame(data, columns=['id', 'route_name', 'route_link', 'busname',
                                 'bustype', 'departing_time', 'duration',
                                 'reaching_time', 'star_rating', 'price',
                                 'seats_available'])

st.title("Redbus Data")
st.sidebar.title("Options")

# Sidebar select box for route names
route_names = df['route_name'].unique().tolist()
route_name = st.sidebar.selectbox('Select Route Name', [''] + route_names)

bus_types = ['AC', 'Non AC', 'Others']
bus_type = st.sidebar.selectbox('Select Bus Type', ['', *bus_types])

seat_types = ['Sleeper', 'Semi-Sleeper', 'Seater', 'Others']
seat_type = st.sidebar.selectbox('Select Seat Type', ['', *seat_types])

star_rating = st.sidebar.slider('Select Star Rating', 1.0, 5.0, (1.0, 5.0), 0.1)
price_range = st.sidebar.slider('Select Price Range', 1, 10000, (1, 13000), 500)
search_button = st.sidebar.button("Search")

# Construct the query with filters
query = "SELECT * FROM bus_routes WHERE 1=1"
params = []

if route_name:
    query += " AND route_name = %s"
    params.append(route_name)

if bus_type:
    if bus_type == 'AC':
        query += " AND (bustype REGEXP %s AND bustype NOT REGEXP %s)"
        params.extend([r'AC|A\.C|A/C', r'Non AC|Non A/C|Non A\.C|NON-AC'])
    elif bus_type == 'Non AC':
        query += " AND bustype REGEXP %s"
        params.append(r'Non AC|Non A/C|Non A\.C|NON-AC')
    elif bus_type == 'Others':
        query += " AND (bustype NOT REGEXP %s AND bustype IS NOT NULL)"
        params.append(r'AC|A\.C|A/C|Non AC|Non A/C|Non A\.C|NON-AC')

if seat_type:
    if seat_type == 'Sleeper':
        query += " AND bustype LIKE %s AND bustype NOT LIKE %s"
        params.extend(['%Sleeper%', '%Semi Sleeper%'])
    elif seat_type == 'Semi-Sleeper':
        query += " AND bustype LIKE %s"
        params.append('%Semi Sleeper%')
    elif seat_type == 'Seater':
        query += " AND bustype LIKE %s"
        params.append('%Seater%')
    elif seat_type == 'Others':
        query += " AND (bustype NOT LIKE %s AND bustype NOT LIKE %s AND bustype NOT LIKE %s AND bustype IS NOT NULL)"
        params.extend(['%Sleeper%', '%Semi Sleeper%', '%Seater%'])

if star_rating:
    query += " AND star_rating BETWEEN %s AND %s"
    params.extend(star_rating)

if price_range:
    query += " AND price BETWEEN %s AND %s"
    params.extend(price_range)

# Execute the query with parameterized inputs
if search_button:
    writer.execute(query, tuple(params))
    filtered_data = writer.fetchall()

    # Create DataFrame with filtered data
    filtered_df = pd.DataFrame(filtered_data, columns=['id', 'route_name', 'route_link', 'busname',
                                                       'bustype', 'departing_time', 'duration',
                                                       'reaching_time', 'star_rating', 'price',
                                                       'seats_available'])

    st.write(f"Total results: {len(filtered_df)}")
    st.write(filtered_df)

# Close the cursor and connection
writer.close()
connection.close()
