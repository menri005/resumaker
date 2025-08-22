# ResuMaker

**ResuMaker** is an application that helps you create a resume from a YAML template. 

When you're in the market and you need to quickly customize your resume to align to a certain job profile, or you're looking to hack the algorithms that sort through resumes with certain keywords, or your red team needs to make it easier to manage different "personas", this tool gives you the speed and flexibility to do so. 

The DOCX resume template used is Applicant Tracking System (ATS) compliant, so it will parse nicely by companies that follow this standard.

---

## Features

- Uses a YAML template for resume content
- Applicant name, description, skillset are dynamically generated from YAML template
- Creates cover page with content from YAML template
- DOCX resume is ATS compliant

---

## Requirements

- Python 3.x
- pyYAML, docxtpl, Jinja2

---

## Usage

```bash
python3 resumaker.py -y YAML_TEMPLATE_PATH -r RESUME_TEMPLATE_PATH -l LETTER_TEMPLATE_PATH -o OUTPUT_PATH
```

---

## Templates

There is a templates directory where you will find the default document templates, including the YAML template that will contain your own applicant name, skills and description. In the resume DOCX template, make sure to update the **EXPERIENCE**, **EDUCATION** and **LICENSES AND CERTIFICATIONS** sections with your own career experience and words. These might be added to the YAML template in the future. Also update the wording on the cover letter to match your own. 

The Jinja2 expressions such as `{{ applicant_name }}` are placeholders for the script to put values in coming from the YAML template, so these do not need to be changed or modified.

You may also use your OWN DOCX template if you are familiar with Jinja2 syntax and want to try out a different resume style that still bears your content. 

---

## Author
Martin Enriquez
tuxedo.netcat@gmail.com
https://github.com/menri005