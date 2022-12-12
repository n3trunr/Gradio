'''
Components Attributes
We saw some simple Textbox components in the previous examples, 
but what if you want to change how the UI components look or behave?

Let's say you want to customize the input text field — 
for example, you wanted it to be larger and have a text placeholder. 

If we use the actual class for Textbox instead of using the string shortcut, 
you have access to much more customizability through component attributes.
'''

import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=2, placeholder="Name Here..."),
    outputs="text",
)
demo.launch()