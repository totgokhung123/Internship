import pandas as pd
from pathlib import Path

# --- Configuration ---
input_path = 'E:/AWS_FCJ/Repo_Internship/Internship/submissions/Chu_Tien_Binh/worklog/Worklog_report/Worklog.xlsx'          # Đường dẫn file Excel
sheet_name = 'Daily Report'          # Tên sheet chứa worklog
output_dir = Path('E:/AWS_FCJ/Repo_Internship/Internship/submissions/Chu_Tien_Binh/worklog/Worklog_report')      # Thư mục lưu file .md

# --- Đọc và chuẩn bị dữ liệu ---
df = pd.read_excel(input_path, sheet_name=sheet_name)
df.columns = df.columns.str.strip()  # Loại bỏ khoảng trắng ở đầu/cuối tên cột

# Loại bỏ các dòng không có Week # hoặc Daily Goals hoặc Task complete
df = df.dropna(subset=['Week #', 'Daily Goals', 'Task complete'])

# Tính day_index theo thứ tự xuất hiện trong mỗi tuần
df['Week #'] = df['Week #'].astype(int)  # Chuyển sang int
df['day_index'] = df.groupby('Week #').cumcount() + 1

# Tạo thư mục đầu ra nếu chưa tồn tại
output_dir.mkdir(parents=True, exist_ok=True)

# --- Sinh file Markdown ---
for _, row in df.iterrows():
    week_num = row['Week #']
    day_num = row['day_index']
    filename = f"week-{week_num:02d}-day-{day_num:02d}.md"
    filepath = output_dir / filename

    # Chuyển các dòng Goals và Tasks thành list item
    goals = row['Daily Goals']
    tasks = row['Task complete']
    goals_list = "\n".join(f"- {g.strip()}" for g in str(goals).split('\n') if g.strip())
    tasks_list = "\n".join(f"- {t.strip()}" for t in str(tasks).split('\n') if t.strip())

    # Nội dung template Markdown
    md_content = f"""# Week {week_num:02d} - Day {day_num:02d}

## 🎯 Daily Goals

{goals_list}

## ✅ Task Complete

{tasks_list}
"""

    # Ghi file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)

print(f"Đã sinh {len(df)} file .md vào thư mục: {output_dir}")
