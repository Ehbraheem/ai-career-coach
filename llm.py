from os import getenv
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes, DecodingMethods
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from dotenv import load_dotenv

load_dotenv()


Watsonx_API = getenv('IBM_WATSON_X_API_KEY')
Project_id = getenv('IBM_WATSON_X_PROJECT_ID') or 'skills-network'
Watsonx_URL = getenv('IBM_WATSON_X_URL') or 'https://us-south.ml.cloud.ibm.com'

credentials = {
    'url': Watsonx_URL,
    'apikey' : Watsonx_API
}

model_id = ModelTypes.LLAMA_3_70B_INSTRUCT.value

params = {
    GenParams.MAX_NEW_TOKENS: 1024,
    GenParams.TEMPERATURE: 0.5,
}

model = Model(
    model_id = model_id,
    project_id = Project_id,
    credentials = credentials,
    params = params,
)

def career_advice(position, job_description, resume):
    prompt = f"Considering the job description: {job_description}, and the resume provided: {resume}, identify areas for enhancement in the resume. Offer specific suggestions on how to improve these aspects to better match the job requirements and increase the likelihood of being selected for the position of {position}."

    return __process_prompt__(prompt)
    

def cover_letter(company, position, job_description, resume, skills = None):
    prompt = (
        f"Generate a customized cover letter using the company name: {company}, "
        f"the position applied for: {position}, and the job description: {job_description}. "
        f"Ensure the cover letter highlights my qualifications and experience as detailed in the "
        f"resume content: {resume}. Adapt the content carefully to avoid including experiences "
        f"not present in my resume but mentioned in the job description. The goal is to emphasize "
        f"the alignment between my existing skills and the requirements of the role."
    )

    if skills:
        prompt += f" Consider including these job skills keywords: {skills} where necessary."

    # Remove excess whitespace
    prompt = ' '.join(prompt.split())

    return __process_prompt__(prompt)

def polish_resume(position, resume, polish_prompt = ''):
    if polish_prompt.strip():
        prompt = f"Given the resume content: '{resume}', polish it based on the following instructions: {polish_prompt} for the {position} position"
    else:
        prompt = f"Suggest improvements for the following resume content: '{resume}' to better align with the requirements and expectations of a {position} position. Return the polished version, highlighting necessary adjustments for clarity, relevance, and impact in relation to the targeted role."

    return __process_prompt__(prompt)



def process_message(user_message):
    prompt = f'''Respond to the query: ```{user_message}```'''
    return __process_prompt__(prompt)



def __process_prompt__(prompt):
    response_text = model.generate_text(prompt=prompt)
    print('WatsonX response: ', response_text)

    return response_text


if __name__ == '__main__':
    prompt = "How to be a good Data Scientist?"
    response = process_message(prompt)
    print(response)
