# Worklog - Ngày 01/06/2025

## 📅 Thông tin cơ bản
- **Ngày**: 01/06/2025
- **Thứ**: Chủ Nhật
- **Tuần thực tập**: Tuần thứ 3/8
- **Thời gian làm việc**: 9:00 - 17:00
- **Mood**: 🐳 Phấn khởi với container orchestration

## 🎯 Mục tiêu ngày hôm nay
- [x] Cài đặt eksctl và AWS CLI, kubectl
- [x] Tạo EKS cluster cơ bản với 2 node nhóm managed node group
- [x] Build Docker image và push lên Amazon ECR repository
- [x] Viết manifest Deployment & Service cho app mẫu
- [x] Deploy lên cluster, kiểm tra pods, services qua kubectl
- [x] Xóa resources: Deployment, Service, EKS cluster

## 💼 Công việc đã thực hiện

### 1. Cài đặt và Cấu hình Tools ⏱️ 9:00-10:00
- **Mô tả**:
  - Cài đặt AWS CLI version 2 và configure credentials
  - Download và cài đặt eksctl command line tool
  - Cài đặt kubectl cho Kubernetes management
  - Verify installations và test connectivity
  - Configure AWS CLI profiles cho different environments
  - Setup shell completion cho improved productivity
  - Cài đặt Docker cho local container development
- **Kết quả**:
  - All required tools cài đặt thành công
  - AWS CLI được cấu hình với appropriate credentials
  - Kubectl có thể connect tới AWS services
  - Docker environment ready cho container builds
  - Command line utilities hoạt động với proper permissions
- **Tools/Tech**:
  - AWS CLI v2
  - eksctl
  - kubectl
  - Docker Desktop
  - Shell configuration
  - IAM credentials

### 2. Tạo và Cấu hình EKS Cluster ⏱️ 10:00-12:00
- **Mô tả**:
  - Design cluster architecture với networking considerations
  - Create EKS cluster sử dụng eksctl với declarative configuration
  - Configure VPC, subnets, và security groups
  - Setup managed node groups với 2 nodes t3.medium
  - Configure IAM OIDC provider cho service accounts
  - Setup cluster autoscaler (horizontal pod autoscaler)
  - Verify cluster components và node status
  - Configure kubectl context để connect với cluster
- **Kết quả**:
  - EKS cluster running với all components healthy
  - 2 nodes registered và ready trong cluster
  - Networking correctly configured với proper security groups
  - IAM integration working cho authentication
  - Kubectl context configured và working correctly
  - Cluster details được documented cho reference
- **Tools/Tech**:
  - Amazon EKS
  - eksctl configuration
  - Kubernetes architecture
  - VPC networking
  - IAM roles và service accounts
  - Node management

### 3. Build và Push Docker Image ⏱️ 13:00-14:00
- **Mô tả**:
  - Create sample application (Node.js hoặc Python web API)
  - Viết Dockerfile với best practices (multi-stage builds, security)
  - Tạo Amazon ECR repository cho container images
  - Build Docker image locally với optimizations
  - Tag image với appropriate versioning
  - Authenticate Docker client với ECR
  - Push Docker image lên ECR repository
  - Verify image availability và scan cho vulnerabilities
- **Kết quả**:
  - Sample application được containerized thành công
  - Docker image optimized cho size và security
  - ECR repository được tạo với proper permissions
  - Image pushed successfully lên ECR
  - Image scanning shows no critical vulnerabilities
  - Documentation của image build process
- **Tools/Tech**:
  - Dockerfile best practices
  - Multi-stage builds
  - Amazon ECR
  - Docker CLI
  - Container security
  - Image tagging

### 4. Viết và Áp dụng Kubernetes Manifests ⏱️ 14:00-15:30
- **Mô tả**:
  - Design application deployment strategy
  - Create Deployment manifest với appropriate replicas và resources
  - Configure Pod specifications với health checks và resource limits
  - Create Service manifest để expose application
  - Write ConfigMap và Secret manifests cho application configuration
  - Implement appropriate labels và selectors
  - Document manifest structure và dependencies
  - Apply manifests tới cluster sử dụng kubectl
- **Kết quả**:
  - Kubernetes manifests được viết theo best practices
  - Deployment object applied và running trên cluster
  - Service correctly routing traffic đến pods
  - ConfigMaps và Secrets properly integrated
  - Resource limits và requests defined appropriately
  - Application accessible thông qua Service endpoint
- **Tools/Tech**:
  - Kubernetes YAML manifests
  - Deployment resources
  - Service configuration
  - ConfigMaps và Secrets
  - Resource management
  - kubectl apply

### 5. Test, Monitoring và Cleanup ⏱️ 15:30-17:00
- **Mô tả**:
  - Verify pod status và health với kubectl
  - Test application functionality thông qua Service endpoint
  - Configure basic monitoring với CloudWatch Container Insights
  - Check logs từ running containers
  - Scale deployment lên/xuống để test autoscaling
  - Document EKS best practices và findings
  - Delete all resources systematically (Deployments, Services)
  - Delete EKS cluster và verify cleanup completion
