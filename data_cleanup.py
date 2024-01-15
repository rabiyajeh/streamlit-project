import pandas as pd

# Read the Excel file into a DataFrame
file_path = 'archive/CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx'
sheet_name = 'FULL'  

# Columns of interest
columns_of_interest = [
    'Name (English)',
    'Region of Focus',
    'Language',
    'Entity owner (English)',
    'Parent entity (English)',
    'X (Twitter) handle',
    'X (Twitter) URL',
    'X (Twitter) Follower #',
    'Facebook page',
    'Facebook URL',
    'Facebook Follower #',
    'Instragram page',
    'Instagram URL',
    'Instagram Follower #',
    'Threads account',
    'Threads URL',
    'Threads Follower #',
    'YouTube account',
    'YouTube URL',
    'YouTube Subscriber #',
    'TikTok account',
    'TikTok URL',
    'TikTok Subscriber #'
]

try:
    # Read the specified columns from the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=columns_of_interest)

    # Display the first few rows 
    # print(df.head())

    #Change to platform of analysis
    platform = 'TikTok'

    # Get columns containing 'Twitter' in their names
    platform_columns = [col for col in df.columns if platform in col]

    # Keep the columns related to Twitter along with specified columns
    columns_to_keep = [
        'Name (English)',
        'Region of Focus',
        'Language',
        'Entity owner (English)',
        'Parent entity (English)'
    ] + platform_columns

    # Filter the DataFrame to keep only specified columns
    df_platform = df[columns_to_keep]

    # Remove rows with any empty entries
    df_platform = df_platform.dropna()

    # Double check if desired items are contained
    print(df_platform.columns.to_list)
    print(df_platform.shape)

    # Saves the cleaned-files
    output_file_path = f'cleaned_data_{platform}.csv'
    df_platform.to_csv(output_file_path, index=False)
    print(f"Cleaned data saved to '{output_file_path}'")

    # Double check:
    # tester = pd.read_csv(output_file_path)
    # print(tester.shape)
    


except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
