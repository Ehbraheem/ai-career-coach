import gradio as gr
from llm import polish_resume

app = gr.Interface(
    fn = polish_resume,
    allow_flagging = 'never',
    inputs = [
        gr.Textbox(label = "Position Name", placeholder = "Enter the name of the position..."),
        gr.Textbox(label = "Resume Content", placeholder = "Paste your resume content here...", lines = 20),
        gr.Textbox(label = "Polish Instruction (Optional)", placeholder = "Enter specific instructions or areas for improvement (optional)...", lines = 2),
    ],
    outputs = gr.Textbox(label = 'Polished Content'),
    title = 'Resume Polish Application',
    description = 'This application helps you polish your resume. Enter the position your want to apply, your resume content, and specific instructions or areas for improvement (optional), then get a polished version of your content.'
)


if __name__ == '__main__':
    app.launch()
