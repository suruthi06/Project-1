## Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

## Introduction   

This project is focused on building a dynamic dashboard using Streamlit to visualize and interact with data scraped from Redbus using Selenium. The goal is to extract data such as bus routes, availability, prices, and timings. The data is then filtered and displayed interactively through Streamlit’s intuitive interface.   

## Domain: Travel & Transportation

## Skills Takeaway:      
-> Python scripting   
-> Web scraping using Selenium   
-> Data visualization using Streamlit   
-> Dynamic data filtering   
-> Real-time data interaction   

## Overview    
## Data Harvesting:   

Utilizing Selenium to scrape real-time data from the Redbus website, including:   

-> Bus routes   
-> Seat availability   
-> Pricing information   
-> Timings   
-> Bus operator details   

## Dynamic Filtering:   
Create a dashboard that allows users to dynamically filter the bus data by route, price, operator, and timing.
Visualize filtered results with ease through Streamlit widgets.   

## Data Storage:   
Local Storage: The data scraped is stored in a structured format (e.g., CSV, JSON, or a database).
Optionally, the data can be stored in a MySQL database for larger datasets or more complex filtering. 

## Data Analysis and Visualization:   
Streamlit Dashboard: Create an interactive UI with options to filter by various parameters such as route, price, timing, and availability.
Real-time Interaction: Allow users to input data and display updated results immediately in the dashboard.   
Data Analysis: Perform simple aggregations and summaries, such as calculating the average ticket price per route or the most popular routes.   

## Technology and Tools:   

-> Python   
-> Selenium (for web scraping)   
-> Streamlit (for building the interactive dashboard)   
-> MySQL (optional for storing data)   
-> Pandas (for data manipulation)   

## Packages and Libraries:   

-> Selenium: For web scraping Redbus website data.   
from selenium import webdriver   
-> Streamlit: For building the dynamic dashboard.   
import streamlit as st   
-> Pandas: For data manipulation and filtering.   
import pandas as pd   
-> MySQL: For storing data in a relational database.   
import mysql.connector   
-> Datetime: For handling timestamps.   
from datetime import datetime   

## Features:   
## Web Scraping:   
Scrape bus route details, timings, seat availability, and prices using Selenium from the Redbus website.
Use XPath or CSS selectors to locate the elements to extract the necessary data points.   

## Dynamic Filtering:   
Allow users to filter bus details by:   
-> Bus route   
-> Seat availability   
-> Price range   
-> Time of departure   
-> Display the results in a dynamic table.      

## Data Display in Streamlit:   
-> Display the scraped data in a clean and well-structured layout.   
-> Use interactive widgets like dropdowns, sliders, and buttons to enable filtering.   

## Usage:   
-> Web Scraping: Start by entering a bus route or city in the input field. The data scraping will begin, and details will be fetched from Redbus.   

-> Dynamic Filtering: Once the data is displayed, use the filter options on the sidebar to refine results based on price, timing, and operator.   

-> Data Display: Filtered results will be shown in a tabular format, and users can click to view additional details such as seat availability and operator information.   

## Contact:   
LinkedIn: https://www.linkedin.com/in/suruthi-boopalan/
Email: suruthipriya50@gmail.com   
