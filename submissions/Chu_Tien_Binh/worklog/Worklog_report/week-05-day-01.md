# Worklog - Ngày 09/06/2025

## 📅 Thông tin cơ bản
- **Ngày**: 09/06/2025
- **Thứ**: Thứ Hai
- **Tuần thực tập**: Tuần thứ 5/8
- **Thời gian làm việc**: 9:00 - 17:00
- **Mood**: 🚀 Hào hứng với việc triển khai dự án

## 🎯 Mục tiêu ngày hôm nay
- [x] Triển khai hosting dự án thực thế, ứng dụng web kết hợp 2 port Backend Python và Frontend React với EC2 trên OS Windows

## 💼 Công việc đã thực hiện

### 1. Tìm hiểu về EC2 hosting cho Windows OS ⏱️ 9:00-10:30
- **Mô tả**:
  - Nghiên cứu về Windows instances trên EC2
  - So sánh các AMI Windows Server có sẵn
  - Tìm hiểu về RDP connection và Windows EC2 management
  - Nghiên cứu best practices cho Windows security groups
  - Phân tích performance considerations cho Windows workloads
  - Tìm hiểu licensing và cost considerations
- **Kết quả**:
  - Hiểu rõ về Windows AMIs trên EC2 và lựa chọn phù hợp
  - Nắm được cách kết nối và quản lý Windows instances
  - Biết các considerations về licensing và cost
  - Hiểu performance requirements cho web applications
  - Biết cách cấu hình security groups phù hợp cho Windows
- **Tools/Tech**:
  - EC2 Windows instances
  - Windows Server AMIs
  - RDP connection
  - Security groups
  - Windows administration
  - AWS Management Console

### 2. Khởi tạo EC2 Windows instance ⏱️ 10:30-12:00
- **Mô tả**:
  - Chọn Windows Server 2019 AMI
  - Cấu hình instance type t2.large cho performance
  - Setup storage với 50GB SSD
  - Configure security groups cho RDP access
  - Generate và lưu trữ key pair an toàn
  - Launch instance và verify status
  - Retrieve Windows password sử dụng key pair
  - Test RDP connection tới instance
- **Kết quả**:
  - EC2 Windows instance running thành công
  - RDP access hoạt động đúng cách
  - Disk và memory đủ cho web application
  - Security groups configured đúng cho administrative access
  - Windows password retrieved và lưu trữ an toàn
  - Instance sẵn sàng cho web deployment
- **Tools/Tech**:
  - EC2 instance launching
  - Windows Server configuration
  - Key pairs và password management
  - RDP client
  - Security groups configuration
  - Instance sizing

### 3. Cài đặt Web Environment ⏱️ 13:00-14:30
- **Mô tả**:
  - Install Python 3.9 cho backend services
  - Setup Python virtual environment
  - Install Node.js và npm cho React frontend
  - Configure IIS cho web hosting
  - Install SQL Server Express cho database (nếu cần)
  - Configure Windows Firewall cho ports cần thiết
  - Setup environment variables
  - Install development tools và dependencies
- **Kết quả**:
  - Python 3.9 installed với virtual environment
  - Node.js và npm cài đặt thành công
  - IIS configured cho web hosting
  - SQL Server running (nếu cần)
  - Development tools sẵn sàng
  - All necessary ports open trong Windows Firewall
  - Environment variables configured correctly
- **Tools/Tech**:
  - Python setup
  - Node.js và npm
  - IIS configuration
  - SQL Server Express
  - Windows Firewall
  - Development tools installation
  - Environment configuration

### 4. Tạo Security Groups cho access control ⏱️ 14:30-15:30
- **Mô tả**:
  - Tạo security group cho admin access (RDP port 3389)
  - Tạo security group cho web users (HTTP/HTTPS ports 80/443)
  - Configure source IP restrictions cho admin access
  - Open ports cho backend services (e.g., Python Flask port)
  - Open ports cho frontend React service
  - Implement security group rules với least privilege
  - Document security group configurations
- **Kết quả**:
  - Security group cho admin users created và restricted
  - Security group cho web users created và configured
  - Backend service ports mở đúng cách
  - Frontend ports accessible cho users
  - All rules follow least privilege principle
  - Documentation hoàn chỉnh về security groups
- **Tools/Tech**:
  - EC2 Security Groups
  - Network security concepts
  - Port management
  - Admin và user access controls
  - IP restrictions
  - AWS security best practices

### 5. Deploy Backend Python Application ⏱️ 15:30-16:15
- **Mô tả**:
  - Upload backend code lên Windows EC2 instance
  - Install required Python packages từ requirements.txt
  - Configure application settings cho production
  - Setup service để run backend app automatically
  - Configure logging cho backend service
  - Test backend API functionality
  - Setup monitoring cho backend service
- **Kết quả**:
  - Backend application running thành công
  - All dependencies installed correctly
  - Service configured để start automatically
  - API endpoints accessible và functional
  - Logging setup cho troubleshooting
  - Monitoring in place để track performance
- **Tools/Tech**:
  - Flask/Django deployment
  - Python virtual environments
  - Windows services
  - API testing
  - Production configuration
  - Application logging
  - Service monitoring

