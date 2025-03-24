# Professional Email Generator

A web-based tool that utilizes **Streamlit** and **OpenAI's GPT-4** model to automatically generate professional email drafts based on user input. This tool allows users to describe the email they need, and the app generates a polished and professional email suitable for business correspondence.

## Features

- **Generate Professional Emails**: Simply describe the email you need, and the tool generates a fully formatted, professional email.
- **Customizable Templates**: Easily adapt to different scenarios, such as meeting requests, follow-ups, business inquiries, and more.
- **Intuitive Interface**: The user-friendly Streamlit interface allows anyone, even with minimal technical expertise, to create professional emails in seconds.
- **Powered by GPT-4**: Uses OpenAI’s GPT-4 to generate coherent, context-aware email drafts.

## Requirements

- **Python 3.x**: A modern version of Python is required.
- **Streamlit**: For building the web interface.
- **OpenAI**: For generating email content via the GPT-4 model.

### Main Libraries:

1. **openai**: For interacting with OpenAI’s GPT-4 API to generate email content.
2. **streamlit**: For creating the web interface that users interact with.
3. **python-dotenv**: For securely loading the OpenAI API key from an environment file.

## Setup Instructions

### 1. Clone the Repository

To get started, clone the repository to your local machine:

### 2. Set Up OpenAI API Key

You will need an **OpenAI API key** to use GPT-4. You can obtain it from [OpenAI’s website](https://beta.openai.com/signup/).

Once you have the API key, create a `.env` file in the project root directory and add the following:

OPENAI_API_KEY=your_openai_api_key

### 3. Install Dependencies

Run the following command to install all required Python dependencies:
``sh
pip install -r requirements.txt
``sh

### 4. Run the Application

To start the application, execute the following command in the project root directory:
``sh
streamlit run email_bot_generator.py
``sh
