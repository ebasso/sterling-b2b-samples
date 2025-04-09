import pandas as pd
import glob
import os
import re

def load_files_to_dataframe(directory):
    # Get all files 
    pattern = re.compile(r"S\d{8}\.\d{3}")

    all_files = glob.glob(os.path.join(directory, "*"))

    matched_files = [file for file in all_files if pattern.search(os.path.basename(file))]

    # Init DataFrames
    df_list = []

    # Loop through the list of matched files and read each one into a DataFrame
    for file in matched_files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                 # Split the line by pipe separator
                items = line.strip().split('|')
                data = {}
                for item in items:
                    if '=' in item:
                        key, value = item.split('=', 1)  # Split only on the first '='
                        data[key] = value
                # Append the data dictionary to the list
                df_list.append(data)

    # Convert the list of dictionaries into a DataFrame
    combined_df = pd.DataFrame(df_list)

    return combined_df

def process_dataframe(df):
    # Convert the 'STAR' column to datetime
    df['STAR'] = pd.to_datetime(df['STAR'], format='%Y%m%d %H:%M:%S.%f')

    # Extract the hour from the 'STAR' column
    df['hour'] = df['STAR'].dt.floor('h')

    return df


def group_by_hour_and_pnum(df):
    # Group by the hour and PNUM, then count the occurrences
    grouped_df = df.groupby(['hour', 'PNUM']).size().reset_index(name='count')
    
    # Sort by count in descending order and select the top 20
    top_20_df = grouped_df.sort_values(by='count', ascending=False).head(20)
    
    return top_20_df

def count_unique_pnum_by_hour(df):
    # Group by hour and count unique PNUM values
    unique_pnum_df = df.groupby('hour')['PNUM'].nunique().reset_index(name='unique_pnum_count')
    
    return unique_pnum_df


def find_top_pnum_execution_time(df):
    # Ensure the 'STAR' column is in datetime format
    df['STAR'] = pd.to_datetime(df['STAR'], format='%Y%m%d %H:%M:%S.%f', errors='coerce')
    
    # Sort by 'PNAM', 'PNUM', and 'STAR'
    df = df.sort_values(by=['PNAM', 'PNUM', 'STAR'])
    
    # Calculate time differences between successive rows
    df['next_STAR'] = df.groupby(['PNAM', 'PNUM'])['STAR'].shift(-1)
    df['execution_time'] = (df['next_STAR'] - df['STAR']).dt.total_seconds()
    
    # Drop rows with NaN values in execution_time
    df = df.dropna(subset=['execution_time'])
    
    # Convert execution time from seconds to minutes
    df['execution_time_minutes'] = df['execution_time'] / 60

    # Group by PNUM and sum the execution time in minutes
    pnum_execution_df = df.groupby(['PNAM', 'PNUM'])['execution_time_minutes'].sum().reset_index()
    
    # Sort by total execution time in minutes in descending order and select the top 10
    top_10_pnum_df = pnum_execution_df.sort_values(by='execution_time_minutes', ascending=False).head(10)

    return top_10_pnum_df

def count_lines_by_hour(df):
    # Count the number of lines for each hour
    lines_count_df = df.groupby('hour').size().reset_index(name='lines_count')
    
    return lines_count_df

def count_lines_every_10_minutes(df):
    # Filter the DataFrame for the time range between 08:00 and 10:00
    filtered_df = df[(df['STAR'].dt.hour >= 8) & (df['STAR'].dt.hour < 10)]

    # Round the 'STAR' column to the nearest 10 minutes
    filtered_df['10_minute'] = filtered_df['STAR'].dt.floor('10T')

    # Count the number of lines for each 10-minute interval
    lines_10_minute_df = filtered_df.groupby('10_minute').size().reset_index(name='lines_count')

    return lines_10_minute_df

def count_lines_every_5_minutes(df):
    # Filter the DataFrame for the time range between 08:00 and 10:00
    filtered_df = df[(df['STAR'].dt.hour >= 8) & (df['STAR'].dt.hour < 10)]

    # Round the 'STAR' column to the nearest 10 minutes
    filtered_df['5_minute'] = filtered_df['STAR'].dt.floor('5T')

    # Count the number of lines for each 10-minute interval
    lines_5_minute_df = filtered_df.groupby('5_minute').size().reset_index(name='lines_count')

    return lines_5_minute_df

def main():
    directory = '.'  # Replace with the path to your directory
    combined_df = load_files_to_dataframe(directory)
    processed_df = process_dataframe(combined_df)
    lines_count_df = count_lines_by_hour(processed_df)
    #lines_10_minute_df = count_lines_every_10_minutes(processed_df)
    lines_5_minute_df = count_lines_every_5_minutes(processed_df)
    top_20_df = group_by_hour_and_pnum(processed_df)


    # Print the top 20 occurrences of PNUM by hour
    print("Top 20 occurrences of PNUM by hour:")
    print(top_20_df)
    
    unique_pnum_df = count_unique_pnum_by_hour(processed_df)
    
    # Print the number of unique PNUM by hour
    print("\nNumber of unique PNUM by hour:")
    print(unique_pnum_df)


    top_10_pnum_execution_df = find_top_pnum_execution_time(processed_df)

    # Print the top 10 PNUMs with the longest execution time
    print("\nTop 10 PNUMs with the longest execution time:")
    print(top_10_pnum_execution_df)
    
    # Print the number of lines by hour
    
    print("\nNumber of lines by hour:")
    print(lines_count_df)

    # # Print the number of lines every 10 minutes between 08:00 and 10:00
    # print("\nNumber of lines every 10 minutes between 08:00 and 10:00:")
    # print(lines_10_minute_df)

    # Print the number of lines every 10 minutes between 08:00 and 10:00
    print("\nNumber of lines every 5 minutes between 08:00 and 10:00:")
    print(lines_5_minute_df)

if __name__ == "__main__":
    main()
