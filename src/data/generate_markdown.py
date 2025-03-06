import numpy as np
import pandas as pd

# File paths
input_json_file = "nodes.json"  # Path to the input JSON file
output_markdown_file = "output_table.md"  # Path to save the markdown table

# Predefined category order
categories_order = [
    "Camera",
    "Peripheral",
    "Actuator",
    "Chassis",
    "Arm",
    "Robot",
    "Voice Activity Detection(VAD)",
    "Speech to Text(STT)",
    "Object Detection",
    "Segmentation",
    "Large Language Model(LLM)",
    "Vision Language Model(VLM)",
    "Vision Language Action(VLA)",
    "Translation",
    "Text to Speech(TTS)",
    "Recorder",
    "Visualization",
    "Simulator",
]

# Read JSON data into a DataFrame using pandas
df = pd.read_json(input_json_file)

# Map categories to the predefined order
df["category"] = pd.Categorical(
    df["category"], categories=categories_order, ordered=True
)

# Sort the DataFrame by the 'category' column
df = df.sort_values("category")

# Replace NaN values with empty strings
df = df.replace({np.nan: ""})

# Create the 'title' column as a markdown link to the 'source'
df["title"] = df.apply(
    lambda row: f"[{row['title']}]({row['source']})" if row["source"] else row["title"],
    axis=1,
)

# Convert shields to markdown image syntax
df["downloads"] = df["downloads"].apply(lambda x: f"![Downloads]({x})" if x else "")
df["license"] = df["license"].apply(lambda x: f"![License]({x})" if x else "")
df["last_release"] = df["last_release"].apply(lambda x: f"![Release]({x})" if x else "")


# Function to generate a markdown table for a single category
def generate_category_table(category, group):
    table = (
        f"### {category}\n\n"
        "| Title | Support | Description | Downloads | License | Release | \n"
        "|-------|---------|-------------|-----------|---------|---------|\n"
    )
    for _, row in group.iterrows():
        table += f"| {row['title']} | {row['support']} | {row['description']} | {row['downloads']} | {row['license']} | {row['last_release']} |\n"
    return table + "\n"


# Generate markdown tables for each category
markdown_tables = []
for category, group in df.groupby("category", sort=False):
    markdown_tables.append(generate_category_table(category, group))

# Combine all tables into a single markdown file
markdown_content = "\n".join(markdown_tables)

# Save the markdown content to a file
with open(output_markdown_file, "w") as file:
    file.write(markdown_content)
