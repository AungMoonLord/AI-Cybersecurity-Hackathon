<br />
<div align="center">
  <a>
    <img src="images/logo.png" alt="Logo" width="auto" height="auto">
  </a>

  <h1 style="margin-top: 2rem; align: center">Mjolnir: AI-Powered Fraud Detection and Personalized Report Generation from Financial Transaction Logs</h1>

  <h3 align="center">
    A fraud detection and prevention project for <i>Samsung × KBTG Digital Fraud Cybersecurity Hackathon</i>.
    <br/>
    <br/>
    <a href="https://n8nsys.giize.com/form/7ba35445-b45e-4027-bb70-c84243abda6a">
      <img src="images/try-the-demo.svg" alt="Try the Demo" width="auto" height="40">
    </a>
    &nbsp;
    <a href="https://youtu.be/si21QpFcjiE">
      <img src="images/see-the-demo.svg" alt="See the Demo in Action" width="auto" height="40">
    </a>
  </h3>
</div>

## About the Project

Mjolnir is an AI-powered security tool that automates the detection of fraud in financial transaction logs. It uses a fine-tuned BERT model to classify each query into `normal` and `anomaly` and an LLM to translate those technical threats into plain English. Instead of generic alerts, it generates personalized reports for managers, developers, and executives like CISOs. Mjolnir's objective is to rapidly detect, prevent, and mitigate the potential damage these cyberattacks by automating such processes.

In the future, we aim to improve the system's accuracy by introducing human-in-the-loop checking for chances of the model incorrectly classifying a query and developing the model that can constantly train itself from new and corrected data.

> [!NOTE]
> While the production environment will monitor data 24/7 and generate reports by comparing the oldest and newest entries of an appropriate timeframe, the current prototype is limited to occasional manual runs with a smaller workload of log excerpts (about 200 lines) due to resource constraints.

## Usage

Select an employee type for report personalization. Then, choose a sample query [from the provided list](https://github.com/AungMoonLord/AI-Cybersecurity-Hackathon/tree/main/Sample%20Queries). Soon upon submission, the page will reload with the generated report with an option to copy it.


## Technology Stack

### LLM Models

| Name                                                                                                            | Purpose                                                       |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [AungMoonLord/bert-log-anomaly-detection](https://huggingface.co/AungMoonLord/bert-log-anomaly-detection)                           | Our fine-tuned classification inference model on transaction logs (more details inside) |
| [meta-llama/llama-4-scout-17b-16e-instruct](https://console.groq.com/docs/model/llama-4-scout-17b-16e-instruct) | Report writing and summarization model                        |


### AI/ML Services

| Name                                                                                             | Purpose                                                                        |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| [GroqCloud](https://groq.com/groqcloud)                                                          | Run LLM summarization model                                                    |
| [Hugging Face](https://huggingface.co) with [Hugging Face Spaces](https://huggingface.co/spaces) | Store and host the fine-tuned model and run inferences                         |
| [Gradio](https://www.gradio.app)                                                                 | Deploy an interface for the fine-tuned model and connect it to n8n via its API |

### Process Automation

| Name                  | Purpose                                                            |
| --------------------- | ------------------------------------------------------------------ |
| [n8n](https://n8n.io) | Connect various services and handle the entire workflow automation |
<details>
<summary>View workflow diagram</summary>
<img src="images/n8n-workflow.png" alt="n8n Workflow" width="auto" height="auto">
</details>

### Infrastructure

| Name                                            | Purpose                                              |
| ----------------------------------------------- | ---------------------------------------------------- |
| [Google Cloud Server](https://cloud.google.com) | Host the n8n instance on GCP free tier (e2-micro VM) |
| [Docker](https://www.docker.com)                | Run n8n in a containerized environment               |
| [Nginx](https://nginx.org)                      | Reverse proxy for routing external traffic to n8n    |
| [Certbot](https://certbot.eff.org)              | Issue and renew SSL certificates for HTTPS via Nginx |
| [Dynu](https://www.dynu.com)                    | Free domain hosting service                          |
