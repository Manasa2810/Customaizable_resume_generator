import argparse
from fpdf import FPDF

class CustomResumePDF(FPDF):
    def __init__(self, font_size, font_color, background_color):
        super().__init__()
        self.font_size = font_size
        self.font_color = font_color
        self.background_color = background_color
        self.set_auto_page_break(auto=True, margin=20)
        self.set_left_margin(15)
        self.set_right_margin(15)

    def header(self):
        pass  # Optional: Add a header if needed

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def add_section_title(self, title):
        self.set_font("Arial", "B", self.font_size + 6)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, title, ln=True, align='C', border='B')
        self.ln(6)

    def add_bullet_point(self, content):
        self.set_font("Arial", size=self.font_size + 2)
        self.set_text_color(0, 0, 0)
        self.cell(10)  # Indentation for bullet
        self.multi_cell(0, 8, f"- {content}")  # Use a simple dash (-) as a bullet
        self.ln(1)

    def add_content(self, content):
        self.set_font("Arial", size=self.font_size + 2)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 8, content)
        self.ln(6)

    def add_table(self, data):
        self.set_font("Arial", "B", self.font_size + 3)
        col_widths = [90, 50, 40]

        headers = ["Education", "Year", "CGPA"]
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align='C')
        self.ln()

        self.set_font("Arial", size=self.font_size + 3)
        for row in data:
            for i, item in enumerate(row):
                self.cell(col_widths[i], 10, item, border=1, align='C')
            self.ln()
        self.ln(6)

    def create_resume(self, data):
        self.add_page()

        # Name and Contact
        self.set_font("Arial", "B", self.font_size + 10)
        self.cell(0, 15, data['name'], ln=True, align='C')
        self.set_font("Arial", size=self.font_size + 3)
        self.cell(0, 10, data['contact'], ln=True, align='C')
        self.ln(10)

        # Sections
        self.add_section_title("Education")
        self.add_table(data['education'])

        self.add_section_title("Projects")
        for project in data['projects']:
            self.set_font("Arial", "B", self.font_size + 3)
            self.cell(0, 10, project['title'], ln=True)
            for detail in project['details']:
                self.add_bullet_point(detail)

        self.add_section_title("Experience")
        for exp in data['experience']:
            self.set_font("Arial", "B", self.font_size + 4)
            self.cell(0, 10, exp['title'], ln=True)
            for detail in exp['details']:
                self.add_bullet_point(detail)

        self.add_section_title("Skills")
        self.add_content(data['skills'])

        self.add_section_title("Extracurricular Activities")
        self.add_content(data['extracurriculars'])

def main():
    parser = argparse.ArgumentParser(description="Generate a professional resume PDF.")
    parser.add_argument('--font-size', type=int, default=14, help="Font size for the text.")
    parser.add_argument('--font-color', type=str, default="#000000", help="Font color in hex format.")
    parser.add_argument('--background-color', type=str, default="#FFFFFF", help="Background color in hex format.")

    args = parser.parse_args()

    resume_data = {
        "name": "Jane Doe",
        "contact": "Email: jane.doe@example.com | Phone: 987-654-3210",
        "education": [
            ["ABC High School", "2018", "9.8/10"],
            ["DEF Senior School", "2020", "9.6/10"],
            ["XYZ University", "2025", "9.2/10"]
        ],
        "projects": [
            {
                "title": "Expense Tracker App",
                "details": [
                    "Built a full-stack web application using React and Node.js to track expenses and visualize spending patterns.",
                    "Deployed on AWS and used by 500+ users."
                ]
            },
            {
                "title": "Library Management System",
                "details": [
                    "Developed a desktop application using Java and MySQL for managing library operations.",
                    "Reduced book issuance time by 30% through optimized search algorithms."
                ]
            }
        ],
        "experience": [
            {
                "title": "Software Engineering Intern at XYZ Corp",
                "details": [
                    "Developed a feature to improve user onboarding, reducing drop-off by 15%.",
                    "Collaborated with a team to redesign the UI, improving user satisfaction scores."
                ]
            },
            {
                "title": "Volunteer Developer for Open Source Project",
                "details": [
                    "Contributed to a library used by 10,000+ developers.",
                    "Resolved 20+ issues and implemented 5 new features based on user feedback."
                ]
            }
        ],
        "skills": "- Python\n- Data Structures and Algorithms\n- Web Development (HTML, CSS, JavaScript, React)\n- Database Management (MySQL, MongoDB)",
        "extracurriculars": "- Member of University Coding Club: Organized 5 hackathons and participated in coding competitions.\n- Volunteer at Local Animal Shelter: Managed social media campaigns to increase adoption rates."
    }

    pdf = CustomResumePDF(font_size=args.font_size, font_color=args.font_color, background_color=args.background_color)
    #pdf.add_font('Arial', '', 'arial.ttf', uni=True)  # Ensure a Unicode font is added
    pdf.create_resume(resume_data)

    output_file = "sample_resume.pdf"
    pdf.output(output_file)
    print(f"Resume saved as {output_file}")

if __name__ == "__main__":
    main()
