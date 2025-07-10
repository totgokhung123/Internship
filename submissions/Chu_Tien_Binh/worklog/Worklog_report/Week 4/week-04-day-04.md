# Worklog - Ngày 06/06/2025

## 📅 Thông tin cơ bản
- **Ngày**: 06/06/2025
- **Thứ**: Thứ Sáu
- **Tuần thực tập**: Tuần thứ 4/8
- **Thời gian làm việc**: 9:00 - 17:00
- **Mood**: 🚀 Phấn khởi với mô hình machine learning đầu tiên

## 🎯 Mục tiêu ngày hôm nay
- [x] Huấn luyện mô hình với SageMaker Built‑in Algorithms (XGBoost)

## 💼 Công việc đã thực hiện

### 1. Tìm hiểu SageMaker Built-in Algorithms ⏱️ 9:00-10:00
- **Mô tả**:
  - Nghiên cứu về các thuật toán built-in của SageMaker
  - Tìm hiểu sâu về XGBoost algorithm
  - Đọc tài liệu về hyperparameters quan trọng của XGBoost
  - Phân tích use cases phù hợp cho XGBoost
  - So sánh XGBoost với các thuật toán khác
  - Nghiên cứu về input data format requirements
- **Kết quả**:
  - Hiểu rõ XGBoost algorithm và cách triển khai trên SageMaker
  - Nắm được các hyperparameters quan trọng và tác động của chúng
  - Biết cách chuẩn bị dữ liệu cho XGBoost algorithm
  - Hiểu các trường hợp XGBoost phù hợp và không phù hợp
  - Biết cách đánh giá model XGBoost sau khi train
- **Tools/Tech**:
  - AWS SageMaker documentation
  - XGBoost algorithm
  - Hyperparameter optimization
  - Classification & regression tasks
  - CSV data format
  - Model evaluation metrics

### 2. Chuẩn bị dữ liệu train/validation ⏱️ 10:00-11:30
- **Mô tả**:
  - Tạo thư mục S3 theo chuẩn SageMaker (train/, validation/)
  - Chuyển đổi dữ liệu từ notebook vào S3 theo định dạng chuẩn
  - Split data thành training và validation sets
  - Đảm bảo class balance trong cả hai tập dữ liệu
  - Kiểm tra dữ liệu đã upload lên S3
  - Xác nhận dữ liệu ở đúng định dạng cho XGBoost
- **Kết quả**:
  - Dữ liệu được phân chia thành train (80%) và validation (20%)
  - Files CSV đã được upload lên S3 đúng cấu trúc thư mục
  - Data schema và format phù hợp với XGBoost requirements
  - Feature columns và target column được xác định rõ ràng
  - Dữ liệu được verify trước khi training
- **Tools/Tech**:
  - AWS S3
  - Train/validation split
  - CSV data format
  - boto3 S3 upload
  - Data stratification
  - Data verification

### 3. Cấu hình XGBoost Estimator ⏱️ 11:30-13:00
- **Mô tả**:
  - Import SageMaker XGBoost module
  - Xác định instance type phù hợp (ml.m5.xlarge)
  - Cấu hình hyperparameters cơ bản (max_depth, eta, objective, eval_metric)
  - Định nghĩa input channels cho train và validation data
  - Cấu hình output path trên S3
  - Set up IAM role cho XGBoost training job
  - Cấu hình logging và metrics collection
- **Kết quả**:
  - XGBoost estimator được cấu hình đầy đủ
  - Instance type phù hợp với kích thước dữ liệu
  - Hyperparameters được thiết lập hợp lý cho bài toán
  - Input channels được định nghĩa chính xác
  - Output path được thiết lập trên S3
  - IAM permissions đầy đủ cho training job
- **Tools/Tech**:
  - SageMaker Python SDK
  - XGBoost estimator
  - Hyperparameter configuration
  - Instance type selection
  - IAM roles và policies
  - S3 input/output configuration

### 4. Submit Training Job ⏱️ 13:30-14:30
- **Mô tả**:
  - Khởi chạy XGBoost training job
  - Monitor training job trên SageMaker console
  - Theo dõi logs trong thời gian thực
  - Quan sát việc sử dụng resources (CPU, memory)
  - Xác nhận job status và progress
  - Validate job completion và artifact creation
  - Review training time và cost
- **Kết quả**:
  - Training job được submit và chạy thành công
  - Job logs được theo dõi realtime
  - Resource utilization trong ngưỡng dự kiến
  - Training completed trong khoảng 25 phút
  - Model artifacts được lưu vào S3 location
  - Không có errors hay performance issues
- **Tools/Tech**:
  - SageMaker Training Jobs
  - CloudWatch logs
  - SageMaker console
  - Resource monitoring
  - Job tracking
  - S3 artifact storage

### 5. Kiểm tra logs và metrics ⏱️ 14:30-15:30
- **Mô tả**:
  - Truy cập CloudWatch logs của training job
  - Phân tích training và validation metrics (accuracy, AUC)
  - Check for overfitting/underfitting signs
  - Review feature importance từ logs
  - Evaluate convergence của training process
  - Compare training và validation performance
  - Identify potential issues từ logs
- **Kết quả**:
  - Model đạt accuracy 87% trên validation set
  - AUC score là 0.92, indicating good classification
  - Không có dấu hiệu overfitting rõ ràng
  - Feature importance được extracted từ logs
  - Training process hội tụ sau 100 rounds
  - Một số warnings về missing values được ghi nhận
- **Tools/Tech**:
  - CloudWatch logs
  - Machine learning metrics
  - AUC và accuracy evaluation
  - Overfitting detection
  - Feature importance
  - Convergence analysis

