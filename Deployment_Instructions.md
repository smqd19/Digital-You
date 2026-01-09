# Deployment Protocol: Hugging Face Spaces

This document outlines the **deployment protocol** for deploying your **Digital Twin Orchestrator** to **Hugging Face Spaces** using the **Gradio CLI**.  
This method automates **Space creation**, **secret management**, and **dependency provisioning** in a single guided session.

## 1. Prerequisites (Hugging Face Infrastructure)

Before initiating deployment, ensure you have the following ready:

### Hugging Face Account

- Register at: https://huggingface.co

### Access Token

1. Navigate to **Settings → Access Tokens**
2. Click **Create New Token**
3. Set:
   - **Name**: `HF-TOKEN`
   - **Type**: `Write`
4. Copy the token immediately and store it securely

### No README File In the Directory

1. Delete the existing **README.md** file.

## 2. Provider Authentication

Authenticate your local environment using the Hugging Face CLI.

Replace `<YOUR_TOKEN>` with the token created above:

```bash
uv run hf auth login --token <YOUR_TOKEN>
```

### Expected Output

If successful, you will see:

```
Login successful
```

## 3. Interactive Service Deployment

Launch the Gradio deployment orchestrator:

```bash
uv run gradio deploy
```

This command will guide you through Space creation and configuration.

## 4. Step-by-Step CLI Prompts

Respond to the interactive prompts as follows to ensure correct configuration:

| Prompt                   | Recommended Action / Input                                                                                                          |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| Spaces app title         | Enter a name (e.g. `Digital-Twin`)                                                                                                  |
| Gradio app file          | Press **Enter** (defaults to `app.py`)                                                                                              |
| Spaces hardware          | Press **Enter** (defaults to `cpu-basic`)                                                                                           |
| Any Spaces secrets?      | Type **y**                                                                                                                          |
| Secret name              | `OPENAI_API_KEY`                                                                                                                    |
| Secret value             | Paste your actual OpenAI API key                                                                                                    |
| Create requirements.txt? | Type **Y**                                                                                                                          |
| Enter a dependency       | Add the following one by one:<br>- `gradio==5.34.2`<br>- `openai`<br>- `python-dotenv`<br>- `requests`<br>- `If any other was used` |

When finished adding dependencies, **leave the input blank** and press **Enter**.

## 5. Verification and Lifecycle

After deployment completes, the CLI will output a URL similar to:

```
https://huggingface.co/spaces/your-username/your-app-name
```

### Verification Steps

- Open the URL in your browser
- Monitor **Build Logs** during container startup
- Confirm the Space status changes to **Running**

## 6. Security Post-Flight Check

After deployment:

1. Navigate to your Space on Hugging Face
2. Open **Settings → Variables and Secrets**
3. Confirm `OPENAI_API_KEY` is present
4. Verify that:
   - `.env` was **not uploaded**
   - No sensitive credentials are visible in the repository
