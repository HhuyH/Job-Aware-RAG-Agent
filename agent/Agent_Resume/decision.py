"""
Decision / Reasoning Agent

Chức năng:
- Nhận đầu vào từ các agent khác:
  - ResumeAgent (CV Analyzer)
  - JD Collector
  - Company Verifier (nếu có)
- Thực hiện suy luận / reasoning:
  - So sánh CV ↔ JD
  - Tính Matching Score
  - Xác định Skill Gap (skills thiếu / cần cải thiện)
  - Đánh giá mức độ phù hợp
- Xuất kết quả quyết định:
  - Phù hợp hay không
  - Recommendation cho ứng viên
  - Có thể ghi ra Excel hoặc JSON cho downstream pipeline

Mục tiêu: Tập hợp các dữ liệu đã chuẩn hóa, đưa ra quyết định chính xác cho việc match job.
"""
