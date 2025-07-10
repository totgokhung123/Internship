# Worklog - Ngày 29/05/2025

## 📅 Thông tin cơ bản
- **Ngày**: 29/05/2025
- **Thứ**: Thứ Năm
- **Tuần thực tập**: Tuần thứ 3/8
- **Thời gian làm việc**: 9:00 - 17:00
- **Mood**: 🧩 Thích thú với orchestration của serverless workflows

## 🎯 Mục tiêu ngày hôm nay
- [x] Xây dựng state machine JSON trong Step Functions: Parallel, Choice, Retry và Catch
- [x] Tạo 2 Lambda tasks: xử lý dữ liệu input và lưu kết quả S3
- [x] Deploy state machine và trigger thử bằng SDK CLI
- [x] Giám sát execution history & tracing
- [x] Cấu hình SNS notifications khi execution thất bại
- [x] Xóa state machine và cleanup

## 💼 Công việc đã thực hiện

### 1. Tìm hiểu AWS Step Functions ⏱️ 9:00-10:00
- **Mô tả**:
  - Nghiên cứu về AWS Step Functions và state machine concepts
  - Tìm hiểu về Amazon States Language (ASL) để định nghĩa workflows
  - Phân tích các loại states: Task, Choice, Parallel, Map, Wait, etc.
  - Tìm hiểu về error handling, retry logic, và timeout configuration
  - Nghiên cứu integration patterns với các AWS services
- **Kết quả**:
  - Hiểu rõ về Step Functions và state machine paradigm
  - Nắm được syntax của Amazon States Language
  - Hiểu được các state types và use cases
  - Biết cách thiết kế complex workflows với proper error handling
- **Tools/Tech**:
  - AWS Step Functions documentation
  - Amazon States Language (ASL)
  - State machine patterns
  - Workflow orchestration concepts

### 2. Thiết kế và Xây dựng State Machine ⏱️ 10:00-12:00
- **Mô tả**:
  - Thiết kế workflow logic với các states phù hợp
  - Xây dựng state machine JSON với ASL
  - Implement Parallel state để xử lý dữ liệu đồng thời
  - Implement Choice state cho conditional branching
  - Cấu hình Retry và Catch cho error handling
  - Thêm Wait state để simulate long-running processes
- **Kết quả**:
  - State machine JSON hoàn chỉnh với all required states
  - Complex workflow logic được implement chính xác
  - Error handling và retry logic được cấu hình đúng
  - State machine design có khả năng mở rộng
- **Tools/Tech**:
  - AWS Step Functions Designer
  - Amazon States Language (ASL)
  - JSON structure và validation
  - Step Functions state types
  - Error handling patterns

### 3. Tạo Lambda Functions cho State Machine ⏱️ 13:00-14:30
- **Mô tả**:
  - Tạo Lambda function đầu tiên để xử lý dữ liệu input
  - Implement data transformation và validation logic
  - Tạo Lambda function thứ hai để lưu kết quả vào S3
  - Cấu hình IAM roles với các permissions cần thiết
  - Implement error handling và logging trong Lambda functions
  - Test Lambda functions với các input parameters khác nhau
- **Kết quả**:
  - Hai Lambda functions hoạt động chính xác
  - Data processing logic được implement hoàn chỉnh
  - S3 integration hoạt động và lưu được kết quả
  - IAM permissions được cấu hình theo principle of least privilege
  - Error logging và reporting được implement
- **Tools/Tech**:
  - AWS Lambda
  - Python programming
  - AWS SDK for Python (Boto3)
  - IAM roles và policies
  - S3 integration
  - Error handling trong Lambda

### 4. Deploy và Test State Machine ⏱️ 14:30-15:30
- **Mô tả**:
  - Deploy state machine trong AWS Step Functions console
  - Cấu hình input data cho testing
  - Trigger state machine execution bằng AWS CLI
  - Trigger execution qua SDK trong Python script
  - Monitor execution flow và step transitions
  - Verify output data và S3 objects
- **Kết quả**:
  - State machine deployed và hoạt động đúng
  - Execution chạy thành công với expected results
  - CLI và SDK triggering hoạt động đúng
  - Data flow giữa các states chính xác
  - Output được verified trong S3 bucket
- **Tools/Tech**:
  - AWS Step Functions console
  - AWS CLI commands
  - AWS SDK for Python
  - Execution monitoring
  - S3 object verification

### 5. Monitoring, Notification và Cleanup ⏱️ 15:30-17:00
- **Mô tả**:
  - Phân tích execution history và tracing
  - Cấu hình CloudWatch Logs cho detailed logging
  - Thiết lập SNS topic cho failure notifications
  - Integrate SNS với state machine cho error notifications
  - Test failure scenarios để verify notifications
  - Cleanup resources: state machine, Lambda functions, S3 objects
- **Kết quả**:
  - Hiểu rõ về execution flow và tracing
  - SNS notifications gửi thành công khi có lỗi
  - Logging cung cấp detailed information cho debugging
  - Cleanup script xóa thành công tất cả resources
  - Documentation đầy đủ cho state machine architecture
