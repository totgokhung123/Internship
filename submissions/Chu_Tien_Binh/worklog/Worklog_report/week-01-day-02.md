# Worklog - Ngày 13/05/2025

## 📅 Thông tin cơ bản
- **Ngày**: 13/05/2025
- **Thứ**: Thứ Ba
- **Tuần thực tập**: Tuần thứ 1/8
- **Thời gian làm việc**: 9:00 - 17:00
- **Mood**: 🤓 Tập trung học hỏi

## 🎯 Mục tiêu ngày hôm nay
- [x] Tìm hiểu về AWS Global Infrastructure
- [x] Nghiên cứu các dịch vụ nền tảng của AWS
- [x] Khám phá Amazon EC2, Amazon S3, Amazon RDS, Amazon VPC
- [x] Tìm hiểu về AWS Lambda và serverless computing
- [x] Khám phá Amazon CloudWatch monitoring

## 💼 Công việc đã thực hiện

### 1. Nghiên cứu AWS Global Infrastructure ⏱️ 9:00-10:30
- **Mô tả**:
  - Nghiên cứu về cấu trúc toàn cầu của AWS
  - Tìm hiểu về Regions, Availability Zones, Local Zones, và Edge Locations
  - Hiểu cách AWS đảm bảo high availability và disaster recovery
  - Phân tích cách lựa chọn Region phù hợp cho workload
- **Kết quả**:
  - Hiểu rõ cấu trúc phân bố toàn cầu của AWS
  - Biết cách AWS đảm bảo redundancy và high availability
  - Hiểu tầm quan trọng của việc chọn Region phù hợp
- **Tools/Tech**:
  - AWS Global Infrastructure documentation
  - AWS Region Selector
  - AWS Availability Zone design

### 2. Khám phá Amazon EC2 ⏱️ 10:30-12:00
- **Mô tả**:
  - Tìm hiểu về dịch vụ Elastic Compute Cloud (EC2)
  - Nghiên cứu các instance types và use cases tương ứng
  - Tìm hiểu về AMIs (Amazon Machine Images)
  - Nghiên cứu về EC2 pricing models (On-Demand, Reserved, Spot Instances)
  - Tìm hiểu về Auto Scaling và Elastic Load Balancing
- **Kết quả**:
  - Hiểu rõ EC2 là gì và cách sử dụng
  - Biết cách lựa chọn instance type phù hợp cho từng workload
  - Hiểu các mô hình pricing và khi nào nên dùng mỗi loại
- **Tools/Tech**:
  - Amazon EC2 documentation
  - EC2 Instance Types
  - EC2 Pricing Calculator

### 3. Nghiên cứu Amazon S3 và Storage Solutions ⏱️ 13:00-14:30
- **Mô tả**:
  - Tìm hiểu về Simple Storage Service (S3) và use cases
  - Nghiên cứu về S3 storage classes (Standard, IA, Glacier, etc.)
  - Tìm hiểu về S3 bucket policies và permissions
  - Khám phá các tính năng bảo mật của S3
  - Tìm hiểu về các storage solutions khác: EBS, EFS, Storage Gateway
- **Kết quả**:
  - Hiểu rõ S3 là gì và cách sử dụng hiệu quả
  - Biết cách lựa chọn storage class phù hợp cho từng use case
  - Hiểu best practices cho data lifecycle management
- **Tools/Tech**:
  - Amazon S3 documentation
  - S3 Storage Classes
  - S3 Security Best Practices

### 4. Khám phá Amazon VPC và Networking ⏱️ 14:30-16:00
- **Mô tả**:
  - Tìm hiểu về Virtual Private Cloud (VPC) và network isolation
  - Nghiên cứu về subnets, route tables, và security groups
  - Tìm hiểu về Internet Gateways và NAT Gateways
  - Khám phá VPC Peering và Transit Gateway
  - Tìm hiểu về Network ACLs và Security Groups
- **Kết quả**:
  - Hiểu cấu trúc cơ bản của VPC
  - Biết cách thiết kế network architecture an toàn
  - Hiểu sự khác biệt giữa các security controls
- **Tools/Tech**:
  - Amazon VPC documentation
  - VPC design patterns
  - Network security best practices

### 5. Nghiên cứu Amazon RDS và Database Services ⏱️ 16:00-17:00
- **Mô tả**:
  - Tìm hiểu về Relational Database Service (RDS)
  - Nghiên cứu các engine được hỗ trợ (MySQL, PostgreSQL, SQL Server, etc.)
  - Tìm hiểu về Multi-AZ deployments và Read Replicas
  - Khám phá DynamoDB và NoSQL databases
  - Tìm hiểu về Aurora và performance benefits
- **Kết quả**:
  - Hiểu về managed database services của AWS
  - Biết khi nào nên dùng SQL vs NoSQL databases
  - Hiểu cách thiết kế highly available database architecture
- **Tools/Tech**:
  - Amazon RDS documentation
  - Database engine comparison
  - Amazon DynamoDB

## 📚 Kiến thức học được