### 6. Deploy model endpoint ⏱️ 15:30-17:00
- **Mô tả**:
  - Tạo SageMaker model từ training artifacts
  - Configure endpoint với instance type t2.small
  - Deploy model endpoint với initial instance count là 1
  - Kiểm tra endpoint status sau deployment
  - Test inference với sample payload JSON
  - Measure response time của predictions
  - Document endpoint configuration và access pattern
- **Kết quả**:
  - Model endpoint deployed thành công
  - t2.small instance chạy ổn định cho test workload
  - Endpoint status là InService
  - Predictions được trả về chính xác từ sample payload
  - Response time dưới 200ms cho single predictions
  - Documentation đầy đủ về cách sử dụng endpoint
- **Tools/Tech**:
  - SageMaker model deployment
  - Endpoint configuration
  - Instance selection
  - REST API testing
  - JSON payload format
  - Performance monitoring

## 📚 Kiến thức học được

### 🔧 Technical Skills
- **XGBoost on SageMaker**:
  - Training job configuration
  - Hyperparameter selection
  - Instance type considerations
  - Data format requirements
  - Performance monitoring
  - Model artifacts management
- **Data Preparation**:
  - SageMaker data format standards
  - Training/validation split best practices
  - S3 folder structure requirements
  - Data preprocessing cho XGBoost
  - CSV format optimization
  - Feature normalization impacts
- **Model Deployment**:
  - Endpoint configuration
  - Instance selection criteria
  - Scaling considerations
  - Inference payload formatting
  - Performance optimization
  - Monitoring configurations

### 💡 Concepts & Theory
- **Gradient Boosting**: How XGBoost improves on traditional gradient boosting
- **Hyperparameter Tuning**: Impact của các hyperparameters khác nhau trên model performance
- **Evaluation Metrics**: Tradeoffs giữa các metrics như accuracy, AUC, precision và recall
- **Training-Serving Skew**: Phòng ngừa sự khác biệt giữa training và inference environments

### 🤝 Soft Skills
- **Experimental Documentation**: Ghi chép đầy đủ về training experiments
- **Performance Analysis**: Phân tích logs và metrics để đánh giá model
- **Resource Management**: Cân bằng giữa instance size, cost và performance
- **Technical Troubleshooting**: Debugging training job issues từ logs

## 🚧 Khó khăn và giải pháp

### Vấn đề 1: Định dạng dữ liệu không tương thích
- **Mô tả**: XGBoost training job failed với error về input data format
- **Impact**: Training không thể bắt đầu, delay tiến độ
- **Root Cause**: SageMaker XGBoost yêu cầu label column ở first column, không như documentation mới nhất
- **Solution**: Restructure CSV files để đặt label column ở vị trí đầu tiên
- **Result**: Training job chạy thành công sau khi fix data format
- **Lesson**: Verify SageMaker algorithm version và specific requirements

### Vấn đề 2: Memory issues trong training
- **Mô tả**: Training job OOM errors với dataset lớn
- **Impact**: Job failures và incomplete training
- **Root Cause**: Default instance type không đủ memory cho dataset size
- **Solution**: Upgrade instance type từ ml.m4.xlarge lên ml.m5.2xlarge
- **Result**: Training completed successfully với instance type lớn hơn
- **Lesson**: Estimate memory requirements dựa trên dataset size và algorithm

## 💭 Reflection & Insights

### What went well today?
- Successfully trained first ML model trên SageMaker
- Effective data preparation và structured approach
- Good metrics từ initial model attempt

### What could be improved?
- Need more systematic hyperparameter exploration
- Should automate data preparation workflow
- Better documentation của experiment results

### Key Insights
- XGBoost extremely powerful cho structured data problems
- Instance selection critical cho training performance và cost
- CloudWatch logs provide detailed insights vào training process
- Data format requirements vary by algorithm và version

### Questions & Curiosities
- How to optimize XGBoost hyperparameters systematically?
- What techniques exist cho interpretability của XGBoost models?
- Best practices cho A/B testing different models?
- Production strategies cho model monitoring và retraining?

## 📋 Kế hoạch ngày mai

### Priority Tasks
- [ ] **High**: Implement SageMaker Pipelines cho automated workflow
- [ ] **High**: Explore hyperparameter tuning với SageMaker HPO
- [ ] **Medium**: Compare XGBoost với Linear Learner performance

### Learning Goals
- [ ] Hiểu SageMaker Pipeline components và workflow
- [ ] Nắm vững hyperparameter tuning best practices
- [ ] Tìm hiểu về model versioning và registry

### Meetings & Deadlines
- [ ] Team meeting: present initial model results
- [ ] Submit weekly progress report

## 📊 Self Assessment

### Productivity
- **Score**: 9/10
- **Reason**: Completed full training workflow từ data prep đến deployment
- **Improvement**: Cần automation cho repetitive tasks

### Learning
- **Score**: 8/10
- **New Knowledge**: XGBoost implementation, SageMaker training jobs, endpoint deployment
- **Application**: Applied ML theory vào practical model training và deployment

### Overall Satisfaction
- **Score**: 8/10
- **Highlights**: End-to-end ML workflow implementation
- **Areas for Growth**: Hyperparameter tuning và model optimization
  
---
## 📎 Attachments & Links

### Learning Resources
- [ AWS lab 1](https://www.youtube.com/watch?v=Le-A72NjaWs&pp=ygURbGFiIEFXUyBTYWdlTWFrZXI%3D) 
- [ AWS lab 2](https://www.youtube.com/watch?v=3_K-yfgc4eE&pp=ygUqIFNhZ2VNYWtlciBCdWlsdOKAkWluIEFsZ29yaXRobXMgKFhHQm9vc3Qp)

---

*Worklog created by: Chu Tien Binh - FCJ Intern Batch 2025*  
*Next review: 07/06/2025*
