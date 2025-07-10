# Worklog - Ngày 28/05/2025

## 📅 Thông tin cơ bản
- **Ngày**: 28/05/2025
- **Thứ**: Thứ Tư
- **Tuần thực tập**: Tuần thứ 3/8
- **Thời gian làm việc**: 9:00 - 17:00
- **Mood**: 🚀 Hào hứng với serverless architecture

## 🎯 Mục tiêu ngày hôm nay
- [x] Tạo function Lambda mẫu (Node.js hoặc Python) trả về JSON response
- [x] Cấu hình API Gateway REST API với phương thức GET & POST
- [x] Thiết lập Integration Request từ API Gateway đến Lambda Function
- [x] Thử nghiệm API endpoint qua Postman

## 💼 Công việc đã thực hiện

### 1. Tạo và Cấu hình AWS Lambda Function ⏱️ 9:00-10:30
- **Mô tả**:
  - Nghiên cứu về AWS Lambda và serverless computing model
  - Tạo Lambda function mới sử dụng Node.js 18.x runtime
  - Viết code xử lý request parameters và trả về JSON response
  - Thiết lập IAM role với permissions cần thiết cho Lambda
  - Thêm environment variables cho configuration
  - Test function với các test event khác nhau
- **Kết quả**:
  - Lambda function chạy thành công và trả về JSON response đúng format
  - Hiểu rõ về Lambda execution context và cold start
  - Function xử lý được cả GET và POST requests
  - IAM permissions được thiết lập theo principle of least privilege
- **Tools/Tech**:
  - AWS Lambda Console
  - Node.js 18.x
  - AWS IAM
  - JSON formatting
  - Lambda Test Events

### 2. Thiết lập API Gateway REST API ⏱️ 10:30-12:30
- **Mô tả**:
  - Tạo REST API mới trong API Gateway
  - Tạo resources và configure path parameters
  - Thiết lập phương thức GET và POST cho API endpoints
  - Cấu hình request validators và models
  - Thiết lập throttling và usage plans
  - Cấu hình CORS settings cho cross-domain requests
- **Kết quả**:
  - REST API được tạo thành công với các endpoints cần thiết
  - API structure được tổ chức hợp lý với resources hierarchy
  - Request validation và error handling được thiết lập
  - CORS configuration hoạt động cho cross-domain access
- **Tools/Tech**:
  - Amazon API Gateway
  - REST API design
  - API Gateway console
  - Request validators
  - CORS configuration

### 3. Tích hợp API Gateway với Lambda ⏱️ 13:00-14:30
- **Mô tả**:
  - Thiết lập Integration Request để kết nối API Gateway với Lambda
  - Cấu hình mapping templates để chuyển đổi request parameters
  - Thiết lập Integration Response để format Lambda output
  - Cấu hình error handling và response codes
  - Tạo API Gateway models cho request/response validation
  - Thiết lập caching để tối ưu performance
- **Kết quả**:
  - Integration giữa API Gateway và Lambda hoạt động mượt mà
  - Request parameters được mapping chính xác giữa client và Lambda
  - Response codes và error messages được định nghĩa rõ ràng
  - API schema và documentation được tạo tự động
- **Tools/Tech**:
  - API Gateway Integration Request/Response
  - Velocity Template Language (VTL)
  - Mapping templates
  - Response models
  - API Gateway caching

### 4. Testing API Endpoints ⏱️ 14:30-16:00
- **Mô tả**:
  - Deploy API vào stage (dev)
  - Cấu hình Postman để test API endpoints
  - Thực hiện các test case khác nhau cho GET và POST requests
  - Kiểm tra response codes, headers và body
  - Test error handling và validation failures
  - Monitor API calls trong CloudWatch Logs
- **Kết quả**:
  - API endpoints hoạt động đúng như mong đợi
  - GET và POST requests trả về kết quả chính xác
  - Error handling hoạt động tốt với các error cases
  - API performance đáp ứng yêu cầu về latency
- **Tools/Tech**:
  - API Gateway deployment
  - Postman
  - HTTP methods
  - API testing
  - CloudWatch Logs

### 5. Tối ưu hóa và Documentation ⏱️ 16:00-17:00
- **Mô tả**:
  - Phân tích và tối ưu Lambda cold start
  - Cấu hình Lambda concurrency cho better scaling
  - Thiết lập CloudWatch alarms cho API errors
  - Tạo API documentation sử dụng Swagger/OpenAPI
  - Tạo access keys và usage plans cho API consumers
  - Document architecture và configuration decisions
- **Kết quả**:
  - API có documentation đầy đủ cho developers
  - Monitoring và alerting được thiết lập
  - Lambda function được tối ưu để giảm cold start
  - API security được cải thiện với proper authentication
- **Tools/Tech**:
  - CloudWatch Alarms
  - Swagger/OpenAPI
  - API Gateway usage plans
  - Lambda provisioned concurrency
  - Architecture diagrams

