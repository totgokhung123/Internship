# Worklog - Ngày 30/05/2025

## 📅 Thông tin cơ bản
- **Ngày**: 30/05/2025
- **Thứ**: Thứ Sáu
- **Tuần thực tập**: Tuần thứ 3/8
- **Thời gian làm việc**: 9:00 - 17:00
- **Mood**: 📨 Hứng thú với distributed messaging

## 🎯 Mục tiêu ngày hôm nay
- [x] Tạo Queue SQS Standard và FIFO
- [x] Tạo SNS topic và Subscription email/SQS
- [x] Viết script Python gửi message vào SNS topic
- [x] Kiểm tra message nhận trên SQS queue
- [x] Thực hành Dead-Letter Queue và Visibility Timeout

## 💼 Công việc đã thực hiện

### 1. Nghiên cứu SQS và SNS Fundamentals ⏱️ 9:00-10:30
- **Mô tả**:
  - Tìm hiểu về Amazon SQS và các loại queues (Standard vs FIFO)
  - Nghiên cứu về Amazon SNS, topics và subscription types
  - So sánh message queuing vs pub/sub patterns
  - Tìm hiểu về các concepts: visibility timeout, dead-letter queues, message retention
  - Nghiên cứu về message filtering và message attributes
  - Tìm hiểu các use cases phù hợp cho SQS và SNS
- **Kết quả**:
  - Hiểu rõ về SQS và SNS architecture và use cases
  - Nắm được key differences giữa Standard và FIFO queues
  - Hiểu message delivery semantics (at-least-once vs exactly-once)
  - Biết cách lựa chọn messaging service phù hợp cho use case
- **Tools/Tech**:
  - Amazon SQS documentation
  - Amazon SNS documentation
  - Messaging patterns
  - Distributed systems concepts

### 2. Tạo và Cấu hình SQS Queues ⏱️ 10:30-12:00
- **Mô tả**:
  - Tạo Standard SQS queue với default settings
  - Cấu hình visibility timeout, message retention và delay delivery
  - Tạo FIFO SQS queue với message deduplication
  - Thiết lập access policies và permissions
  - Cấu hình CloudWatch metrics và alarms
  - Tạo Dead-Letter Queue cho message handling failures
- **Kết quả**:
  - Standard và FIFO queues được tạo và cấu hình thành công
  - Security permissions được thiết lập correctly
  - Dead-Letter Queue được liên kết với main queues
  - Monitoring và alerting được cấu hình
- **Tools/Tech**:
  - Amazon SQS console
  - AWS CLI for SQS
  - IAM policies
  - CloudWatch metrics
  - DLQ configuration

### 3. Thiết lập SNS Topic và Subscriptions ⏱️ 13:00-14:30
- **Mô tả**:
  - Tạo SNS topic với appropriate settings
  - Cấu hình topic policy và access permissions
  - Tạo email subscription và xác nhận subscription
  - Tạo SQS queue subscription để liên kết với queues
  - Implement message filtering với subscription filter policies
  - Cấu hình message delivery retry policy
- **Kết quả**:
  - SNS topic được tạo thành công
  - Multiple subscription types được cấu hình (email, SQS)
  - Message filtering hoạt động với attribute-based filters
  - Cross-account subscriptions được thiết lập (nếu cần)
- **Tools/Tech**:
  - Amazon SNS console
  - Subscription management
  - Filter policies
  - Message attributes
  - Delivery policies

### 4. Viết và Thực thi Python Scripts ⏱️ 14:30-16:00
- **Mô tả**:
  - Viết Python script sử dụng boto3 để gửi messages đến SNS topics
  - Implement message formatting và attributes
  - Viết Python consumer để poll và process messages từ SQS
  - Implement proper error handling và retries
  - Thêm message deletion sau khi xử lý thành công
  - Test với các message formats và sizes khác nhau
- **Kết quả**:
  - Python scripts hoạt động và gửi/nhận messages thành công
  - Message flow từ SNS đến SQS được verified
  - Error handling mechanisms hoạt động như mong đợi
  - Messages được processed và deleted correctly
- **Tools/Tech**:
  - Python programming
  - AWS SDK for Python (boto3)
  - SQS/SNS API calls
  - Error handling patterns
  - Message processing logic

### 5. Testing Advanced Features ⏱️ 16:00-17:00
- **Mô tả**:
  - Test Dead-Letter Queue functionality bằng cách simulate failures
  - Experiment với visibility timeout để handle processing delays
  - Test message ordering trong FIFO queues
  - Implement long polling để reduce API calls
  - Verify message deduplication trong FIFO queues
  - Document findings và best practices
- **Kết quả**:
  - Dead-Letter Queue hoạt động correctly với failed messages
  - Visibility timeout behavior được hiểu và tối ưu
  - Message ordering được maintained trong FIFO queues
  - Long polling giảm đáng kể số API calls
  - Best practices được documented cho team
- **Tools/Tech**:
  - SQS extended client
  - Failure simulation
  - Message visibility management
  - Long polling implementation
  - Documentation tools

