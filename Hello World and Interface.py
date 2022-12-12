import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch() 

'''
The Interface Class
You'll notice that in order to make the demo, we created a gradio.Interface. This Interface class can wrap any Python function with a user interface. In the example above, we saw a simple text-based function, but the function could be anything from music generator to a tax calculator to the prediction function of a pretrained machine learning model.

The core Interface class is initialized with three required parameters:

fn: the function to wrap a UI around
inputs: which component(s) to use for the input (e.g. "text", "image" or "audio")
outputs: which component(s) to use for the output (e.g. "text", "image" or "label")
Let's take a closer look at these components used to provide input and output.
'''