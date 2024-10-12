# AI Career Coach: Your Personalized Job Application Coach Based on LLM

## Project Overview

Embark on a journey to master the integration of cutting-edge large language models (LLM) into user-friendly applications. This project will guide you through creating powerful tools to enhance the job application process using AI.

### Estimated Time Needed: 60 minutes

## Modules

### 1. Introduction to Gradio

Gain hands-on experience with Gradio by creating a simple yet powerful sample application. Gradio allows you to quickly build and share machine learning models with a user-friendly interface.

### 2. Unlocking the Potential of watsonx.ai's Large Language Model

Dive deeper into the capabilities of watsonx.ai's LLM. Learn how to harness its power for real-world applications, making your AI solutions more effective and impactful.

### 3. Developing Specialized Tools

By the end of this project, you will be adept at developing three specialized tools:

- **AI-driven Resume Enhancer**: Improve and optimize resumes using AI.
- **Personalized Cover Letter Generator**: Generate customized cover letters tailored to specific job applications.
- **Strategic Job Hunting Advisor**: Provide strategic advice for job seekers based on AI analysis.

## Learning Outcomes

Each module is carefully designed to not only teach you the technical know-how but also to provide insights into the ever-evolving job market. This project will make you well-equipped to cater to the needs of modern job seekers. "AI Career Coach" is more than just a learning experience; it's a stepping stone to a future where AI bridges the gap between talent and opportunity.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- An IBM Cloud account (for watsonx.ai)
- A GitHub account (for GitHub models)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ehbraheem/ai-career-coach.git
   cd ai-career-coach
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables by copying the sample file and filling in the required keys:
   ```bash
   cp .env.sample .env
   ```

### Setting Up IBM Watsonx.ai

1. Obtain your IBM Cloud credentials and API keys.
2. Fill in the following variables in your `.env` file:
   ```env
   IBM_WATSON_X_API_KEY=your_ibm_watsonx_api_key
   IBM_WATSON_X_PROJECT_ID=your_ibm_watsonx_project_id
   IBM_WATSON_X_URL=your_ibm_watsonx_url
   ```

### Setting Up GitHub Models

1. Obtain your GitHub credentials and API keys.
2. Fill in the following variables in your `.env` file:
   ```env
   GITHUB_MODEL_URL=your_github_model_url
   GITHUB_MODEL_NAME=your_github_model_name
   GITHUB_TOKEN=your_github_token
   ```

For more details on setting up GitHub models, refer to the [GitHub models documentation](https://docs.github.com/en/github-models/prototyping-with-ai-models).

### Usage

Run the application:

```bash
python app.py
```

You can now interact with the AI Career Coach through the Gradio interface. Follow the prompts to enhance your resume, generate cover letters, and receive job hunting advice.

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgements

[IBM](https://www.ibm.com/watson) Watson for providing the AI capabilities.
[Gradio](https://gradio.app) for the user-friendly interface.
All contributors and users for their support.

For more details on GitHub models, refer to the [GitHub models documentation](https://docs.github.com/en/github-models/prototyping-with-ai-models).
