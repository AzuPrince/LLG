from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

def main():
    print("Hello from llg!")
    #print("Your Google API Key is:", os.getenv("GOOGLE_API_KEY"))

    information = "Azu Prince Tojah is a software developer with a passion for building innovative solutions. With expertise in Python, JavaScript, and cloud technologies, Azu has successfully delivered numerous projects across various industries. Azu is known for their problem-solving skills and dedication to creating efficient and scalable applications."
    summary_template = "given the information about a person, summarize it into 1. Name 2. Occupation 3. Skills 4. Achievements. Information: {information}"
    
    input_variables=["information"]
    template=summary_template
    summary_prompt_template = PromptTemplate(input_variables, template)

    llm = GoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.7)
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print(response)
    
    
if __name__ == "__main__":
    main()
   
