from pdfminer.high_level import extract_text
import pandas as pd
import re
import os

# Tách chữ từ file pdf
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

sample_text = extract_text_from_pdf("../resumes/resume.pdf")
# print(sample_text[:1000])

# Clean dữ liệu text được trích xuất bỏ bốt các khoảng trắng thừa và xuống dòng thừa
def clean_text(text):
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()

cleaned = clean_text(sample_text)
# print(cleaned)

# Tách thông tin email và số điện thoại sử dụng regex
def extract_email(text):
    match = re.search(r'\S+@\S+', text)
    return match.group (0) if match else None

def extract_phone(text):
    # Ưu tiên số có 9–11 chữ số liên tiếp (bỏ space, -, ())
    candidates = re.findall(r'(?:\+?\d[\s\-()]*){9,12}', text)
    for c in candidates:
        digits = re.sub(r'\D', '', c)
        if 9 <= len(digits) <= 11:
            return c.strip()
    return None

# Định dạng số điện thoại để Excel không tự động chuyển định dạng
def format_phone_for_excel(phone):
    if phone:
        return "'" + phone
    return None

email = extract_email(cleaned)
phone = extract_phone(cleaned)
# print("Email:", email, "Phone:", phone)

# Extract tên từ CV (giả sử tên thường nằm ở đầu CV)
def extract_name(text):
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    if not lines:
        return None
    first_line = lines[0]
    # tên thường ngắn, không có số, không có ký tự đặc biệt
    if (
        len(first_line.split()) <= 4
        and not re.search(r'\d|@', first_line)
    ):
        return first_line
    return None

# print("Name:", extract_name(cleaned))

# Extract kỹ năng từ CV
SKILL_SET = ['Python', 'SQL', 'Excel', 'Power BI', 'Machine Learning', 'Data Analysis']
def extract_skills(text, skills=SKILL_SET):
    found = [skill for skill in skills if skill.lower() in text.lower()]
    return list(set(found))

# Extract trình độ học vấn từ CV
EDU_KEYWORDS = ['Bachelor', 'Master', 'B.Sc', 'M.Sc', 'PhD', 'B.E', 'M.Ε']
def extract_education(text):
    lines = text.split('\n')
    education = []
    for line in lines:
        for word in EDU_KEYWORDS:
            if word.lower() in line.lower():
                education.append(line.strip())
    return education

# Extract kinh nghiệm làm việc từ CV
def extract_experience (text):
    experience_keywords = ['experience', 'work', 'internship', 'employment']
    exp_lines = []
    lines = text.split('\n')
    for line in lines:
        for keyword in experience_keywords:
            if keyword.lower() in line.lower():
                exp_lines.append(line.strip())
    return exp_lines

parsed_resume ={
    'Name':extract_name(cleaned),
    'Email':extract_email(cleaned),
    'Phone':extract_phone(cleaned),
    'Skills':extract_skills(cleaned),
    'Education':extract_education (cleaned),
    'Experience':extract_experience (cleaned)
}

# print(parsed_resume)

# Xử lý nhiều file trong thư mục resumes và lưu kết quả vào file CSV
def process_folder(folder_path):
    results = []
    for file in os.listdir (folder_path):
        if file.endswith(".pdf"):
            path = os.path.join(folder_path, file)
            text = clean_text(extract_text_from_pdf(path))
            parsed = {
                'File': file,
                'Name': extract_name(text),
                'Email': extract_email(text),
                'Phone': format_phone_for_excel(extract_phone(text)),
                'Skills': extract_skills(text),
                'Education': extract_education(text),
                'Experience': extract_experience (text)
            }
            results.append(parsed)
    return pd.DataFrame (results)

df = process_folder("../resumes")
df.to_csv("../resumes/parsed_resumes.csv", index=False, encoding="utf-8-sig")