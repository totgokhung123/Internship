# Worklog - Ngày 17/06/2025

## 📅 Thông tin cơ bản
- **Ngày**: 17/06/2025
- **Thứ**: Thứ Ba
- **Tuần thực tập**: Tuần thứ 6/8
- **Thời gian làm việc**: 9:00 - 17:00
- **Mood**: 🔄 Tập trung vào disaster recovery và business continuity

## 🎯 Mục tiêu ngày hôm nay
- [x] Làm lab AWS Elastic Disaster Recovery Workshop

## 💼 Công việc đã thực hiện

### 1. Tìm hiểu AWS Elastic Disaster Recovery ⏱️ 9:00-10:15
- **Mô tả**:
  - Nghiên cứu về AWS Elastic Disaster Recovery (DRS)
  - Tìm hiểu về DR concepts và terminologies
  - Đọc tài liệu về DRS architecture và components
  - Phân tích DRS benefits và use cases
  - Tìm hiểu về recovery point objectives (RPO)
  - Research về recovery time objectives (RTO)
  - Compare DRS với các DR solutions khác
- **Kết quả**:
  - Hiểu rõ về AWS DRS architecture và benefits
  - Nắm được concepts chính về disaster recovery
  - Biết cách DRS replicates servers từ source environment
  - Hiểu các stages của disaster recovery process
  - Nắm được RPO và RTO capabilities của DRS
  - Biết các use cases phù hợp cho DRS
- **Tools/Tech**:
  - AWS Elastic Disaster Recovery
  - Disaster recovery concepts
  - Replication technologies
  - Recovery objectives (RPO/RTO)
  - AWS infrastructure
  - Business continuity planning
  - High availability

### 2. Thiết lập Workshop Environment ⏱️ 10:15-11:15
- **Mô tả**:
  - Access workshop materials và instructions
  - Review workshop architecture và components
  - Verify prerequisites cho lab environment
  - Understand lab objectives và flow
  - Setup note-taking cho workshop progress
  - Review provided AWS account permissions
  - Check resource limits cho lab completion
  - Prepare testing environment
- **Kết quả**:
  - Workshop materials accessed và understood
  - Lab environment prerequisites verified
  - Clear understanding của lab objectives
  - Workshop flow và steps documented
  - Required permissions confirmed
  - Resource limits checked và sufficient
  - Environment ready cho workshop completion
- **Tools/Tech**:
  - AWS workshop platform
  - Lab environment
  - AWS console access
  - Documentation review
  - Architecture diagrams
  - Permission verification
  - Resource planning

### 3. Kết nối đến Bastion Host ⏱️ 11:15-12:30
- **Mô tả**:
  - Locate bastion host details trong workshop
  - Download SSH key cho bastion host connection
  - Configure SSH client cho secure connection
  - Connect tới bastion host via SSH
  - Verify connectivity và permissions
  - Test access tới source server environment
  - Configure SSH forwarding nếu cần thiết
  - Document connection process
- **Kết quả**:
  - Successfully connected tới bastion host
  - SSH key configured và working correctly
  - Connection security verified
  - Access tới source servers confirmed
  - All required permissions available
  - Connection process documented cho reference
  - Environment ready cho DRS configuration
- **Tools/Tech**:
  - SSH client configuration
  - Bastion host architecture
  - Key pair authentication
  - Linux/Windows connectivity
  - Security best practices
  - Network routing
  - Remote server access

### 4. Thực hiện cấu hình DRS ⏱️ 13:00-14:15
- **Mô tả**:
  - Navigate tới AWS DRS console
  - Configure DRS replication settings
  - Set up network requirements cho DRS
  - Configure security groups và permissions
  - Set up source network & subnet mapping
  - Configure replication server settings
  - Set default settings cho recovery instances
  - Document configuration decisions
- **Kết quả**:
  - AWS DRS successfully configured
  - Replication settings optimized cho lab environment
  - Network mapping completed correctly
  - Security groups configured appropriately
  - Permissions set up cho replication
  - Recovery instance defaults configured
  - Configuration documented cho reference
  - DRS ready cho agent installation
- **Tools/Tech**:
  - AWS DRS console
  - Replication settings
  - Network configuration
  - Security groups
  - IAM permissions
  - Subnet mapping
  - Instance type selection
  - Documentation

### 5. Cấu hình DRS Agent ⏱️ 14:15-15:30
- **Mô tả**:
  - Generate DRS agent installation commands
  - Connect tới source servers qua bastion host
  - Install DRS agent trên source servers
  - Verify agent installation và connectivity
  - Monitor initial data replication progress
  - Configure agent throttling nếu cần thiết
  - Troubleshoot any agent connectivity issues
  - Document agent installation process
- **Kết quả**:
  - DRS agent installation commands generated
  - Agents successfully installed trên source servers
  - Agent connectivity verified với AWS DRS
  - Initial data replication started
  - Replication progress monitored
  - Agent settings optimized cho lab environment
  - Installation process documented thoroughly
  - Source servers shown trong DRS console
- **Tools/Tech**:
  - DRS agent installation
  - Linux/Windows command execution
  - Agent configuration
  - Network connectivity
  - Replication monitoring
  - Bandwidth throttling
  - Troubleshooting
  - SSH access

