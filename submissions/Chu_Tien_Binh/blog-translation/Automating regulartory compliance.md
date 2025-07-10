# Tự động hóa tuân thủ quy định: Giải pháp đa tác tử sử dụng Amazon Bedrock và CrewAI

> **📖 Bài viết gốc**: [Automating regulatory compliance: A multi-agent solution using Amazon Bedrock and CrewAI](https://aws.amazon.com/vi/blogs/machine-learning/automating-regulatory-compliance-a-multi-agent-solution-using-amazon-bedrock-and-crewai/)  
> **👤 Tác giả**: Balu Mathew - Senior Solutions Architect tại AWS  
> **📅 Ngày xuất bản**: 10/04/2025  
> **🌐 Nguồn**: AWS Machine Learning Blog  
> **👨‍💻 Người dịch**: Chu Tiến Bình - FCJ Intern  
> **📅 Ngày dịch**: 01/07/2024  
> **⏱️ Thời gian đọc**: 20 phút

---

## 📋 Tóm tắt

Bài viết giới thiệu giải pháp tự động hóa tuân thủ quy định cho các tổ chức tài chính bằng cách kết hợp Amazon Bedrock Knowledge Bases với CrewAI - framework điều phối đa tác tử mã nguồn mở. Giải pháp này triển khai ba tác tử AI chuyên biệt: (1) tác tử phân tích tuân thủ giám sát và phân tích các thay đổi quy định, (2) tác tử chuyên gia tuân thủ chuyển đổi yêu cầu thành chính sách tổ chức, và (3) tác tử kiến trúc sư doanh nghiệp thiết kế và triển khai các biện pháp kiểm soát bảo mật cần thiết. Thông qua việc kết hợp CrewAI với Amazon Bedrock, giải pháp tạo ra hệ thống tự động hóa tuân thủ toàn diện giúp tổ chức chuyển từ quy trình xem xét tuân thủ thủ công, tốn thời gian sang phương pháp quản lý tuân thủ tự động, thích ứng với các yêu cầu quy định đang phát triển.

**🎯 Đối tượng đọc**: Kỹ sư ML/AI, kiến trúc sư giải pháp, chuyên gia tuân thủ quy định, chuyên gia tài chính  
**📊 Độ khó**: Intermediate (200)  
**🏷️ Tags**: Amazon Bedrock, CrewAI, Multi-Agent System, Regulatory Compliance, Machine Learning

## 📚 Mục lục

- [Tự động hóa tuân thủ quy định: Giải pháp đa tác tử sử dụng Amazon Bedrock và CrewAI](#tự-động-hóa-tuân-thủ-quy-định-giải-pháp-đa-tác-tử-sử-dụng-amazon-bedrock-và-crewai)
  - [📋 Tóm tắt](#-tóm-tắt)
  - [📚 Mục lục](#-mục-lục)
  - [Tổng quan giải pháp](#tổng-quan-giải-pháp)
  - [Thành phần giải pháp](#thành-phần-giải-pháp)
  - [Điều kiện tiên quyết](#điều-kiện-tiên-quyết)
  - [Các tác tử tuân thủ](#các-tác-tử-tuân-thủ)
  - [Giải quyết thách thức LLM với kiến thức chuyên ngành](#giải-quyết-thách-thức-llm-với-kiến-thức-chuyên-ngành)
    - [Tạo Amazon Bedrock Knowledge Base với thông tin ngữ cảnh từ nguồn dữ liệu của bạn](#tạo-amazon-bedrock-knowledge-base-với-thông-tin-ngữ-cảnh-từ-nguồn-dữ-liệu-của-bạn)
  - [Amazon Bedrock Agents](#amazon-bedrock-agents)
  - [Amazon Bedrock Guardrails](#amazon-bedrock-guardrails)
  - [Tích hợp Amazon Bedrock Agents với CrewAI](#tích-hợp-amazon-bedrock-agents-với-crewai)
  - [Dọn dẹp](#dọn-dẹp)
  - [Kết luận](#kết-luận)
  - [Tổng quan giải pháp](#tổng-quan-giải-pháp-1)
  - [Thành phần giải pháp](#thành-phần-giải-pháp-1)
  - [Điều kiện tiên quyết](#điều-kiện-tiên-quyết-1)
  - [Các tác tử tuân thủ](#các-tác-tử-tuân-thủ-1)
  - [Giải quyết thách thức LLM với kiến thức chuyên ngành](#giải-quyết-thách-thức-llm-với-kiến-thức-chuyên-ngành-1)
    - [Tạo Amazon Bedrock Knowledge Base với thông tin ngữ cảnh từ nguồn dữ liệu của bạn](#tạo-amazon-bedrock-knowledge-base-với-thông-tin-ngữ-cảnh-từ-nguồn-dữ-liệu-của-bạn-1)
  - [Amazon Bedrock Agents](#amazon-bedrock-agents-1)
  - [Tích hợp Amazon Bedrock Agents với CrewAI](#tích-hợp-amazon-bedrock-agents-với-crewai-1)
  - [Dọn dẹp](#dọn-dẹp-1)
  - [Kết luận](#kết-luận-1)
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

Các tổ chức tài chính ngày nay đối mặt với thế giới quy định ngày càng phức tạp đòi hỏi cơ chế tuân thủ mạnh mẽ và hiệu quả. Mặc dù các tổ chức truyền thống thường dành vô số giờ để xem xét các quy định như quy tắc Chống Rửa Tiền (AML) và Đạo luật Bảo mật Ngân hàng (BSA), các giải pháp AI hiện đại mang đến cách tiếp cận đột phá cho thách thức này. Bằng cách sử dụng Amazon Bedrock Knowledge Bases kết hợp với CrewAI - framework điều phối đa tác tử mã nguồn mở, các tổ chức giờ đây có thể triển khai hệ thống thông minh nơi nhiều tác tử AI làm việc cùng nhau để tự động hóa và hợp lý hóa các quy trình tuân thủ cụ thể. Sự kết hợp mạnh mẽ này cho phép các tổ chức tài chính chuyển từ việc xem xét tuân thủ thủ công, tốn thời gian sang cách tiếp cận quản lý tuân thủ được hỗ trợ, được hợp lý hóa và thích ứng với các yêu cầu quy định đang phát triển.

Trong bài viết này, chúng tôi khám phá cách các tác tử AI có thể hợp lý hóa việc tuân thủ và đáp ứng các yêu cầu quy định cho các tổ chức tài chính bằng cách sử dụng Amazon Bedrock và CrewAI. Chúng tôi sẽ hướng dẫn cách xây dựng hệ thống đa tác tử có thể tự động tóm tắt các quy định mới, đánh giá tác động của chúng đến hoạt động kinh doanh và cung cấp hướng dẫn kỹ thuật theo quy định. Bạn sẽ học cách sử dụng Amazon Bedrock Knowledge Bases và Amazon Bedrock Agents với CrewAI để tạo ra giải pháp tuân thủ tự động, toàn diện.

Kiến trúc của giải pháp này có thể được điều chỉnh để giúp các hệ thống chăm sóc sức khỏe, hỗ trợ các nhà sản xuất duy trì tài liệu an toàn ISO và hỗ trợ các nhà bán lẻ giám sát các quy định quảng cáo của Ủy ban Thương mại Liên bang (FTC). Nó cũng có thể hỗ trợ trong các lĩnh vực khác như pháp lý, tài chính hoặc nhân sự, mang lại tiềm năng rộng lớn cho việc tự động hóa quy trình và tăng hiệu quả trên nhiều ngành công nghiệp khác nhau. Mã nguồn sử dụng cho bài đăng này có sẵn trên [GitHub](https://github.com/aws-samples/sample-compliance-assistant-with-agents).

## Tổng quan giải pháp

Các ứng dụng mô hình ngôn ngữ lớn (LLM) truyền thống rất giỏi trong việc tuân theo các hướng dẫn định sẵn, nhưng giải quyết các thách thức phức tạp như tự động hóa tuân thủ đòi hỏi một mạng lưới tự trị của các tác tử chuyên biệt phản ánh cấu trúc của một bộ phận tuân thủ toàn diện. Hệ thống của chúng tôi sử dụng ba tác tử chính:

1. Tác tử phân tích tuân thủ liên tục giám sát và phân tích các thay đổi quy định
2. Tác tử chuyên gia tuân thủ chuyển đổi các yêu cầu thành chính sách tổ chức
3. Tác tử kiến trúc sư doanh nghiệp thiết kế và triển khai các biện pháp kiểm soát bảo mật cần thiết

Trong cách tiếp cận đa tác tử này, các tác tử AI chuyên biệt làm việc cùng nhau một cách liền mạch để hợp lý hóa vòng đời tuân thủ. Tác tử phân tích tuân thủ thu thập các thay đổi quy định mới nhất và giúp đi trước các thay đổi quy định và tác động tiềm ẩn của chúng, trong khi tác tử chuyên gia tuân thủ chuyển dịch các yêu cầu quy định này thành các quy trình tổ chức có thể hành động. Đồng thời, tác tử kiến trúc sư doanh nghiệp đảm bảo rằng các biện pháp kiểm soát kỹ thuật phù hợp với các biện pháp kiểm soát tổ chức. CrewAI cung cấp framework mã nguồn mở để điều phối hệ thống cộng tác này, cho phép các tác tử này làm việc phối hợp trong khi duy trì sự bàn giao rõ ràng và trách nhiệm giải trình. Tiếp theo, chúng ta sẽ khám phá cách tạo hệ thống tự động hóa tuân thủ đa tác tử này bằng cách sử dụng CrewAI.

Mặc dù giải pháp này thể hiện khả năng của CrewAI, nhưng điều quan trọng cần lưu ý là Amazon Bedrock Agents có hỗ trợ tích hợp cho hợp tác đa tác tử và các tổ chức có thể triển khai quy trình tác tử của họ hoàn toàn trong Amazon Bedrock Agents. Tuy nhiên, chúng tôi đã chọn CrewAI cho bản demo này để thể hiện cách các framework mã nguồn mở có thể mở rộng khả năng của Amazon Bedrock trong khi vẫn duy trì bảo mật cấp doanh nghiệp thông qua Bedrock Guardrails.

## Thành phần giải pháp

Giải pháp này chỉ cho bạn cách kết hợp nhiều khả năng. Nó chỉ cách:

1. Phát triển giải pháp đa tác tử sử dụng framework CrewAI
2. Làm phong phú giải pháp bằng dữ liệu chuyên ngành sử dụng Amazon Bedrock Knowledge Bases
3. Bảo vệ ứng dụng AI tạo sinh bằng Amazon Bedrock Guardrails
4. Kết hợp tất cả bằng CrewAI và Amazon Bedrock Agents

Bạn có thể sử dụng CrewAI để phát triển các tác tử AI và điều phối nhiệm vụ giữa các tác tử đó. Cấu trúc này cho phép quản lý có hệ thống các quy trình AI phức tạp trong khi vẫn duy trì giám sát tương tác và kết quả của tác tử. Framework có các thành phần sau, được hiển thị trong hình dưới đây:

![CrewAI Framework Components](./images/crewai-framework-components.png)

Framework CrewAI được xây dựng dựa trên các thành phần sau:

* **Agents** (Tác tử) trong CrewAI là các thành phần tự trị được thiết kế để thực hiện các nhiệm vụ hoặc vai trò cụ thể trong hệ thống đa tác tử. Chúng có các vai trò cụ thể (như nhà nghiên cứu hoặc người viết) và đưa ra quyết định tự chủ với hoặc không sử dụng các công cụ bên ngoài. LLMs là trí thông minh cốt lõi đằng sau các tác tử CrewAI. LLMs cho phép các tác tử hiểu ngữ cảnh, đưa ra quyết định và tạo ra phản hồi giống con người.
* **Tasks** (Nhiệm vụ) là các công việc được định nghĩa được giao cho các tác tử với mục tiêu rõ ràng, bao gồm chi tiết thực hiện và tài nguyên cần thiết.
* **Crews** (Đội) là các nhóm tác tử phối hợp làm việc cùng nhau vì mục tiêu chung. Crews yêu cầu xác định vai trò tác tử, phân công nhiệm vụ và thứ tự thực hiện.
* **Tools** (Công cụ) đề cập đến các kỹ năng hoặc chức năng mà tác tử có thể sử dụng để thực hiện các hành động khác nhau.
* **Processes** (Quy trình) chịu trách nhiệm điều phối cách thức thực hiện nhiệm vụ bởi các tác tử, tương tự như quản lý dự án trong các nhóm con người. Các quy trình này đảm bảo rằng nhiệm vụ được phân bổ và hoàn thành một cách hiệu quả, theo chiến lược được xác định trước.

## Điều kiện tiên quyết

Trước khi bắt đầu với giải pháp, bạn cần truy cập các mô hình Amazon Bedrock:
1. Đăng nhập vào bảng điều khiển Amazon Bedrock và trong bảng điều hướng dưới **Bedrock configurations**, chọn **Model access** để yêu cầu truy cập các mô hình Amazon Bedrock. Bước này được hiển thị trong ảnh chụp màn hình sau.

![Amazon Bedrock Model Access](./images/bedrock-model-access.png)
Trong ví dụ này, chúng tôi sử dụng Amazon Nova Pro thông qua Amazon Bedrock làm LLM. CrewAI cung cấp tích hợp tích hợp sẵn với Amazon Bedrock.
2. Clone GitHub repo vào thư mục cục bộ

```
git clone https://github.com/aws-samples/sample-compliance-assistant-with-agents.git
```

3. Sử dụng lệnh sau để cài đặt các phụ thuộc để chạy CrewAI trong môi trường Python của bạn:

```
pip install crewai uv
```

## Các tác tử tuân thủ

Trong bước này, bạn sẽ định nghĩa các tác tử của mình:

1. Định nghĩa các tác tử tuân thủ trong tệp `agents.yaml`. Mỗi tác tử có vai trò cụ thể:

```yaml
compliance_analyst:
  role: {topic} Senior Compliance Analyst
  goal: Review and understand regulatory and compliance requirements around {topic}
  backstory: You're a seasoned Compliance analyst with deep expertise in areas such as PCI DSS, HIPAA, NIST, ISO and knack for uncovering the latest regulations and requirements in {topic}.
compliance_specialist:
  role: {topic} Compliance Specialist
  goal: Create detailed reports based on {topic} compliance analysis and research findings
  backstory: You're a meticulous compliance specialist with deep understanding of compliance and regulatory landscape for Financial services and Technology Industry. You create standards and policies for the organization to meet regulations and compliance needs.
```

2. Định nghĩa nhiệm vụ cho các tác tử:

```yaml
compliance_analysis_task:
  description: Conduct a thorough analysis about {topic}. Make sure you find relevant information given the current year is {current_year}.
  expected_output: A list with 10 bullet points of the most relevant information about {topic}
  agent: compliance_analyst
compliance_reporting_task:
  description: Review the context you got and expand each topic into a full section for a report.
    Make sure the report is detailed and contains any and all relevant information for Financial Services Organization
  expected_output: A fully fledged report with the main topics, each with a full section of information.
  agent: compliance_specialist
```
3. Các bước thực thi và quy trình được định nghĩa trong `crew.py`:

```python
def crew(self) -> Crew:
"""Creates the Compliance Automation crew"""
    return Crew(
       agents=self.agents,
       tasks=self.tasks,
       process=Process.sequential,
       verbose=True)
```
4. Định nghĩa LLM, chủ đề và tham số thời gian chạy trong tệp `.env`:

```
MODEL=bedrock/us.amazon.nova-pro-v1:0
AWS_REGION_NAME=us-west-2
TOPIC='GDPR requirements for Data Privacy'
```
5. Chạy crew như sau:

```
crewai run
```
6. Bản demo sau đây cho thấy đầu ra của crew. Bạn có thể thấy các tác tử cộng tác để tạo ra một giải pháp chi tiết:

![Compliance Agents - Topic GDPR](./images/compliance-agents-gdpr.png)
Trong đầu ra, lưu ý rằng nhà phân tích tuân thủ và chuyên gia tuân thủ đang làm việc cùng nhau để giải quyết nhiều khía cạnh của yêu cầu Quy định Bảo vệ Dữ liệu Chung (GDPR) cho dịch vụ giao dịch. Chú ý đến sự cộng tác hiệp trợ giữa các tác tử khi họ tinh chỉnh cách tiếp cận và phát triển phản hồi quản lý tuân thủ toàn diện thông qua giải quyết vấn đề lặp đi lặp lại.

## Giải quyết thách thức LLM với kiến thức chuyên ngành

LLMs, mặc dù ấn tượng trong kiến thức rộng của chúng, đối mặt với hai hạn chế chính khi xử lý các lĩnh vực chuyên môn hoặc thông tin gần đây. Đầu tiên, chúng gặp khó khăn với thông tin chuyên biệt dành riêng cho tổ chức của bạn. Thứ hai, vì kiến thức của chúng bị giới hạn trong dữ liệu đào tạo, chúng có thể không phản ánh những cập nhật mới nhất trong các lĩnh vực thay đổi nhanh chóng. Hạn chế này trở nên đặc biệt quan trọng khi xử lý các yêu cầu tuân thủ đang phát triển, chẳng hạn như Tiêu chuẩn Bảo mật Dữ liệu Ngành Thẻ thanh toán (PCI DSS), GDPR, quy tắc AML và quy định Hiểu biết về Khách hàng (KYC). Ngoài ra, các tổ chức cần các giải pháp được tùy chỉnh theo yêu cầu tuân thủ cụ thể và tiêu chuẩn nội bộ của họ, thay vì các phản hồi chung từ LLMs.

Retrieval Augmented Generation (RAG) là một kỹ thuật cho phép các mô hình AI tạo sinh truy xuất và kết hợp thông tin tổ chức và chuyên ngành hiện tại từ các cơ sở dữ liệu bên ngoài. Amazon Bedrock Knowledge Base là một khả năng được quản lý giúp bạn triển khai toàn bộ kỹ thuật RAG mà không cần phải xây dựng tích hợp tùy chỉnh với các nguồn dữ liệu và quản lý luồng dữ liệu. Bằng cách kết hợp cơ sở tri thức chứa các ấn phẩm mới nhất, cập nhật quy định và hướng dẫn tuân thủ từ các nguồn có thẩm quyền như NIST, ISO, PCI và các cơ quan quản lý, Amazon Bedrock Knowledge Bases giúp đảm bảo rằng hệ thống AI của bạn luôn cập nhật với các yêu cầu tuân thủ mới nhất. Trong quá trình tạo prompt, RAG đầu tiên truy xuất dữ liệu liên quan từ cơ sở tri thức liên tục cập nhật này, sau đó sử dụng nó để tạo ra phản hồi thông báo. Điều này giúp cung cấp phản hồi phù hợp hơn, chính xác hơn và được tùy chỉnh phù hợp với các tiêu chuẩn quy định và tổ chức hiện hành. Ví dụ, khi truy vấn về yêu cầu PCI DSS v4.0 hoặc các sửa đổi GDPR gần đây, hệ thống có thể lấy thông tin cập nhật nhất trực tiếp từ các nguồn có thẩm quyền thay vì dựa vào dữ liệu đào tạo có thể đã lỗi thời.

### Tạo Amazon Bedrock Knowledge Base với thông tin ngữ cảnh từ nguồn dữ liệu của bạn

1. Từ bảng điều hướng Amazon Bedrock, chọn **Knowledge Bases** dưới **Builder tools** và chọn **a Knowledge Base with vector store**.
2. Cung cấp **Knowledge Base name** và **Data source details**. Bạn sẽ sử dụng web crawler để thu thập dữ liệu.
3. Web crawler được cung cấp bởi Amazon Bedrock kết nối và thu thập các URL bạn đã chọn để sử dụng trong Amazon Bedrock knowledge base. Thêm URL làm nguồn dữ liệu trong **Source URLs**.
4. Chọn mô hình cho embeddings. Chúng tôi đã chọn Amazon Titan Text Embeddings v2, như hình chụp màn hình dưới đây.

![Knowledge Base Configuration](./images/kb-configuration.png)
Sau vài phút, knowledge base sẽ sẵn sàng. Sau khi đã đồng bộ hóa, Amazon Bedrock Knowledge Bases xử lý việc tạo, chạy và định dạng kết quả của truy vấn, đơn giản hóa việc xây dựng giao diện ngôn ngữ tự nhiên cho dữ liệu có cấu trúc.

## Amazon Bedrock Agents

Amazon Bedrock Agents là môi trường toàn diện để xây dựng hệ thống tác tử AI phức tạp. Về cốt lõi, nó cho phép hợp tác đa tác tử liền mạch và duy trì ngữ cảnh hội thoại thông qua khả năng ghi nhớ gốc xuyên suốt các tương tác. Amazon Bedrock Agents tích hợp tự nhiên với cơ sở tri thức và thực thi bảo mật thông qua guardrails tích hợp sẵn. Đối với giải pháp này, chúng tôi tập trung vào hai khả năng chính: tính năng RAG, cho phép các tác tử truy cập và sử dụng thông tin từ cơ sở tri thức, và các tính năng bảo mật được cung cấp thông qua Amazon Bedrock Guardrails. Các guardrails này đóng vai trò là biện pháp bảo vệ thiết yếu cho ứng dụng AI tạo sinh của bạn, thúc đẩy tương tác AI có trách nhiệm và an toàn.

1. Để tạo tác tử, từ bảng điều hướng Amazon Bedrock dưới **Builder tools**, chọn **Agents** và chọn **Create Agent**.
2. Dưới **Agent details**, chọn mô hình. Chúng tôi sử dụng Amazon Nova Pro cho trường hợp sử dụng của chúng tôi, như trong ảnh chụp màn hình sau.

![Agent Model Selection](./images/agent-model.png)
3. Dưới **Knowledge Bases**, thêm knowledge base vào tác tử của bạn.
4. Chọn tên knowledge base từ danh sách thả xuống, như trong ảnh chụp màn hình sau.

![Add Knowledge Base to Agent](./images/add-kb-to-agent.png)
## Amazon Bedrock Guardrails

Amazon Bedrock Guardrails cung cấp các kiểm soát an toàn giúp duy trì việc sử dụng AI có trách nhiệm bằng cách cung cấp một lớp bảo mật. Guardrails cung cấp lọc nội dung để giám sát và lọc đầu ra của mô hình AI để giúp ngăn chặn nội dung có hại, không phù hợp hoặc thiên vị. Bạn có thể thiết lập bộ lọc cho những thứ như phát ngôn thù địch, nội dung rõ ràng hoặc thông tin nhận dạng cá nhân (PII). Bạn cũng có thể áp dụng các quy tắc có thể tùy chỉnh và xác thực đầu vào/đầu ra.

1. Bạn có thể tìm thấy **Guardrails** trong bảng điều hướng Amazon Bedrock dưới **Safeguards**. Chọn **Create guardrail** và cung cấp tên guardrail
2. Như được hiển thị trong ảnh chụp màn hình sau, chọn bộ lọc nội dung bạn muốn triển khai cho ứng dụng dựa trên Amazon Bedrock của mình

![Content Filters](./images/content-filters.png)

3. Thêm chủ đề bị từ chối với các ví dụ cụ thể
4. Sau khi bạn đã tạo guardrail, gắn guardrail vào tác tử.

## Tích hợp Amazon Bedrock Agents với CrewAI

CrewAI cung cấp tích hợp liền mạch với các tính năng của Amazon Bedrock, bao gồm Amazon Bedrock Knowledge Bases và Amazon Bedrock Agents thông qua chức năng công cụ CrewAI. Khi các công cụ này được kích hoạt từ các tác tử CrewAI, chúng xử lý truy vấn của bạn, truy xuất thông tin liên quan từ Amazon Bedrock knowledge base và trả về phản hồi cho tác tử CrewAI.

1. Tham khảo mã mẫu thể hiện công cụ CrewAI cho Amazon Bedrock Agent. Bạn cần định nghĩa Amazon Bedrock AgentId và Alias của mình làm tham số trong tệp .env.
2. Thực thi crew một lần nữa với Amazon Bedrock Agents:

```
crewai run
```

3. Bạn có thể tìm thấy đầu ra được tạo bên dưới:

![PCI Compliance Output](./images/compliance-agents-pci.png)

Khi bạn thực thi crew, tác tử phân tích tuân thủ bắt đầu quy trình bằng cách gọi công cụ Bedrock CrewAI để trích xuất các yêu cầu quy định từ Amazon Bedrock Knowledge Bases, sau đó được chuyển đổi liền mạch thành các yêu cầu kỹ thuật bởi tác tử chuyên gia tuân thủ. Thông qua sự cộng tác lặp đi lặp lại, các tác tử chuyên biệt này làm việc cùng nhau để lấp đầy khoảng trống thông tin, và tác tử kiến trúc sư doanh nghiệp tổng hợp các thông tin thu thập được để phát triển chiến lược triển khai mạnh mẽ và kế hoạch thực hiện. Quy trình hợp lý này thể hiện cách nhiều tác tử AI có thể phối hợp hiệu quả để chuyển đổi các yêu cầu tuân thủ thành các giải pháp kỹ thuật có thể hành động.

## Dọn dẹp

Để tránh phí liên tục, hãy làm theo các bước này để dọn dẹp tài nguyên:

1. Xóa Amazon Bedrock knowledge base bạn đã tạo:

```
aws bedrock-agent delete-knowledge-base --knowledge-base-id <your-kb-id>
```

2. Xóa Amazon Bedrock agents bạn đã tạo:

```
aws bedrock-agent delete-agent --agent-id <your-agent-id>
```

## Kết luận

Trong bài viết này, chúng tôi đã trình bày cách:

* Xây dựng hệ thống AI đa tác tử sử dụng CrewAI mô phỏng cấu trúc của bộ phận tuân thủ toàn diện với các tác tử chuyên biệt cho các chức năng khác nhau
* Nâng cao phản hồi AI với kiến thức chuyên ngành bằng cách triển khai RAG sử dụng Amazon Bedrock Knowledge Bases
* Bảo vệ ứng dụng AI tạo sinh với Amazon Bedrock Guardrails để giúp ngăn chặn nội dung có hại, không phù hợp hoặc thiên vị
* Tạo công cụ tùy chỉnh trong CrewAI để tích hợp với Amazon Bedrock Agents cho các giải pháp tuân thủ mạnh mẽ hơn và nhận biết ngữ cảnh
* Tự động hóa toàn bộ vòng đời tuân thủ từ giám sát các thay đổi quy định đến triển khai các biện pháp kiểm soát kỹ thuật mà không cần nỗ lực thủ công rộng rãi
* Triển khai giải pháp sẵn sàng cho sản xuất liên tục thích ứng với các yêu cầu quy định phát triển trong các ngành dịch vụ tài chính và các ngành được quản lý cao khác

Giải pháp này kết hợp Amazon Bedrock Knowledge Bases và CrewAI để tạo ra hệ thống AI đa tác tử thông minh giúp hợp lý hóa các nhiệm vụ tuân thủ quy định. Với triển khai RAG đơn giản hóa, quy trình làm việc phức tạp phản ánh các nhóm con người và thích ứng nhanh hơn với các quy định mới, cách tiếp cận này cho thấy cách AI có thể hỗ trợ các tổ chức đối với các khía cạnh cụ thể của các yêu cầu quy định phức tạp.

Giải pháp này đóng vai trò là điểm khởi đầu thực tế cho các tổ chức muốn nâng cao quy trình tuân thủ của họ với khả năng AI, thể hiện cách các hệ thống thông minh có thể bổ sung và hợp lý hóa quy trình tuân thủ hiện có. Mã nguồn hoàn chỉnh cho dự án này có sẵn trên kho lưu trữ [GitHub](https://github.com/aws-samples/sample-compliance-assistant-with-agents). Hãy thoải mái khám phá, fork hoặc đóng góp!

---

Các tổ chức tài chính ngày nay đối mặt với thế giới quy định ngày càng phức tạp đòi hỏi cơ chế tuân thủ mạnh mẽ và hiệu quả. Mặc dù các tổ chức truyền thống thường dành vô số giờ để xem xét các quy định như quy tắc Chống Rửa Tiền (AML) và Đạo luật Bảo mật Ngân hàng (BSA), các giải pháp AI hiện đại mang đến cách tiếp cận đột phá cho thách thức này. Bằng cách sử dụng Amazon Bedrock Knowledge Bases kết hợp với CrewAI - framework điều phối đa tác tử mã nguồn mở, các tổ chức giờ đây có thể triển khai hệ thống thông minh nơi nhiều tác tử AI làm việc cùng nhau để tự động hóa và hợp lý hóa các quy trình tuân thủ cụ thể. Sự kết hợp mạnh mẽ này cho phép các tổ chức tài chính chuyển từ việc xem xét tuân thủ thủ công, tốn thời gian sang cách tiếp cận quản lý tuân thủ được hỗ trợ, được hợp lý hóa và thích ứng với các yêu cầu quy định đang phát triển.

Trong bài viết này, chúng tôi khám phá cách các tác tử AI có thể hợp lý hóa việc tuân thủ và đáp ứng các yêu cầu quy định cho các tổ chức tài chính bằng cách sử dụng Amazon Bedrock và CrewAI. Chúng tôi sẽ hướng dẫn cách xây dựng hệ thống đa tác tử có thể tự động tóm tắt các quy định mới, đánh giá tác động của chúng đến hoạt động kinh doanh và cung cấp hướng dẫn kỹ thuật theo quy định. Bạn sẽ học cách sử dụng Amazon Bedrock Knowledge Bases và Amazon Bedrock Agents với CrewAI để tạo ra giải pháp tuân thủ tự động, toàn diện.

Kiến trúc của giải pháp này có thể được điều chỉnh để giúp các hệ thống chăm sóc sức khỏe, hỗ trợ các nhà sản xuất duy trì tài liệu an toàn ISO và hỗ trợ các nhà bán lẻ giám sát các quy định quảng cáo của Ủy ban Thương mại Liên bang (FTC). Nó cũng có thể hỗ trợ trong các lĩnh vực khác như pháp lý, tài chính hoặc nhân sự, mang lại tiềm năng rộng lớn cho việc tự động hóa quy trình và tăng hiệu quả trên nhiều ngành công nghiệp khác nhau. Mã nguồn sử dụng cho bài đăng này có sẵn trên [GitHub](https://github.com/aws-samples/sample-compliance-assistant-with-agents).

## Tổng quan giải pháp

Các ứng dụng mô hình ngôn ngữ lớn (LLM) truyền thống rất giỏi trong việc tuân theo các hướng dẫn định sẵn, nhưng giải quyết các thách thức phức tạp như tự động hóa tuân thủ đòi hỏi một mạng lưới tự trị của các tác tử chuyên biệt phản ánh cấu trúc của một bộ phận tuân thủ toàn diện. Hệ thống của chúng tôi sử dụng ba tác tử chính:

1. Tác tử phân tích tuân thủ liên tục giám sát và phân tích các thay đổi quy định
2. Tác tử chuyên gia tuân thủ chuyển đổi các yêu cầu thành chính sách tổ chức
3. Tác tử kiến trúc sư doanh nghiệp thiết kế và triển khai các biện pháp kiểm soát bảo mật cần thiết

Trong cách tiếp cận đa tác tử này, các tác tử AI chuyên biệt làm việc cùng nhau một cách liền mạch để hợp lý hóa vòng đời tuân thủ. Tác tử phân tích tuân thủ thu thập các thay đổi quy định mới nhất và giúp đi trước các thay đổi quy định và tác động tiềm ẩn của chúng, trong khi tác tử chuyên gia tuân thủ chuyển dịch các yêu cầu quy định này thành các quy trình tổ chức có thể hành động. Đồng thời, tác tử kiến trúc sư doanh nghiệp đảm bảo rằng các biện pháp kiểm soát kỹ thuật phù hợp với các biện pháp kiểm soát tổ chức. CrewAI cung cấp framework mã nguồn mở để điều phối hệ thống cộng tác này, cho phép các tác tử này làm việc phối hợp trong khi duy trì sự bàn giao rõ ràng và trách nhiệm giải trình. Tiếp theo, chúng ta sẽ khám phá cách tạo hệ thống tự động hóa tuân thủ đa tác tử này bằng cách sử dụng CrewAI.

Mặc dù giải pháp này thể hiện khả năng của CrewAI, nhưng điều quan trọng cần lưu ý là Amazon Bedrock Agents có hỗ trợ tích hợp cho hợp tác đa tác tử và các tổ chức có thể triển khai quy trình tác tử của họ hoàn toàn trong Amazon Bedrock Agents. Tuy nhiên, chúng tôi đã chọn CrewAI cho bản demo này để thể hiện cách các framework mã nguồn mở có thể mở rộng khả năng của Amazon Bedrock trong khi vẫn duy trì bảo mật cấp doanh nghiệp thông qua Bedrock Guardrails.

## Thành phần giải pháp

Giải pháp này chỉ cho bạn cách kết hợp nhiều khả năng. Nó chỉ cách:

1. Phát triển giải pháp đa tác tử sử dụng framework CrewAI
2. Làm phong phú giải pháp bằng dữ liệu chuyên ngành sử dụng Amazon Bedrock Knowledge Bases
3. Bảo vệ ứng dụng AI tạo sinh bằng Amazon Bedrock Guardrails
4. Kết hợp tất cả bằng CrewAI và Amazon Bedrock Agents

Bạn có thể sử dụng CrewAI để phát triển các tác tử AI và điều phối nhiệm vụ giữa các tác tử đó. Cấu trúc này cho phép quản lý có hệ thống các quy trình AI phức tạp trong khi vẫn duy trì giám sát tương tác và kết quả của tác tử. Framework có các thành phần sau, được hiển thị trong hình dưới đây:

![CrewAI Framework Components](./images/crewai-framework-components.png)

Framework CrewAI được xây dựng dựa trên các thành phần sau:

* **Agents** (Tác tử) trong CrewAI là các thành phần tự trị được thiết kế để thực hiện các nhiệm vụ hoặc vai trò cụ thể trong hệ thống đa tác tử. Chúng có các vai trò cụ thể (như nhà nghiên cứu hoặc người viết) và đưa ra quyết định tự chủ với hoặc không sử dụng các công cụ bên ngoài. LLMs là trí thông minh cốt lõi đằng sau các tác tử CrewAI. LLMs cho phép các tác tử hiểu ngữ cảnh, đưa ra quyết định và tạo ra phản hồi giống con người.
* **Tasks** (Nhiệm vụ) là các công việc được định nghĩa được giao cho các tác tử với mục tiêu rõ ràng, bao gồm chi tiết thực hiện và tài nguyên cần thiết.
* **Crews** (Đội) là các nhóm tác tử phối hợp làm việc cùng nhau vì mục tiêu chung. Crews yêu cầu xác định vai trò tác tử, phân công nhiệm vụ và thứ tự thực hiện.
* **Tools** (Công cụ) đề cập đến các kỹ năng hoặc chức năng mà tác tử có thể sử dụng để thực hiện các hành động khác nhau.
* **Processes** (Quy trình) chịu trách nhiệm điều phối cách thức thực hiện nhiệm vụ bởi các tác tử, tương tự như quản lý dự án trong các nhóm con người. Các quy trình này đảm bảo rằng nhiệm vụ được phân bổ và hoàn thành một cách hiệu quả, theo chiến lược được xác định trước.

## Điều kiện tiên quyết

Trước khi bắt đầu với giải pháp, bạn cần truy cập các mô hình Amazon Bedrock:
1. Đăng nhập vào bảng điều khiển Amazon Bedrock và trong bảng điều hướng dưới **Bedrock configurations**, chọn **Model access** để yêu cầu truy cập các mô hình Amazon Bedrock. Bước này được hiển thị trong ảnh chụp màn hình sau.

![Amazon Bedrock Model Access](./images/bedrock-model-access.png)
Trong ví dụ này, chúng tôi sử dụng Amazon Nova Pro thông qua Amazon Bedrock làm LLM. CrewAI cung cấp tích hợp tích hợp sẵn với Amazon Bedrock.
2. Clone GitHub repo vào thư mục cục bộ

```
git clone https://github.com/aws-samples/sample-compliance-assistant-with-agents.git
```

3. Sử dụng lệnh sau để cài đặt các phụ thuộc để chạy CrewAI trong môi trường Python của bạn:

```
pip install crewai uv
```

## Các tác tử tuân thủ

Trong bước này, bạn sẽ định nghĩa các tác tử của mình:

1. Định nghĩa các tác tử tuân thủ trong tệp `agents.yaml`. Mỗi tác tử có vai trò cụ thể:

```yaml
compliance_analyst:
  role: {topic} Senior Compliance Analyst
  goal: Review and understand regulatory and compliance requirements around {topic}
  backstory: You're a seasoned Compliance analyst with deep expertise in areas such as PCI DSS, HIPAA, NIST, ISO and knack for uncovering the latest regulations and requirements in {topic}.
compliance_specialist:
  role: {topic} Compliance Specialist
  goal: Create detailed reports based on {topic} compliance analysis and research findings
  backstory: You're a meticulous compliance specialist with deep understanding of compliance and regulatory landscape for Financial services and Technology Industry. You create standards and policies for the organization to meet regulations and compliance needs.
```

2. Định nghĩa nhiệm vụ cho các tác tử:

```yaml
compliance_analysis_task:
  description: Conduct a thorough analysis about {topic}. Make sure you find relevant information given the current year is {current_year}.
  expected_output: A list with 10 bullet points of the most relevant information about {topic}
  agent: compliance_analyst
compliance_reporting_task:
  description: Review the context you got and expand each topic into a full section for a report.
    Make sure the report is detailed and contains any and all relevant information for Financial Services Organization
  expected_output: A fully fledged report with the main topics, each with a full section of information.
  agent: compliance_specialist
```
3. Các bước thực thi và quy trình được định nghĩa trong `crew.py`:

```python
def crew(self) -> Crew:
"""Creates the Compliance Automation crew"""
    return Crew(
       agents=self.agents,
       tasks=self.tasks,
       process=Process.sequential,
       verbose=True)
```
4. Định nghĩa LLM, chủ đề và tham số thời gian chạy trong tệp `.env`:

```
MODEL=bedrock/us.amazon.nova-pro-v1:0
AWS_REGION_NAME=us-west-2
TOPIC='GDPR requirements for Data Privacy'
```
5. Chạy crew như sau:

```
crewai run
```
6. Bản demo sau đây cho thấy đầu ra của crew. Bạn có thể thấy các tác tử cộng tác để tạo ra một giải pháp chi tiết:

![Compliance Agents - Topic GDPR](./images/compliance-agents-gdpr.png)
Trong đầu ra, lưu ý rằng nhà phân tích tuân thủ và chuyên gia tuân thủ đang làm việc cùng nhau để giải quyết nhiều khía cạnh của yêu cầu Quy định Bảo vệ Dữ liệu Chung (GDPR) cho dịch vụ giao dịch. Chú ý đến sự cộng tác hiệp trợ giữa các tác tử khi họ tinh chỉnh cách tiếp cận và phát triển phản hồi quản lý tuân thủ toàn diện thông qua giải quyết vấn đề lặp đi lặp lại.
## Giải quyết thách thức LLM với kiến thức chuyên ngành

LLMs, mặc dù ấn tượng trong kiến thức rộng của chúng, đối mặt với hai hạn chế chính khi xử lý các lĩnh vực chuyên môn hoặc thông tin gần đây. Đầu tiên, chúng gặp khó khăn với thông tin chuyên biệt dành riêng cho tổ chức của bạn. Thứ hai, vì kiến thức của chúng bị giới hạn trong dữ liệu đào tạo, chúng có thể không phản ánh những cập nhật mới nhất trong các lĩnh vực thay đổi nhanh chóng. Hạn chế này trở nên đặc biệt quan trọng khi xử lý các yêu cầu tuân thủ đang phát triển, chẳng hạn như Tiêu chuẩn Bảo mật Dữ liệu Ngành Thẻ thanh toán (PCI DSS), GDPR, quy tắc AML và quy định Hiểu biết về Khách hàng (KYC). Ngoài ra, các tổ chức cần các giải pháp được tùy chỉnh theo yêu cầu tuân thủ cụ thể và tiêu chuẩn nội bộ của họ, thay vì các phản hồi chung từ LLMs.

Retrieval Augmented Generation (RAG) là một kỹ thuật cho phép các mô hình AI tạo sinh truy xuất và kết hợp thông tin tổ chức và chuyên ngành hiện tại từ các cơ sở dữ liệu bên ngoài. Amazon Bedrock Knowledge Base là một khả năng được quản lý giúp bạn triển khai toàn bộ kỹ thuật RAG mà không cần phải xây dựng tích hợp tùy chỉnh với các nguồn dữ liệu và quản lý luồng dữ liệu. Bằng cách kết hợp cơ sở tri thức chứa các ấn phẩm mới nhất, cập nhật quy định và hướng dẫn tuân thủ từ các nguồn có thẩm quyền như NIST, ISO, PCI và các cơ quan quản lý, Amazon Bedrock Knowledge Bases giúp đảm bảo rằng hệ thống AI của bạn luôn cập nhật với các yêu cầu tuân thủ mới nhất. Trong quá trình tạo prompt, RAG đầu tiên truy xuất dữ liệu liên quan từ cơ sở tri thức liên tục cập nhật này, sau đó sử dụng nó để tạo ra phản hồi thông báo. Điều này giúp cung cấp phản hồi phù hợp hơn, chính xác hơn và được tùy chỉnh phù hợp với các tiêu chuẩn quy định và tổ chức hiện hành. Ví dụ, khi truy vấn về yêu cầu PCI DSS v4.0 hoặc các sửa đổi GDPR gần đây, hệ thống có thể lấy thông tin cập nhật nhất trực tiếp từ các nguồn có thẩm quyền thay vì dựa vào dữ liệu đào tạo có thể đã lỗi thời.
### Tạo Amazon Bedrock Knowledge Base với thông tin ngữ cảnh từ nguồn dữ liệu của bạn

1. Từ bảng điều hướng Amazon Bedrock, chọn **Knowledge Bases** dưới **Builder tools** và chọn **a Knowledge Base with vector store**
2. Cung cấp **Knowledge Base name** và **Data source details**. Bạn sẽ sử dụng web crawler để thu thập dữ liệu
3. Web crawler được cung cấp bởi Amazon Bedrock kết nối và thu thập các URL bạn đã chọn để sử dụng trong Amazon Bedrock knowledge base. Thêm URL làm nguồn dữ liệu trong **Source URLs**
4. Chọn mô hình cho embeddings. Chúng tôi đã chọn Amazon Titan Text Embeddings v2, như hình chụp màn hình dưới đây
![Knowledge Base Configuration](./images/kb-configuration.png)
Sau vài phút, knowledge base sẽ sẵn sàng. Sau khi đã đồng bộ hóa, Amazon Bedrock Knowledge Bases xử lý việc tạo, chạy và định dạng kết quả của truy vấn, đơn giản hóa việc xây dựng giao diện ngôn ngữ tự nhiên cho dữ liệu có cấu trúc.
## Amazon Bedrock Agents

Amazon Bedrock Agents là môi trường toàn diện để xây dựng hệ thống tác tử AI phức tạp. Về cốt lõi, nó cho phép hợp tác đa tác tử liền mạch và duy trì ngữ cảnh hội thoại thông qua khả năng ghi nhớ gốc xuyên suốt các tương tác. Amazon Bedrock Agents tích hợp tự nhiên với cơ sở tri thức và thực thi bảo mật thông qua guardrails tích hợp sẵn. Đối với giải pháp này, chúng tôi tập trung vào hai khả năng chính: tính năng RAG, cho phép các tác tử truy cập và sử dụng thông tin từ cơ sở tri thức, và các tính năng bảo mật được cung cấp thông qua Amazon Bedrock Guardrails. Các guardrails này đóng vai trò là biện pháp bảo vệ thiết yếu cho ứng dụng AI tạo sinh của bạn, thúc đẩy tương tác AI có trách nhiệm và an toàn.

1. Để tạo tác tử, từ bảng điều hướng Amazon Bedrock dưới **Builder tools**, chọn **Agents** và chọn **Create Agent**
2. Dưới **Agent details**, chọn mô hình. Chúng tôi sử dụng Amazon Nova Pro cho trường hợp sử dụng của chúng tôi, như trong ảnh chụp màn hình sau
![Agent Model Selection](./images/agent-model.png)
Dưới Knowledge Bases, thêm knowledge base vào tác tử của bạn.
Chọn tên knowledge base từ danh sách thả xuống, như trong ảnh chụp màn hình sau.
!Add Knowledge Base to Agent
Amazon Bedrock Guardrails
Amazon Bedrock Guardrails cung cấp các kiểm soát an toàn giúp duy trì việc sử dụng AI có trách nhiệm bằng cách cung cấp một lớp bảo mật. Guardrails cung cấp lọc nội dung để giám sát và lọc đầu ra của mô hình AI để giúp ngăn chặn nội dung có hại, không phù hợp hoặc thiên vị. Bạn có thể thiết lập bộ lọc cho những thứ như phát ngôn thù địch, nội dung rõ ràng hoặc thông tin nhận dạng cá nhân (PII). Bạn cũng có thể áp dụng các quy tắc có thể tùy chỉnh và xác thực đầu vào/đầu ra.
Bạn có thể tìm thấy Guardrails trong bảng điều hướng Amazon Bedrock dưới Safeguards. Chọn Create guardrail và cung cấp tên guardrail.
Như được hiển thị trong ảnh chụp màn hình sau, chọn bộ lọc nội dung bạn muốn triển khai cho ứng dụng dựa trên Amazon Bedrock của mình.
![Content Filters](./images/content-filters.png)
3. Thêm chủ đề bị từ chối với các ví dụ cụ thể
4. Sau khi bạn đã tạo guardrail, gắn guardrail vào tác tử

## Tích hợp Amazon Bedrock Agents với CrewAI
CrewAI cung cấp tích hợp liền mạch với các tính năng của Amazon Bedrock, bao gồm Amazon Bedrock Knowledge Bases và Amazon Bedrock Agents thông qua chức năng công cụ CrewAI. Khi các công cụ này được kích hoạt từ các tác tử CrewAI, chúng xử lý truy vấn của bạn, truy xuất thông tin liên quan từ Amazon Bedrock knowledge base và trả về phản hồi cho tác tử CrewAI.
1. Tham khảo mã mẫu thể hiện công cụ CrewAI cho Amazon Bedrock Agent. Bạn cần định nghĩa Amazon Bedrock AgentId và Alias của mình làm tham số trong tệp .env.
2. Thực thi crew một lần nữa với Amazon Bedrock Agents:

```
crewai run
```

3. Bạn có thể tìm thấy đầu ra được tạo bên dưới:

![PCI Compliance Output](./images/compliance-agents-pci.png)
Khi bạn thực thi crew, tác tử phân tích tuân thủ bắt đầu quy trình bằng cách gọi công cụ Bedrock CrewAI để trích xuất các yêu cầu quy định từ Amazon Bedrock Knowledge Bases, sau đó được chuyển đổi liền mạch thành các yêu cầu kỹ thuật bởi tác tử chuyên gia tuân thủ. Thông qua sự cộng tác lặp đi lặp lại, các tác tử chuyên biệt này làm việc cùng nhau để lấp đầy khoảng trống thông tin, và tác tử kiến trúc sư doanh nghiệp tổng hợp các thông tin thu thập được để phát triển chiến lược triển khai mạnh mẽ và kế hoạch thực hiện. Quy trình hợp lý này thể hiện cách nhiều tác tử AI có thể phối hợp hiệu quả để chuyển đổi các yêu cầu tuân thủ thành các giải pháp kỹ thuật có thể hành động.

## Dọn dẹp
Để tránh phí liên tục, hãy làm theo các bước này để dọn dẹp tài nguyên:
1. Xóa Amazon Bedrock knowledge base bạn đã tạo:

```
aws bedrock-agent delete-knowledge-base --knowledge-base-id <your-kb-id>
```

2. Xóa Amazon Bedrock agents bạn đã tạo:

```
aws bedrock-agent delete-agent --agent-id <your-agent-id>
```

## Kết luận

Trong bài viết này, chúng tôi đã trình bày cách:

* Xây dựng hệ thống AI đa tác tử sử dụng CrewAI mô phỏng cấu trúc của bộ phận tuân thủ toàn diện với các tác tử chuyên biệt cho các chức năng khác nhau
* Nâng cao phản hồi AI với kiến thức chuyên ngành bằng cách triển khai RAG sử dụng Amazon Bedrock Knowledge Bases
* Bảo vệ ứng dụng AI tạo sinh với Amazon Bedrock Guardrails để giúp ngăn chặn nội dung có hại, không phù hợp hoặc thiên vị
* Tạo công cụ tùy chỉnh trong CrewAI để tích hợp với Amazon Bedrock Agents cho các giải pháp tuân thủ mạnh mẽ hơn và nhận biết ngữ cảnh
* Tự động hóa toàn bộ vòng đời tuân thủ từ giám sát các thay đổi quy định đến triển khai các biện pháp kiểm soát kỹ thuật mà không cần nỗ lực thủ công rộng rãi
* Triển khai giải pháp sẵn sàng cho sản xuất liên tục thích ứng với các yêu cầu quy định phát triển trong các ngành dịch vụ tài chính và các ngành được quản lý cao khác

Giải pháp này kết hợp Amazon Bedrock Knowledge Bases và CrewAI để tạo ra hệ thống AI đa tác tử thông minh giúp hợp lý hóa các nhiệm vụ tuân thủ quy định. Với triển khai RAG đơn giản hóa, quy trình làm việc phức tạp phản ánh các nhóm con người và thích ứng nhanh hơn với các quy định mới, cách tiếp cận này cho thấy cách AI có thể hỗ trợ các tổ chức đối với các khía cạnh cụ thể của các yêu cầu quy định phức tạp.

Giải pháp này đóng vai trò là điểm khởi đầu thực tế cho các tổ chức muốn nâng cao quy trình tuân thủ của họ với khả năng AI, thể hiện cách các hệ thống thông minh có thể bổ sung và hợp lý hóa quy trình tuân thủ hiện có. Mã nguồn hoàn chỉnh cho dự án này có sẵn trên kho lưu trữ [GitHub](https://github.com/aws-samples/sample-compliance-assistant-with-agents). Hãy thoải mái khám phá, fork hoặc đóng góp!
## 📖 Glossary - Thuật ngữ

| English | Tiếng Việt | Định nghĩa |
|---------|------------|------------|
| Large Language Model (LLM) | Mô hình ngôn ngữ lớn | Mô hình AI được đào tạo trên lượng văn bản lớn có khả năng tạo văn bản, hiểu ngữ cảnh và thực hiện nhiều tác vụ ngôn ngữ |
| Retrieval Augmented Generation (RAG) | Sinh nội dung tăng cường bằng truy xuất | Kỹ thuật kết hợp truy xuất thông tin với mô hình ngôn ngữ để tạo phản hồi chính xác và cập nhật hơn |
| Multi-agent system | Hệ thống đa tác tử | Hệ thống bao gồm nhiều tác tử AI hoạt động cùng nhau để giải quyết các vấn đề phức tạp |
| Knowledge Base | Cơ sở tri thức | Kho lưu trữ thông tin có cấu trúc được sử dụng để tăng cường khả năng của mô hình AI |
| Guardrails | Rào chắn bảo vệ | Các biện pháp bảo vệ giới hạn hành vi của mô hình AI để đảm bảo phản hồi an toàn và phù hợp |
| Anti-Money Laundering (AML) | Chống rửa tiền | Các quy định ngăn chặn việc chuyển đổi tiền bất hợp pháp thành tài sản hợp pháp |
| Bank Secrecy Act (BSA) | Đạo luật Bảo mật Ngân hàng | Luật Hoa Kỳ yêu cầu các tổ chức tài chính giúp chính phủ phát hiện và ngăn chặn rửa tiền |
| General Data Protection Regulation (GDPR) | Quy định Bảo vệ Dữ liệu Chung | Quy định của EU về bảo vệ dữ liệu và quyền riêng tư |
## 🔗 Tài liệu tham khảo

### Tài liệu gốc
- [Bài viết gốc](https://aws.amazon.com/vi/blogs/machine-learning/automating-regulatory-compliance-a-multi-agent-solution-using-amazon-bedrock-and-crewai/): Automating regulatory compliance: A multi-agent solution using Amazon Bedrock and CrewAI
- [Hồ sơ tác giả](https://aws.amazon.com/blogs/author/balmat/): Balu Mathew - Senior Solutions Architect tại AWS
- [Mã nguồn dự án](https://github.com/aws-samples/sample-compliance-assistant-with-agents): GitHub repository của dự án mẫu

### Tài liệu tiếng Việt
- [Tài liệu Amazon Bedrock](https://aws.amazon.com/vi/bedrock/): Thông tin về Amazon Bedrock bằng tiếng Việt
- [AWS Machine Learning Blog](https://aws.amazon.com/vi/blogs/machine-learning/): Blog AWS về Machine Learning có phiên bản tiếng Việt

### Tools và Services
- [Amazon Bedrock](https://aws.amazon.com/bedrock/): Dịch vụ cung cấp các mô hình nền tảng thông qua API
- [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html): Tính năng quản lý cơ sở tri thức cho RAG
- [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html): Công cụ xây dựng tác tử AI
- [CrewAI](https://github.com/crewai/crewai): Framework mã nguồn mở để điều phối đa tác tử AI
## 💬 Ghi chú của người dịch

Trong quá trình dịch bài viết này, tôi đã gặp phải một số thách thức và học hỏi nhiều điều thú vị về công nghệ AI tạo sinh và hệ thống đa tác tử.

### Challenges trong quá trình dịch
- **Technical Terms**: Nhiều thuật ngữ chuyên ngành như "Retrieval Augmented Generation", "Guardrails", "Multi-agent" khó dịch sang tiếng Việt mà vẫn giữ nguyên ý nghĩa kỹ thuật. Tôi đã phải nghiên cứu kỹ để chọn cách dịch phù hợp nhất.
- **Cultural Context**: Các ví dụ về tuân thủ quy định tài chính của Mỹ như BSA cần được làm rõ để độc giả Việt Nam dễ hiểu.
- **Complex Concepts**: Cơ chế hoạt động của hệ thống đa tác tử là một khái niệm phức tạp, cần diễn đạt sao cho dễ hiểu với cả độc giả không chuyên.

### Insights gained
- **Technical Learning**: Hiểu sâu hơn về cách các hệ thống AI đa tác tử có thể áp dụng trong lĩnh vực tuân thủ quy định, một nhu cầu quan trọng trong ngành tài chính.
- **Language Skills**: Phát triển kỹ năng chuyển ngữ các khái niệm kỹ thuật phức tạp sang tiếng Việt một cách rõ ràng, chính xác.
- **Industry Knowledge**: Nắm bắt được các xu hướng mới trong việc ứng dụng AI cho các ngành được quản lý chặt chẽ như tài chính, y tế.

## 🤝 Đóng góp và Feedback

Bài dịch này được thực hiện trong khuôn khổ FCJ Internship Program.

- **📧 Liên hệ**: chutienbinh2003@gmail.com
- **💬 Feedback**: Mọi góp ý để cải thiện chất lượng dịch thuật xin gửi về email trên
- **🔄 Updates**: Bài dịch sẽ được cập nhật dựa trên feedback từ cộng đồng

© 2025 - Bản dịch thuộc về Chu Tiến Bình. Vui lòng ghi nguồn khi sử dụng.