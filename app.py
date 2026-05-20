import gradio as gr
from search import search_and_ask
from history import add_to_history, download_txt, download_pdf, clear_history

def handle_query(query):
    answer, sources, full_response = search_and_ask(query)
    add_to_history(query, answer, sources)
    return full_response

with gr.Blocks(title="Local Search Bot") as demo:
    gr.Markdown("# Local Search Bot")
    gr.Markdown("A professional AI search assistant powered by phi3:mini + Tavily.")

    query_input = gr.Textbox(label="Your Question", placeholder="Type your question here...")
    answer_output = gr.Textbox(label="Answer")
    submit_btn = gr.Button("Submit", variant="primary")
    submit_btn.click(fn=handle_query, inputs=query_input, outputs=answer_output)

    gr.Markdown("### Chat History")
    with gr.Row():
        txt_btn = gr.Button("Download as TXT")
        pdf_btn = gr.Button("Download as PDF")
        clear_btn = gr.Button("Clear History", variant="stop")

    txt_file = gr.File(label="TXT Download")
    pdf_file = gr.File(label="PDF Download")
    clear_output = gr.Textbox(label="Status", interactive=False)

    txt_btn.click(fn=download_txt, outputs=txt_file)
    pdf_btn.click(fn=download_pdf, outputs=pdf_file)
    clear_btn.click(fn=clear_history, outputs=clear_output)

demo.launch()