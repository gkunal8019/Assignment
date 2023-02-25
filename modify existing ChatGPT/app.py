import os
import openai
import gradio as gr

openai.api_key = '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'

start_sequence = "\nAI:"
restart_sequence = "\nHuman:"

prompt = "Amazon.com, Inc. (/mzn/ AM--zon) is an American multinational technology company focusing on e-commerce [1], cloud computing, online advertising, digital streaming, and artificial intelligence. It is one of the Big Four technology companies, along with Google, Apple and Facebook. Founded by Jeff Bezos in 1994, Amazon started as an online book store, but has since expanded to include a wide range of products and services such as consumer electronics, apparel, furniture, food, toys, and jewelry. Amazon is also the world’s largest provider of cloud infrastructure services, offering a suite of products that enable customers to build sophisticated applications with increased flexibility, scalability, and reliability. Additionally, Amazon operates a number of subsidiaries, including Whole Foods Market, Audible, and Zappos."

def openai_creat(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    ) 
    return response.choices[0].text


def conversation_history(input, history):
    history = history or []
    s = list(sum(history,()))
    s.append(input)
    inp =' '.join(s)
    output = openai_creat(inp)
    history. append((input, output))
    return history, history

blocks = gr.Blocks()

with blocks:
    chatbot = gr.Chatbot()
    massage = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit =gr.Button('Click')
    submit.click(conversation_history,inputs=[massage,state],outputs=[chatbot,state])
    

blocks.launch(debug=True)