import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_df = pd.read_csv('https://raw.githubusercontent.com/Nanashua/Proyek-Analisis-Data-Dicoding/main/day_data.csv')
hour_df = pd.read_csv('https://raw.githubusercontent.com/Nanashua/Proyek-Analisis-Data-Dicoding/main/hour_data.csv')

# Title for the Dashboard
st.title("Bike Sharing Dashboard")

# Question 1
st.markdown("### Question 1: Which month has the highest and lowest number of users?")

# Sidebar information
with st.sidebar:
    st.markdown("""
        # Bike Sharing Dashboard
        **Bike Sharing Data Analysis Project**  
        Created with ❤️ by [Mutsaqoful Izah Yumna]
    """)

# Plot for the monthly user count
month_counts = day_df.groupby('Month')['Count'].sum().reset_index()

# Improved figure
fig, ax = plt.subplots(figsize=(10, 6))

# Customizing color palette for better aesthetics
sns.set_palette("Blues_r")
sns.barplot(x='Month', y='Count', data=month_counts, ax=ax)

# Adding horizontal lines for better reference
ax.axhline(month_counts['Count'].max(), color='red', linestyle='--', label=f"Highest: Month {month_counts['Month'].max()}")
ax.axhline(month_counts['Count'].min(), color='blue', linestyle='--', label=f"Lowest: Month {month_counts['Month'].min()}")

# Customizing labels and title
ax.set_xlabel('Month', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Users', fontsize=14, fontweight='bold')
ax.set_title('Total Number of Users by Month', fontsize=16, fontweight='bold')

# Rotate x-axis labels for better visibility
ax.tick_params(axis='x', rotation=45)
ax.legend(loc='upper right')
st.pyplot(fig)

# Question 2
st.markdown("### Question 2: How is the distribution of casual and registered users in each season?")

# Plot for casual vs registered users per season
season_counts = day_df.groupby('Season')[['Casual', 'Registered']].sum().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))

# Improved stacked bar chart
season_counts.plot(kind='bar', stacked=True, color=['#76c7c0', '#ff8a5b'], ax=ax)

# Customizing labels and title
ax.set_xlabel('Season', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Users', fontsize=14, fontweight='bold')
ax.set_title('Distribution of Casual and Registered Users by Season', fontsize=16, fontweight='bold')
ax.legend(['Casual Users', 'Registered Users'], loc='upper right')
st.pyplot(fig)

# Question 3
st.markdown("### Question 3: Is there a difference in user behavior based on service usage by hour?")

# Plot for user count by hour
hour_counts = hour_df.groupby('Hour')['Count'].sum().reset_index()

# Menentukan jam dengan jumlah pengguna tertinggi dan terendah
max_usage_hour = hour_counts.loc[hour_counts['Count'].idxmax()]['Hour']
min_usage_hour = hour_counts.loc[hour_counts['Count'].idxmin()]['Hour']

fig, ax = plt.subplots(figsize=(10, 6))

# Improved line plot
sns.lineplot(x='Hour', y='Count', data=hour_counts, marker='o', color='purple', ax=ax)

# Menambahkan garis vertikal untuk jam tertinggi dan terendah
ax.axvline(x=max_usage_hour, color='r', linestyle='--', label=f'Peak: Hour {int(max_usage_hour)}')
ax.axvline(x=min_usage_hour, color='b', linestyle='--', label=f'Lowest: Hour {int(min_usage_hour)}')

# Customizing labels and title
ax.set_xlabel('Hour', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Users', fontsize=14, fontweight='bold')
ax.set_title('Total Number of Users by Hour', fontsize=16, fontweight='bold')

# Add grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Menambahkan legend untuk garis vertikal
ax.legend()

st.pyplot(fig)

# Further Analysis
st.markdown("## Further Analysis")

# Further Analysis 1 ---------------------------------------------------------------------------
st.markdown("### Analysis of Busy Hours vs. Quiet Hours")

# Definisikan jam sibuk dan sepi
busy_hours = [7, 8, 17, 18]
quiet_hours = [0, 1, 2, 3, 4, 5, 6, 22, 23]

# Hitung total pengguna pada jam sibuk dan sepi
busy_usage = hour_df[hour_df['Hour'].isin(busy_hours)]['Count'].sum()
quiet_usage = hour_df[hour_df['Hour'].isin(quiet_hours)]['Count'].sum()

# Buat bar chart
labels = ['Busy Hours', 'Quiet Hours']
values = [busy_usage, quiet_usage]
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(labels, values, color=['coral', 'lightblue'])

# Menambahkan label dan judul
ax.set_ylabel('Number of Users')
ax.set_title('Comparison of Users During Busy and Quiet Hours')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Menampilkan visualisasi di Streamlit
st.pyplot(fig)

# Cetak informasi pengguna
st.write(f"Total users during peak hours: {busy_usage}")
st.write(f"Total users during quiet hours: {quiet_usage}")

# Further Analysis 2 ------------------------------------------------------------------------------------
st.markdown("### Analysis of Usage Trends Over Several Months")

# Group data by month and hour to analyze trends
monthly_hourly_usage = hour_df.groupby(['Month', 'Hour'])['Count'].sum().unstack()

# Plotting heatmap with improvements
fig, ax = plt.subplots(figsize=(12, 6))  # Create a figure and axis for the plot

# Use a better color map and add linewidths for clearer separation between cells
sns.heatmap(monthly_hourly_usage, cmap='YlGnBu', linewidths=0.5, annot=False, ax=ax)

# Customize title and labels
ax.set_title('Trend of Service Usage per Month and Hour', fontsize=16, fontweight='bold')
ax.set_xlabel('Hour of the Day', fontsize=14, fontweight='bold')
ax.set_ylabel('Month', fontsize=14, fontweight='bold')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot in the Streamlit app
plt.tight_layout()  # Adjusts the plot to fit within the figure area
st.pyplot(fig)  # Use st.pyplot to display the figure in the Streamlit app


# Furtune Analysis 3 -----------------------------------------------------------------------------------
# Analisis Dampak Cuaca pada Penggunaan per Jam
st.markdown("### Analysis of Weather Impact on Hourly Usage")

# Catatan mengenai kondisi cuaca
st.markdown("""
**Weather Conditions (Weathersit):**
1. **1**: Clear, Few clouds, Partly cloudy, Partly cloud
2. **2**: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
3. **3**: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
4. **4**: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
""")

# Mengelompokkan data berdasarkan jam dan kondisi cuaca
weather_hourly_usage = hour_df.groupby(['Hour', 'Weathersit'])['Count'].sum().unstack()

# Visualisasi
fig, ax = plt.subplots(figsize=(12, 6))
weather_hourly_usage.plot(kind='bar', stacked=True, colormap='viridis', ax=ax)
ax.set_title('Hourly Service Usage by Weather Situation', fontsize=16, fontweight='bold')
ax.set_xlabel('Hour', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Users', fontsize=14, fontweight='bold')
ax.set_xticklabels(weather_hourly_usage.index, rotation=0)
ax.legend(title='Situasi Cuaca', loc='upper right')
plt.tight_layout()  # Mengatur layout agar lebih rapi
st.pyplot(fig)