### 6. Cấu hình Launch Template ⏱️ 15:30-17:00
- **Mô tả**:
  - Review server details trong DRS console
  - Create và configure launch templates
  - Set appropriate instance types cho recovery
  - Configure subnet và security group mappings
  - Set up post-launch scripts nếu cần thiết
  - Configure instance tags và metadata
  - Test launch template settings
  - Review recovery instance settings
- **Kết quả**:
  - Launch templates created cho each server
  - Instance types selected based on source servers
  - Network settings properly configured
  - Security groups appropriately mapped
  - Post-launch settings configured
  - Instance metadata và tags set up
  - Templates tested và validated
  - Recovery readiness confirmed
- **Tools/Tech**:
  - EC2 launch templates
  - Instance type selection
  - Network configuration
  - Security groups
  - User data scripts
  - Instance metadata
  - Resource tagging
  - Recovery validation

## 📚 Kiến thức học được

### 🔧 Technical Skills
- **Disaster Recovery Planning**:
  - DRS architecture và components
  - Replication configuration và monitoring
  - Recovery point objectives (RPO)
  - Recovery time objectives (RTO)
  - Agent-based replication
  - Recovery instance configuration
  - Drill testing methodology
- **AWS Infrastructure**:
  - Multi-region deployment
  - Network configuration across regions
  - Security group management
  - IAM roles và permissions
  - EC2 launch templates
  - Subnet mapping
  - Cross-region networking
- **System Administration**:
  - Bastion host configuration
  - SSH key management
  - Agent installation và monitoring
  - System replication concepts
  - Linux/Windows server management
  - Network troubleshooting
  - Remote server access

### 💡 Concepts & Theory
- **Business Continuity**: Strategies cho maintaining operations during disasters
- **Disaster Recovery Tiers**: Different levels của disaster recovery solutions
- **Replication Technologies**: Block-level vs application-level replication
- **Recovery Testing**: Importance và methodologies cho DR testing

### 🤝 Soft Skills
- **Disaster Planning**: Structured approach to recovery planning
- **Documentation**: Creating clear records của recovery configurations
- **Problem Solving**: Troubleshooting replication và connectivity issues
- **Risk Assessment**: Evaluating recovery options và trade-offs

## 🚧 Khó khăn và giải pháp

### Vấn đề 1: Network Connectivity Issues
- **Mô tả**: DRS agent không thể connect tới replication servers
- **Impact**: Initial replication không thể start
- **Root Cause**: Security group rules không allow traffic từ source network
- **Solution**: Update security groups with correct inbound rules
- **Result**: Agent successfully connected và replication started
- **Lesson**: Carefully verify network paths và security group rules trước agent install

### Vấn đề 2: Replication Lag
- **Mô tả**: Slow replication speed với high lag reporting
- **Impact**: Extended time to achieve stable recovery point
- **Root Cause**: Default bandwidth throttling quá aggressive
- **Solution**: Adjust bandwidth throttling settings cho lab environment
- **Result**: Replication speed improved và lag reduced
- **Lesson**: Tune replication settings based on network conditions và data volume

## 💭 Reflection & Insights

### What went well today?
- Successfully configured complete DRS environment
- Effective agent deployment trên multiple server types
- Clean configuration của launch templates cho recovery

### What could be improved?
- Need better documentation của network requirements
- Could implement more thorough testing của recovery scenarios
- Should automate more của agent installation process

### Key Insights
- AWS DRS significantly simplifies disaster recovery setup
- Agent-based replication provides flexibility for diverse environments
- Launch templates critical cho successful recovery execution
- Testing is essential component của disaster recovery planning

### Questions & Curiosities
- Best practices cho automating DR failover processes?
- Strategies cho reducing RPO trong high-change environments?
- Approaches to cost optimization cho DR environments?
- Methods cho testing DR without business disruption?

## 📋 Kế hoạch ngày mai

### Priority Tasks
- [ ] **High**: Perform drill testing của recovery instances
- [ ] **High**: Document complete DR runbook cho environment
- [ ] **Medium**: Test application functionality trong recovered environment

### Learning Goals
- [ ] Hiểu recovery drill testing best practices
- [ ] Nắm vững runbook documentation standards
- [ ] Tìm hiểu về DR monitoring và alerting

### Meetings & Deadlines
- [ ] DR planning review meeting
- [ ] Submit lab completion report

## 📊 Self Assessment

### Productivity
- **Score**: 9/10
- **Reason**: Completed all lab steps và configuration successfully
- **Improvement**: Could document process more thoroughly during execution

### Learning
- **Score**: 8/10
- **New Knowledge**: AWS DRS, replication technologies, recovery planning
- **Application**: Applied DR concepts to practical lab implementation

### Overall Satisfaction
- **Score**: 8/10
- **Highlights**: Functional DR environment với reliable replication
- **Areas for Growth**: Recovery testing và automation

---
## 📎 Attachments & Links

### Learning Resources
- [ AWS lab](https://000100.awsstudygroup.com/vi/7-template/)

---

*Worklog created by: Chu Tien Binh - FCJ Intern Batch 2025*  
*Next review: 18/06/2025*
