import gradio as gr
from llm import career_advice

app = gr.Interface(
    fn = career_advice,
    allow_flagging = 'never',
    inputs = [
        gr.Textbox(label = "Position Applied For", placeholder = "Enter the position you are applying for..."),
        gr.Textbox(label = "Job Description Information", placeholder = "Paste the job description here...", lines = 10),
        gr.Textbox(label = "Your Resume Content", placeholder = "Paste your resume content here...", lines = 10),
    ],
    outputs = gr.Textbox(label = 'Advice'),
    title = "Career Advisor",
    description = "Enter the position you're applying for, paste the job description, and your resume content to get advice on what to improve for getting this job."
)

if __name__ == '__main__':
    app.launch()