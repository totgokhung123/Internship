# Worklog - Ngày 06/07/2025

## 📅 Thông tin cơ bản
- **Ngày**: 06/07/2025
- **Thứ**: Chủ Nhật
- **Tuần thực tập**: Tuần thứ 8/8
- **Thời gian làm việc**: 9:00 - 17:00
- **Mood**: 🔄 Tập trung vào workflow automation

## 🎯 Mục tiêu ngày hôm nay
- [x] Tự triển khai pipeline với SageMaker Pipelines

## 💼 Công việc đã thực hiện

### 1. Tìm hiểu SageMaker Pipelines ⏱️ 9:00-10:00
- **Mô tả**:
  - Nghiên cứu về SageMaker Pipelines architecture
  - Tìm hiểu về các step types: Processing, Training, Model, etc.
  - Đọc tài liệu về pipeline definition và execution
  - Tìm hiểu về pipeline parameters và property files
  - Nghiên cứu về pipeline DAG và step dependencies
  - Tìm hiểu về cách pipeline lưu trữ và quản lý artifacts
- **Kết quả**:
  - Hiểu rõ về architecture của SageMaker Pipelines
  - Nắm được các loại steps và use cases tương ứng
  - Biết cách định nghĩa pipeline trong Python SDK
  - Hiểu cách tạo và quản lý dependencies giữa các steps
  - Nắm vững cách truyền parameters và artifacts giữa các steps
- **Tools/Tech**:
  - SageMaker Pipelines documentation
  - Python SDK
  - DAG (Directed Acyclic Graph)
  - Pipeline step types
  - Artifact management
  - Pipeline parameters

### 2. Định nghĩa ProcessingStep ⏱️ 10:00-11:15
- **Mô tả**:
  - Import các module cần thiết từ SageMaker SDK
  - Tạo SKLearnProcessor cho data preprocessing
  - Viết preprocessing script cho data cleaning và feature engineering
  - Cấu hình input data sources từ S3
  - Thiết lập output paths cho processed data
  - Cấu hình instance type và count cho processing job
  - Định nghĩa ProcessingStep trong pipeline workflow
- **Kết quả**:
  - ProcessingStep được định nghĩa đầy đủ
  - Preprocessing script hoàn chỉnh với data transformation logic
  - Input và output data paths được cấu hình chính xác
  - Instance type phù hợp với khối lượng dữ liệu
  - Step được thêm vào pipeline với correct dependencies
  - Preprocessing logic được unit tested trước khi integration
- **Tools/Tech**:
  - SKLearnProcessor
  - ProcessingStep definition
  - Script mode programming
  - Data transformation
  - S3 input/output configuration
  - Resource allocation

### 3. Định nghĩa TrainingStep ⏱️ 11:15-12:30
- **Mô tả**:
  - Import Estimator từ SageMaker Python SDK
  - Cấu hình XGBoost estimator với hyperparameters
  - Thiết lập input channels từ ProcessingStep outputs
  - Cấu hình model output path
  - Định nghĩa training resources và instance types
  - Tạo TrainingStep với dependencies to ProcessingStep
  - Configure model evaluation logic trong training script
- **Kết quả**:
  - TrainingStep được định nghĩa với XGBoost estimator
  - Input channels correctly linked to ProcessingStep outputs
  - Model artifacts path được cấu hình đúng
  - Hyperparameters được thiết lập cho bài toán
  - Resource allocation phù hợp với training workload
  - Step dependencies được thiết lập chính xác
- **Tools/Tech**:
  - Estimator configuration
  - TrainingStep definition
  - XGBoost algorithm
  - Hyperparameter settings
  - Step dependencies
  - Model artifacts

### 4. Định nghĩa ModelStep ⏱️ 13:30-14:30
- **Mô tả**:
  - Import Model class từ SageMaker SDK
  - Create model từ TrainingStep output artifacts
  - Configure model environment và code image
  - Setup inference entry point script
  - Define input và output data structure cho inference
  - Tạo ModelStep với dependency to TrainingStep
  - Configure model registration với SageMaker Model Registry