### 🔧 Technical Skills
- **AWS Core Services**:
  - EC2: Virtual servers trong cloud
  - S3: Object storage với durability 99.999999999%
  - VPC: Network isolation và security
  - RDS: Managed database services
- **Global Infrastructure**:
  - Region và Availability Zone architecture
  - Edge Locations và CloudFront
  - Global service deployment strategies
- **High Availability Design**:
  - Multi-AZ deployments
  - Auto Scaling và load balancing
  - Disaster recovery patterns

### 💡 Concepts & Theory
- **Cloud Service Models**: IaaS, PaaS, SaaS và khi nào nên dùng
- **Elasticity vs Scalability**: Phân biệt và ứng dụng
- **Pay-as-you-go Model**: Hiểu về pricing và cost optimization
- **Reliability Pillars**: Well-Architected Framework foundations

### 🤝 Soft Skills
- **Systematic Learning**: Phương pháp học từ đơn giản đến phức tạp
- **Documentation**: Ghi chép có tổ chức và tạo diagram
- **Comparative Analysis**: So sánh services để hiểu rõ use cases
- **Visualization**: Tạo mental models để hiểu kiến trúc phức tạp

## 🚧 Khó khăn và giải pháp

### Vấn đề 1: Quá tải thông tin về dịch vụ AWS
- **Mô tả**: AWS có hơn 200 services, cảm thấy overwhelming khi tìm hiểu
- **Impact**: Khó tập trung và hiểu sâu về từng service
- **Root Cause**: Scope quá rộng cho một ngày học
- **Solution**: Tập trung vào "AWS Fundamentals - Core Services" trước
- **Result**: Hiểu rõ 5-6 core services quan trọng nhất
- **Lesson**: Nên có roadmap học tập có cấu trúc thay vì cố gắng học tất cả

### Vấn đề 2: Khó hiểu về mô hình networking trong VPC
- **Mô tả**: Các khái niệm như CIDR, subnet masks, route tables khá phức tạp
- **Impact**: Khó hình dung cách thiết kế VPC hiệu quả
- **Root Cause**: Thiếu kiến thức nền tảng về networking
- **Solution**: Tìm các video tutorials và visual guides về VPC
- **Result**: Hiểu rõ hơn về VPC design patterns và best practices
- **Lesson**: Với các chủ đề phức tạp, visual learning hiệu quả hơn text-based

## 💭 Reflection & Insights

### What went well today?
- Có được overview tổng quan về AWS core services
- Hiểu được mối liên hệ giữa các services và cách chúng hoạt động cùng nhau
- Tạo được mental model về AWS architecture

### What could be improved?
- Cần hands-on labs để củng cố kiến thức lý thuyết
- Nên tạo more structured notes để dễ review sau này
- Cần đào sâu hơn về pricing và cost optimization

### Key Insights
- AWS thiết kế services theo hướng modular, cho phép kết hợp linh hoạt
- Global Infrastructure là nền tảng quan trọng cho reliability và performance
- Hiểu service limits và constraints quan trọng không kém hiểu features

### Questions & Curiosities
- Làm thế nào để thiết kế multi-region architecture hiệu quả?
- Chiến lược nào tốt nhất cho cost optimization trong AWS?
- Khi nào nên dùng serverless vs container-based architectures?

## 📋 Kế hoạch ngày mai

### Priority Tasks
- [ ] **High**: Làm lab quản lý chi phí với AWS Budgets
- [ ] **High**: Tạo EC2 instance đầu tiên và kết nối qua SSH
- [ ] **Medium**: Tạo S3 bucket và upload files

### Learning Goals
- [ ] Hiểu chi tiết về AWS cost management và billing
- [ ] Học cách sử dụng AWS CLI cho EC2 và S3
- [ ] Tìm hiểu về security best practices cho EC2

### Meetings & Deadlines
- [ ] Daily standup với team vào 9:00
- [ ] Báo cáo tiến độ cuối ngày

## 📊 Self Assessment

### Productivity
- **Score**: 8/10
- **Reason**: Nghiên cứu được nhiều services trong một ngày
- **Improvement**: Cần cân bằng giữa breadth và depth của kiến thức

### Learning
- **Score**: 7/10
- **New Knowledge**: AWS core services, global infrastructure, service integration
- **Application**: Cần thêm hands-on practice để củng cố kiến thức

### Overall Satisfaction
- **Score**: 8/10
- **Highlights**: Đã có foundation solid về AWS services
- **Areas for Growth**: Cần hands-on experience và thực hành với real-world scenarios
- 
---
## 📎 Attachments & Links

### Learning Resources
- [ AWS Account](https://000001.awsstudygroup.com/vi/)
- [AWS Cloud lab Resources 01](https://specialforce.awsstudygroup.com/#/course/week-1:-network-foundation)
- [AWS Cloud lab Resources 02](https://000003.awsstudygroup.com/vi/3-prerequiste/3.1-createvpc/)
---

*Worklog created by: Chu Tien Binh - FCJ Intern Batch 2025*  
*Next review: 14/05/2025*