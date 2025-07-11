# Mô hình Llama 4 từ Meta hiện đã có sẵn trong SageMaker JumpStart

> **📖 Bài viết gốc**: [Llama 4 family of models from Meta are now available in SageMaker JumpStart](https://aws.amazon.com/blogs/machine-learning/llama-4-family-of-models-from-meta-are-now-available-in-sagemaker-jumpstart/)  
> **👤 Tác giả**: Fei Huang và Simrat Hundal  
> **📅 Ngày xuất bản**: 10/06/2025  
> **🌐 Nguồn**: AWS Blog  
> **👨‍💻 Người dịch**: Chu Tiến Bình - FCJ Intern  
> **📅 Ngày dịch**: 01/07/2025  
> **⏱️ Thời gian đọc**: 10 phút

---

## 📋 Tóm tắt

Bài viết này thông báo về việc ra mắt các mô hình Llama 4 của Meta trên Amazon SageMaker JumpStart. Những mô hình này đại diện cho thế hệ mới nhất của dòng Llama, với hiệu suất được cải thiện đáng kể trong nhiều tác vụ, bao gồm lập luận, làm việc với kiến thức chuyên ngành, và tuân thủ hướng dẫn. Bài viết hướng dẫn cách dễ dàng triển khai các mô hình Llama 4 trên SageMaker, cùng với các tùy chọn tùy chỉnh và các ví dụ sử dụng thực tế.

**🎯 Đối tượng đọc**: Kỹ sư ML, Nhà phát triển ứng dụng AI, Kiến trúc sư giải pháp  
**📊 Độ khó**: Intermediate  
**🏷️ Tags**: Amazon SageMaker, Llama 4, Meta, Large Language Models, Foundation Models, JumpStart

---

## 📚 Mục lục

- [Mô hình Llama 4 từ Meta hiện đã có sẵn trong SageMaker JumpStart](#mô-hình-llama-4-từ-meta-hiện-đã-có-sẵn-trong-sagemaker-jumpstart)
  - [📋 Tóm tắt](#-tóm-tắt)
  - [📚 Mục lục](#-mục-lục)
- [Phần 1: Giới thiệu về Llama 4](#phần-1-giới-thiệu-về-llama-4)
- [Phần 2: Triển khai và sử dụng Llama 4 trên SageMaker JumpStart](#phần-2-triển-khai-và-sử-dụng-llama-4-trên-sagemaker-jumpstart)
  - [Triển khai thông qua AWS Console](#triển-khai-thông-qua-aws-console)
  - [Triển khai thông qua Studio JumpStart UI](#triển-khai-thông-qua-studio-jumpstart-ui)
  - [Triển khai thông qua SageMaker Python SDK](#triển-khai-thông-qua-sagemaker-python-sdk)
- [Phần 3: Tùy chỉnh và optimizations](#phần-3-tùy-chỉnh-và-optimizations)
- [Kết luận](#kết-luận)
  - [📖 Glossary - Thuật ngữ](#-glossary---thuật-ngữ)
  - [🔗 Tài liệu tham khảo](#-tài-liệu-tham-khảo)
    - [Tài liệu gốc](#tài-liệu-gốc)
    - [Tài liệu tiếng Việt](#tài-liệu-tiếng-việt)
    - [Tools và Services](#tools-và-services)
  - [💬 Ghi chú của người dịch](#-ghi-chú-của-người-dịch)
    - [Challenges trong quá trình dịch](#challenges-trong-quá-trình-dịch)
    - [Insights gained](#insights-gained)
  - [🤝 Đóng góp và Feedback](#-đóng-góp-và-feedback)

---

# Phần 1: Giới thiệu về Llama 4

Meta đã gần đây công bố Llama 4, thế hệ mới nhất của dòng mô hình Llama, với hai kích thước mô hình chính: 8B và 80B tham số. Các mô hình này đã được cải thiện đáng kể về khả năng lập luận, làm việc với kiến thức chuyên ngành, và tuân thủ hướng dẫn. Meta cũng giới thiệu Llama Chat, một bộ mô hình được tối ưu hóa cho hội thoại và các trường hợp sử dụng tương tác.

Theo thông báo của Meta, Llama 4 đã đạt được hiệu suất cao hơn so với các mô hình mã nguồn mở khác có kích thước tương tự và vượt trội so với Llama 3 ở nhiều benchmark. Nó được đào tạo trên một tập dữ liệu lớn hơn và mới hơn, cho phép nó có được kiến thức cập nhật về các sự kiện gần đây.

Các mô hình Llama 4 được triển khai trên Amazon SageMaker JumpStart bao gồm:

1. **Mô hình cơ sở Llama 4 (8B)** - Phù hợp cho các ứng dụng cần mô hình nhỏ gọn nhưng mạnh mẽ
2. **Mô hình Llama 4 Chat (8B)** - Tối ưu cho các ứng dụng hội thoại, với kích thước nhỏ
3. **Mô hình Llama 4 Chat (80B)** - Mô hình hội thoại cao cấp nhất của Meta với hiệu suất vượt trội

SageMaker JumpStart cung cấp cách dễ dàng để triển khai và tinh chỉnh các mô hình Llama 4 trong môi trường bảo mật và có thể mở rộng của AWS. Điều này cho phép các tổ chức tận dụng sức mạnh của các mô hình ngôn ngữ lớn này mà không cần xây dựng cơ sở hạ tầng phức tạp hoặc quản lý các thách thức về quy mô.

Tiếp theo, chúng ta sẽ khám phá cách triển khai và sử dụng các mô hình Llama 4 trên SageMaker JumpStart.

# Phần 2: Triển khai và sử dụng Llama 4 trên SageMaker JumpStart

Có nhiều cách để triển khai các mô hình Llama 4 trên SageMaker JumpStart. Chúng tôi sẽ trình bày ba phương pháp phổ biến nhất: thông qua AWS Console, Studio JumpStart UI, và SageMaker Python SDK.

## Triển khai thông qua AWS Console

1. Đăng nhập vào [AWS Management Console](https://console.aws.amazon.com/) và điều hướng đến SageMaker.
2. Trong phần JumpStart, tìm kiếm "Llama 4".
3. Chọn mô hình Llama 4 mà bạn muốn triển khai.
4. Nhấp vào "Deploy" và cấu hình các tham số triển khai theo nhu cầu của bạn.
5. Đợi vài phút để mô hình được triển khai dưới dạng một endpoint SageMaker.

Sau khi triển khai, bạn có thể sử dụng endpoint này để tạo dự đoán bằng cách gửi các yêu cầu HTTP tới API của endpoint.

## Triển khai thông qua Studio JumpStart UI

1. Mở Amazon SageMaker Studio.
2. Chọn JumpStart từ thanh điều hướng bên trái.
3. Tìm kiếm "Llama 4" trong danh sách mô hình.
4. Chọn mô hình Llama 4 mà bạn muốn triển khai.
5. Nhấp vào "Deploy" và cấu hình các tham số triển khai.
6. Đợi vài phút để mô hình được triển khai.

Sau khi triển khai, bạn có thể tương tác với mô hình thông qua giao diện notebook của SageMaker Studio.

## Triển khai thông qua SageMaker Python SDK

Bạn cũng có thể triển khai các mô hình Llama 4 bằng mã Python, như ví dụ sau:

```python
import sagemaker
from sagemaker.jumpstart.model import JumpStartModel

# Khởi tạo SageMaker session
session = sagemaker.Session()

# Định nghĩa model_id cho Llama 4-8B-Chat
model_id = "meta-textgeneration-llama-4-8b-chat"

# Các tham số triển khai
inference_instance_type = "ml.g5.2xlarge"

# Khởi tạo và triển khai mô hình
model = JumpStartModel(model_id=model_id)
predictor = model.deploy(
    instance_type=inference_instance_type,
    initial_instance_count=1,
    accept_eula=True
)

# Truy vấn mô hình
prompt = "Hãy giải thích khái niệm máy học đơn giản như tôi là một đứa trẻ 10 tuổi."
response = predictor.predict({
    "inputs": prompt,
    "parameters": {
        "max_new_tokens": 512,
        "top_p": 0.9,
        "temperature": 0.6
    }
})

print(response)
```

Với cách tiếp cận này, bạn có thể dễ dàng tích hợp Llama 4 vào các quy trình làm việc ML hiện có của mình hoặc xây dựng các ứng dụng tùy chỉnh.

Sau đây là một ví dụ hoàn chỉnh hơn để triển khai và tương tác với mô hình Llama 4-8B-Chat:

```python
import json
import sagemaker
from sagemaker.jumpstart.model import JumpStartModel

# Khởi tạo SageMaker session
session = sagemaker.Session()

# Định nghĩa model_id cho Llama 4-8B-Chat
model_id = "meta-textgeneration-llama-4-8b-chat"

# Các tham số triển khai
inference_instance_type = "ml.g5.2xlarge"

# Khởi tạo và triển khai mô hình
model = JumpStartModel(model_id=model_id)
predictor = model.deploy(
    instance_type=inference_instance_type,
    initial_instance_count=1,
    accept_eula=True
)

# Hàm tạo đoạn chat
def generate_text(prompt, 
                 max_new_tokens=512, 
                 temperature=0.6, 
                 top_p=0.9):
    
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": max_new_tokens,
            "temperature": temperature,
            "top_p": top_p
        }
    }
    
    response = predictor.predict(payload)
    return response

# Truy vấn mô hình với một prompt đơn giản
prompt = "Hãy giải thích khái niệm máy học đơn giản như tôi là một đứa trẻ 10 tuổi."
response = generate_text(prompt)
print(json.dumps(response, indent=4))

# Truy vấn mô hình với một prompt phức tạp hơn
prompt = """
Viết một đoạn mã Python để phân tích cảm xúc từ một bài đánh giá sản phẩm.
Sử dụng thư viện NLTK hoặc TextBlob và giải thích từng bước của mã.
"""
response = generate_text(prompt, max_new_tokens=1024, temperature=0.7)
print(json.dumps(response, indent=4))

# Dọn dẹp tài nguyên khi không cần nữa
predictor.delete_endpoint()
```

# Phần 3: Tùy chỉnh và optimizations

Khi triển khai các mô hình Llama 4 trên SageMaker, bạn có thể tối ưu hóa hiệu suất và chi phí thông qua một số tùy chỉnh:

**1. Lựa chọn loại instance phù hợp:**
- Đối với Llama 4 8B: ml.g5.2xlarge là đủ cho hầu hết các trường hợp sử dụng.
- Đối với Llama 4 80B: ml.g5.12xlarge hoặc lớn hơn được khuyến nghị.

**2. Sử dụng DeepSpeed:**
SageMaker JumpStart tích hợp DeepSpeed để tối ưu hóa suy luận, giúp giảm độ trễ và tăng thông lượng. Bạn có thể bật DeepSpeed trong tham số triển khai:

```python
model = JumpStartModel(
    model_id=model_id,
    model_version="*",
    env={"ENABLE_DEEPSPEED": "true"}
)
```

**3. Tinh chỉnh Tham số:**
Bạn có thể điều chỉnh các tham số như temperature, top_p, và max_new_tokens để cân bằng giữa sáng tạo và nhất quán trong các phản hồi:

```python
response = predictor.predict({
    "inputs": prompt,
    "parameters": {
        "max_new_tokens": 512,  # Kiểm soát độ dài phản hồi
        "top_p": 0.9,           # Giá trị thấp hơn = ít ngẫu nhiên hơn
        "temperature": 0.6,     # Giá trị thấp hơn = ít sáng tạo hơn
        "top_k": 50,            # Số lượng tokens có khả năng cao nhất để xem xét
    }
})
```

**4. Tinh chỉnh (Fine-tuning):**
Đối với các ứng dụng đặc thù, bạn có thể tinh chỉnh các mô hình Llama 4 trên dữ liệu của riêng mình:

```python
from sagemaker.jumpstart.estimator import JumpStartEstimator

# Định nghĩa model_id và hyperparameters
model_id = "meta-textgeneration-llama-4-8b"
hyperparameters = {
    "epochs": 3,
    "learning_rate": 2e-5,
    "per_device_train_batch_size": 4
}

# Khởi tạo estimator
estimator = JumpStartEstimator(
    model_id=model_id,
    hyperparameters=hyperparameters
)

# Tinh chỉnh mô hình
estimator.fit({"train": "s3://bucket/path/to/training-data"})
```

**5. Inference Endpoints Bền vững:**
Đối với các ứng dụng sản xuất, hãy cân nhắc sử dụng SageMaker Inference Endpoints với auto-scaling để tối ưu hóa chi phí và hiệu suất:

```python
from sagemaker.jumpstart.model import JumpStartModel
from sagemaker.autoscaling.models import AutoScalingConfig

# Tạo cấu hình auto-scaling
autoscaling_config = AutoScalingConfig(
    min_instance_count=1,
    max_instance_count=4,
    scale_in_cooldown_in_seconds=60,
    scale_out_cooldown_in_seconds=60
)

# Khởi tạo và triển khai mô hình với auto-scaling
model = JumpStartModel(model_id=model_id)
predictor = model.deploy(
    instance_type=inference_instance_type,
    initial_instance_count=1,
    accept_eula=True,
    autoscaling_config=autoscaling_config
)
```

# Kết luận

Sự ra mắt của các mô hình Llama 4 trên Amazon SageMaker JumpStart là một bước tiến quan trọng, cho phép các tổ chức dễ dàng tiếp cận các mô hình ngôn ngữ lớn tiên tiến này. Với khả năng lập luận và hiệu suất được cải thiện, các mô hình Llama 4 cung cấp một lựa chọn mạnh mẽ cho nhiều ứng dụng AI, từ các trợ lý ảo đến phân tích văn bản và sinh mã.

SageMaker JumpStart đơn giản hóa toàn bộ quy trình từ triển khai đến sản xuất, cho phép các tổ chức tập trung vào việc xây dựng các ứng dụng có giá trị thay vì quản lý cơ sở hạ tầng phức tạp. Các tính năng như tích hợp DeepSpeed, auto-scaling, và các tùy chọn tinh chỉnh cung cấp sự linh hoạt cần thiết để tối ưu hóa hiệu suất và chi phí.

Khi bắt đầu với Llama 4 trên SageMaker JumpStart, hãy cân nhắc các yêu cầu cụ thể của ứng dụng của bạn, bao gồm độ trễ, thông lượng, và ràng buộc chi phí. Chọn kích thước mô hình và loại instance phù hợp, và tận dụng các tùy chọn tối ưu hóa có sẵn để đạt được hiệu suất tốt nhất cho trường hợp sử dụng của bạn.

---

## 📖 Glossary - Thuật ngữ

| English | Tiếng Việt | Định nghĩa |
|---------|------------|------------|
| Large Language Model (LLM) | Mô hình ngôn ngữ lớn | Mô hình AI được đào tạo trên lượng lớn dữ liệu văn bản |
| Foundation Model | Mô hình nền tảng | Mô hình AI đa năng có thể được điều chỉnh cho nhiều tác vụ khác nhau |
| Fine-tuning | Tinh chỉnh | Quá trình đào tạo thêm một mô hình đã được huấn luyện trước trên dữ liệu cụ thể |
| Inference | Suy luận | Quá trình sử dụng mô hình đã đào tạo để tạo dự đoán |
| Endpoint | Điểm cuối | Dịch vụ triển khai ML có thể nhận các yêu cầu và trả về dự đoán |
| Temperature | Nhiệt độ | Tham số kiểm soát mức độ ngẫu nhiên trong quá trình tạo văn bản |
| Top-p (Nucleus Sampling) | Lấy mẫu Top-p | Kỹ thuật giới hạn lựa chọn từ vựng cho các token tiếp theo |
| DeepSpeed | DeepSpeed | Thư viện tối ưu hóa để tăng tốc đào tạo và suy luận của các mô hình lớn |
| Auto-scaling | Tự động mở rộng | Tính năng tự động điều chỉnh số lượng tài nguyên tính toán dựa trên nhu cầu |
| JumpStart | JumpStart | Thư viện mô hình ML của SageMaker với các mô hình được đào tạo trước |

## 🔗 Tài liệu tham khảo

### Tài liệu gốc
- [Llama 4 family of models from Meta are now available in SageMaker JumpStart](https://aws.amazon.com/blogs/machine-learning/llama-4-family-of-models-from-meta-are-now-available-in-sagemaker-jumpstart/): Bài viết gốc
- [Llama 4 Technical Report](https://ai.meta.com/research/publications/llama-4-technical-report/): Báo cáo kỹ thuật về Llama 4
- [Meta Llama 4 Announcement](https://ai.meta.com/blog/meta-llama-4/): Thông báo chính thức về Llama 4 từ Meta

### Tài liệu tiếng Việt
- [AWS Documentation VN](https://aws.amazon.com/vi/): Tài liệu AWS tiếng Việt
- [Amazon SageMaker Overview](https://aws.amazon.com/vi/sagemaker/): Tổng quan về Amazon SageMaker

### Tools và Services
- [Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker/jumpstart/): Thư viện mô hình ML của SageMaker
- [Amazon SageMaker](https://aws.amazon.com/sagemaker/): Nền tảng ML đầy đủ của AWS
- [DeepSpeed](https://github.com/microsoft/DeepSpeed): Thư viện tối ưu hóa cho các mô hình lớn

---

## 💬 Ghi chú của người dịch

Trong quá trình dịch bài viết này, tôi đã gặp một số thách thức và học hỏi được nhiều điều thú vị về các mô hình ngôn ngữ lớn và cách triển khai chúng trên AWS.

### Challenges trong quá trình dịch
- **Technical Terms**: Nhiều thuật ngữ kỹ thuật như "nucleus sampling", "top-k sampling" không có thuật ngữ tương đương trong tiếng Việt. Tôi đã giữ nguyên một số thuật ngữ và cung cấp giải thích.
- **Code Examples**: Việc duy trì tính rõ ràng của các ví dụ mã trong khi thêm bình luận tiếng Việt đòi hỏi sự cân nhắc cẩn thận.

### Insights gained
- **LLM Evolution**: Tôi đã học được về sự tiến hóa của các mô hình Llama và cách Meta đang cải thiện hiệu suất qua từng thế hệ.
- **Deployment Strategies**: Hiểu rõ hơn về các chiến lược triển khai mô hình ngôn ngữ lớn trên AWS và các tùy chọn tối ưu hóa.

---

## 🤝 Đóng góp và Feedback

Bài dịch này được thực hiện trong khuôn khổ **FCJ Internship Program**. 

**📧 Liên hệ**: [chutienbinh2003@gmail.com]  
**💬 Feedback**: Mọi góp ý để cải thiện chất lượng dịch thuật xin gửi về email trên  
**🔄 Updates**: Bài dịch sẽ được cập nhật dựa trên feedback từ cộng đồng

---

*© 2024 - Bản dịch thuộc về Chu Tiến Bình. Vui lòng credit khi sử dụng.* 