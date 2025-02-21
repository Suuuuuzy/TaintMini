#!/media/dataj/wechat-devtools-linux/testing/myenv/bin/python
import os, csv, json, sys
unpack_path = "/media/dataj/wechat-devtools-linux/testing/auto-testing/data/newcrawl/pkg_unpack"
output_dir = sys.argv[1]
summary_csv = os.path.join(output_dir, "summary/summary.csv")  # New CSV file for summary


# List all files in the output directory (excluding bench.csv files)
files = [f for f in os.listdir(output_dir) if f.endswith(".csv") and not f.endswith("bench.csv")]

# Initialize results list and counter
results = []
cnt = 0
detected = []
# Process each file
for file in files:
    file_path = os.path.join(output_dir, file)
    su = False
    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            reader = csv.reader(f, delimiter="|")
            headers = next(reader)  # Read the header row
            for row in reader:
                # Skip empty rows
                if not row:
                    continue
                # Clean up whitespace in each cell
                row = [cell.strip() for cell in row]
                # Add the file name as the first column
                appid = file.replace('-result.csv', '')
                miniapp_path = os.path.join(unpack_path, appid)
                row.insert(0, miniapp_path)
                row.insert(0, appid)
                row.append(0)
                if row not in results:
                    results.append(row)
                    cnt += 1
                    su = True
    if su:
        detected.append(file)

# Print summary statistics
print("Num of successfully run appids:", len(files))
print("Num of detected appids:", len(detected))
print(f"Percentage of reported appids out of all tested: {100.0 * len(detected) / len(files):.2f}%")
print("Total num of flows:", cnt)

# Generate the new CSV file
def generate_csv(summary_csv, results, headers):
    # Add "File Name" to the headers
    headers = ["App ID"] + ["File Name"] + headers + ["TP"]
    
    # Open the CSV file for writing
    with open(summary_csv, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="|")
        
        # Write headers
        writer.writerow(headers)
        
        # Write data rows
        writer.writerows(results)

# Generate the new CSV file
generate_csv(summary_csv, results, headers)
print(f"New CSV file '{summary_csv}' has been created.")