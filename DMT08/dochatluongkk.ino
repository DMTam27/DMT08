#define MQ2_PIN A0  // Chân analog đọc dữ liệu từ MQ-2

void setup() {
  Serial.begin(9600);  // Khởi động Serial Monitor
}

void loop() {
  int sensorValue = analogRead(MQ2_PIN); // Đọc giá trị từ cảm biến
  float voltage = sensorValue * (5.0 / 1023.0); // Chuyển đổi ADC sang Volt
  
  Serial.print("Giá trị MQ-2: ");
  Serial.println(sensorValue);
  
  delay(1000); // Chờ 1 giây trước khi đọc tiếp
}