- **Kết quả**:
  - ModelStep được định nghĩa đầy đủ
  - Model correctly linked với training artifacts
  - Inference script được cấu hình cho model serving
  - Input và output data formats được định nghĩa
  - Model registration logic được thiết lập
  - Step dependencies được cấu hình chính xác
- **Tools/Tech**:
  - SageMaker Model definition
  - ModelStep configuration
  - Inference script
  - Model registry
  - Artifact linking
  - Container images

### 5. Xây dựng Pipeline JSON ⏱️ 14:30-15:15
- **Mô tả**:
  - Import Pipeline từ SageMaker Python SDK
  - Combine tất cả steps thành DAG pipeline
  - Add pipeline parameters cho flexibility
  - Define pipeline name và description
  - Generate JSON definition của pipeline
  - Validate pipeline structure và dependencies
  - Add metadata tags cho organization
- **Kết quả**:
  - Pipeline được định nghĩa với tất cả steps
  - Parameters được thiết lập cho reusability
  - Pipeline structure validation thành công
  - JSON definition được generated
  - Pipeline metadata được cấu hình đầy đủ
  - Step dependencies được verified
- **Tools/Tech**:
  - Pipeline definition
  - JSON generation
  - DAG validation
  - Parameter definition
  - Metadata configuration
  - Pipeline structure

### 6. Thêm Conditional Step ⏱️ 15:15-16:00
- **Mô tả**:
  - Import ConditionStep từ SageMaker SDK
  - Define condition expression dựa trên model metrics
  - Create JsonGet để extract metrics từ evaluation output
  - Configure branching logic based on model performance
  - Add RegisterModel step cho successful models
  - Configure failure notification nếu model không đạt threshold
  - Update pipeline definition với conditional logic
- **Kết quả**:
  - ConditionStep được thêm vào pipeline
  - Branching logic based on accuracy threshold
  - Metrics extraction được cấu hình đúng
  - RegisterModel step chỉ chạy khi model đạt yêu cầu
  - Notification được setup cho failed conditions
  - Pipeline structure updated với conditional branching
- **Tools/Tech**:
  - ConditionStep
  - JsonGet for metrics extraction
  - Condition expressions
  - RegisterModel step
  - Branching logic
  - Notification configuration

### 7. Chạy và theo dõi Pipeline ⏱️ 16:00-17:00
- **Mô tả**:
  - Submit pipeline definition để tạo pipeline trong SageMaker
  - Start pipeline execution với input parameters
  - Monitor execution progress trên SageMaker Studio UI
  - Examine logs cho từng step execution
  - Verify artifact generation tại mỗi step
  - Check conditional logic execution
  - Document pipeline performance và results
- **Kết quả**:
  - Pipeline created và executed successfully
  - All steps completed theo expected sequence
  - Artifacts được generated tại mỗi step
  - Conditional logic executed correctly
  - Pipeline execution time là 45 phút
  - Results và metrics được documented
- **Tools/Tech**:
  - Pipeline execution
  - SageMaker Studio UI
  - Step monitoring
  - Log analysis
  - Artifact verification
  - Execution documentation

## 📚 Kiến thức học được

### 🔧 Technical Skills
- **SageMaker Pipelines**:
  - Pipeline structure và architecture
  - Step definitions và dependencies
  - Parameter passing between steps
  - Conditional execution logic
  - Artifact management
  - Pipeline monitoring
- **MLOps Concepts**:
  - End-to-end automation của ML workflows
  - Reproducible experimentation
  - Model evaluation và validation
  - Conditional model registration
  - Pipeline versioning
  - Resource optimization
- **Python SDK**:
  - Pipeline definition trong code
  - JSON generation và validation
  - Dependency configuration
  - Parameter management
  - Error handling trong pipelines
  - Script mode implementation

