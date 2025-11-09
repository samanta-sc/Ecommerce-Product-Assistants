# Ecommerce Chatbot

Welcome to the Ecommerce Chatbot project! This chatbot is designed to assist users with their online shopping experience by providing product recommendations, answering questions, and assisting with various inquiries related to the ecommerce store on bilingual(English + Bengali).

![Ecommerce chatbot](https://github.com/samanta-sc/Ecommerce-Product-Assistants/blob/main/resources/Chatbot.gif)

## Overview

The Ecommerce Chatbot is built using Python and FastAPI framework. It leverages natural language processing (NLP) techniques to understand user queries and generate appropriate responses. The chatbot integrates with the ecommerce store's product database to provide personalized recommendations and information about available products.

## Features

- Interactive chat interface for users to interact with the chatbot.
- Natural language processing for understanding user queries.
- Product recommendation engine based on user preferences and browsing history.
- Integration with the ecommerce store's product database.
- Ability to handle various user inquiries such as product availability, pricing, shipping information, etc.
- CI/CD added using github action via aws ec2 instances, containerized via docker, FastAPI

## Dataset Curation
- Flipcart Product Data is translated into Bengali Language using Gemini API
- Translated data is merged with original

## Installation

To set up the Ecommerce Chatbot locally, follow these steps:

1. Clone the repository to your local machine:
```
   git clone https://github.com/your-username/ecommerce-chatbot.git
```

2. Navigate to the project directory:
```
   cd ecommerce-chatbot
```

3. Install the required Python packages using pip:
```
pip install -r requirements.txt
```

4. Set up environment variables:
- Create a .env file in the project directory.
- Define the necessary environment variables such as database connection strings, API keys, etc.
  
5. Run docker desktop Application:
```
docker build -t fastapi-ecommbot .
docker run -d -p 5000:5000 fastapi-ecommbot
```
6. Paste on browser
   - localhost:5000
  
## 📸 Demo

<table>
  <tr>
    <td>Chatbot API</td>
     <td>English Query</td>
     <td>Bengali Query</td>
  </tr>
  <tr>
    <td><img align="left" src="resources/Screenshot (10).png" width=290 height=480></td>
    <td><img align="left" src="resources/Screenshot (11).png" width=290 height=480></td>
    <td><img align="left" src="resources/Screenshot (12).png" width=290 height=480></td>
  </tr>
 </table>
