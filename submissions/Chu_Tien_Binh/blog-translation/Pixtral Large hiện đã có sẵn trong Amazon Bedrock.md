# Pixtral Large hiện đã có sẵn trong Amazon Bedrock

> **📖 Bài gốc**: [Pixtral Large is now available in Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/pixtral-large-is-now-available-in-amazon-bedrock/)  
> **👤 Tác giả**: Deepesh Dhapola, Andre Boaventura, Ankit Agarwal, Shane Rai, Aris Tsakpinis, Preston Tuggle, và Niithiyn Vijeaswaran   
> **📅 Ngày đăng**: 10/04/2025   
> **🌐 Nguồn**: AWS Machine Learning Blog  
> **👨‍💻 Dịch giả**: Chu Tiến Bình - Thực tập sinh FCJ  
> **📅 Ngày dịch**: 01/07/2025  
> **⏱️ Thời gian đọc**: 10 phút  

---

## 📋 Tóm tắt

Bài viết giới thiệu về việc mô hình nền tảng (FM) Pixtral Large của Mistral AI hiện đã được cung cấp chính thức trên Amazon Bedrock. Pixtral Large là mô hình đa phương thức tiên tiến cho phép người dùng xây dựng, thử nghiệm và mở rộng ý tưởng AI tạo sinh trên AWS. AWS là nhà cung cấp đám mây lớn đầu tiên cung cấp Pixtral Large dưới dạng mô hình không máy chủ, được quản lý hoàn toàn. Bài viết trình bày chi tiết về các tính năng của Pixtral Large, hướng dẫn bắt đầu sử dụng, và minh họa các trường hợp sử dụng tiềm năng thông qua các ví dụ thực tế.

**🎯 Đối tượng**: Nhà phát triển AI, kỹ sư ML, chuyên gia dữ liệu  
**📊 Mức độ**: Trung cấp (200)  
**🏷️ Từ khóa**: Amazon Bedrock, Mistral AI, Pixtral Large, Mô hình đa phương thức, AI tạo sinh  

---

## 📚 Mục lục