## 📚 Kiến thức học được

### 🔧 Technical Skills
- **AWS Lambda Fundamentals**:
  - Lambda execution model và runtime environments
  - Handler patterns và best practices
  - Cold start optimization techniques
  - Function versioning và aliases
- **API Gateway Configuration**:
  - REST API vs HTTP API differences
  - Endpoint configuration và path parameters
  - Integration types và mapping templates
  - API deployment và staging
- **Serverless Integration**:
  - Event-driven architecture patterns
  - Request/response transformation
  - Error handling strategies
  - Service integration và permissions

### 💡 Concepts & Theory
- **Serverless Architecture**: Lợi ích và tradeoffs của serverless model so với traditional deployments
- **API Design Principles**: RESTful design và resource modeling cho APIs
- **Statelessness**: Importance và implications trong Lambda functions
- **Event-Driven Computing**: Fundamental principles và patterns

### 🤝 Soft Skills
- **API Documentation**: Tạo technical documentation rõ ràng cho API consumers
- **Architectural Decision Making**: Evaluating tradeoffs giữa các integration patterns
- **Performance Analysis**: Identifying bottlenecks và optimizing serverless workflows
- **Security Mindset**: Implementing principle of least privilege trong API permissions

## 🚧 Khó khăn và giải pháp

### Vấn đề 1: Lambda Cold Start Latency
- **Mô tả**: API có độ trễ lớn khi first request sau một thời gian không hoạt động
- **Impact**: User experience không tốt với first-time requests
- **Root Cause**: Lambda cold starts do execution environment cần được khởi tạo
- **Solution**: Implement Lambda Provisioned Concurrency cho critical functions
- **Result**: First-time request latency giảm từ >1s xuống còn ~100ms
- **Lesson**: Serverless không phải luôn là zero-maintenance; planning cho cold starts là cần thiết

### Vấn đề 2: API Gateway Mapping Template Errors
- **Mô tả**: API Gateway trả về 500 errors khi mapping request body sang Lambda
- **Impact**: Một số POST requests thất bại với invalid payload
- **Root Cause**: Mapping templates không xử lý đúng một số data types và null values
- **Solution**: Refactor mapping templates với proper error handling và type checking
- **Result**: API xử lý đúng mọi payload formats và trả về appropriate error messages
- **Lesson**: Spend time testing mapping templates với diverse input data để đảm bảo robustness

## 💭 Reflection & Insights

### What went well today?
- Thiết lập thành công end-to-end serverless API với Lambda và API Gateway
- Hiểu rõ về integration patterns giữa các AWS services
- Xử lý được nhiều edge cases trong request/response handling

### What could be improved?
- Cần documentation chi tiết hơn cho API endpoints
- Nên implement authorization layer (như Cognito hoặc JWT)
- Cần thêm test cases cho error conditions và edge cases

### Key Insights
- API Gateway + Lambda cung cấp powerful, scalable solution mà không cần quản lý infrastructure
- Mapping templates là critical cho transforming data giữa client và Lambda
- Serverless architecture đơn giản hóa deployment nhưng có những challenges riêng (cold starts, timeout limits)

### Questions & Curiosities
- Cách tối ưu Lambda function để hạn chế cold start tối đa?
- Làm thế nào để implement canary deployments với API Gateway?
- So sánh performance và cost giữa API Gateway REST API và HTTP API?

## 📋 Kế hoạch ngày mai

### Priority Tasks
- [ ] **High**: Implement AWS Step Functions để điều phối serverless workflow
- [ ] **High**: Xây dựng state machine JSON với nhiều states
- [ ] **Medium**: Tạo Lambda functions cho các steps khác nhau

### Learning Goals
- [ ] Hiểu rõ về Step Functions và state machine concepts
- [ ] Nắm vững cách thiết kế complex workflows
- [ ] Tìm hiểu về error handling và retry logic trong Step Functions

### Meetings & Deadlines
- [ ] Daily standup với team vào 9:00
- [ ] Demo serverless API cho mentor

## 📊 Self Assessment

### Productivity
- **Score**: 9/10
- **Reason**: Completed end-to-end serverless API với full functionality
- **Improvement**: Nên tự động hóa thêm quá trình testing

### Learning
- **Score**: 8/10
- **New Knowledge**: Lambda integration, API Gateway, serverless patterns
- **Application**: Successfully applied serverless concepts vào functioning API

### Overall Satisfaction
- **Score**: 9/10
- **Highlights**: Full serverless implementation working as expected
- **Areas for Growth**: Advanced API features và security best practices

---
## 📎 Attachments & Links

### Learning Resources
- [ AWS lab 01]("https://000010.awsstudygroup.com/vi/)
- [ AWS lab 02](https://000060.awsstudygroup.com/vi/)
- [ AWS lab 03](https://000094.awsstudygroup.com/vi/)

---

*Worklog created by: Chu Tien Binh - FCJ Intern Batch 2025*  
*Next review: 29/05/2025*