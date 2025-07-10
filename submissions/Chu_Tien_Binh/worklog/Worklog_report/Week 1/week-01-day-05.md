# Worklog - Ngày 16/05/2025

## 📅 Thông tin cơ bản
- **Ngày**: 16/05/2025
- **Thứ**: Thứ Sáu
- **Tuần thực tập**: Tuần thứ 1/8
- **Thời gian làm việc**: 9:00 - 17:00
- **Mood**: 🚀 Hào hứng với compute services

## 🎯 Mục tiêu ngày hôm nay
- [x] Tìm hiểu về Amazon EC2 và các instance types
- [x] Launch EC2 instance với custom configuration
- [x] Connect vào EC2 instance thông qua SSH
- [x] Thiết lập và sử dụng IAM Roles cho EC2
- [x] Install web server và deploy application

## 💼 Công việc đã thực hiện

### 1. Tìm hiểu Amazon EC2 Fundamentals ⏱️ 9:00-10:30
- **Mô tả**:
  - Nghiên cứu về Amazon EC2 và virtual servers
  - Tìm hiểu về các EC2 instance types và use cases
  - Nghiên cứu về Amazon Machine Images (AMIs)
  - Tìm hiểu về instance lifecycle (launch, stop, terminate)
  - Nghiên cứu về instance purchasing options (On-Demand, Reserved, Spot)
- **Kết quả**:
  - Hiểu rõ cách EC2 hoạt động và các thành phần
  - Biết cách lựa chọn instance type phù hợp cho workload
  - Hiểu được các purchasing options và cost implications
- **Tools/Tech**:
  - EC2 Documentation
  - Instance Types guide
  - EC2 Pricing Calculator

### 2. Launch và Configure EC2 Instance ⏱️ 10:30-12:00
- **Mô tả**:
  - Chọn Amazon Linux 2 AMI
  - Chọn t2.micro instance type (Free tier eligible)
  - Configure network settings trong VPC đã tạo hôm trước
  - Thiết lập Storage với 8GB gp2 EBS volume
  - Configure Security Group cho SSH, HTTP, và HTTPS
  - Tạo và download key pair cho SSH access
  - Launch instance và verify trạng thái
- **Kết quả**:
  - EC2 instance running trong VPC
  - Security configuration đảm bảo access cần thiết
  - SSH key pair được bảo vệ
  - Instance accessible thông qua SSH
- **Tools/Tech**:
  - EC2 Launch Wizard
  - Security Groups
  - SSH key pairs
  - EBS volumes

### 3. SSH Access và Basic Configuration ⏱️ 13:00-14:00
- **Mô tả**:
  - Configure SSH client với private key permissions
  - Connect vào instance thông qua SSH
  - Update packages và install basic tools
  - Configure hostname và system settings
  - Monitor system resources và logs
  - Setup basic monitoring
- **Kết quả**:
  - Successful SSH connection vào instance
  - System updated và configured
  - Basic monitoring in place
  - Familiar với Linux environment trên EC2
- **Tools/Tech**:
  - SSH client
  - Linux commands
  - Package management (yum/apt)
  - System monitoring

### 4. Thiết lập IAM Roles cho EC2 ⏱️ 14:00-15:30
- **Mô tả**:
  - Tìm hiểu về IAM Roles và instance profiles
  - Tạo IAM Role với permissions cho S3 và CloudWatch
  - Attach permissions policies vào role
  - Create trust relationship cho EC2 service
  - Attach IAM role vào running EC2 instance
  - Test permissions bằng AWS CLI từ instance
- **Kết quả**:
  - IAM Role được tạo thành công với appropriate permissions
  - EC2 instance có thể access AWS services securely
  - Không cần hard-coded credentials trong code
  - Hiểu rõ về security benefits của IAM Roles
- **Tools/Tech**:
  - IAM Roles và Policies
  - Trust relationships
  - EC2 instance profiles
  - AWS CLI credentials

### 5. Deploy Web Application ⏱️ 15:30-17:00
- **Mô tả**:
  - Install Apache Web Server
  - Configure firewall để allow HTTP/HTTPS traffic
  - Deploy sample application code
  - Configure Apache virtual hosts
  - Test web application
  - Monitor application logs và performance
- **Kết quả**:
  - Web server running và accessible
  - Application deployed và functional
  - Logs và monitoring configured
  - End-to-end deployment pipeline thiết lập
