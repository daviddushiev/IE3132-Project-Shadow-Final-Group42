from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

output = "website/archive/documents/project-shadow-memo.pdf"

c = canvas.Canvas(output, pagesize=A4)

width, height = A4

c.setTitle("Project Shadow Internal Research Memo")
c.setAuthor("Solace Dynamics")

c.setFont("Helvetica-Bold", 18)
c.drawString(25 * mm, height - 30 * mm, "SOLACE DYNAMICS")

c.setFont("Helvetica-Bold", 14)
c.drawString(25 * mm, height - 42 * mm, "Internal Research Memorandum")

c.setFont("Helvetica", 11)

lines = [
    "Classification: INTERNAL USE ONLY",
    "",
    "Project: Project Shadow",
    "Research Division: Secure Systems Research",
    "",
    "Prepared by: J Alvarez",
    "Role: Senior Research Analyst",
    "",
    "Project Shadow systems are currently being migrated",
    "from the legacy research infrastructure.",
    "",
    "Researchers requiring access should use the new",
    "internal research portal:",
    "",
    "http://portal.solace.test:8081",
    "",
    "Assigned researcher account:",
    "jalvarez",
    "",
    "Temporary authentication credentials are managed",
    "separately by the Research Infrastructure Team.",
    "",
    "Do not distribute this document outside Solace Dynamics.",
]

y = height - 60 * mm

for line in lines:
    c.drawString(25 * mm, y, line)
    y -= 7 * mm

c.save()

print(f"Created: {output}")
