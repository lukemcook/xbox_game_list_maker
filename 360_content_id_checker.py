import os
import csv

# Get filepath
path = os.getcwd()

# Create list of files & folders
in_path = os.listdir(path)

# Separate folders from files (Xbox Content IDs)
content_folders = []
for item in in_path:
    if len(item) == 8:
        content_folders.append(item)

# Check for lack of entries
if len(content_folders) == 0:
    print("No Xbox content IDs found. Exiting...")
    exit()

# Use a set to track unique title names to avoid duplicates
unique_titles = set()
matches = []

# Search Xbox 360 content IDs for matching games
with open("gamelist_xbox360.csv", 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    
    for row in reader:
        if row['title_id'] in content_folders:
            title_name = row['title_name']
            # Only add if we haven't seen this title name before
            if title_name not in unique_titles:
                unique_titles.add(title_name)
                matches.append({
                    'title_id': row['title_id'],
                    'title_name': title_name
                })

# Search Xbox content IDs for matching games
with open("gamelist_xbox.csv", 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    
    for row in reader:
        if row['title_id'] in content_folders:
            title_name = row['title_name']
            # Only add if we haven't seen this title name before
            if title_name not in unique_titles:
                unique_titles.add(title_name)
                matches.append({
                    'title_id': row['title_id'],
                    'title_name': title_name
                })

# Display results and write to file
if matches:
    print(f"Found {len(matches)} matching games.")
    # Open file ONCE and write all matches
    with open("game_list.txt", "w") as game_list:
        for match in matches:
            game_list.write(f"Title ID: {match['title_id']} - {match['title_name']}\n")
    print(f"Game entries written to game_list.txt")
else:
    print("No matches found in CSV file.")
