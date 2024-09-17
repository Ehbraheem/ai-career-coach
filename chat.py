import gradio as gr
from llm import process_message

app = gr.Interface(
    fn = process_message,
    allow_flagging = 'never',
    inputs = gr.Textbox(label = 'Input', lines = 2, placeholder = 'Type your question here...'),
    outputs = gr.Textbox(label = 'Output'),
    title = 'AI chatbot',
    description = 'Ask any question and the chatbot will try to answer.'
)

app.launch()
