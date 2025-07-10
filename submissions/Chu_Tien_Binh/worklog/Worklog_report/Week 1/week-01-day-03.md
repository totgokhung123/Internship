# Worklog - Ngày 14/05/2025

## 📅 Thông tin cơ bản
- **Ngày**: 14/05/2025
- **Thứ**: Thứ Tư
- **Tuần thực tập**: Tuần thứ 1/8
- **Thời gian làm việc**: 9:00 - 17:00
- **Mood**: 💪 Tự tin với hands-on labs

## 🎯 Mục tiêu ngày hôm nay
- [x] Hiểu cách AWS tính phí cho các dịch vụ
- [x] Thiết lập AWS Budgets để quản lý và giám sát chi phí
- [x] Tạo alerts cho budget thresholds
- [x] Nghiên cứu các best practices cho cost optimization
- [x] Áp dụng các chiến lược tiết kiệm chi phí

## 💼 Công việc đã thực hiện

### 1. Tìm hiểu AWS Billing và Pricing Models ⏱️ 9:00-10:30
- **Mô tả**:
  - Nghiên cứu AWS pricing models cho các core services
  - Tìm hiểu AWS Free Tier và limitations
  - Khám phá AWS Pricing Calculator
  - Nghiên cứu cấu trúc của AWS bill và cost allocation
  - Tìm hiểu về Reserved Instances và Savings Plans
- **Kết quả**:
  - Hiểu rõ cách AWS tính phí cho từng dịch vụ
  - Biết cách ước tính chi phí cho workloads
  - Hiểu cách tối ưu chi phí với commitment-based discounts
- **Tools/Tech**:
  - AWS Billing Dashboard
  - AWS Pricing Calculator
  - AWS Free Tier documentation

### 2. Thiết lập AWS Cost Explorer ⏱️ 10:30-12:00
- **Mô tả**:
  - Truy cập và kích hoạt AWS Cost Explorer
  - Tìm hiểu cách phân tích chi phí theo services, regions, tags
  - Tạo custom reports cho different cost views
  - Nghiên cứu cost forecast và trend analysis
  - Export và chia sẻ cost reports
- **Kết quả**:
  - Tạo được custom cost reports
  - Hiểu cách phân tích cost trends
  - Biết cách sử dụng filters và groupings hiệu quả
- **Tools/Tech**:
  - AWS Cost Explorer
  - Cost Analysis Reports
  - Cost data export features

### 3. Thiết lập AWS Budgets ⏱️ 13:00-15:00
- **Mô tả**:
  - Tạo budget cho AWS account
  - Thiết lập budget thresholds (80%, 90%, 100%)
  - Cấu hình email notifications cho budget alerts
  - Tạo custom budget filters theo services
  - Thiết lập forecasted budget alerts
- **Kết quả**:
  - Tạo thành công multiple budgets với các threshold khác nhau
  - Cấu hình notifications khi vượt threshold
  - Hiểu cách theo dõi actual vs forecasted spend
- **Tools/Tech**:
  - AWS Budgets
  - Budget alert configurations
  - SNS notifications

### 4. Cost Optimization Strategies ⏱️ 15:00-17:00
- **Mô tả**:
  - Nghiên cứu các best practices cho cost optimization
  - Tìm hiểu về right-sizing instances
  - Nghiên cứu về auto-scaling để tối ưu chi phí
  - Khám phá tiết kiệm chi phí với spot instances
  - Tìm hiểu về data transfer costs và optimization
- **Kết quả**:
  - Tạo checklist cost optimization
  - Hiểu các phương pháp giảm chi phí cho từng service
  - Biết cách áp dụng tagging strategy cho cost allocation
- **Tools/Tech**:
  - AWS Well-Architected Framework (Cost Optimization Pillar)
  - Right-sizing tools
  - AWS Trusted Advisor

## 📚 Kiến thức học được

### 🔧 Technical Skills
- **AWS Cost Management**:
  - AWS Budgets: Thiết lập và quản lý budgets
  - Cost Explorer: Phân tích và forecast chi phí
  - Cost Allocation Tags: Tracking costs theo resources
- **Pricing Models**:
  - On-Demand: Pay per use without commitments
  - Reserved Instances: 1-3 year commitments với discounts
  - Savings Plans: Flexible commitment options
  - Spot Instances: Utilize unused capacity với discount lớn
- **Monitoring & Reporting**:
  - Budget alerts và notifications
  - Cost anomaly detection
  - Custom cost reports

