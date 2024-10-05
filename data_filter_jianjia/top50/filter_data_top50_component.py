#!/media/dataj/wechat-devtools-linux/testing/myenv/bin/python

# suzy: this is used to go through all js files under a miniapp to see whether they contain the source/sink
# when we run the tool, we are not limited to this

import json
import os
import re
from multiprocessing import Pool, cpu_count


# List of APIs to search for
with open("../../config.json") as f:
    config = json.load(f)
api_list = config['component_related']
api_list = [str(i) for i in api_list]
print(api_list)

base_directory = "/media/dataj/wechat-devtools-linux/testing/auto-testing/miniapp_data/top50/packages_unpack"
# Output JSON file path
output_file = "component_related_filter_api_search_results_top50.json"
navigate_output_file = "component_related_filter_navigateToMiniProgram_top50.json"
processed_dirs_file = "component_related_filter_processed_dirs_top50.txt"  # File to track processed directories


# Function to search for APIs in a file
def search_apis_in_file(file_path, apis):
    matching_apis = []
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        for api in apis:
            # Simple search or regex for exact API matches
            if re.search(r'\b' + re.escape(api) + r'\b', file_content):
                matching_apis.append(api)
    return matching_apis

# Function to search through all JavaScript files in a directory
def search_apis_in_js_files(directory, apis):
    results = {}
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".wxml"):
                file_path = os.path.join(root, file_name)
                found_apis = search_apis_in_file(file_path, apis)
                for api in found_apis:
                    # short_path = file_path.replace(base_directory, "")
                    short_path = file_path
                    if api not in results:
                        results[api] = [short_path]
                    else:
                        results[api].append(short_path)
    return results

def search_miniapp(directory):
    result = {}
    appid = directory.split("/")[-1]
    result[appid] = search_apis_in_js_files(directory, api_list)
    return result

# Function to read the list of processed directories from file
def get_processed_dirs():
    if os.path.exists(processed_dirs_file):
        with open(processed_dirs_file, 'r') as f:
            return set(f.read().splitlines())
    return set()

# Function to save the processed directories to file
def save_processed_dirs(directories):
    with open(processed_dirs_file, 'a') as f:
        for directory in directories:
            f.write(directory + '\n')
            
def update_navigateToMiniprogram(combined_results):
    result = {}
    for i in combined_results:
        if 'navigateToMiniProgram' in combined_results[i]:
            result[i] = {"navigateToMiniProgram":combined_results[i]["navigateToMiniProgram"]}
        
    # with open(navigate_output_file, 'w') as f:
    #     json.dump(result, f, indent = 2)
    
    
    if os.path.exists(navigate_output_file):
        with open(navigate_output_file, 'r+', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)
            for i in result:
                if i not in existing_data:
                    existing_data[i] = result[i]
            json_file.seek(0)
            json.dump(existing_data, json_file, indent=2)
    else:
        with open(navigate_output_file, 'w', encoding='utf-8') as json_file:
            json.dump(result, json_file, indent=2)
                

def get_navigateToMiniprogram_num():
    with open(navigate_output_file) as f:
        result = json.load(f)
        return len(result)  

def get_filtered_num():
    with open(output_file) as f:
        result = json.load(f)
        return len(result)  
    
def run_multiprocessing():
    # Get the list of already processed directories
    processed_dirs = get_processed_dirs()

    # Get a list of all subdirectories in the base directory that haven't been processed yet
    all_directories = [os.path.join(base_directory, d) for d in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, d))]
    new_directories = [d for d in all_directories if d not in processed_dirs]
    # new_directories = new_directories[:100]
    
    if new_directories:
        # Use multiprocessing to search in all directories
        with Pool(cpu_count()) as pool:
            results = pool.map(search_miniapp, new_directories)
        
        # Combine all results into a single dictionary
        combined_results = {}
        for result in results:
            combined_results.update(result)
       
        # Output the results to a JSON file
        if os.path.exists(output_file):
            with open(output_file, 'r+', encoding='utf-8') as json_file:
                existing_data = json.load(json_file)
                existing_data.update(combined_results)
                json_file.seek(0)
                json.dump(existing_data, json_file, indent=4)
                update_navigateToMiniprogram(existing_data)
        else:
            with open(output_file, 'w', encoding='utf-8') as json_file:
                json.dump(combined_results, json_file, indent=4)
                update_navigateToMiniprogram(combined_results)
                
        # Save the newly processed directories to the log file
        save_processed_dirs(new_directories)

        print(f"Results have been saved to {output_file} for {len(new_directories)} new directories.")
    else:
        print("No new directories to process.")
    
    
    print(get_filtered_num())
    print(get_navigateToMiniprogram_num())
    
# Run the multiprocessing search
if __name__ == "__main__":
    run_multiprocessing()
    