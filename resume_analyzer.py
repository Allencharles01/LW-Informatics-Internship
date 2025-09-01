import gradio as gr
import fitz  # PyMuPDF
import requests
import json
import os
from dotenv import load_dotenv

# --- API KEY handling (safe) ---
load_dotenv()
# fallback to the literal in code only if .env isn't set
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or "ENTER GEMINI API KEY HERE"

def extract_text_from_pdf(pdf_file):
    """Works with Gradio v5: get the file path and read bytes."""
    if pdf_file is None:
        return ""

    # Gradio provides an object with .name (temp path) OR sometimes a dict/path string
    path = getattr(pdf_file, "name", None)
    if path is None and isinstance(pdf_file, dict):
        path = pdf_file.get("name") or pdf_file.get("path")
    if path is None and isinstance(pdf_file, str):
        path = pdf_file

    if not path:
        return ""

    with open(path, "rb") as f:
        data = f.read()

    text = ""
    with fitz.open(stream=data, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()

def analyze_resume(resume_text, role, company, location):
    prompt = f"""
You are a helpful assistant analyzing a candidate's resume for a job application.

Candidate Resume:
{resume_text}

Target Role: {role}
Target Company: {company}
Location: {location}

Please return the response in this exact format (no markdown):

1. Match Score (out of 100) and a short explanation.
2. Missing Skills or Experience: (3–5 bullet points)
3. Suggested Project Idea: (1 sentence)
4. Keywords to Add: (3–5 bullet points)
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=60)
        result = response.json()
        raw = result['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"<h3 style='color:red;'>❌ Gemini API Error: {str(e)}</h3>"

    # Try to extract structured output
    try:
        score = raw.split("1.")[1].split("2.")[0].strip()
        skills = raw.split("2.")[1].split("3.")[0].strip().split("\n")
        project = raw.split("3.")[1].split("4.")[0].strip()
        keywords = raw.split("4.")[1].strip().split("\n")
    except Exception:
        return f"""
        <div style="padding: 20px; background:#1e1e1e; color:#f5f5f5; font-family:'Segoe UI'; border-radius:12px;">
            <h3 style="color:#ff5e5e;">⚠ Gemini Response Was Not Structured</h3>
            <details open><summary>📄 Raw Output</summary>
            <pre style="background:#2a2a2a; padding:15px; border-radius:8px;">{raw}</pre>
            </details>
        </div>
        """

    # Build AI feedback HTML
    html = f"""
    <div style="font-family:'Segoe UI'; padding:24px; background:#1e1e1e; color:#f0f0f0; border:1px solid #444; border-radius:12px;">
        <h2 style="color:#77dd77;">📄 Gemini Resume Analysis for <b>{role}</b> at <b>{company}</b> ({location})</h2>

        <details open style="margin-top: 15px;">
            <summary style="color:#00ffd0; font-weight: bold;">🧪 Match Score</summary>
            <p style="padding-left: 10px;">{score}</p>
        </details>

        <details style="margin-top: 15px;">
            <summary style="color:#ff6b6b; font-weight: bold;">❌ Missing Skills</summary>
            <ul style="padding-left: 20px; line-height: 1.6;">
    """
    for skill in skills:
        if skill.strip():
            html += f"<li>🧩 {skill.strip().replace('*', '')}</li>"

    html += f"""
            </ul>
        </details>

        <details style="margin-top: 15px;">
            <summary style="color:#ffd166; font-weight: bold;">💡 Suggested Project</summary>
            <p style="padding-left: 10px;">{project}</p>
        </details>

        <details style="margin-top: 15px;">
            <summary style="color:#feca57; font-weight: bold;">🔑 Keywords to Add</summary>
            <ul style="padding-left: 20px; line-height: 1.6;">
    """
    for keyword in keywords:
        if keyword.strip():
            html += f"<li>📌 {keyword.strip().replace('*', '')}</li>"

    # Add job links section
    html += f"""
            </ul>
        </details>

        <details style="margin-top: 15px;">
            <summary style="color:#90caf9; font-weight: bold;">💼 Suggested Job Links</summary>
            <ul style="padding-left: 20px; line-height: 1.6;">
                <li><a href="https://www.linkedin.com/jobs/search/?keywords={role}&location={location}" target="_blank" style="color:#82b1ff;">🔗 LinkedIn: {role} in {location}</a></li>
                <li><a href="https://www.indeed.com/jobs?q={role}&l={location}" target="_blank" style="color:#82b1ff;">🔗 Indeed: {role} jobs</a></li>
                <li><a href="https://internshala.com/internships/{role.lower().replace(' ', '-')}-internship" target="_blank" style="color:#82b1ff;">🔗 Internshala: {role} internships</a></li>
            </ul>
        </details>
    </div>
    """
    return html

def smart_resume_analyzer(input_mode, resume_text, resume_pdf, role, company, location):
    try:
        resume_data = resume_text if input_mode == "Paste Text" else extract_text_from_pdf(resume_pdf)
    except Exception as e:
        return f"<h3 style='color:red;'>❌ PDF Read Error: {str(e)}</h3>"
    if not resume_data:
        return "<h3 style='color:orange;'>⚠ No text extracted from the PDF. If it’s a scanned/image PDF, try pasting text.</h3>"
    return analyze_resume(resume_data, role, company, location)

# Gradio UI
with gr.Blocks(css="""
body {
  font-family: 'Segoe UI', sans-serif;
  background: #121212;
}
.gr-button {
  background-color: #4CAF50 !important;
  color: white !important;
  font-weight: bold;
  border-radius: 8px;
}
.gr-html-box {
  background-color: #1e1e1e;
  border-radius: 12px;
  padding: 20px;
  border: 1px solid #444;
}
""") as demo:

    gr.Markdown("# 🧠 Gemini Resume Analyzer")
    gr.Markdown("✨ Paste or upload your resume to get AI-powered analysis with match score, suggestions, and job links.")

    input_mode = gr.Radio(["Paste Text", "Upload PDF"], label="Choose Resume Input Method", value="Paste Text")

    with gr.Row():
        resume_text = gr.Textbox(label="📄 Resume Text", lines=10, visible=True)
        resume_pdf = gr.File(label="📄 Upload PDF", file_types=[".pdf"], visible=False)

    def toggle_inputs(mode):
        return gr.update(visible=(mode == "Paste Text")), gr.update(visible=(mode == "Upload PDF"))

    input_mode.change(fn=toggle_inputs, inputs=input_mode, outputs=[resume_text, resume_pdf])

    with gr.Row():
        role = gr.Textbox(label="💼 Job Role", placeholder="e.g. Full Stack Developer")
        company = gr.Textbox(label="🏢 Target Company", placeholder="e.g. Google")
        location = gr.Textbox(label="📍 Location", placeholder="e.g. Hyderabad")

    analyze_btn = gr.Button("📊 Analyze Resume")
    output = gr.HTML()

    analyze_btn.click(fn=smart_resume_analyzer,
                      inputs=[input_mode, resume_text, resume_pdf, role, company, location],
                      outputs=output)

demo.launch()

