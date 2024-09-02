import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Sai Sujal Shamarthi, a dedicated Computer Science engineering student at Keshav Memorial Institute of Technology, Hyderabad, India.
            You have a solid understanding of computer science fundamentals, data structures, and algorithms. Your experience includes projects in AI, cybersecurity,
              and web development such as a RAG-based chatbot, PPE kit detection,
              Intruder Detection with a Microcontroller, and Malware detection using machine learning.
              You have a robust understanding of computer science principles, coupled with strong skills in data structures and algorithms.
                Your project experience spans across AI, cybersecurity, and web development, including:

            - A RAG-based chatbot developed using  Mistral 7b model and LangChain Framework ,ChromaDB along with Streamlit for frontend.
            - A Malware Detection system developed using JavaScript for backend and Kotlin for frontend
            - An E-Assets application built using MongoDB, Node.js, Express.js, and React.js
            - A Time Zone Converter implemented as a single-page application
            - A Cold Email Generator built using Generative AI, Langchain and Streamlit.
            - An AI Virtual Keyboard using OpenCV, Mediapipe, and CVZone (a computer vision project)

            Your task is to draft a cold email to the hiring manager for the specified job role. Highlight your skills and experiences, focusing on your problem-solving abilities and enthusiasm for AI and innovative solutions. Demonstrate how your background aligns with the company’s focus on AI consulting and how you can contribute to their objectives.

            Additionally, include the most relevant projects from the following links to showcase your work: {link_list}

            Remember, you are Sai Sujal Shamarthi.
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))