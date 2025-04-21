from fpdf import FPDF

# Step 1: Define the text content
text_content = """OpenAI

o3 (April 2025)
Advanced reasoning model with "private chain of thought" planning.
Performs well on complex tasks in coding, math, and science.

o4-mini (April 2025)
Lighter, multimodal version of o3.
Available to free-tier ChatGPT users.
Can interpret images and sketches.

Google

Gemini 2.5 Flash (April 2025)
Includes a "thinking budget" feature to control computational reasoning effort.
Designed for balance between speed, cost, and quality.

Gemini Robotics (March 2025)
Vision-language-action model built for robotics.
Enables adaptive behavior in real-world settings.

Meta

LLaMA 4 (April 2025)
Released in three versions: Scout, Maverick, and Behemoth (still training).
Designed to handle socially and politically sensitive topics.
Scout and Maverick are open-weight models.

China

DeepSeek-R1 (January 2025)
685-billion-parameter model with transparent reasoning steps.
Low-cost training approach.
Strong in code and mathematical tasks.

Qwen 2.5 Series (March 2025)
Developed by Alibaba.
Includes Qwen2.5-VL-32B-Instruct and Qwen2.5-Omni-7B.
Open-source under Apache 2.0.
Competitive on language understanding benchmarks.

Research and Open Source

NeoBERT (February 2025)
Next-generation encoder.
Outperforms BERT and RoBERTa on multiple text benchmarks.

BriLLM (March 2025)
Brain-inspired LLM with signal-flow architecture.
Designed for high interpretability.

Salamandra (February 2025)
Open-source decoder-only model family (2B, 7B, 40B parameters).
Trained on 35 European languages and programming code."""

# Step 2: Create a PDF instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Step 3: Set font for the PDF
pdf.set_font("Arial", size=12)

# Step 4: Add content to the PDF
for line in text_content.split("\n"):  # Split the text into lines
    pdf.cell(0, 10, txt=line, ln=True)  # Add each line to the PDF

# Step 5: Save the PDF to the current directory
output_file = "new_llm_models.pdf"
pdf.output(output_file)

print(f"PDF has been created and saved as '{output_file}' in the current directory.")
