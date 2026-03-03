import tkinter as tk
from tkinter import messagebox, filedialog
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

def generate_portfolio():
    name = name_entry.get()
    education = education_entry.get("1.0", tk.END).strip()
    bio = bio_entry.get("1.0", tk.END).strip()
    skills = skills_entry.get("1.0", tk.END).strip().split('\n')
    projects = projects_entry.get("1.0", tk.END).strip().split('\n')

    if not name or not bio:
        messagebox.showerror("Input Error", "Name and Bio are required.")
        return

    output = f"PORTFOLIO\n\n"
    output += f"Name: {name}\n\n"
    output += f"Education:\n{education}\n\n"
    output += f"Bio:\n{bio}\n\n"
    output += "Skills:\n"
    output += '\n'.join([f"• {skill}" for skill in skills if skill]) + "\n\n"
    output += "Projects:\n"
    output += '\n'.join([f"• {proj}" for proj in projects if proj])

    output_box.config(state='normal')
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, output)
    output_box.config(state='disabled')


def save_as_pdf():
    name = name_entry.get()
    education = education_entry.get("1.0", tk.END).strip()
    bio = bio_entry.get("1.0", tk.END).strip()
    skills = skills_entry.get("1.0", tk.END).strip().split('\n')
    projects = projects_entry.get("1.0", tk.END).strip().split('\n')

    if not name:
        messagebox.showerror("Error", "Please enter Name before saving PDF")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save Portfolio As"
    )

    if not file_path:
        return

    doc = SimpleDocTemplate(file_path, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("<b>PORTFOLIO</b>", styles["Title"]))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"<b>Name:</b> {name}", styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph("<b>Education:</b>", styles["Heading3"]))
    elements.append(Paragraph(education.replace("\n", "<br/>"), styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph("<b>Bio:</b>", styles["Heading3"]))
    elements.append(Paragraph(bio, styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph("<b>Skills:</b>", styles["Heading3"]))
    elements.append(ListFlowable(
        [ListItem(Paragraph(skill, styles["Normal"])) for skill in skills if skill],
        bulletType='bullet'
    ))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph("<b>Projects:</b>", styles["Heading3"]))
    elements.append(ListFlowable(
        [ListItem(Paragraph(project, styles["Normal"])) for project in projects if project],
        bulletType='bullet'
    ))

    doc.build(elements)
    messagebox.showinfo("Success", "PDF downloaded successfully!")


# GUI Setup
root = tk.Tk()
root.title("Portfolio Generator")
root.geometry("650x750")

tk.Label(root, text="Portfolio Generator Tool",
         font=("Helvetica", 18, "bold")).pack(pady=10)

# Name
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack(pady=5)

# Education
tk.Label(root, text="Education:").pack()
education_entry = tk.Text(root, height=3, width=50)
education_entry.pack(pady=5)

# Bio
tk.Label(root, text="Bio:").pack()
bio_entry = tk.Text(root, height=3, width=50)
bio_entry.pack(pady=5)

# Skills
tk.Label(root, text="Skills (one per line):").pack()
skills_entry = tk.Text(root, height=4, width=50)
skills_entry.pack(pady=5)

# Projects
tk.Label(root, text="Projects (one per line):").pack()
projects_entry = tk.Text(root, height=4, width=50)
projects_entry.pack(pady=5)

tk.Button(root, text="Generate Portfolio",
          command=generate_portfolio,
          bg="#3498db", fg="white",
          font=("Arial", 12)).pack(pady=10)

tk.Button(root, text="Download PDF",
          command=save_as_pdf,
          bg="#2ecc71", fg="white",
          font=("Arial", 12)).pack(pady=5)

output_box = tk.Text(root, height=15, width=80)
output_box.pack(pady=10)
output_box.config(state='disabled')

root.mainloop()