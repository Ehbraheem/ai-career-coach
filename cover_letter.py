import gradio as gr
from llm import cover_letter

app  =  gr.Interface(
    fn = cover_letter,
    allow_flagging = "never",
    inputs = [
        gr.Textbox(label = "Company Name", placeholder = "Enter the name of the company..."),
        gr.Textbox(label = "Position Name", placeholder = "Enter the name of the position..."),
        gr.Textbox(label = "Job Description Information", placeholder = "Paste the job description here...", lines = 10),
        gr.Textbox(label = "Resume Content", placeholder = "Paste your resume content here...", lines = 10),
        gr.Textbox(label = " Job Skills Keywords (Optional)", placeholder = "Paste the job required skills keywords here...", lines = 2),

    ],
    outputs = gr.Textbox(label = "Customized Cover Letter"),
    title = "Customized Cover Letter Generator",
    description = "Generate a customized cover letter by entering the company name, position name, job description and your resume."
)


if __name__ == '__main__':
    app.launch()