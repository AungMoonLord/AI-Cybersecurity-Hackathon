<br />
<div align="center">
  <a>
    <img src="images/mjolnir-logo.svg" alt="Logo" width="auto" height="100">
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

There are many great README templates available on GitHub; however, I didn't find one that really suited my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!

Use the `BLANK_README.md` to get started.

> [!NOTE]
> Useful information that users should know, even when skimming content.

## Technology Stack


### LLM Models

| Name                                                                                  | Purpose                                                       |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) | Fine-tuned classification inference model on transaction logs |
| [llama-3.1-8b-instant](https://console.groq.com/docs/model/llama-3.1-8b-instant)      | Report writing and summarization model                        |

### AI/ML Services

| Name                                                                                             | Purpose                                                |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| [GroqCloud](https://groq.com/groqcloud)                                                          | Run LLM summarization models (llama-3.1-8b-instant)    |
| [Hugging Face](https://huggingface.co) with [Hugging Face Spaces](https://huggingface.co/spaces) | Store and host the fine-tuned model and run inferences |

### Process Automation

| Name | Purpose                                                        |
| ---- | -------------------------------------------------------------- |
| n8n  | Connect various services and handle entire workflow automation |
<details>
<summary>View workflow diagram</summary>
<img src="images/n8n-workflow.png" alt="n8n Workflow" width="auto" height="auto">
</details>

### Model Interface Layer

| Name   | Purpose                                                 |
| ------ | ------------------------------------------------------- |
| Gradio | Deploy an interface for the model and connect it to n8n |

### Infrastructure & DevOps

| Name                | Purpose                                                   |
| ------------------- | --------------------------------------------------------- |
| Google Cloud Server | Host the n8n instance on GCP free tier (e2-micro VM)      |
| Docker              | Run n8n in a containerized environment                    |
| Nginx               | Reverse proxy for routing external HTTP(S) traffic to n8n |
| Certbot             | Issue and renew SSL certificates for HTTPS via Nginx      |

### Networking & Domain

| Name | Purpose                     |
| ---- | --------------------------- |
| Dynu | Free domain hosting service |


## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
