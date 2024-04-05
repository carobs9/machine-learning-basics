def generate_markdown_file():
    # Prompting user for inputs
    repository_name = input("\n Enter the name of your GitHub repository: ")
    project_description = input("Enter a short description of your project: ")
    installation_instructions = input("Enter installation instructions for your project: ")
    usage_instructions = input("Enter usage instructions for your project: ")
    contributors = input("Enter the contributors to your project (separated by commas): ")

    # Generating badges
    stars_badge = "[![GitHub stars](https://img.shields.io/github/stars/{})](https://github.com/{}/stargazers)".format(repository_name, repository_name)
    forks_badge = "[![GitHub forks](https://img.shields.io/github/forks/{})](https://github.com/{}/network/members)".format(repository_name, repository_name)
    issues_badge = "[![GitHub issues](https://img.shields.io/github/issues/{})](https://github.com/{}/issues)".format(repository_name, repository_name)

    # Generating Markdown content
    markdown_content = f"""
    # {repository_name}

    {project_description}

    ## Table of Contents
    - [Installation](#installation)
    - [Usage](#usage)
    - [Contributors](#contributors)
    - [Badges](#badges)
    - [GitHub Repository](#github-repository)

    ## Installation
    ```
    {installation_instructions}
    ```
    ## Usage
    ```
    {usage_instructions}
    ```
    ## Contributors
    {contributors}

    ## Badges
    {stars_badge} {forks_badge} {issues_badge} {license_badge}
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