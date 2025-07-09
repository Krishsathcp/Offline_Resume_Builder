

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.pdf_generator import generate_pdf_from_html

generate_pdf_from_html('templates/resume_template_1.html', 'output1_resume.pdf')
