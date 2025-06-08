import gradio as gr
from groq_utils import summarize_article
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_summary(article_text):
    summary = summarize_article(article_text)

    pdf_path = "summary.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    text = c.beginText(40, height - 50)
    text.setFont("Helvetica", 12)

    for line in summary.split('\n'):
        text.textLine(line)
    c.drawText(text)
    c.showPage()
    c.save()

    return summary, pdf_path

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        <div style="text-align: center; font-size: 32px; font-weight: bold; margin-bottom: 10px;">📰 Briefly</div>
        <div style="text-align: center; font-size: 16px; color: gray; margin-bottom: 20px;">
        Paste any news article and get a simple, clear summary — with a downloadable PDF!
        </div>
        """,
        elem_id="header"
    )

    with gr.Row():
        with gr.Column(scale=1):
            article_input = gr.Textbox(
                lines=20, 
                label="📄 Paste News Article", 
                placeholder="Paste your news article here...",
                show_copy_button=True
            )
            summarize_btn = gr.Button("✨ Summarize Article", variant="primary")

        with gr.Column(scale=1):
            output_summary = gr.Textbox(
                lines=20, 
                label="📝 Simplified Summary",
                show_copy_button=True
            )
            download_btn = gr.File(label="📥 Download Summary as PDF")

    summarize_btn.click(
        fn=generate_summary,
        inputs=[article_input],
        outputs=[output_summary, download_btn]
    )

demo.launch()
