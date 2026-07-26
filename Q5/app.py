import gradio as gr
import os
import json
from PIL import Image

# -------------------------------
# Load Q1 JSON
# -------------------------------

def load_q1():
    json_path = "outputs/q1_result.json"

    if os.path.exists(json_path):
        with open(json_path, "r") as f:
            data = json.load(f)
        return json.dumps(data, indent=4)
    else:
        return "Q1 JSON output not found."

# -------------------------------
# Load Q2 Outputs
# -------------------------------

def load_q2():
    parsing = "outputs/human_parsing_map.png"
    agnostic = "outputs/agnostic_person.png"
    garment = "outputs/garment_mask.png"

    return parsing, agnostic, garment

# -------------------------------
# Gradio UI
# -------------------------------

with gr.Blocks(title="Virtual Try-On Assessment Demo") as demo:

    gr.Markdown("# 👕 Virtual Try-On Assessment Demo")
    gr.Markdown("### MCA Final Project Submission")

    with gr.Tab("Q1 - Garment Understanding"):

        gr.Markdown("### Garment Attributes")
        btn1 = gr.Button("Load Q1 Result")
        output_json = gr.Code(language="json")

        btn1.click(load_q1, outputs=output_json)

    with gr.Tab("Q2 - Human Parsing"):

        btn2 = gr.Button("Load Q2 Outputs")

        parsing = gr.Image(label="Human Parsing Map")
        agnostic = gr.Image(label="Agnostic Person")
        garment = gr.Image(label="Garment Mask")

        btn2.click(
            load_q2,
            outputs=[parsing, agnostic, garment]
        )

    with gr.Tab("Q3 & Q4"):

        gr.Markdown("""
## Status

Q3 – Virtual Try-On

Attempted using CatVTON. The implementation could not be completed due to dependency and compatibility issues encountered during setup.

Q4 – Evaluation

Evaluation metrics could not be generated because a final try-on image was not produced.
""")

demo.launch()
