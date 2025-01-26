# Resume Generator PDF

This Python script allows you to generate a professional resume in PDF format using the `argparse` and `FPDF` libraries. It allows for customization of font size, font color, and background color, and includes sections for education, projects, experience, skills, and extracurricular activities.

## Features

- Customizable font size, font color, and background color.
- Sections for **Education**, **Projects**, **Experience**, **Skills**, and **Extracurricular Activities**.
- Support for bullet points for details under each section.
- A table format for displaying educational qualifications with columns for institution name, year, and CGPA.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `argparse` (for command-line argument parsing)
  - `fpdf` (for PDF generation)

You can install the required package using `pip`:
```bash
pip install fpdf
```

## Usage

### Command-Line Arguments

You can specify custom font size, font color, and background color via command-line arguments.

#### Arguments:
- `--font-size`: Font size for the text (default is `14`).
- `--font-color`: Font color in hex format (default is `#000000`).
- `--background-color`: Background color in hex format (default is `#FFFFFF`).

### Example Usage

To generate a resume with a custom font size and color:
```bash
python resume_generator.py --font-size 16 --font-color "#333333" --background-color "#F0F0F0"
```

## Resume Data Structure

The `resume_data` dictionary contains the information that will be populated in the resume. Here's an example of how it’s structured:

```python
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
                "Built a full-stack web application using React and Node.js to track expenses.",
                "Deployed on AWS and used by 500+ users."
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
        }
    ],
    "skills": "- Python\n- Web Development (React, Node.js)\n- Database Management (MySQL)",
    "extracurriculars": "- Member of University Coding Club\n- Volunteer at Local Animal Shelter"
}
```

### Modify `resume_data` to reflect your own personal information, education, experience, skills, and more.
