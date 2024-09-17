import gradio as gr

demo = gr.Interface(
    fn = lambda Num1, Num2: Num1 + Num2,
    inputs = ["number", "number"],
    outputs = "number"
)

demo.launch(server_name="0.0.0.0", server_port= 7860)
