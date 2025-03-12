import requests
from github import Github

# Replace with your GitHub token
GITHUB_TOKEN = 'your_github_token'

# Initialize GitHub client
g = Github(GITHUB_TOKEN)

# Search for repositories related to 'Email'
query = "Email"
result = g.search_repositories(query=query)

# Function to extract user emails from a list of repositories
def extract_user_emails(repositories):
    user_emails = []
    for repo in repositories[:10]:  # Limiting to the top 10 repositories
        repo_name = repo.full_name
        contributors = repo.get_contributors()
        for contributor in contributors:
            user = g.get_user(contributor.login)
            if user.email:
                user_emails.append((user.login, user.email))
            # Stop after finding 10 users with emails
            if len(user_emails) >= 10:
                return user_emails
    return user_emails

# Get the top 10 user emails
user_emails = extract_user_emails(result)

# Print the user emails
for login, email in user_emails:
    print(f"User: {login}, Email: {email}")
