# Worklog - Ngày 15/05/2025

## 📅 Thông tin cơ bản
- **Ngày**: 15/05/2025
- **Thứ**: Thứ Năm
- **Tuần thực tập**: Tuần thứ 1/8
- **Thời gian làm việc**: 9:00 - 17:00
- **Mood**: 🧩 Thử thách và tập trung

## 🎯 Mục tiêu ngày hôm nay
- [x] Hiểu kiến trúc và concept của Amazon VPC
- [x] Tạo VPC với multiple subnets across AZs
- [x] Thiết lập Internet Gateway và route tables
- [x] Cấu hình Security Groups và Network ACLs
- [x] Thiết lập VPC peering connection

## 💼 Công việc đã thực hiện

### 1. Cơ bản về Amazon VPC và Network Fundamentals ⏱️ 9:00-10:30
- **Mô tả**:
  - Nghiên cứu khái niệm cơ bản của Amazon VPC
  - Tìm hiểu về CIDR blocks và IP address allocation
  - Hiểu về Subnets, Route Tables, và Internet Gateways
  - Phân biệt Public vs Private Subnets
  - Nghiên cứu về Security Groups vs Network ACLs
- **Kết quả**:
  - Hiểu rõ kiến trúc VPC và các thành phần của nó
  - Nắm được cách thiết kế IP addressing scheme
  - Hiểu được cách traffic flow trong VPC
- **Tools/Tech**:
  - AWS VPC Documentation
  - CIDR notation và subnet calculator
  - AWS Network Fundamentals

### 2. Tạo và Cấu hình VPC ⏱️ 10:30-12:30
- **Mô tả**:
  - Tạo VPC mới với CIDR block 10.0.0.0/16
  - Tạo 4 subnets (2 public, 2 private) across 2 AZs
  - Public subnets: 10.0.1.0/24, 10.0.2.0/24
  - Private subnets: 10.0.3.0/24, 10.0.4.0/24
  - Cấu hình Internet Gateway và attach vào VPC
  - Tạo custom route tables cho public và private subnets
  - Cấu hình routes cho public subnets thông qua IGW
- **Kết quả**:
  - VPC được tạo thành công với architecture hợp lý
  - Public subnets có thể truy cập internet
  - Private subnets được isolated
  - Hiểu rõ cách route tables điều khiển traffic
- **Tools/Tech**:
  - AWS VPC Console
  - AWS CLI cho VPC configuration
  - Route table configuration
  - CIDR allocation strategies

### 3. Thiết lập Network Security ⏱️ 13:30-15:00
- **Mô tả**:
  - Tạo và cấu hình Security Groups cho EC2 instances
  - Web tier SG: Allow HTTP/HTTPS từ internet, SSH từ specific IP
  - App tier SG: Allow traffic từ Web tier SG, deny direct internet access
  - Database SG: Allow chỉ MySQL traffic từ App tier SG
  - Cấu hình Network ACLs với inbound và outbound rules
  - Implement defense-in-depth strategy
- **Kết quả**:
  - Thiết lập multiple layers of security
  - Security Groups được cấu hình theo principle of least privilege
  - Network ACLs bổ sung thêm layer security
  - Hiểu rõ stateful vs stateless security controls
- **Tools/Tech**:
  - Security Group configuration
  - Network ACLs rules
  - Security best practices
  - Network traffic filtering

### 4. Thiết lập VPC Connectivity ⏱️ 15:00-16:30
- **Mô tả**:
  - Tạo NAT Gateway trong public subnet
  - Cấu hình route table cho private subnets để sử dụng NAT Gateway
  - Tạo second VPC cho testing VPC Peering
  - Thiết lập VPC Peering connection giữa hai VPCs
  - Cấu hình route tables để allow traffic giữa peered VPCs
  - Test connectivity giữa resources trong hai VPCs
- **Kết quả**:
  - Private resources có thể access internet thông qua NAT Gateway
  - VPC Peering connection hoạt động thành công
  - Traffic có thể flow giữa các resources trong peered VPCs
  - Hiểu rõ các connectivity options trong AWS
- **Tools/Tech**:
  - NAT Gateway
  - VPC Peering
  - Cross-VPC routing
  - Network connectivity testing

### 5. Testing và Troubleshooting ⏱️ 16:30-17:00
- **Mô tả**:
  - Launch EC2 instances trong public và private subnets
  - Test connectivity từ public instances ra internet
  - Test connectivity từ private instances ra internet thông qua NAT Gateway
  - Kiểm tra Security Group và NACL rules hoạt động
  - Sử dụng VPC Flow Logs để troubleshoot connectivity issues
  - Document architecture và configuration
- **Kết quả**:
  - Xác nhận network architecture hoạt động như thiết kế
  - Hiểu cách debug network connectivity issues
  - Tạo được comprehensive network diagram
  - Có khả năng giải thích traffic flows trong VPC