- **Kết quả**:
  - Application running correctly in Kubernetes environment
  - Monitoring showing healthy status cho pods
  - Logs correctly captured và accessible
  - Scaling operations working as expected
  - All resources successfully deleted
  - Complete documentation của deployment và cleanup process
- **Tools/Tech**:
  - kubectl commands
  - Kubernetes monitoring
  - CloudWatch Container Insights
  - Log analysis
  - Resource cleanup
  - eksctl delete cluster

## 📚 Kiến thức học được

### 🔧 Technical Skills
- **EKS Management**:
  - Cluster provisioning và configuration
  - Node group management
  - IAM integration với Kubernetes
  - Networking setup cho Kubernetes
  - Cluster monitoring và troubleshooting
- **Container Development**:
  - Dockerfile optimization techniques
  - Multi-stage build implementation
  - Image security best practices
  - ECR repository management
  - Image tagging và versioning
- **Kubernetes Deployment**:
  - Manifest writing và application
  - Pod lifecycle management
  - Service và networking configuration
  - Resource management và limits
  - Namespace organization

### 💡 Concepts & Theory
- **Container Orchestration**: Principles và benefits của Kubernetes so với single container deployments
- **Declarative Infrastructure**: Advantages của declarative approach trong Kubernetes
- **Service Discovery**: How Kubernetes manages service routing và discovery
- **Control Plane**: Understanding Kubernetes architecture và components

### 🤝 Soft Skills
- **Complex System Design**: Architecting multi-component container deployments
- **Resource Planning**: Estimating và allocating resources trong Kubernetes
- **Technical Documentation**: Creating clear documentation cho container deployments
- **Troubleshooting Methodology**: Systematic approach to debugging distributed systems

## 🚧 Khó khăn và giải pháp

### Vấn đề 1: Node IAM Permissions
- **Mô tả**: Worker nodes không thể pull images từ ECR
- **Impact**: Pods stuck trong "ImagePullBackOff" state
- **Root Cause**: Node IAM role thiếu ECR permissions cần thiết
- **Solution**: Update node IAM role để include ECR read permissions
- **Result**: Nodes successfully pulling images từ ECR
- **Lesson**: Validate node IAM permissions trước deployment để ensure access tới required AWS services

### Vấn đề 2: Networking Configuration
- **Mô tả**: Pods không thể communicate với external services
- **Impact**: Application không thể access dependencies
- **Root Cause**: Security groups và network policies blocking traffic
- **Solution**: Update security groups và configure network policies appropriately
- **Result**: Pods successfully communicating với external services
- **Lesson**: Thoroughly test và configure network settings sớm trong deployment process

## 💭 Reflection & Insights

### What went well today?
- Successfully created EKS cluster và deployed containerized application
- Docker image build và push process streamlined và documented
- Kubernetes manifests đúng best practices và working correctly

### What could be improved?
- Need infrastructure as code (IaC) for more repeatable deployments
- Better monitoring và alerting setup cho production environments
- More comprehensive testing của failure scenarios và recovery

### Key Insights
- EKS simplifies Kubernetes management nhưng vẫn yêu cầu deep understanding
- Proper resource planning is critical cho container orchestration
- IAM integration is a key component của secure Kubernetes deployments on AWS
- Declarative manifests make infrastructure reproducible và maintainable

### Questions & Curiosities
- How to implement GitOps workflow với EKS?
- Best practices cho stateful applications trên Kubernetes?
- Performance considerations cho large-scale EKS deployments?
- Strategies cho efficient multi-tenant EKS clusters?

## 📋 Kế hoạch ngày mai

### Priority Tasks
- [ ] **High**: Explore AWS CI/CD services cho automated deployments
- [ ] **High**: Setup CodeCommit, CodeBuild và CodeDeploy pipeline
- [ ] **Medium**: Integrate deployment automation với applications

### Learning Goals
- [ ] Hiểu về CI/CD principles và implementation trong AWS
- [ ] Nắm vững AWS CodePipeline và related services
- [ ] Tìm hiểu về automated testing trong CI/CD pipelines

### Meetings & Deadlines
- [ ] Week start planning meeting
- [ ] Prepare demo cho EKS deployment

## 📊 Self Assessment

### Productivity
- **Score**: 9/10
- **Reason**: Successfully implemented complex EKS deployment workflow
- **Improvement**: Need more automation và IaC approach

### Learning
- **Score**: 9/10
- **New Knowledge**: EKS, Kubernetes, container orchestration
- **Application**: Applied container deployment patterns trong Kubernetes environment

### Overall Satisfaction
- **Score**: 9/10
- **Highlights**: End-to-end container deployment từ build đến orchestration
- **Areas for Growth**: Infrastructure automation và advanced Kubernetes features

---
## 📎 Attachments & Links

### Learning Resources
- [ AWS lab](https://www.youtube.com/watch?v=qhfHda0HEtE&pp=ygU9IEFtYXpvbiBFS1MgJiBEb2NrZXI6IFRyaeG7g24ga2hhaSBjb250YWluZXIgdHLDqm4gS3ViZXJuZXRlcw%3D%3D)

---

*Worklog created by: Chu Tien Binh - FCJ Intern Batch 2025*  
*Next review: 02/06/2025*