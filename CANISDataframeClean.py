import pandas as pd

# get the file path
# input your own file path
file_name = input("Enter the path to the dataframe: ")
#file_name = "C:/Users/sua10/Downloads/CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx"

# open file
df = pd.read_excel(file_name, 'FULL')

# print initial dataframe
print("Printing the dataframe\n")
print(df.head())

# print the columns of the dataframe
print("\nThe columns of dataframe\n")
for col in df.columns:
    print(col)

# print the general information and description of the dataframe
print("\nOriginal DataFrame:\n", df)
df.info()
print("Description of the dataframe\n")
print(df.describe())

# print if there are any duplicate rows in the dataframe
duplicates = df.duplicated().sum()
print("\nThere are no duplicates: " + str(duplicates) + '\n')

# delete Name (Chinese) column
df.drop(columns=['Name (Chinese)'], inplace=True)
print("\nName (Chinese) deleted\n")
for col in df.columns:
    print(col)

# delete Entity owner (Chinese) column
df.drop(columns=['Entity owner (Chinese)'], inplace=True)
print("\nEntity owner (Chinese) deleted\n")
for col in df.columns:
    print(col)

# delete Parent entity (Chinese) column
df.drop(columns=['Parent entity (Chinese)'], inplace=True)
print("\nParent entity (Chinese) deleted\n")
for col in df.columns:
    print(col)

# delete X (Twitter) URL column
df.drop(columns=['X (Twitter) URL'], inplace=True)
print("\nX (Twitter) URL deleted\n")
for col in df.columns:
    print(col)

# delete X (Twitter) Follower # column
df.drop(columns=['X (Twitter) Follower #'], inplace=True)
print("\nX (Twitter) Follower # deleted\n")
for col in df.columns:
    print(col)

# delete Facebook URL column
df.drop(columns=['Facebook URL'], inplace=True)
print("\nFacebook URL deleted\n")
for col in df.columns:
    print(col)

# delete Facebook Follower # column
df.drop(columns=['Facebook Follower #'], inplace=True)
print("\nFacebook Follower # deleted\n")
for col in df.columns:
    print(col)

# delete Instagram URL column
df.drop(columns=['Instagram URL'], inplace=True)
print("\nInstagram URL deleted\n")
for col in df.columns:
    print(col)

# delete Instagram Follower # column
df.drop(columns=['Instagram Follower #'], inplace=True)
print("\nInstagram Follower # deleted\n")
for col in df.columns:
    print(col)

# delete Threads URL column
df.drop(columns=['Threads URL'], inplace=True)
print("\nThreads URL deleted\n")
for col in df.columns:
    print(col)

# delete Threads Follower # column
df.drop(columns=['Threads Follower #'], inplace=True)
print("\nThreads Follower # deleted\n")
for col in df.columns:
    print(col)

# delete YouTube URL column
df.drop(columns=['YouTube URL'], inplace=True)
print("\nYouTube URL deleted\n")
for col in df.columns:
    print(col)

# delete YouTube Subscriber # column
df.drop(columns=['YouTube Subscriber #'], inplace=True)
print("\nYouTube Subscriber # deleted\n")
for col in df.columns:
    print(col)

# delete TikTok URL column
df.drop(columns=['TikTok URL'], inplace=True)
print("\nTikTok URL deleted #\n")
for col in df.columns:
    print(col)

# delete TikTok Subscriber # column
df.drop(columns=['TikTok Subscriber #'], inplace=True)
print("\nTikTok Subscriber # deleted\n")
for col in df.columns:
    print(col)

# print the modified dataframe
print('\nModified DataFrame:\n', df)
print(df.head())

# all the columns in the new dataframe
df.columns = ['Name (English)', 'Region of Focus', 'Language', 'Entity owner (English)', 'Parent entity (English)', 'X (Twitter) handle', 'Facebook page', 'Instagram page', 'Threads account', 'YouTube account', 'TikTok account']

# check duplicates for region of focus, entity owner, parent entity
print("Unique values in Region of Focus: ", df['Region of Focus'].nunique())
print("Unique values in Language: ", df['Language'].nunique())
print("Unique values in Entity owner (English): ", df['Entity owner (English)'].nunique())
print("Unique values in Parent entity (English): ", df['Parent entity (English)'].nunique())
print("Unique values in X (Twitter) handle: ", df['X (Twitter) handle'].nunique())
print("Unique values in Facebook page: ", df['Facebook page'].nunique())
print("Unique values in Instagram page: ", df['Instagram page'].nunique())
print("Unique values in Threads account: ", df['Threads account'].nunique())
print("Unique values in YouTube account: ", df['YouTube account'].nunique())
print("Unique values in TikTok account: ", df['TikTok account'].nunique())

# get the count of the duplicates in each column
print(df['Region of Focus'].value_counts())
print(df['Language'].value_counts())
print(df['Entity owner (English)'].value_counts())
print(df['Parent entity (English)'].value_counts())
print(df['X (Twitter) handle'].value_counts())
print(df['Facebook page'].value_counts())
print(df['Instagram page'].value_counts())
print(df['Threads account'].value_counts())
print(df['YouTube account'].value_counts())
print(df['TikTok account'].value_counts())

# print the resulting table
print(df.to_string())



