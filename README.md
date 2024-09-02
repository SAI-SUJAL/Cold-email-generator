📧 Cold Mail Generator

Cold email generator using groq, langchain and streamlit. It allows users to input the URL of a company's careers page. The tool then extracts job listings from that page and generates personalized cold emails. These emails include relevant portfolio links sourced from a vector database, based on the specific job descriptions.

Take a scenario: Cold emails can be an effective way for students to reach out to hiring managers for various reasons. Here’s a scenario illustrating how and why students might send cold emails:

Scenario: Job Search for a Recent Graduate Background: Sai Sujan is a recent graduate with a degree in Computer Science. He has just completed a coding bootcamp and is looking for a full-time job as a software developer. He has identified several companies where he’d like to work, but he doesn’t have any direct connections within those organizations.

Objective: Sai Sujan wants to introduce himself to hiring managers at these companies to express his interest in potential job opportunities and to demonstrate his enthusiasm and qualifications.

The Cold email tool helps in generating a direct email for the respective job description upon giving it as input, thus saving time and also aligning itself accordingly to the job role.
![Screenshot (5)](https://github.com/user-attachments/assets/ee0005a2-ab5e-4b14-ac7b-653053ffb561)

![image](https://github.com/user-attachments/assets/c14e6cfc-cec9-4918-82bd-d93316b6d17c)


Set-up To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside app/.env update the value of GROQ_API_KEY with the API_KEY you created.

To get started,
first install the dependencies using: 
          pip install -r requirements.txt

Run the streamlit app: 
          streamlit run app/main.py
