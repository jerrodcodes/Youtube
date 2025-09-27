"""Gradio app comparing base FLAN-T5 vs the fine-tuned checkpoint."""

import os

import gradio as gr
from transformers import pipeline

BASE_MODEL_ID = os.getenv("BASE_MODEL_ID", "google/flan-t5-small")
FINETUNED_MODEL_ID = os.getenv("FINETUNED_MODEL_ID", "<YOUR-USERNAME>/google-t5-samsum-demo")
TASK_PREFIX = os.getenv("TASK_PREFIX", "summarize: ")


base_pipe = pipeline("summarization", model=BASE_MODEL_ID)
finetuned_pipe = pipeline("summarization", model=FINETUNED_MODEL_ID)


def summarize(text: str) -> tuple[str, str]:
    prompt = TASK_PREFIX + text
    base_summary = base_pipe(prompt, max_length=60, min_length=10, do_sample=False)[0]["summary_text"]
    finetuned_summary = finetuned_pipe(prompt, max_length=60, min_length=10, do_sample=False)[0][
        "summary_text"
    ]
    return base_summary, finetuned_summary


iface = gr.Interface(
    fn=summarize,
    inputs=gr.Textbox(lines=8, label="Dialogue", placeholder="Paste a conversation here"),
    outputs=[
        gr.Textbox(label=f"Base model ({BASE_MODEL_ID})"),
        gr.Textbox(label=f"Fine-tuned model ({FINETUNED_MODEL_ID})"),
    ],
    title="T5 SAMSum Demo",
    description="Compare the original FLAN-T5-small summarization with the fine-tuned checkpoint.",
)


if __name__ == "__main__":
    iface.launch()
