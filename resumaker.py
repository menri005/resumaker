import argparse
import yaml

from docxtpl import DocxTemplate
from pathlib import Path

def clean_up_text(text_string):
	'''
	Replaces white space with underscores, and removes punctuation, colons and quotes.
	This is so that this string can be included in a filename. 

	args:
		text_string (str): the string to be sanitized

	returns:
		(str): a cleaned up version of the input string to be used for filenames / paths. 
	'''

	return text_string.replace(' ', '_').replace(',','').replace('.', '').replace("'", '')

# argument parser
parser = argparse.ArgumentParser(description="Resumaker helps you automatically generate a resume and cover letter from a template.")
parser.add_argument("-y", '--yaml_template_path', type=Path, help='YAML template used to fill out content.')
parser.add_argument("-r", '--resume_template_path', type=Path, help='DOCX RESUME template you want to use.')
parser.add_argument("-l", '--letter_template_path', type=Path, help='DOCX COVER LETTER template you want to use.')
parser.add_argument("-o", '--output_path', type=Path, help='Where the resulting output will be saved to.')
args = parser.parse_args()

# populate context from YAML template
context_dict = yaml.safe_load(open(args.yaml_template_path))

# template file paths
resume_template_path = args.resume_template_path
resume_output_path = args.output_path / f"{clean_up_text(context_dict['applicant_name'])}_Resume_{clean_up_text(context_dict['company_name'])}_{clean_up_text(context_dict['position_name'])}.docx"
letter_template_path = args.letter_template_path
cover_letter_output_path = args.output_path / f"{clean_up_text(context_dict['applicant_name'])}_Cover_Letter_{clean_up_text(context_dict['company_name'])}_{clean_up_text(context_dict['position_name'])}.docx"


def fill_resume_template(resume_template_path, resume_output_path, letter_template_path, cover_letter_output_path, context_dict):
	# convert list of skills to pipe separated string
	skills_string = " | ".join(context_dict['skills'])

	# generate top three skills from YAML template for cover letter
	context_dict['top_three_skills'] = f"{context_dict['skills'][0]}, {context_dict['skills'][1]} and {context_dict['skills'][2]}"

	# reassign context placeholder with string of skills
	context_dict['skills'] = skills_string

	# render the resume document
	resume_docx = DocxTemplate(resume_template_path)
	resume_docx.render(context_dict)
	resume_docx.save(resume_output_path)

	# render the cover letter document
	cover_letter_docx = DocxTemplate(letter_template_path)
	cover_letter_docx.render(context_dict)
	cover_letter_docx.save(cover_letter_output_path)


if __name__ == '__main__':

	fill_resume_template(
		resume_template_path=resume_template_path,
		resume_output_path=resume_output_path,
		letter_template_path=letter_template_path,
		cover_letter_output_path=cover_letter_output_path,
		context_dict=context_dict)