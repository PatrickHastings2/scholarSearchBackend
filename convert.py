result = []

with open("idata.txt", "r") as file:
    data = file.readlines()

record = ''
for line in data:
    # Remove commas from the line
    line = line.replace(',', '')
    
    if line.startswith('#'):
        if record:  # If there is a previous record, process it
            record_dict = {}
            lines = record.strip().split('\n')  # Split the record into lines and remove leading/trailing whitespaces
            for line in lines:
                if ':' in line:  # Check if the line contains a colon
                    key, value = line.strip().split(':', 1)  # Split each line into key and value
                    record_dict[key.strip()] = value.strip()  # Store key-value pair in the dictionary
            result.append(record_dict)  # Append the dictionary to the result list
        record = ''  # Reset record for the next college
    else:
        if ':' in line:
            key, value = line.strip().split(':', 1)
            record += f"{key.strip()}: {value.strip()}\n"  # Append line to record with colon and value
        else:
            record += line  # Append line to record

# Process the last record
if record:
    record_dict = {}
    lines = record.strip().split('\n')
    for line in lines:
        if ':' in line:
            key, value = line.strip().split(':', 1)
            record_dict[key.strip()] = value.strip()
    result.append(record_dict)

# Writing to temp.txt
with open("data.txt", "w") as output_file:
    for college in result:
        output_file.write(str(college) + '\n')
