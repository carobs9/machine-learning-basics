# SOURCE: https://medium.com/pythoneers/10-mindblowing-automation-scripts-you-need-to-try-using-python-8bd935f88125

def generate_markdown_file():
    # Prompting user for inputs
    repository_name = input("\n Enter the name of your GitHub repository: ")
    project_description = input("Enter a short description of your project: ")
    installation_instructions = input("Enter installation instructions for your project: ")
    usage_instructions = input("Enter usage instructions for your project: ")
    contributors = input("Enter the contributors to your project (separated by commas): ")

    # Generating Markdown content
    markdown_content = f"""# {repository_name}

{project_description}

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [GitHub Repository](#github-repository)

## Installation
{installation_instructions}
## Usage
{usage_instructions}
## Contributors
{contributors}
## GitHub Repository
[Link to GitHub repository](https://github.com/{repository_name})
"""

    # Writing content to Markdown file
    markdown_file_name = f"{repository_name}_README.md"
    with open(markdown_file_name, "w") as markdown_file:
        markdown_file.write(markdown_content)
    print(f"Markdown file '{markdown_file_name}' generated successfully!")

if __name__ == "__main__":
    generate_markdown_file()
