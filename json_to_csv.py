# Import Libraries
import json
import pandas as pd

# Assign The Number Of Rows Needed
n_rows: int = 100

# Enable/Disable Data Extraction
start_extraction: int = 1

# Get JSON Objects From JSON File
objects = [json.loads(line) for line in open('convert_file.json', 'r')]

# Get The Total Length
obj_length: int = len(objects)

# Create An Empty Array Lists
new_objects = []
extract_objects = []

# Create An Empty String Variable
all_objects = ""

# Create Count Variables
count: int = 0

# Scan All JSON Objects
for obj in objects:

    # Convert List To String And Replace Empty String With #
    all_objects = str(' '.join(obj.keys())).replace(" ", "#")

    # Split String Using Regex #
    new_split = all_objects.split("#")

    # Scan Through All The Split String Values
    for x in range(len(new_split)):

        # Check If New String Is In Appended List
        if new_split[x] not in new_objects:

            # Append New String To The List
            new_objects.append(new_split[x])

# Create Dataframe Column Names With Available Object Names
df = pd.DataFrame(columns=new_objects)

# Scan All JSON Array
for obj in objects:

    # Stop Inner Loop If The Assigned Number Of Rows Is Equal To The New Row Value
    if start_extraction == 0:
        break

    # Check If Extracted JSON Name Exist In JSON Object
    for i in range(len(new_objects)):

        # Get The Object Name
        obj_name: str = str(new_objects[i])

        # Json Object Exists
        if obj_name in obj:
            extract_objects.append(obj[obj_name])

        # Json Object Does Not Exist
        else:
            extract_objects.append(None)

        # Check If The Column Scan Is Completed
        if i == len(new_objects) - 1:

            # Insert A New Row
            df.loc[count] = extract_objects

            # Clear The Previous Appended Objects
            extract_objects = []

            # Assign A New Value For The Row
            count = count + 1

            # Monitor The Conversion Stage
            print(count, " Of ", obj_length)

            # Stop Inner Loop If The Assigned Number Of Rows Is Equal To The New Row Value
            if count == n_rows:
                start_extraction = 0
                break

# Convert Dataframe To CSV File
df.to_csv('json_to_csv_file.csv', index=False)


