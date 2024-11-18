You can follow these steps:

## Enable Push Protection:

- Go to your repository on GitHub.
- Navigate to Settings > Code security and analysis.
- Enable Push protection under the Secret scanning section.

### Create a Secret:

- Add a secret to your repository to simulate a sensitive data leak. For example, add a fake API key or password in your code.
- Create a GitHub Action:
- Create a GitHub Action workflow that includes a step to push code containing the secret. This will trigger the push protection feature.