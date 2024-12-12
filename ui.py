import gradio as gr
from example1 import chain



def chat(question,history):
    if question = "":
return "pkease ask question"
else:
return chain.invoke(question)

gr.ChatInterface(
    fn=chat,
    type = "messages"
).lounch()