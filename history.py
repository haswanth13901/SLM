from fpdf import FPDF
from datetime import datetime

chat_history = []

def add_to_history(question, answer, sources):
    chat_history.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "question": question,
        "answer": answer,
        "sources": sources
    })

def download_txt():
    if not chat_history:
        return None
    path = "chat_history.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write("LOCAL SEARCH BOT — CHAT HISTORY\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n\n")
        for i, entry in enumerate(chat_history, 1):
            f.write(f"[{i}] {entry['time']}\n")
            f.write(f"Q: {entry['question']}\n")
            f.write(f"A: {entry['answer']}\n")
            f.write(f"Sources:\n{entry['sources']}\n")
            f.write("-" * 50 + "\n\n")
    return path

def download_pdf():
    if not chat_history:
        return None
    path = "chat_history.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Local Search Bot - Chat History", ln=True, align="C")
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 8, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
    pdf.ln(5)

    for i, entry in enumerate(chat_history, 1):
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(0, 8, f"[{i}] {entry['time']}", ln=True)
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 7, "Question:", ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 6, entry['question'])
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 7, "Answer:", ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 6, entry['answer'])
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 7, "Sources:", ln=True)
        pdf.set_font("Helvetica", "", 9)
        pdf.multi_cell(0, 6, entry['sources'])
        pdf.ln(4)
        pdf.set_draw_color(200, 200, 200)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(4)

    pdf.output(path)
    return path

def clear_history():
    chat_history.clear()
    return "Chat history cleared."