- **Tools/Tech**:
  - EC2 instances
  - SSH và curl testing
  - VPC Flow Logs
  - Network troubleshooting tools

## 📚 Kiến thức học được

### 🔧 Technical Skills
- **VPC Architecture**:
  - VPC design và CIDR planning
  - Public vs Private subnet architecture
  - Multi-AZ network design cho high availability
  - VPC Endpoints và Gateway services
- **Network Security**:
  - Defense-in-depth với multiple security layers
  - Security Groups vs Network ACLs
  - Stateful vs Stateless packet filtering
  - Network isolation best practices
- **Connectivity Options**:
  - Internet Gateway cho public access
  - NAT Gateway cho private subnet outbound traffic
  - VPC Peering cho private connectivity
  - Transit Gateway cho hub-and-spoke network models

### 💡 Concepts & Theory
- **Network Segmentation**: Tầm quan trọng của isolation và security domains
- **Principle of Least Privilege**: Chỉ cung cấp access cần thiết tối thiểu
- **High Availability Network Design**: Multi-AZ deployments cho fault tolerance
- **Transitive Routing Limitations**: VPC Peering không hỗ trợ transitive routing

### 🤝 Soft Skills
- **Network Diagramming**: Tạo visual representations của complex networks
- **Documentation**: Chi tiết hóa network configuration và design decisions
- **Problem Solving**: Troubleshoot complex network connectivity issues
- **Architecture Planning**: Thiết kế network topology phù hợp với application requirements

## 🚧 Khó khăn và giải pháp

### Vấn đề 1: Khó khăn trong CIDR Planning
- **Mô tả**: Chọn CIDR blocks phù hợp cho VPC và subnets khá phức tạp
- **Impact**: Có thể dẫn đến IP shortage hoặc poor subnet allocation
- **Root Cause**: Thiếu kinh nghiệm trong network planning
- **Solution**: Sử dụng subnet calculator và planning tools
- **Result**: Tạo được well-structured IP allocation scheme với room for growth
- **Lesson**: Always plan network addressing với future growth trong tâm

### Vấn đề 2: Troubleshooting Connectivity Issues với Security Groups
- **Mô tả**: EC2 instance trong private subnet không thể connect internet qua NAT Gateway
- **Impact**: Không thể update packages hoặc download dependencies
- **Root Cause**: Missing outbound rules trong Security Group
- **Solution**: Review và update Security Group rules
- **Result**: Outbound traffic hoạt động bình thường
- **Lesson**: Security Groups cần cả inbound và outbound rules được cấu hình đúng

## 💭 Reflection & Insights

### What went well today?
- Tạo thành công complex VPC architecture với multiple subnets
- Hiểu rõ networking fundamentals và application trong AWS
- Implement được nhiều security layers phù hợp với best practices

### What could be improved?
- Cần automation cho VPC creation thay vì manual configuration
- Network diagram có thể chi tiết hơn với clear traffic flows
- Cần hiểu sâu hơn về VPC Endpoints và PrivateLink

### Key Insights
- Network design là foundation cho mọi AWS deployment
- Security nên được implement theo layers, không phải single point
- Availability và security thường có tradeoffs cần cân nhắc

### Questions & Curiosities
- How to design transit gateway architecture cho multi-account setup?
- Best practices cho scaling VPC khi số lượng resources tăng?
- Cách integrate với on-premises networks thông qua Direct Connect?

## 📋 Kế hoạch ngày mai

### Priority Tasks
- [ ] **High**: Làm lab Amazon EC2 và tìm hiểu instance types
- [ ] **High**: Thiết lập IAM Roles cho EC2 instances
- [ ] **Medium**: Tạo static website hosting với S3

### Learning Goals
- [ ] Hiểu EC2 instance lifecycle và AMIs
- [ ] Nắm vững IAM Roles và instance profiles
- [ ] Tìm hiểu về S3 static website hosting và security

### Meetings & Deadlines
- [ ] Daily standup với team vào 9:00
- [ ] Demo VPC architecture cho mentor

## 📊 Self Assessment

### Productivity
- **Score**: 8/10
- **Reason**: Hoàn thành đầy đủ VPC lab với nhiều components
- **Improvement**: Có thể tối ưu thời gian bằng cách sử dụng CloudFormation

### Learning
- **Score**: 9/10
- **New Knowledge**: VPC architecture, security controls, network connectivity
- **Application**: Thiết kế được secure và resilient network architecture

### Overall Satisfaction
- **Score**: 8/10
- **Highlights**: Deep understanding về AWS networking và security
- **Areas for Growth**: Automation và Infrastructure as Code cho network deployment

---
## 📎 Attachments & Links

### Learning Resources
- [ AWS lab](https://000003.awsstudygroup.com/vi/)

---

*Worklog created by: Chu Tien Binh - FCJ Intern Batch 2025*  
*Next review: 16/05/2025*