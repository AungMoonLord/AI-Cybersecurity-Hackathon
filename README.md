<br />
<div align="center">
  <a>
    <img src="images/mjolnir-logo.svg" alt="Logo" width="auto" height="120">
  </a>

  <h1 style="margin-top: 2rem; align: center">Mjolnir: LLM-Powered Fraud Detection and Personalized Report Generation from Financial Transactions</h1>

  <h3 align="center">
    A fraud detection and prevention project for <i>Samsung × KBTG Digital Fraud Cybersecurity Hackathon</i>.
    <br/>
    <br/>
    <a href="https://n8nsys.giize.com/form/7ba35445-b45e-4027-bb70-c84243abda6a">
      <img src="images/try-the-demo.svg" alt="Try the Demo" width="auto" height="45">
    </a>
    &nbsp;
    <a href="https://youtu.be/2ONQI-wyqlo">
      <img src="images/see-the-demo.svg" alt="See the Demo in Action" width="auto" height="45">
    </a>
  </h3>
</div>

## About the Project

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

> [!NOTE]
> - The workflow is currently designed to be manually executed for prototypal purposes using static data, rather than being automatically executed weekly with constant flow of new logs.
> - We used transaction logs from custom databases and generated 600,000 records for our fine-tuned model in a financial context.


## Usage

Select an employee type for report personalization. Then, choose a sample query [from the provided list](https://github.com/AungMoonLord/AI-Cybersecurity-Hackathon/tree/main/Sample%20Queries). Soon upon submission, the page will reload with the generated report with an option to copy it.

## How It Works

…………………………………………………………… our model will run an inference on each query and pass the results to the generative LLM for report generation.


## Technology Stack

### LLM Models

| Name                                                                                  | Purpose                                                       |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) | Fine-tuned classification inference model on transaction logs |
| [llama-3.1-8b-instant](https://console.groq.com/docs/model/llama-3.1-8b-instant)      | Report writing and summarization model                        |


### AI/ML Services

| Name                                                                                             | Purpose                                                                        |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| [GroqCloud](https://groq.com/groqcloud)                                                          | Run LLM summarization model (llama-3.1-8b-instant)                             |
| [Hugging Face](https://huggingface.co) with [Hugging Face Spaces](https://huggingface.co/spaces) | Store and host the fine-tuned model and run inferences                         |
| [Gradio](https://www.gradio.app)                                                                 | Deploy an interface for the fine-tuned model and connect it to n8n via its API |

### Process Automation

| Name | Purpose                                                            |
| ---- | ------------------------------------------------------------------ |
| n8n  | Connect various services and handle the entire workflow automation |
<details>
<summary>View workflow diagram</summary>
<img src="images/n8n-workflow.png" alt="n8n Workflow" width="auto" height="auto">
</details>

### Infrastructure

| Name                | Purpose                                              |
| ------------------- | ---------------------------------------------------- |
| Google Cloud Server | Host the n8n instance on GCP free tier (e2-micro VM) |
| Docker              | Run n8n in a containerized environment               |
| Nginx               | Reverse proxy for routing external traffic to n8n    |
| Certbot             | Issue and renew SSL certificates for HTTPS via Nginx |
| Dynu                | Free domain hosting service                          |