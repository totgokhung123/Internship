# Đa người thuê trong ứng dụng RAG với một Amazon Bedrock Knowledge Base duy nhất thông qua lọc metadata

> **📖 Bài viết gốc**: [Multi-tenancy in RAG applications in a single Amazon Bedrock Knowledge Base with metadata filtering](https://aws.amazon.com/blogs/machine-learning/multi-tenancy-in-rag-applications-in-a-single-amazon-bedrock-knowledge-base-with-metadata-filtering/)  
> **👤 Tác giả**: James Jory và Raju Penmatcha  
> **📅 Ngày xuất bản**: 14/05/2024  
> **🌐 Nguồn**: AWS Blog  
> **👨‍💻 Người dịch**: Chu Tiến Bình - FCJ Intern  
> **📅 Ngày dịch**: 01/07/2025  
> **⏱️ Thời gian đọc**: 12 phút

---

## 📋 Tóm tắt

Bài viết này trình bày cách thiết kế và triển khai ứng dụng RAG (Retrieval-Augmented Generation) đa người thuê sử dụng một Amazon Bedrock Knowledge Base duy nhất, thông qua cơ chế lọc metadata. Cách tiếp cận này cho phép duy trì ranh giới dữ liệu rõ ràng giữa các người thuê khác nhau trong cùng một Knowledge Base, từ đó tối ưu chi phí và đơn giản hóa việc quản lý hạ tầng. Bài viết cung cấp hướng dẫn chi tiết về kiến trúc, mã triển khai và các cân nhắc về bảo mật cho việc xây dựng ứng dụng RAG đa người thuê.

**🎯 Đối tượng đọc**: Kỹ sư phần mềm, Kiến trúc sư giải pháp, Nhà phát triển ứng dụng AI  
**📊 Độ khó**: Intermediate to Advanced  
**🏷️ Tags**: Amazon Bedrock, RAG, Knowledge Base, Multi-tenancy, Metadata Filtering, Generative AI

---

## 📚 Mục lục

- [Đa người thuê trong ứng dụng RAG với một Amazon Bedrock Knowledge Base duy nhất thông qua lọc metadata](#đa-người-thuê-trong-ứng-dụng-rag-với-một-amazon-bedrock-knowledge-base-duy-nhất-thông-qua-lọc-metadata)
  - [📋 Tóm tắt](#-tóm-tắt)
  - [📚 Mục lục](#-mục-lục)
- [Phần 1: Giới thiệu](#phần-1-giới-thiệu)
- [Phần 2: Kiến trúc giải pháp](#phần-2-kiến-trúc-giải-pháp)
  - [Ingestion pipeline](#ingestion-pipeline)
  - [Truy vấn và phục vụ pipeline](#truy-vấn-và-phục-vụ-pipeline)
- [Phần 3: Triển khai](#phần-3-triển-khai)
  - [Môi trường](#môi-trường)
  - [Triển khai CloudFormation stack](#triển-khai-cloudformation-stack)
  - [Cấu hình ứng dụng](#cấu-hình-ứng-dụng)
  - [Thêm dữ liệu ví dụ](#thêm-dữ-liệu-ví-dụ)
  - [Chạy truy vấn](#chạy-truy-vấn)
  - [Dọn dẹp](#dọn-dẹp)
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

# Phần 1: Giới thiệu

Trong thời đại AI tạo sinh, nhiều doanh nghiệp đang triển khai các ứng dụng sử dụng Retrieval-Augmented Generation (RAG) để tạo ra các phản hồi thông minh, chính xác và dựa trên dữ liệu của riêng họ. Khi xây dựng ứng dụng RAG thương mại, đặc biệt là các ứng dụng Software-as-a-Service (SaaS), việc thiết kế và triển khai cơ chế đa người thuê (multi-tenancy) hiệu quả trở thành một yêu cầu quan trọng.

Đa người thuê cho phép một phiên bản duy nhất của ứng dụng phục vụ nhiều khách hàng hoặc "người thuê" (tenants) khác nhau, đồng thời duy trì sự tách biệt dữ liệu thích hợp. Điều này đặc biệt quan trọng trong các ứng dụng RAG, nơi dữ liệu của mỗi người thuê phải được lưu trữ và truy vấn một cách an toàn, không để lộ thông tin sang người thuê khác.

Amazon Bedrock Knowledge Base là một dịch vụ được quản lý giúp tổ chức dễ dàng lưu trữ, quản lý và tìm kiếm dữ liệu của họ, làm cho việc xây dựng ứng dụng RAG trở nên đơn giản hơn. Khi triển khai một ứng dụng RAG đa người thuê, bạn có thể lựa chọn một trong hai cách tiếp cận sau:

1. **Một Knowledge Base cho mỗi người thuê** - Tạo và quản lý một Knowledge Base riêng biệt cho mỗi người thuê.
2. **Một Knowledge Base duy nhất cho tất cả người thuê** - Sử dụng một Knowledge Base duy nhất với cơ chế lọc metadata để phân biệt dữ liệu giữa các người thuê.

Trong bài viết này, chúng tôi sẽ tập trung vào cách tiếp cận thứ hai, sử dụng một Knowledge Base duy nhất cho tất cả người thuê. Cách tiếp cận này có thể cung cấp nhiều lợi ích:

- **Tối ưu hóa chi phí** - Chỉ tạo và quản lý một Knowledge Base duy nhất thay vì nhiều KB riêng biệt.
- **Đơn giản hóa quản lý** - Giảm thiểu số lượng tài nguyên cần quản lý.
- **Tăng hiệu quả vận hành** - Dễ dàng cập nhật, bảo trì và mở rộng một KB duy nhất.

Chúng tôi sẽ triển khai một ứng dụng web đơn giản để minh họa cách sử dụng Amazon Bedrock Knowledge Base trong một kịch bản đa người thuê. Ứng dụng của chúng tôi sẽ sử dụng lọc metadata để đảm bảo mỗi người thuê chỉ có thể truy cập dữ liệu của riêng họ.

# Phần 2: Kiến trúc giải pháp

Hình dưới đây mô tả kiến trúc tổng thể của ứng dụng RAG đa người thuê của chúng tôi:

![Architecture diagram](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/03/26/ML-16728-arch-diagram.png)

Kiến trúc bao gồm hai luồng chính:

1. **Ingestion pipeline** - Quá trình nạp và xử lý dữ liệu
2. **Truy vấn và phục vụ pipeline** - Quá trình xử lý truy vấn người dùng và tạo phản hồi

## Ingestion pipeline

Quá trình nạp dữ liệu bao gồm các bước sau:

1. Người dùng tải lên tài liệu thông qua giao diện người dùng web.
2. Các tệp được lưu trữ trong một Amazon S3 bucket dành riêng.
3. Mỗi tệp được gán một tenant ID duy nhất (hoặc lấy từ thông tin xác thực của người dùng) và được lưu trữ dưới một tiền tố dựa trên tenant ID.
4. Một AWS Lambda function được kích hoạt bởi sự kiện S3 PutObject để xử lý tệp:
   - Nó chia tài liệu thành các phần nhỏ hơn.
   - Thêm metadata bao gồm tenant ID vào mỗi phần.
   - Tải các phần đã chia vào Amazon Bedrock Knowledge Base.

Trong pipeline này, tenant ID được gán như một trường metadata cho mỗi phần tài liệu, cho phép chúng ta phân biệt dữ liệu của các người thuê khác nhau trong cùng một Knowledge Base.

## Truy vấn và phục vụ pipeline

Quá trình truy vấn diễn ra như sau:

1. Người dùng gửi truy vấn thông qua giao diện người dùng web.
2. Tenant ID được lấy từ thông tin xác thực của người dùng.
3. API Gateway nhận yêu cầu và chuyển tiếp đến một AWS Lambda function.
4. Lambda function:
   - Sử dụng tính năng lọc metadata của Amazon Bedrock Knowledge Base để truy vấn chỉ các tài liệu thuộc về tenant cụ thể.
   - Truyền ngữ cảnh được truy xuất đến một mô hình Amazon Bedrock LLM (Claude của Anthropic) để tạo phản hồi.
   - Trả lại phản hồi cho người dùng.

Lọc metadata là thành phần quan trọng nhất cho việc thực hiện đa người thuê. Trong mỗi yêu cầu truy vấn, chúng ta thêm một bộ lọc metadata để đảm bảo rằng chỉ dữ liệu thuộc về tenant hiện tại mới được truy xuất từ Knowledge Base.

# Phần 3: Triển khai

## Môi trường

Để triển khai và kiểm tra ứng dụng này, bạn sẽ cần:

- Một tài khoản AWS với quyền truy cập vào Amazon Bedrock
- AWS CLI được cài đặt và cấu hình
- Git
- Python 3.10 hoặc cao hơn

## Triển khai CloudFormation stack

Bắt đầu bằng cách clone repository mẫu và triển khai CloudFormation stack:

```bash
git clone https://github.com/aws-samples/amazon-bedrock-samples.git
cd amazon-bedrock-samples/multi-tenant-rag-knowledge-base
```

Trước khi triển khai, hãy chắc chắn rằng bạn đã bật Claude và Titan Embeddings trong Amazon Bedrock:

1. Mở [Amazon Bedrock console](https://console.aws.amazon.com/bedrock)
2. Chọn "Model access" từ menu bên trái
3. Chọn "Manage model access"
4. Bật access cho:
   - Anthropic Claude (v2 hoặc cao hơn)
   - Amazon Titan Embeddings
5. Chọn "Save changes"

Bây giờ, triển khai CloudFormation stack:

```bash
aws cloudformation deploy \
  --template-file cloudformation/template.yaml \
  --stack-name multi-tenant-kb-rag \
  --capabilities CAPABILITY_IAM
```

Quá trình triển khai có thể mất 10-15 phút. Stack sẽ tạo ra:

- Một Amazon Bedrock Knowledge Base
- Các S3 bucket cần thiết
- Lambda functions
- API Gateway
- Các tài nguyên hỗ trợ khác

## Cấu hình ứng dụng

Sau khi stack được triển khai, bạn cần cấu hình giao diện ứng dụng web:

```bash
cd web-ui
npm install
```

Tạo một tệp `.env` với nội dung sau:

```
VITE_API_ENDPOINT=$(aws cloudformation describe-stacks --stack-name multi-tenant-kb-rag --query "Stacks[0].Outputs[?OutputKey=='APIEndpoint'].OutputValue" --output text)
```

Chạy ứng dụng web:

```bash
npm run dev
```

Ứng dụng sẽ khả dụng tại http://localhost:5173/

## Thêm dữ liệu ví dụ

Trong ứng dụng web:

1. Chọn một tenant ID (ví dụ: "tenant1") và nhập vào trường Tenant ID.
2. Chọn "Upload Files" và tải lên một số tài liệu PDF hoặc văn bản.
3. Lặp lại với một tenant ID khác (ví dụ: "tenant2") và tải lên các tài liệu khác.

Dữ liệu sẽ được xử lý và thêm vào Knowledge Base với metadata tenant ID tương ứng.

## Chạy truy vấn

Để kiểm tra tính năng đa người thuê:

1. Nhập một tenant ID (ví dụ: "tenant1").
2. Đặt một câu hỏi liên quan đến dữ liệu của tenant đó.
3. Quan sát rằng phản hồi chỉ dựa trên dữ liệu thuộc về tenant đã chọn.
4. Chuyển sang tenant ID khác và đặt câu hỏi tương tự.
5. Xác minh rằng phản hồi chỉ dựa trên dữ liệu của tenant thứ hai.

Các phản hồi sẽ chỉ bao gồm thông tin từ tài liệu thuộc về tenant được chỉ định, chứng minh rằng ranh giới dữ liệu được duy trì.

## Dọn dẹp

Khi bạn đã hoàn thành việc khám phá ứng dụng, hãy dọn dẹp tài nguyên để tránh phát sinh phí:

```bash
aws cloudformation delete-stack --stack-name multi-tenant-kb-rag
```

# Kết luận

Trong bài viết này, chúng tôi đã minh họa cách xây dựng một ứng dụng RAG đa người thuê sử dụng một Amazon Bedrock Knowledge Base duy nhất với lọc metadata. Cách tiếp cận này cho phép bạn:

- Duy trì ranh giới dữ liệu rõ ràng giữa các người thuê
- Tối ưu chi phí bằng cách sử dụng một Knowledge Base duy nhất
- Đơn giản hóa quản lý và vận hành

Khi xây dựng các ứng dụng RAG trong thế giới thực, việc lựa chọn giữa một Knowledge Base duy nhất hoặc nhiều Knowledge Base phụ thuộc vào các yếu tố như:

- Khối lượng dữ liệu mỗi người thuê
- Số lượng người thuê
- Yêu cầu về hiệu suất
- Mức độ cách ly dữ liệu cần thiết
- Ràng buộc về chi phí và vận hành

Đối với nhiều trường hợp sử dụng, đặc biệt là khi số lượng người thuê lớn với khối lượng dữ liệu trung bình hoặc nhỏ mỗi người, cách tiếp cận sử dụng một Knowledge Base duy nhất với lọc metadata như được mô tả trong bài viết này cung cấp sự cân bằng tối ưu giữa hiệu quả, chi phí và bảo mật.

Khi tiếp tục xây dựng và mở rộng ứng dụng RAG của mình, hãy đảm bảo xem xét cẩn thận cơ chế đa người thuê từ giai đoạn thiết kế ban đầu, vì việc thêm tính năng này sau này có thể phức tạp hơn đáng kể.

---

## 📖 Glossary - Thuật ngữ

| English | Tiếng Việt | Định nghĩa |
|---------|------------|------------|
| Multi-tenancy | Đa người thuê | Kiến trúc phần mềm cho phép một phiên bản ứng dụng duy nhất phục vụ nhiều khách hàng/tổ chức |
| Tenant | Người thuê | Một khách hàng hoặc tổ chức sử dụng ứng dụng SaaS |
| Retrieval-Augmented Generation (RAG) | Tạo sinh tăng cường bằng truy xuất | Phương pháp kết hợp khả năng tạo văn bản của LLM với thông tin được truy xuất từ nguồn dữ liệu bên ngoài |
| Knowledge Base | Cơ sở kiến thức | Kho lưu trữ dữ liệu có cấu trúc được tối ưu hóa cho việc truy xuất thông tin |
| Metadata | Metadata | Dữ liệu mô tả về dữ liệu khác, trong trường hợp này dùng để phân biệt dữ liệu của các người thuê |
| Filtering | Lọc | Quá trình giới hạn kết quả truy vấn dựa trên các tiêu chí cụ thể |
| Ingestion pipeline | Pipeline nạp dữ liệu | Quá trình xử lý dữ liệu từ nguồn gốc đến khi lưu trữ trong hệ thống |
| Data isolation | Cách ly dữ liệu | Đảm bảo dữ liệu của một người thuê không thể truy cập bởi người thuê khác |
| Embedding | Vector nhúng | Biểu diễn dữ liệu văn bản dưới dạng vector số nhiều chiều |
| Chunking | Phân đoạn | Quá trình chia tài liệu thành các phần nhỏ hơn để xử lý hiệu quả |

## 🔗 Tài liệu tham khảo

### Tài liệu gốc
- [Multi-tenancy in RAG applications in a single Amazon Bedrock Knowledge Base with metadata filtering](https://aws.amazon.com/blogs/machine-learning/multi-tenancy-in-rag-applications-in-a-single-amazon-bedrock-knowledge-base-with-metadata-filtering/): Bài viết gốc
- [Amazon Bedrock Knowledge Base Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html): Tài liệu về Amazon Bedrock Knowledge Base
- [GitHub repository](https://github.com/aws-samples/amazon-bedrock-samples): Mã nguồn của ứng dụng mẫu

### Tài liệu tiếng Việt
- [AWS Documentation VN](https://aws.amazon.com/vi/): Tài liệu AWS tiếng Việt
- [AWS Generative AI Resources](https://aws.amazon.com/vi/generative-ai/): Tài nguyên về AI tạo sinh của AWS

### Tools và Services
- [Amazon Bedrock](https://aws.amazon.com/bedrock/): Dịch vụ cung cấp các mô hình nền tảng (FMs)
- [Amazon Bedrock Knowledge Base](https://aws.amazon.com/bedrock/knowledge-base/): Dịch vụ cơ sở kiến thức được quản lý
- [AWS Lambda](https://aws.amazon.com/lambda/): Dịch vụ tính toán serverless
- [Amazon S3](https://aws.amazon.com/s3/): Dịch vụ lưu trữ đối tượng

---

## 💬 Ghi chú của người dịch

Trong quá trình dịch bài viết này, tôi đã gặp một số thách thức liên quan đến thuật ngữ kỹ thuật và cấu trúc phức tạp của ứng dụng RAG đa người thuê.

### Challenges trong quá trình dịch
- **Technical Terms**: Nhiều thuật ngữ như "multi-tenancy", "metadata filtering", "RAG" không có từ tương đương chính xác trong tiếng Việt. Tôi đã quyết định giữ nguyên một số thuật ngữ kỹ thuật và cung cấp giải thích trong phần Glossary.
- **Complex Architecture**: Việc diễn đạt kiến trúc phức tạp của hệ thống đòi hỏi phải tìm cách truyền đạt rõ ràng mà vẫn giữ được tính kỹ thuật của nội dung gốc.

### Insights gained
- **Technical Learning**: Tôi đã học được nhiều về cách triển khai ứng dụng RAG đa người thuê và các cân nhắc quan trọng về bảo mật dữ liệu.
- **AWS Services**: Hiểu sâu hơn về cách Amazon Bedrock Knowledge Base hoạt động và cách nó có thể được sử dụng trong các ứng dụng thực tế.

---

## 🤝 Đóng góp và Feedback

Bài dịch này được thực hiện trong khuôn khổ **FCJ Internship Program**. 

**📧 Liên hệ**: [chutienbinh2003@gmail.com]  
**💬 Feedback**: Mọi góp ý để cải thiện chất lượng dịch thuật xin gửi về email trên  
**🔄 Updates**: Bài dịch sẽ được cập nhật dựa trên feedback từ cộng đồng

---

*© 2024 - Bản dịch thuộc về Chu Tiến Bình. Vui lòng credit khi sử dụng.* 