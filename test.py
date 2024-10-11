





log_path = r'C:\rail_share\utils\logs\2024-10-11\2024-10-11-10-10-20.log'



# Open and read the log file
with open(log_path, 'r', encoding='utf-8') as file:
    log_content = file.readlines()

# Initialize the error count
error_count = 0

# Loop through and process each line
for line in log_content:
    if "ERROR" in line:
        error_count += 1
        print(line.strip())  # Print each error line

# Print the total count of errors
print(f"\nTotal number of 'ERROR' entries: {error_count}")