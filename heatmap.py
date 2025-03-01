import json

# Initialize data structures
k_list = [2, 3, 4, 5]
mark_map = {
    "bar": "Bar",
    "line": "Line",
    "arc": "Pie",
    "point": "Scatter",
    "rect": "Heatmap",
    "boxplot": "Boxplot"
}
mark_list = [value for k, value in mark_map.items()]



heatmap_dict = {k: {mark: 0 for mark in mark_list} for k in k_list}

# Load dataset from file
with open("nvbench2_stepbystep/nvbench2.step.json", "r") as file:
    dataset = json.load(file)

# Process the dataset
for data in dataset:
    output = data["output"]  # Fixed: added quotes around output key
    k = len(output)
    
    # Only process if k is in our k_list
    if k in k_list:
        for chart in output:
            mark = chart["mark"]
            mark = mark_map[mark]
            # Only count if mark is in our mark_list
            if mark in mark_list:
                heatmap_dict[k][mark] += 1

# Convert dictionary to list format
heatmap_list = []
for k in k_list:
    for mark in mark_list:
        heatmap_list.append({
            "mark": mark,
            "k": k,
            "count": heatmap_dict[k][mark]
        })

# Print or return the result
print(heatmap_list)

# Save the heatmap_list to a JSON file
with open("heatmap_count.json", "w") as outfile:
    json.dump(heatmap_list, outfile, indent=4)

print(f"Heatmap data saved to heatmap_results.json")