# Snake Game

Trò chơi rắn (Snake Game) là một trong những trò chơi cổ điển được nhiều người yêu thích. Nó đã trở thành biểu tượng của sự đơn giản và gây nghiện trong lĩnh vực trò chơi điện tử.

## Giới thiệu

Trong trò chơi này, người chơi điều khiển một con rắn di chuyển trên một bản đồ hình vuông. Mục tiêu là để làm cho con rắn dài hơn bằng cách ăn thức ăn  mà xuất hiện ngẫu nhiên trên bản đồ. Mỗi lần con rắn ăn được thức ăn, nó sẽ dài ra một phần đuôi, và điểm số của người chơi sẽ tăng lên.

Tuy nhiên, người chơi cũng cần phải tránh các chướng ngại vật, bao gồm việc đâm vào tường hoặc tự cơ thể của rắn. Nếu con rắn đâm vào bất kỳ chướng ngại vật nào, trò chơi sẽ kết thúc.

## Hướng Dẫn Chơi Game Snake

### Lựa Chọn Độ Khó Của Trò Chơi

Để lựa chọn độ khó để bắt đầu trò chơi, người chơi sử dụng phím mũi tên lên và xuống để chọn mức độ khó ở màn hình Menu, độ khó càng cao thì tốc độ di chuyển của rắn sẽ càng nhanh.

- **Phím mũi tên lên**: Di chuyển xuống mức độ khó phía trên
- **Phím mũi tên xuống**: Di chuyển xuống mức độ khó phía dưới

### Điều Khiển Con Rắn

Để điều khiển con rắn trong trò chơi Con Rắn, người chơi có thể sử dụng các phím mũi tên hoặc các phím tương tự trên bàn phím. Cụ thể:

- **Phím mũi tên lên**: Di chuyển con rắn lên trên màn hình.
- **Phím mũi tên xuống**: Di chuyển con rắn xuống dưới màn hình.
- **Phím mũi tên trái**: Di chuyển con rắn sang trái trên màn hình.
- **Phím mũi tên phải**: Di chuyển con rắn sang phải trên màn hình.

### Phát Hiện Và Tránh Va Chạm

Trong quá trình chơi, người chơi cần phải tránh con rắn va chạm với bản thân hoặc các ranh giới của màn chơi. Khi con rắn va chạm, trò chơi sẽ kết thúc và điểm số của người chơi sẽ được ghi lại.

### Điểm Số Và Màn Chơi

Khi con rắn ăn thức ăn, điểm số của người chơi sẽ tăng lên. Mỗi một mảnh thức ăn sẽ tăng điểm số của người chơi một lượng nhất định. Sau mỗi khoảng thời gian nhất định, một mảnh thức ăn mới sẽ được sinh ra ở một vị trí ngẫu nhiên trên màn chơi. Sau khi ăn một số mồi thức thường, mồi đặc biệt sẽ hiện ra, tuy nhiên mồi này chỉ tồn tại trong 1 thời gian nhất định, thanh thời gian sẽ giảm dần. Đồng thời điểm có được từ việc ăn mồi đặc biệt cũng sẽ giảm dần, ăn được càng sớm số điểm bạn nhận được sẽ càng cao!

### Mô Tả Chi Tiết Về Các Yếu Tố Của Trò Chơi

Các yếu tố trong trò chơi Con Rắn, có ba yếu tố chính:

- **Con rắn**: Đại diện cho nhân vật chính của trò chơi, con rắn sẽ tăng kích thước khi ăn thức ăn và kết thúc trò chơi khi va chạm.
- **Thức ăn**: Một mảnh thức ăn xuất hiện ngẫu nhiên trên màn hình, và con rắn cần ăn thức ăn để tăng điểm số và kích thước.
- **Thức ăn đặc biệt**: Một mảnh thức ăn to hơn bình thường xuất hiện ngẫu trên màng hình, điểm số có được sẽ cực cao, và giảm dần theo thời gian.
- **Màn chơi**: Màn chơi được giới hạn bởi các ranh giới, và con rắn cần tránh va chạm với các ranh giới này để trò chơi tiếp tục.

## Chi Tiết Về Cấu Trúc Dữ Liệu Và Giải Thuật

### Cấu Trúc Dữ Liệu

Trong mã nguồn của trò chơi Con Rắn, các đơn vị đoạn của con rắn được lưu trữ dưới dạng một danh sách liên kết, với mỗi nút trong danh sách đại diện cho một đơn vị đoạn của con rắn. Điều này cho phép việc thêm và xóa đơn vị đoạn một cách dễ dàng khi con rắn di chuyển.

Thức ăn được biểu diễn bằng cặp tọa độ (x, y) trên màn hình, và vị trí của thức ăn được lưu trữ trong một biến tọa độ.

### Giải Thuật

Để xác định hướng di chuyển của con rắn và phát hiện va chạm, trò chơi sử dụng một loạt các câu lệnh điều kiện để kiểm tra các tình huống khác nhau. Ví dụ, để xác định hướng di chuyển mới của con rắn, trò chơi sẽ kiểm tra phím mũi tên được nhấn và hướng di chuyển hiện tại của con rắn.

## Cấu Trúc Chương Trình

Chương trình của trò chơi Con Rắn được chia thành các phần chính như sau:

- Khởi tạo: Khởi tạo các biến và cài đặt ban đầu.
- Vòng lặp chính: Vòng lặp trong đó trò chơi được cập nhật và vẽ lại trên màn hình.
- Phương thức di chuyển: Phương thức để di chuyển con rắn và kiểm tra va chạm.
- Phương thức cập nhật giao diện người dùng: Phương thức để cập nhật giao diện người dùng với thông tin mới.
