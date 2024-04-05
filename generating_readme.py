# SOURCE: https://medium.com/pythoneers/10-mindblowing-automation-scripts-you-need-to-try-using-python-8bd935f88125
import os

def generate_markdown_file():
    # Prompting user for inputs
    repository_name = input("\n Enter the name of your GitHub repository: ")
    link = input("\n Enter the link of the GutHub repository: ")
    project_description = input("Enter a short description of your project: ")
    installation_instructions = input("Enter installation instructions for your project: ")
    usage_instructions = input("Enter usage instructions for your project: ")
    contributors = input("Enter the contributors to your project (separated by commas): ")

    # Generating list of contents
    contents_list = generate_contents_list('breast_cancer_prediction')

    # Generating Markdown content
    markdown_content = f"""# {repository_name}

{project_description}

## Table of Contents
- [Installation](#installation)
- [Contents](#contents)
- [Usage](#usage)
- [Contributors](#contributors)
- [GitHub Repository](#github-repository)

## Installation
{installation_instructions}
## Contents
{contents_list}
## Usage
{usage_instructions}
## Contributors
{contributors}
## GitHub Repository
[Link to GitHub repository]({link})
"""

    # Writing content to Markdown file
    markdown_file_name = "README.md"
    with open(markdown_file_name, "w") as markdown_file:
        markdown_file.write(markdown_content)
    print(f"Markdown file '{markdown_file_name}' generated successfully!")

def generate_contents_list(folder_name):
    contents_list = ""
    folder_path = os.path.join(".", folder_name)
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)  # Get the full path of the item within the folder
        if os.path.isdir(item_path) or os.path.isfile(item_path):  # Check if the item is a directory or a file
            contents_list += f"- {item}\n"
    return contents_list

if __name__ == "__main__":
    generate_markdown_file()