### 💡 Concepts & Theory
- **FinOps Principles**: Cloud financial operations fundamentals
- **Cost Attribution Models**: Cách phân bổ chi phí trong tổ chức
- **TCO Analysis**: Total Cost of Ownership trong cloud vs on-premises
- **Cost Optimization Pillars**: Right sizing, scheduling, storage optimization, etc.

### 🤝 Soft Skills
- **Financial Planning**: Cách lập budget và forecast chi phí
- **Data Analysis**: Phân tích cost data để đưa ra insights
- **Cost Communication**: Cách trình bày chi phí cloud với stakeholders
- **Strategic Thinking**: Long-term planning cho cloud costs

## 🚧 Khó khăn và giải pháp

### Vấn đề 1: Phức tạp trong cấu trúc chi phí AWS
- **Mô tả**: AWS có nhiều pricing components và billing dimensions
- **Impact**: Khó hiểu chính xác cách ước tính và dự báo chi phí
- **Root Cause**: Mô hình pricing phức tạp và khác nhau giữa các services
- **Solution**: Sử dụng AWS Pricing Calculator và sample scenarios
- **Result**: Hiểu rõ hơn cách ước tính chi phí cho các use case phổ biến
- **Lesson**: Break down cost analysis theo từng service, rồi tổng hợp lại

### Vấn đề 2: Khó khăn trong việc chọn right-sizing cho instances
- **Mô tả**: Không chắc cách chọn EC2 instance type tối ưu về cost
- **Impact**: Có thể chọn over-provisioned instances và lãng phí
- **Root Cause**: Thiếu kiến thức về performance benchmarking
- **Solution**: Nghiên cứu AWS Compute Optimizer recommendations
- **Result**: Hiểu cách chọn instance type dựa trên actual workload
- **Lesson**: Nên bắt đầu nhỏ và scale up khi cần thay vì over-provision

## 💭 Reflection & Insights

### What went well today?
- Hiểu rõ AWS cost structure và billing model
- Thiết lập thành công budgets và alerts
- Có được foundation về cost optimization strategies

### What could be improved?
- Cần hands-on với nhiều services hơn để hiểu cost impacts
- Chưa thử nghiệm được Savings Plans và Reserved Instances
- Cần tạo long-term cost projection cho project

### Key Insights
- AWS chi phí có thể tăng nhanh nếu không theo dõi và quản lý chặt chẽ
- Tagging là foundation quan trọng cho cost allocation hiệu quả
- Auto Scaling không chỉ tốt cho availability mà còn cho cost optimization

### Questions & Curiosities
- Làm thế nào để tối ưu data transfer costs trong multi-region deployments?
- Cách hiệu quả nhất để sử dụng Spot Instances cho production workloads?
- AWS Organizations có giúp quản lý chi phí tốt hơn so với single account?

## 📋 Kế hoạch ngày mai

### Priority Tasks
- [ ] **High**: Tạo EC2 instance đầu tiên và connect via SSH
- [ ] **High**: Tạo S3 bucket và thiết lập static website
- [ ] **Medium**: Khám phá Amazon VPC và network configuration

### Learning Goals
- [ ] Hiểu EC2 lifecycle và different instance types
- [ ] Học cách sử dụng S3 cho static content hosting
- [ ] Tìm hiểu về security groups và network ACLs

### Meetings & Deadlines
- [ ] Daily standup với team vào 9:00
- [ ] Submit weekly progress report

## 📊 Self Assessment

### Productivity
- **Score**: 9/10
- **Reason**: Hoàn thành đầy đủ lab và tasks, tạo documentation tốt
- **Improvement**: Cần đào sâu hơn vào advanced cost optimization techniques

### Learning
- **Score**: 8/10
- **New Knowledge**: AWS Budgets, Cost Explorer, pricing models
- **Application**: Áp dụng được cost management cho tài khoản AWS của mình

### Overall Satisfaction
- **Score**: 9/10
- **Highlights**: Hiểu rõ về cost management là foundation quan trọng
- **Areas for Growth**: Cần xem xét chi phí trong bối cảnh kiến trúc toàn diện

---
## 📎 Attachments & Links

### Learning Resources
- [ AWS lab](https://000003.awsstudygroup.com/vi/)

---

*Worklog created by: Chu Tien Binh - FCJ Intern Batch 2025*  
*Next review: 15/05/2025*