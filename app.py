from openai import OpenAI
import gradio as gr
import os

cserve_host = os.getenv("CSERVE_HOST", "http://cserve:8080")
print(f'cserve_host: {cserve_host}')

client = OpenAI(
    base_url=f'{cserve_host}/openai/v1/',
    # required but ignored
    api_key='none',
)

def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})
  
    response = client.chat.completions.create(model='google/gemma-2b-it',
    messages= history_openai_format,
    temperature=1.0,
    stream=True)

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
              partial_message = partial_message + chunk.choices[0].delta.content
              yield partial_message

with gr.Blocks() as demo:

    gr.Markdown("# Chat with CServe!")
    gr.ChatInterface(predict)

demo.launch(server_name='0.0.0.0', server_port=8081, share=True)
