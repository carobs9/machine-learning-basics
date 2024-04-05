# SOURCE: https://medium.com/pythoneers/10-mindblowing-automation-scripts-you-need-to-try-using-python-8bd935f88125
import os

def generate_markdown_file():
    # Prompting user for inputs
    repository_name = input("\n Enter the name of your GitHub repository: ")
    project_description = input("Enter a short description of your project: ")
    installation_instructions = input("Enter installation instructions for your project: ")
    usage_instructions = input("Enter usage instructions for your project: ")
    contributors = input("Enter the contributors to your project (separated by commas): ")

    # Generating list of contents
    contents_list = generate_contents_list()

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
[Link to GitHub repository](https://github.com/carobs9/{repository_name})
"""

    # Writing content to Markdown file
    markdown_file_name = f"{repository_name}_README.md"
    with open(markdown_file_name, "w") as markdown_file:
        markdown_file.write(markdown_content)
    print(f"Markdown file '{markdown_file_name}' generated successfully!")

def generate_contents_list():
    contents_list = ""
    for root, dirs, files in os.walk("."):
        level = root.count(os.sep)
        indent = "    " * (level - 1)
        contents_list += f"{indent}- **{os.path.basename(root)}/**\n"
        sub_indent = "    " * level
        for file in files:
            contents_list += f"{sub_indent}- {file}\n"
    return contents_list

if __name__ == "__main__":
    generate_markdown_file()