## 📚 Kiến thức học được

### 🔧 Technical Skills
- **SQS Management**:
  - Queue creation và configuration
  - Standard vs FIFO queue characteristics
  - Visibility timeout optimization
  - Dead-Letter Queue implementation
  - Long polling và batch processing
- **SNS Configuration**:
  - Topic và subscription management
  - Message filtering với attribute matching
  - Cross-account delivery
  - Retry policies và delivery status
  - Message archiving
- **Messaging Patterns**:
  - Producer-consumer architecture
  - Fan-out pattern implementation
  - Decoupling services với queues
  - Event-driven architectures
  - Message transformation và routing

### 💡 Concepts & Theory
- **Message Delivery Guarantees**: At-least-once vs exactly-once semantics và implications
- **Loose Coupling**: Benefits của decoupled architecture trong distributed systems
- **Asynchronous Processing**: Tradeoffs và advantages so với synchronous communication
- **Back-pressure Handling**: Managing load spikes với queuing systems

### 🤝 Soft Skills
- **System Architecture**: Designing resilient messaging workflows
- **Failure Analysis**: Planning for và mitigating failure scenarios
- **Testing Strategy**: Developing test plans cho asynchronous systems
- **Documentation**: Creating clear process flows cho message-based systems

## 🚧 Khó khăn và giải pháp

### Vấn đề 1: Message Visibility Timeout Issues
- **Mô tả**: Messages bị processed multiple times do visibility timeout quá ngắn
- **Impact**: Duplicate processing causing potential data inconsistencies
- **Root Cause**: Visibility timeout không đủ cho processing time của messages
- **Solution**: Increase visibility timeout và implement idempotent processing
- **Result**: Message được processed đúng một lần, no duplicates
- **Lesson**: Set visibility timeout dựa trên worst-case processing time

### Vấn đề 2: FIFO Queue Message Groups
- **Mô tả**: Message processing bị block dù có available processors
- **Impact**: Reduced throughput và increased processing delay
- **Root Cause**: Single message group ID causing sequential processing
- **Solution**: Implement multiple message group IDs based on data partitioning
- **Result**: Parallel processing increased và throughput improved
- **Lesson**: Careful planning của message groups là critical cho FIFO queue performance

## 💭 Reflection & Insights

### What went well today?
- Successfully implemented end-to-end messaging system với SNS và SQS
- Dead-Letter Queue handling errors effectively
- Python scripts working efficiently để produce và consume messages

### What could be improved?
- Better error handling cho edge cases trong message processing
- Cần thorough testing của failure scenarios và recovery
- Documentation của message flows có thể visual hơn

### Key Insights
- Messaging systems là foundation của scalable distributed architectures
- SQS và SNS complement each other cho different messaging patterns
- Proper configuration của DLQ và visibility timeout là critical cho reliability
- FIFO queues provide powerful ordering guarantees nhưng require careful design

### Questions & Curiosities
- How to handle extremely large messages that exceed SQS size limits?
- Best practices cho scaling SQS consumers dynamically?
- Performance comparison giữa SQS và alternative messaging systems?
- Strategies cho implementing priority queues trong SQS?

## 📋 Kế hoạch ngày mai

### Priority Tasks
- [ ] **High**: Review tuần 3 và consolidate knowledge
- [ ] **High**: Prepare weekly summary và presentation
- [ ] **Medium**: Research AWS Kinesis for next week

### Learning Goals
- [ ] Consolidate understanding của messaging patterns
- [ ] Review serverless architecture best practices
- [ ] Identify areas for deeper exploration

### Meetings & Deadlines
- [ ] Weekly review với mentor
- [ ] Submit weekly progress report

## 📊 Self Assessment

### Productivity
- **Score**: 8/10
- **Reason**: Implemented all planned components của messaging system
- **Improvement**: Cần more comprehensive testing framework

### Learning
- **Score**: 9/10
- **New Knowledge**: SQS/SNS architecture, messaging patterns, failure handling
- **Application**: Successfully implemented real-world messaging patterns

### Overall Satisfaction
- **Score**: 8/10
- **Highlights**: End-to-end messaging solution với proper error handling
- **Areas for Growth**: Advanced patterns và performance optimization

---
## 📎 Attachments & Links

### Learning Resources
- [ AWS lab 01.01](https://www.youtube.com/watch?v=jgpRAiar2LQ&pp=ygU-QVdTIExhbWJkYSArIEFtYXpvbiBBUEkgR2F0ZXdheTogWMOieSBk4buxbmcgQVBJIGtow7RuZyBzZXJ2ZXI%3D)
- [ AWS lab 01.02](https://www.youtube.com/watch?v=pqw8B7tccYw&pp=ygU-QVdTIExhbWJkYSArIEFtYXpvbiBBUEkgR2F0ZXdheTogWMOieSBk4buxbmcgQVBJIGtow7RuZyBzZXJ2ZXLSBwkJ3gkBhyohjO8%3D)

---

*Worklog created by: Chu Tien Binh - FCJ Intern Batch 2025*  
*Next review: 31/05/2025*