- **Tools/Tech**:
  - CloudWatch Logs
  - AWS X-Ray
  - Amazon SNS
  - Error simulation
  - Resource cleanup
  - Architecture documentation

## 📚 Kiến thức học được

### 🔧 Technical Skills
- **Step Functions Workflow Design**:
  - State machine architecture và patterns
  - Amazon States Language syntax và semantics
  - Complex workflows với parallel processing
  - Error handling và recovery mechanisms
- **Lambda Integration**:
  - Data passing giữa Lambda và Step Functions
  - Context object và payload formats
  - Error reporting từ Lambda đến Step Functions
  - Timeout và memory configuration
- **Monitoring và Debugging**:
  - Execution history analysis
  - Visual workflow monitoring
  - Log correlation giữa services
  - Tracing cross-service requests

### 💡 Concepts & Theory
- **Workflow Orchestration**: Differences giữa choreography và orchestration trong microservices
- **State Machines**: Fundamental principles và application trong distributed systems
- **Idempotency**: Importance và implementation trong serverless workflows
- **Saga Pattern**: Implementing long-running transactions với compensation

### 🤝 Soft Skills
- **System Design**: Thiết kế workflows phức tạp với clarity và maintainability
- **Documentation**: Creating clear diagrams và specifications cho state machines
- **Problem Decomposition**: Breaking down complex processes thành discrete steps
- **Failure Analysis**: Anticipating và planning for failure scenarios

## 🚧 Khó khăn và giải pháp

### Vấn đề 1: Data Passing Between States
- **Mô tả**: Data không được truyền đúng format giữa các states
- **Impact**: State machine executions thất bại với invalid input errors
- **Root Cause**: Mismatched data formats và inconsistent JsonPath expressions
- **Solution**: Implement InputPath và ResultPath rõ ràng cho mỗi state, standardize data format
- **Result**: Data flows correctly giữa states với proper format transformation
- **Lesson**: Careful planning của data flow và format transformation là critical cho complex workflows

### Vấn đề 2: IAM Permission Issues với S3
- **Mô tả**: Lambda function không thể write data vào S3 bucket
- **Impact**: State machine execution thất bại tại S3 write step
- **Root Cause**: Lambda execution role thiếu permissions cần thiết cho S3 bucket
- **Solution**: Update IAM policy để include specific S3 actions và resources
- **Result**: S3 write operations hoạt động thành công
- **Lesson**: Test specific service permissions sớm trong development process

## 💭 Reflection & Insights

### What went well today?
- Successfully implemented complex state machine với multiple state types
- Error handling và retry mechanism hoạt động hiệu quả
- SNS notification integration cung cấp good visibility vào failures

### What could be improved?
- Testing process cần được automated hơn
- State machine design cần modular hơn để reuse components
- Documentation cho các error cases có thể chi tiết hơn

### Key Insights
- Step Functions cung cấp powerful way để orchestrate serverless workflows
- Parallel processing significantly improves throughput cho data processing
- Centralized error handling simplifies debugging và monitoring
- Visual representation của workflows improves understanding và communication

### Questions & Curiosities
- How to implement human approval steps trong Step Functions?
- Best practices cho versioning và deployment của state machines?
- Performance considerations cho large-scale Step Functions workflows?
- Cost optimization strategies cho long-running state machines?

## 📋 Kế hoạch ngày mai

### Priority Tasks
- [ ] **High**: Setup SQS và SNS cho lab messaging systems
- [ ] **High**: Implement messaging pattern với queues và topics
- [ ] **Medium**: Explore dead-letter queues và message visibility

### Learning Goals
- [ ] Hiểu sâu về messaging patterns trong distributed systems
- [ ] Nắm vững SQS queue types và use cases
- [ ] Tìm hiểu về message routing và filtering với SNS

### Meetings & Deadlines
- [ ] Daily standup với team vào 9:00
- [ ] Demo Step Functions workflow cho mentor

## 📊 Self Assessment

### Productivity
- **Score**: 9/10
- **Reason**: Successfully implemented complex workflow với multiple integrations
- **Improvement**: Cần automation scripts cho deployment và testing

### Learning
- **Score**: 8/10
- **New Knowledge**: Step Functions, state machines, workflow orchestration
- **Application**: Applied orchestration patterns vào practical workflow

### Overall Satisfaction
- **Score**: 9/10
- **Highlights**: End-to-end workflow với proper error handling và monitoring
- **Areas for Growth**: Advanced patterns và optimizations cho state machines

---
## 📎 Attachments & Links

### Learning Resources
- [ AWS lab](https://www.youtube.com/watch?v=_CBkLDoc7GE&pp=ygU5QVdTIENsb3VkRm9ybWF0aW9uOiBUcmnhu4NuIGtoYWkgaOG6oSB04bqnbmcgdOG7sSDEkeG7mW5n)

---

*Worklog created by: Chu Tien Binh - FCJ Intern Batch 2025*  
*Next review: 30/05/2025*