- **Tools/Tech**:
  - Apache Web Server
  - HTML/CSS/JavaScript
  - Web application deployment
  - Log management

## 📚 Kiến thức học được

### 🔧 Technical Skills
- **EC2 Management**:
  - Instance lifecycle management
  - AMI selection và customization
  - SSH key management
  - Security Group configuration
- **Linux System Administration**:
  - Package management và updates
  - Service configuration
  - User management
  - Security hardening
- **IAM Role Configuration**:
  - Role-based access control
  - Permission policies
  - Trust relationships
  - Secure access to AWS resources

### 💡 Concepts & Theory
- **Instance Rightsizing**: Chọn instance type phù hợp với workload
- **Principle of Least Privilege**: Cung cấp permissions tối thiểu cần thiết
- **Immutable Infrastructure**: Treat servers as replaceable components
- **Security-by-Design**: Build security vào mọi layer của application stack

### 🤝 Soft Skills
- **Infrastructure Planning**: Design server architecture cho application needs
- **Documentation**: Record configuration steps và architecture decisions
- **Troubleshooting**: Diagnose và resolve system issues
- **Resource Optimization**: Balance performance và cost considerations

## 🚧 Khó khăn và giải pháp

### Vấn đề 1: Security Group Configuration
- **Mô tả**: Web application không accessible từ internet
- **Impact**: Không thể test application từ browser
- **Root Cause**: Security Group không allow HTTP traffic (port 80)
- **Solution**: Update Security Group để allow inbound HTTP traffic
- **Result**: Web application accessible từ internet
- **Lesson**: Verify Security Group rules phù hợp với application needs

### Vấn đề 2: IAM Role Permissions
- **Mô tả**: EC2 instance không thể write logs vào CloudWatch
- **Impact**: Missing monitoring data và application insights
- **Root Cause**: IAM Role thiếu CloudWatch Logs write permissions
- **Solution**: Update IAM policy để include CloudWatch Logs permissions
- **Result**: Application logs successfully streamed vào CloudWatch
- **Lesson**: Test permissions sau khi attach roles để verify functionality

## 💭 Reflection & Insights

### What went well today?
- Successful EC2 instance deployment từ đầu đến cuối
- IAM Roles được configured đúng theo security best practices
- Web application deployment hoạt động tốt

### What could be improved?
- Cần automation script để tăng tốc độ deployment
- Chưa implement monitoring và alerting comprehensive
- Security hardening có thể sâu hơn

### Key Insights
- EC2 flexibility cho phép various workloads với minimal configuration
- IAM Roles là foundation cho secure service-to-service communication
- Web applications trên EC2 cần multiple layers của configuration

### Questions & Curiosities
- How to implement Auto Scaling cho web application deployment?
- Best practices cho AMI management trong CI/CD pipeline?
- Làm thế nào để implement immutable infrastructure với EC2?

## 📋 Kế hoạch ngày mai

### Priority Tasks
- [ ] **High**: Tạo S3 bucket và upload content
- [ ] **High**: Thiết lập static website hosting với S3
- [ ] **Medium**: Configure S3 bucket policies và permissions

### Learning Goals
- [ ] Hiểu S3 storage classes và use cases
- [ ] Nắm vững S3 permissions model
- [ ] Tìm hiểu về S3 static website hosting features

### Meetings & Deadlines
- [ ] Weekly summary report
- [ ] Prepare demo cho team weekly review

## 📊 Self Assessment

### Productivity
- **Score**: 9/10
- **Reason**: Completed EC2 và IAM Role lab với đầy đủ functionality
- **Improvement**: Cần tạo documentation tốt hơn cho future reference

### Learning
- **Score**: 8/10
- **New Knowledge**: EC2 management, IAM Roles, web application deployment
- **Application**: Successfully deployed end-to-end web application stack

### Overall Satisfaction
- **Score**: 9/10
- **Highlights**: End-to-end deployment pipeline với security best practices
- **Areas for Growth**: Automation và Infrastructure as Code

---
## 📎 Attachments & Links

### Learning Resources
- [ AWS lab](https://000004.awsstudygroup.com/vi/)

---

*Worklog created by: Chu Tien Binh - FCJ Intern Batch 2025*  
*Next review: 17/05/2025*