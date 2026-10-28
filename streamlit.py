import requests
import streamlit as st

token = st.secrets["GITHUB_TOKEN"]

url = (
    "https://api.github.com/repos/"
    "FinaccessX/Finaccess_Resources/contents/"
)

response = requests.get(
    url,
    headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    },
    timeout=15
)

st.write("HTTP status:", response.status_code)

if response.status_code == 200:
    st.success("Token can read repository contents.")
elif response.status_code == 401:
    st.error("Token is invalid or expired.")
elif response.status_code == 403:
    st.error("GitHub is denying access. Check token permissions and organization policies.")
elif response.status_code == 404:
    st.error("Repository not found or token lacks access.")
else:
    st.warning("Unexpected GitHub API response.")
