# import requests
# import streamlit as st

# token = st.secrets["GITHUB_TOKEN"]

# url = (
#     "https://api.github.com/repos/"
#     "FinaccessX/Finaccess_Resources/contents/"
# )

# response = requests.get(
#     url,
#     headers={
#         "Authorization": f"Bearer {token}",
#         "Accept": "application/vnd.github+json"
#     },
#     timeout=15
# )

# st.write("HTTP status:", response.status_code)

# if response.status_code == 200:
#     st.success("Token can read repository contents.")
# elif response.status_code == 401:
#     st.error("Token is invalid or expired.")
# elif response.status_code == 403:
#     st.error("GitHub is denying access. Check token permissions and organization policies.")
# elif response.status_code == 404:
#     st.error("Repository not found or token lacks access.")
# else:
#     st.warning("Unexpected GitHub API response.")

import requests
import streamlit as st

token = st.secrets["GITHUB_TOKEN"]

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json",
}

url = "https://api.github.com/user/repos"

response = requests.get(
    url,
    headers=headers,
    params={
        "affiliation": "organization_member",
        "per_page": 100
    },
    timeout=15
)

st.write("HTTP status:", response.status_code)

if response.status_code == 200:
    repos = response.json()
    repo_names = [repo["full_name"] for repo in repos]

    st.write("Repositories visible to token:")
    st.write(repo_names)

    st.write(
        "Target repository found:",
        "FinaccessX/Finaccess_Resources" in repo_names
    )
else:
    st.error("Could not retrieve repositories.")