### 6. Deploy Frontend React Application ⏱️ 16:15-17:00
- **Mô tả**:
  - Upload React code tới EC2 instance
  - Run npm install để install dependencies
  - Build production version của React app
  - Configure IIS để serve static React files
  - Setup URL rewriting rules nếu cần
  - Configure CORS để allow backend API calls
  - Test frontend functionality
- **Kết quả**:
  - React application built và deployed thành công
  - All frontend dependencies installed
  - IIS serving React application correctly
  - CORS configured để allow API communication
  - Frontend-to-backend integration hoạt động tốt
  - Web application publicly accessible
- **Tools/Tech**:
  - React deployment
  - npm package management
  - IIS configuration for SPA
  - URL rewriting
  - CORS configuration
  - Frontend testing
  - Static file serving

## 📚 Kiến thức học được

### 🔧 Technical Skills
- **EC2 Windows Management**:
  - Windows AMI selection criteria
  - Instance sizing cho web applications
  - Remote administration via RDP
  - Windows updates và maintenance
  - Performance monitoring trên Windows EC2
  - Cost optimization cho Windows instances
- **Web Deployment**:
  - Multi-tier application deployment
  - Backend và frontend hosting strategies
  - Python service management trên Windows
  - IIS configuration cho React apps
  - Production environment setup
  - Security considerations for web apps
- **Network Security**:
  - Security group design và implementation
  - Principle of least privilege application
  - Port management cho web applications
  - Admin và user access separation
  - Layer security với multiple controls
  - Documentation của security configurations

### 💡 Concepts & Theory
- **Multi-tier Architecture**: Separation của frontend, backend, và database components
- **Infrastructure as Code**: Principles của reproducible infrastructure setup
- **Defense in Depth**: Multiple layers của security controls
- **High Availability Design**: Considerations cho scalable web applications

### 🤝 Soft Skills
- **Project Planning**: Structured approach to production deployment
- **Documentation**: Creating clear records của infrastructure configuration
- **Problem Solving**: Debugging environment và connectivity issues
- **Security Mindset**: Thinking about security from design phase

## 🚧 Khó khăn và giải pháp

### Vấn đề 1: CORS Issues giữa Frontend và Backend
- **Mô tả**: Frontend không thể gọi backend API do CORS restrictions
- **Impact**: Application không hoạt động sau khi deploy
- **Root Cause**: Missing CORS headers trong backend Python application
- **Solution**: Configure CORS trong backend để allow requests từ frontend origin
- **Result**: Frontend successfully communicates với backend API
- **Lesson**: Always test cross-origin communication trong local environment trước deployment

### Vấn đề 2: Windows Firewall Blocking
- **Mô tả**: Backend services không accessible mặc dù security groups đã mở port
- **Impact**: Frontend không thể connect tới backend services
- **Root Cause**: Windows Firewall blocking incoming connections
- **Solution**: Create inbound rules trong Windows Firewall cho services
- **Result**: Backend services accessible như mong đợi
- **Lesson**: Remember to configure both AWS security groups và OS-level firewall

## 💭 Reflection & Insights

### What went well today?
- Successfully deployed multi-tier application trên Windows EC2
- Effective security configuration với separate admin và user access
- Clean integration giữa backend và frontend components

### What could be improved?
- Need better automation cho deployment process
- Should create deployment scripts để avoid manual steps
- Better documentation của configuration steps

### Key Insights
- Windows EC2 instances require different management approach so với Linux
- Security is multi-layered với AWS security groups và OS-level controls
- Web deployment trên Windows có unique challenges so với Linux environments
- IIS requires specific configuration cho modern web applications

### Questions & Curiosities
- Best practices cho automated deployment tới Windows EC2?
- How to implement CI/CD pipelines cho Windows environments?
- Performance tuning của IIS cho React applications?
- Cost optimization strategies cho Windows workloads?

## 📋 Kế hoạch ngày mai

### Priority Tasks
- [ ] **High**: Implement monitoring và logging cho web application
- [ ] **High**: Setup automated backups cho application data
- [ ] **Medium**: Improve security với HTTPS certificate

### Learning Goals
- [ ] Hiểu AWS monitoring tools cho Windows instances
- [ ] Nắm vững backup strategies cho web applications
- [ ] Tìm hiểu về HTTPS configuration với AWS Certificate Manager

### Meetings & Deadlines
- [ ] Infrastructure review meeting
- [ ] Demo của deployed application

## 📊 Self Assessment

### Productivity
- **Score**: 9/10
- **Reason**: Completed end-to-end deployment của complex application
- **Improvement**: Need better automation của manual steps

### Learning
- **Score**: 8/10
- **New Knowledge**: Windows EC2 management, multi-tier deployment, security configuration
- **Application**: Applied infrastructure concepts vào practical deployment

### Overall Satisfaction
- **Score**: 8/10
- **Highlights**: Successfully deployed working application
- **Areas for Growth**: Automation, monitoring, và security hardening

---
## 📎 Attachments & Links

### Learning Resources
- [ AWS lab](https://000004.awsstudygroup.com/vi/4-launchlinuxinstance/4.2-connectlinuxinstance/)

---

*Worklog created by: Chu Tien Binh - FCJ Intern Batch 2025*  
*Next review: 10/06/2025*