### 💡 Concepts & Theory
- **ML Workflow Automation**: End-to-end automation của machine learning lifecycles
- **Pipeline DAGs**: Directed acyclic graphs for managing complex workflows
- **Conditional Logic**: Implementing decision points trong automated pipelines
- **Artifact Lineage**: Tracking data và model versions through pipeline
- **Reproducibility**: Ensuring consistent execution environments và results

### 🤝 Soft Skills
- **System Design**: Architecting end-to-end pipeline solutions
- **Documentation**: Creating clear records của pipeline architecture
- **Troubleshooting**: Debugging complex pipeline issues
- **Resource Planning**: Estimating computing needs for pipeline execution

## 🚧 Khó khăn và giải pháp

### Vấn đề 1: Parameter Passing giữa Steps
- **Mô tả**: Khó khăn trong việc truyền dynamic parameters giữa các pipeline steps
- **Impact**: Pipeline execution failed do parameter mismatch
- **Root Cause**: Misunderstanding về JsonGet và property file handling
- **Solution**: Implement JsonPath correctly và validate output structures
- **Result**: Parameters được truyền thành công giữa các steps
- **Lesson**: Test parameter extraction riêng biệt trước khi integrate vào pipeline

### Vấn đề 2: Conditional Logic Execution
- **Mô tả**: ConditionStep không triggering expected branches
- **Impact**: Model registration không xảy ra dù model đạt threshold
- **Root Cause**: Incorrect condition expression format và parameter reference
- **Solution**: Fix condition expression và ensure JsonGet paths chính xác
- **Result**: Conditional branching hoạt động như mong đợi
- **Lesson**: Test conditional expressions riêng biệt và validate JSON structures

## 💭 Reflection & Insights

### What went well today?
- Successfully built end-to-end ML pipeline với multiple steps
- Effective implementation của conditional logic
- Clean integration của tất cả components

### What could be improved?
- Need better error handling trong pipeline steps
- Should implement more comprehensive logging
- Pipeline visualization could be enhanced

### Key Insights
- SageMaker Pipelines significantly reduces manual effort trong ML workflows
- Conditional steps enable intelligent automation based on metrics
- Parameter passing between steps requires careful planning
- Pipeline design should balance complexity và maintainability

### Questions & Curiosities
- Best practices cho versioning ML pipelines?
- How to implement A/B testing within SageMaker Pipelines?
- Strategies cho parallel step execution để optimize performance?
- Integration of custom metrics cho conditional evaluation?

## 📋 Kế hoạch ngày mai

### Priority Tasks
- [ ] **High**: Implement fine-tuning BERT model với Hugging Face
- [ ] **High**: Setup distributed training cho NLP model
- [ ] **Medium**: Configure batch transform jobs cho bulk inference

### Learning Goals
- [ ] Hiểu Hugging Face integration với SageMaker
- [ ] Nắm vững distributed training principles
- [ ] Tìm hiểu về NLP pre-trained models

### Meetings & Deadlines
- [ ] Final project planning meeting
- [ ] Submit pipeline documentation

## 📊 Self Assessment

### Productivity
- **Score**: 9/10
- **Reason**: Completed full pipeline implementation từ design đến execution
- **Improvement**: Need better validation testing trước execution

### Learning
- **Score**: 9/10
- **New Knowledge**: Pipeline architecture, conditional logic, artifact management
- **Application**: Applied MLOps principles vào practical implementation

### Overall Satisfaction
- **Score**: 8/10
- **Highlights**: End-to-end automation của ML workflow
- **Areas for Growth**: Error handling và pipeline monitoring

---
## 📎 Attachments & Links

### Learning Resources
- [ AWS lab](https://www.youtube.com/watch?v=jSA2Vc7lSwU&pp=ygUicGlwZWxpbmUgduG7m2kgU2FnZU1ha2VyIFBpcGVsaW5lcw%3D%3D)

---

*Worklog created by: Chu Tien Binh - FCJ Intern Batch 2025*  
*Next review: 07/07/2025*