- [Pixtral Large hiện đã có sẵn trong Amazon Bedrock](#pixtral-large-hiện-đã-có-sẵn-trong-amazon-bedrock)
  - [📋 Tóm tắt](#-tóm-tắt)
  - [📚 Mục lục](#-mục-lục)
  - [📄 Nội dung bài dịch](#-nội-dung-bài-dịch)
  - [Tổng quan về Pixtral Large](#tổng-quan-về-pixtral-large)
  - [Bắt đầu với Pixtral Large trong Amazon Bedrock](#bắt-đầu-với-pixtral-large-trong-amazon-bedrock)
  - [Các trường hợp sử dụng Pixtral Large](#các-trường-hợp-sử-dụng-pixtral-large)
    - [Tạo mã SQL từ sơ đồ cơ sở dữ liệu](#tạo-mã-sql-từ-sơ-đồ-cơ-sở-dữ-liệu)
  - [Kết luận](#kết-luận)
  - [Glossary - Thuật ngữ](#glossary---thuật-ngữ)
  - [Tài liệu tham khảo](#tài-liệu-tham-khảo)
    - [Tài liệu gốc](#tài-liệu-gốc)
    - [Tài liệu tiếng Việt](#tài-liệu-tiếng-việt)
    - [Tools và Services](#tools-và-services)
  - [Ghi chú của người dịch](#ghi-chú-của-người-dịch)
    - [Challenges trong quá trình dịch](#challenges-trong-quá-trình-dịch)
    - [Insights gained](#insights-gained)
  - [Đóng góp và Feedback](#đóng-góp-và-feedback)

---

## 📄 Nội dung bài dịch

Hôm nay, chúng tôi vui mừng thông báo rằng mô hình nền tảng (FM) Pixtral Large của Mistral AI đã được cung cấp chính thức trên Amazon Bedrock. Với sự ra mắt này, bạn giờ đây có thể truy cập mô hình đa phương thức hàng đầu của Mistral để xây dựng, thử nghiệm và mở rộng ý tưởng AI tạo sinh một cách có trách nhiệm trên AWS. AWS là nhà cung cấp đám mây lớn đầu tiên cung cấp Pixtral Large dưới dạng mô hình hoàn toàn được quản lý, không máy chủ.

Trong bài viết này, chúng tôi sẽ thảo luận về các tính năng của Pixtral Large và các trường hợp sử dụng tiềm năng của nó.

## Tổng quan về Pixtral Large

Pixtral Large là một mô hình đa phương thức tiên tiến được phát triển bởi Mistral AI, với 124 tỷ tham số. Mô hình này kết hợp một bộ giải mã đa phương thức mạnh mẽ 123 tỷ tham số với một bộ mã hóa thị giác chuyên biệt 1 tỷ tham số. Nó có thể xử lý liền mạch các tác vụ hình ảnh và văn bản phức tạp trong khi vẫn giữ được khả năng xử lý ngôn ngữ xuất sắc của người tiền nhiệm, Mistral Large 2.

Một tính năng nổi bật của Pixtral Large là cửa sổ ngữ cảnh rộng lớn 128.000 token, cho phép nó xử lý đồng thời nhiều hình ảnh cùng với dữ liệu văn bản rộng lớn. Khả năng này làm cho nó đặc biệt hiệu quả trong việc phân tích tài liệu, biểu đồ chi tiết, đồ thị và hình ảnh tự nhiên, đáp ứng nhiều ứng dụng thực tế.

Sau đây là các khả năng chính của Pixtral Large:

* **Phân tích văn bản đa ngôn ngữ** – Pixtral Large giải thích và trích xuất chính xác thông tin được viết bằng nhiều ngôn ngữ từ hình ảnh và tài liệu. Điều này đặc biệt có lợi cho các tác vụ như tự động xử lý biên lai hoặc hóa đơn, nơi nó có thể thực hiện các phép tính và đánh giá nhận thức ngữ cảnh, hợp lý hóa các quy trình như theo dõi chi phí hoặc phân tích tài chính.
* **Hiểu biểu đồ và trực quan hóa dữ liệu** – Mô hình thể hiện khả năng xuất sắc trong việc hiểu các biểu diễn dữ liệu trực quan phức tạp. Nó có thể dễ dàng nhận biết xu hướng, dị thường và các điểm dữ liệu chính trong trực quan hóa đồ họa. Ví dụ, Pixtral Large cực kỳ hiệu quả trong việc phát hiện các bất thường hoặc xu hướng thông minh trong các đường cong mất mát huấn luyện hoặc chỉ số hiệu suất, nâng cao độ chính xác của việc ra quyết định dựa trên dữ liệu.
* **Phân tích hình ảnh tổng quát và hiểu ngữ cảnh** – Pixtral Large thành thạo trong việc phân tích dữ liệu hình ảnh tổng quát, bao gồm ảnh chụp màn hình và hình ảnh, trích xuất thông tin chi tiết tinh tế và đáp ứng hiệu quả các truy vấn dựa trên nội dung hình ảnh. Khả năng này mở rộng đáng kể khả năng sử dụng của nó, cho phép hỗ trợ các tình huống đa dạng—từ giải thích ngữ cảnh hình ảnh trong bài thuyết trình đến tự động kiểm duyệt nội dung và truy xuất hình ảnh theo ngữ cảnh.

Thông tin chi tiết bổ sung về mô hình bao gồm:

* Suy luận đa khu vực khả dụng cho các khu vực sau:  
   * `us-east-2`  
   * `us-west-2`  
   * `us-east-1`  
   * `eu-west-1`  
   * `eu-west-3`  
   * `eu-north-1`  
   * `eu-central-1`
* ID mô hình: `us` hoặc `eu` sau đó là `mistral.pixtral-large-2502-v1:0`
* Cửa sổ ngữ cảnh: `128.000`

## Bắt đầu với Pixtral Large trong Amazon Bedrock

Nếu bạn mới sử dụng các mô hình Mistral AI, bạn có thể yêu cầu quyền truy cập mô hình trên bảng điều khiển Amazon Bedrock. Để biết thêm thông tin, xem [Truy cập các mô hình nền tảng Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).

Để kiểm tra Pixtral Large trên bảng điều khiển Amazon Bedrock, chọn **Text** hoặc **Chat** trong **Playgrounds** ở thanh điều hướng. Sau đó, chọn **Select model** và chọn **Mistral** làm danh mục và **Pixtral Large** làm mô hình.

Bằng cách chọn **View API**, bạn cũng có thể truy cập mô hình bằng cách sử dụng các ví dụ mã trong AWS Command Line Interface (AWS CLI) và các AWS SDK. Bạn có thể sử dụng ID mô hình như `mistral.mistral-large-2407-v1:0`, như được hiển thị trong mã sau:

```
$ aws bedrock-runtime invoke-model \ 
--model-id mistral.pixtral-large-2502-v1:0 \
--body "{\"prompt\":\"<s>[INST] this is where you place your input text [/INST]\", \"max_tokens\":200, \"temperature\":0.5, \"top_p\":0.9, \"top_k\":50}" \ 
--cli-binary-format raw-in-base64-out \
--region eu-north-1 \ 
invoke-model-output.txt
```

Trong các phần sau, chúng tôi sẽ đi sâu vào các khả năng của Pixtral Large.

## Các trường hợp sử dụng Pixtral Large

Trong phần này, chúng tôi cung cấp các ví dụ trường hợp sử dụng của Pixtral Large bằng cách sử dụng các prompt mẫu. Vì Pixtral Large được xây dựng trên Mistral Large 2, nó bao gồm chế độ đầu ra JSON gốc. Tính năng này cho phép các nhà phát triển nhận phản hồi của mô hình ở định dạng có cấu trúc và dễ đọc, có thể tích hợp liền mạch vào các ứng dụng và hệ thống khác nhau. Vì JSON là tiêu chuẩn trao đổi dữ liệu được sử dụng rộng rãi, chức năng này hợp lý hóa quá trình làm việc với đầu ra của mô hình, làm cho nó dễ tiếp cận và thực tế hơn cho các nhà phát triển trên các ngành và trường hợp sử dụng khác nhau. Để biết thêm thông tin về việc tạo JSON bằng API Converse, hãy tham khảo [Tạo JSON với API Converse của Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/converse-generating-json.html).

Ngoài ra, Pixtral Large hỗ trợ API Converse và sử dụng công cụ. Bằng cách sử dụng API Amazon Bedrock, bạn có thể cấp cho mô hình quyền truy cập vào các công cụ giúp tạo phản hồi cho các tin nhắn bạn gửi.

### Tạo mã SQL từ sơ đồ cơ sở dữ liệu

Sơ đồ thực thể-mối quan hệ (ER) là một biểu diễn trực quan được sử dụng trong thiết kế cơ sở dữ liệu để minh họa mối quan hệ giữa các thực thể và thuộc tính của chúng. Đây là một công cụ quan trọng cho mô hình hóa khái niệm, giúp các nhà phát triển và phân tích hiểu và truyền đạt cấu trúc dữ liệu trong cơ sở dữ liệu.

Ví dụ này kiểm tra khả năng của mô hình trong việc tạo ra các câu lệnh `SQL CREATE TABLE` tương thích với PostgreSQL để tạo các thực thể và mối quan hệ của chúng.

Chúng tôi sử dụng prompt sau:

```
prompt = """
You are a database designer. You have created an ER diagram. You need to generate PostgreSQL compatible SQL statements to create the tables"
"""
```

Chúng tôi nhập sơ đồ ER sau.

Phản hồi của mô hình như sau:

```
Sure! Below are the SQL statements to create the tables based on the provided 
ER diagram for a PostgreSQL database.

```sql
-- Create the Airport table
CREATE TABLE Airport (
    Airport_ID SERIAL PRIMARY KEY,
    AirportCity VARCHAR(255),
    AirportCountry VARCHAR(255)
);

-- Create the Calendar table
CREATE TABLE Calendar (
    Day_Date DATE PRIMARY KEY,
    Business_Day_YN BOOLEAN
);

-- Create the Flight_Details table
CREATE TABLE Flight_Details (
    Flight_ID SERIAL PRIMARY KEY,
    Source_Airport_ID INT REFERENCES Airport(Airport_ID),
    Destination_Airport_ID INT REFERENCES Airport(Airport_ID),
    Departure_Date_Time TIMESTAMP,
    Arrival_Date_Time TIMESTAMP,
    Airplane_Type VARCHAR(255)
);

-- Create the Travel_Class table
CREATE TABLE Travel_Class (
    Travel_Class_ID SERIAL PRIMARY KEY,
    Travel_Class_Name VARCHAR(255),
    Travel_Class_Capacity INT
);

-- Create the Seat_Details table
CREATE TABLE Seat_Details (
    Seat_ID SERIAL PRIMARY KEY,
    Travel_Class_ID INT REFERENCES Travel_Class(Travel_Class_ID),
    Flight_ID INT REFERENCES Flight_Details(Flight_ID)
);

-- Create the Flight_Cost table
CREATE TABLE Flight_Cost (
    Seat_ID INT REFERENCES Seat_Details(Seat_ID),
    Valid_From_Date DATE,
    Cost DECIMAL(10, 2),
    Valid_To_Date DATE,
    PRIMARY KEY (Seat_ID, Valid_From_Date)
);

-- Create the Flight_Service table
CREATE TABLE Flight_Service (
    Service_ID SERIAL PRIMARY KEY,
    Service_Name VARCHAR(255)
);

-- Create the Service_Offering table
CREATE TABLE Service_Offering (
    Travel_Class_ID INT REFERENCES Travel_Class(Travel_Class_ID),
    Service_ID INT REFERENCES Flight_Service(Service_ID),
    Offered_YN BOOLEAN,
    From_Date DATE,
    To_Date DATE,
    PRIMARY KEY (Travel_Class_ID, Service_ID)
);

-- Create the Passenger table
CREATE TABLE Passenger (
    Passenger_ID SERIAL PRIMARY KEY,
    P_FirstName VARCHAR(255),
    P_LastName VARCHAR(255),
    P_Email VARCHAR(255),
    P_PhoneNumber VARCHAR(255),
    P_Address VARCHAR(255),
    P_City VARCHAR(255),
    P_State VARCHAR(255),
    P_Zipcode VARCHAR(255),
    P_Country VARCHAR(255)
);

-- Create the Reservation table
CREATE TABLE Reservation (
    Reservation_ID SERIAL PRIMARY KEY,
    Passenger_ID INT REFERENCES Passenger(Passenger_ID),
    Seat_ID INT REFERENCES Seat_Details(Seat_ID),
    Date_Of_Reservation DATE
);

-- Create the Payment_Status table
CREATE TABLE Payment_Status (
    Payment_ID SERIAL PRIMARY KEY,
    Payment_Status_YN BOOLEAN,
    Payment_Due_Date DATE,
    Payment_Amount DECIMAL(10, 2),
    Reservation_ID INT REFERENCES Reservation(Reservation_ID)
);
```
```

### Phân tích biểu đồ thống kê dân số

Trong ví dụ này, chúng tôi kiểm tra khả năng của mô hình trong việc hiểu và phân tích biểu đồ phức tạp.

Chúng tôi sử dụng prompt sau:

```
prompt = """
Analyze the visualization I'm sharing with you:
1. First, describe what the visualization shows:
   - What information is being displayed?
   - How is it displayed (chart type, visual elements)?
   - What are its components?
2. Identify specific patterns:
   - Which regions show the highest proportion of cars?
   - Which regions show the highest proportion of motorcycles?
   - Which regions show the largest total values?
   - Which areas show the most balanced distribution?
3. Compare regional trends:
   - How do the proportions differ between continents?
   - What patterns emerge between different hemispheres?
   - Are there clear differences between different economic zones?
4. Identify interesting outliers:
   - Which regions stand out from their neighbors?
   - Can you identify any unexpected patterns?
   - Where do you notice significant data variations?
5. Consider geographical and demographic factors:
   - How might local conditions influence these patterns?
   - What socioeconomic factors might explain the variations?
   - Can you identify any correlation between size and proportions?
6. Make comparisons between:
   - Different geographical zones
   - Various population densities
   - Different economic development levels"""
```

Chúng tôi nhập hình ảnh sau.

*Nguồn: By Dennis Bratland – Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=15186498*

Phản hồi của mô hình như sau:

```
Mô tả về Biểu đồ:
Thông tin hiển thị: Biểu đồ trình bày dữ liệu về dân số (tính bằng triệu) và tỷ lệ phương tiện (ô tô và xe máy) trên nhiều khu vực trên toàn thế giới.
Phương pháp hiển thị: Dữ liệu được hiển thị bằng các biểu đồ tròn được đặt chồng lên bản đồ thế giới. Kích thước của mỗi biểu đồ tròn tương ứng với dân số của khu vực, với các biểu đồ lớn hơn cho biết dân số lớn hơn.
Thành phần:
Biểu đồ tròn: Mỗi biểu đồ tròn được chia thành hai phần đại diện cho tỷ lệ ô tô (màu xanh nhạt) và xe máy (màu xanh đậm).
Biến thiên kích thước: Kích thước của các biểu đồ tròn cho biết tổng dân số của khu vực, với các biểu đồ lớn hơn đại diện cho dân số cao hơn.
Mẫu cụ thể:
Tỷ lệ ô tô cao nhất: Các khu vực như Hoa Kỳ và một số vùng của châu Âu cho thấy tỷ lệ ô tô cao hơn.
Tỷ lệ xe máy cao nhất: Các quốc gia Đông Nam Á như Indonesia và Việt Nam cho thấy tỷ lệ xe máy cao hơn.
Giá trị tổng lớn nhất: Các biểu đồ tròn lớn được quan sát thấy ở các khu vực đông dân cư như Ấn Độ, Trung Quốc và một số vùng của Đông Nam Á.
Phân bố cân bằng nhất: Một số khu vực ở châu Âu và Nam Mỹ cho thấy sự phân bố cân bằng hơn giữa ô tô và xe máy.
Xu hướng khu vực:
Sự khác biệt giữa các lục địa:
Bắc Mỹ: Chủ yếu là ô tô.
Châu Âu: Một sự kết hợp với ưu tiên nhẹ cho ô tô.
Châu Phi: Nhìn chung có giá trị tổng thấp hơn với tỷ lệ đa dạng.
Châu Á: Dân số cao với tỷ lệ xe máy đáng kể ở Đông Nam Á.
Mẫu bán cầu: Bán cầu Bắc có các khu vực đông dân cư hơn với tỷ lệ phương tiện đa dạng, trong khi Bán cầu Nam cho thấy mật độ dân số thấp hơn và phân bố cân bằng hơn.
Các vùng kinh tế: Các khu vực phát triển có xu hướng có tỷ lệ ô tô cao hơn, trong khi các khu vực đang phát triển, đặc biệt là ở châu Á, cho thấy việc sử dụng xe máy cao hơn.
Các điểm ngoại lệ thú vị:
Indonesia: Nổi bật với tỷ lệ xe máy rất cao so với các khu vực lân cận.
Hoa Kỳ: Cho thấy tỷ lệ ô tô cao chiếm ưu thế, khác biệt với các khu vực khác.
Mẫu không mong đợi: Một số quốc gia châu Phi nhỏ hơn cho thấy tỷ lệ xe máy cao bất ngờ mặc dù dân số thấp hơn.
Các yếu tố địa lý và nhân khẩu học:
Điều kiện địa phương: Đô thị hóa và phát triển cơ sở hạ tầng ảnh hưởng đến sở thích phương tiện.
Các yếu tố kinh tế xã hội: Tình trạng kinh tế và khả năng chi trả đóng vai trò quan trọng trong việc lựa chọn phương tiện.
Tương quan: Dân số lớn hơn ở các khu vực đang phát triển thường tương quan với việc sử dụng xe máy cao hơn do khả năng chi trả và sự tiện lợi.
So sánh:
Các vùng địa lý: Khu vực đô thị ở các nước phát triển cho thấy việc sử dụng ô tô nhiều hơn, trong khi các khu vực nông thôn và đang phát triển ưu tiên xe máy.
Mật độ dân số: Các khu vực đông dân cư ở châu Á cho thấy ưu tiên cho xe máy do tắc nghẽn giao thông và khả năng chi trả.
Phát triển kinh tế: Các nền kinh tế phát triển có tỷ lệ ô tô cao hơn, trong khi các nền kinh tế đang phát triển phụ thuộc nhiều hơn vào xe máy.
```

## Kết luận

Trong bài viết này, chúng tôi đã trình bày cách bắt đầu với mô hình Pixtral Large trong Amazon Bedrock. Mô hình đa phương thức Pixtral Large cho phép bạn giải quyết nhiều trường hợp sử dụng đa dạng, như hiểu tài liệu, lập luận logic, nhận dạng chữ viết tay, so sánh hình ảnh, trích xuất thực thể, trích xuất dữ liệu có cấu trúc từ hình ảnh quét và tạo chú thích. Những khả năng này có thể tăng cường năng suất trong nhiều ứng dụng doanh nghiệp, bao gồm thương mại điện tử (bán lẻ), tiếp thị, dịch vụ tài chính và hơn thế nữa.

Mô hình nền tảng (FM) Pixtral Large của Mistral AI hiện đã có sẵn trong Amazon Bedrock. Để bắt đầu với Pixtral Large trong Amazon Bedrock, hãy truy cập bảng điều khiển Amazon Bedrock.

Muốn khám phá thêm? Hãy xem kho lưu trữ [Mistral-on-AWS](https://github.com/aws-samples/mistral-on-aws). Để biết thêm thông tin về các mô hình Mistral AI có sẵn trên Amazon Bedrock, hãy tham khảo [Các mô hình Mistral AI hiện có sẵn trên Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/mistral-ai-models-now-available-on-amazon-bedrock/).

---

## Glossary - Thuật ngữ

| English                          | Tiếng Việt                      | Định nghĩa                                                                                              |
| -------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------- |
| foundation model (FM)            | mô hình nền tảng                | Mô hình AI được huấn luyện trên tập dữ liệu lớn, đa dạng, có thể tinh chỉnh cho nhiều tác vụ khác nhau  |
| context window                   | cửa sổ ngữ cảnh                 | Số lượng token (từ, ký tự) tối đa mà mô hình có thể xử lý cùng một lúc                                  |
| serverless                       | không máy chủ                   | Mô hình điện toán đám mây không yêu cầu quản lý máy chủ, tự động mở rộng theo nhu cầu                   |
| multimodal model                 | mô hình đa phương thức          | Mô hình AI có khả năng xử lý nhiều loại dữ liệu như văn bản, hình ảnh, âm thanh trong cùng một hệ thống |
| decoder                          | bộ giải mã                      | Thành phần của mô hình AI chịu trách nhiệm tạo ra đầu ra dựa trên biểu diễn ẩn của dữ liệu              |
| encoder                          | bộ mã hóa                       | Thành phần của mô hình AI chuyển đổi dữ liệu đầu vào thành biểu diễn ẩn                                 |
| entity-relationship (ER) diagram | sơ đồ thực thể-mối quan hệ (ER) | Công cụ mô hình hóa dữ liệu hiển thị thực thể, thuộc tính và mối quan hệ giữa chúng trong cơ sở dữ liệu |

## Tài liệu tham khảo

### Tài liệu gốc
- [Bài viết gốc](https://aws.amazon.com/blogs/machine-learning/pixtral-large-is-now-available-in-amazon-bedrock/): Pixtral Large is now available in Amazon Bedrock
- [Hồ sơ tác giả](https://aws.amazon.com/blogs/author/): Deepesh Dhapola, Andre Boaventura và các đồng tác giả khác
- [Kho lưu trữ Mistral-on-AWS](https://github.com/aws-samples/mistral-on-aws): GitHub repository với mẫu triển khai Mistral AI trên AWS

### Tài liệu tiếng Việt
- [Tài liệu Amazon Bedrock](https://aws.amazon.com/vi/bedrock/): Thông tin về Amazon Bedrock bằng tiếng Việt
- [AWS Machine Learning Blog](https://aws.amazon.com/vi/blogs/machine-learning/): Blog AWS về Machine Learning có phiên bản tiếng Việt

### Tools và Services
- [Amazon Bedrock](https://aws.amazon.com/bedrock/): Dịch vụ cung cấp các mô hình nền tảng thông qua API
- [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html): Tính năng quản lý cơ sở tri thức cho RAG
- [Mistral AI Models](https://aws.amazon.com/blogs/machine-learning/mistral-ai-models-now-available-on-amazon-bedrock/): Thông tin về các mô hình Mistral AI trên Amazon Bedrock
- [Generating JSON with the Amazon Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/converse-generating-json.html): Hướng dẫn tạo JSON với API Converse

## Ghi chú của người dịch

Trong quá trình dịch bài viết này, tôi nhận thấy Pixtral Large là một bước tiến quan trọng trong lĩnh vực mô hình đa phương thức với khả năng xử lý đồng thời cả văn bản và hình ảnh.

### Challenges trong quá trình dịch
- **Thuật ngữ kỹ thuật**: Nhiều thuật ngữ chuyên ngành như "multimodal model", "context window", "JSON output mode" khá thách thức khi chuyển ngữ sang tiếng Việt mà vẫn giữ nguyên ý nghĩa kỹ thuật.
- **Cấu trúc kỹ thuật phức tạp**: Bài viết chứa nhiều thông tin kỹ thuật chi tiết về cấu trúc mô hình (123 tỷ tham số cho bộ giải mã và 1 tỷ tham số cho bộ mã hóa thị giác) cần được diễn đạt chính xác.
- **Ví dụ mã nguồn**: Việc duy trì tính chính xác của các đoạn mã nguồn và lệnh CLI trong khi vẫn đảm bảo phần giải thích tiếng Việt rõ ràng.

### Insights gained
- **Hiểu biết sâu hơn về mô hình đa phương thức**: Pixtral Large minh họa xu hướng phát triển mô hình AI có khả năng xử lý đa dạng dữ liệu đầu vào (văn bản, hình ảnh).
- **Tầm quan trọng của cửa sổ ngữ cảnh lớn**: Cửa sổ ngữ cảnh 128.000 token cho phép xử lý nhiều hình ảnh và văn bản cùng lúc, mở ra khả năng ứng dụng trong phân tích tài liệu phức tạp.
- **Sự hội tụ của AI và đám mây**: Việc triển khai mô hình tiên tiến dưới dạng dịch vụ không máy chủ thể hiện xu hướng AI-as-a-Service đang ngày càng phổ biến.

## Đóng góp và Feedback

Bài dịch này được thực hiện trong khuôn khổ FCJ Internship Program.

- **📧 Liên hệ**: chutienbinh2003@gmail.com
- **💬 Feedback**: Mọi góp ý để cải thiện chất lượng dịch thuật xin gửi về email trên
- **🔄 Updates**: Bài dịch sẽ được cập nhật dựa trên feedback từ cộng đồng

© 2025 - Bản dịch thuộc về Chu Tiến Bình. Vui lòng ghi nguồn khi sử dụng. 