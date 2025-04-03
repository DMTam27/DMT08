
#include<Servo.h>
#include <Adafruit_NeoPixel.h>

#define LED_PIN 10       // Chân kết nối với DIN của WS2812
#define LED_COUNT 12    // Số LED trong dải (thay đổi theo thực tế)


int fan1 = 6, fan2 = 9;
Servo servo_fan1, servo_fan2;

int tamX = 0;           // Tọa độ hiện tại
int prevTamX = -1;      // Lưu tọa độ trước đó để so sánh
int tamY = 0;
int prevTamY = -1;
int i=0;
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();
  strip.show(); // Xóa dữ liệu cũ

    Serial.begin(9600);
    servo_fan1.attach(fan1);
    servo_fan2.attach(fan2);
    servo_fan1.write(80);
    delay(10);
    
    servo_fan2.write(0);
    delay(10);
    strip.fill(strip.Color(255, 255, 0)); // Màu vàng (R=255, G=255, B=0)
    strip.show();
    
}

void loop() {
  
    
    

    if (Serial.available() > 0) {
        String input = Serial.readStringUntil('\n');  // Đọc dữ liệu từ Python
        int commaIndex = input.indexOf(',');
        if (commaIndex > 0) {
            tamX = input.substring(0, commaIndex).toInt();  // Chuyển tọa độ tamX sang số nguyên
            tamY = input.substring(commaIndex + 1).toInt(); // Chuyển tọa độ tamY sang số nguyên
        }
        Serial.print("Tọa độ tâm là: ");
        Serial.print(tamX);
        Serial.print(" , ");
        Serial.println(tamY);

        // Kiểm tra sự thay đổi của tamX và tamY
        if (tamX != prevTamX || tamY != prevTamY) {
            prevTamX = tamX;  // Cập nhật tọa độ trước đó
            prevTamY = tamY;
            Serial.println("Đang điều khiển động cơ...");

           // Điều khiển servo_fan1 theo tọa độ tamX 
if (tamX > 0 && tamX < 80) {
    servo_fan1.write(130);
    delay(10);
}
else if (tamX > 80 && tamX < 200) {
    servo_fan1.write(120);
    delay(10);
}
else if (tamX > 200 && tamX < 250) {
    servo_fan1.write(110);
    delay(10);
}
else if (tamX > 250 && tamX < 300) {
    servo_fan1.write(95);
    delay(10);
}

else if (tamX > 300 && tamX < 350) {
    servo_fan1.write(80);
    delay(10);
}
else if (tamX > 350 && tamX < 400) {
    servo_fan1.write(65);
            delay(10);
}

else if (tamX > 400 && tamX < 450) {
    servo_fan1.write(50);
    delay(10);
}
else if (tamX > 450 && tamX < 550) {
    servo_fan1.write(40);
    delay(10);
}
else if (tamX > 550 && tamX < 640) {
    servo_fan1.write(30);
    delay(10);
}

 


            // Điều khiển servo_fan2 theo tọa độ tamY 
            if(tamY>0&& tamY<160){
            servo_fan2.write(0);
            delay(10);
            }
            
            
            else if(tamY>160&& tamY<320){
               servo_fan2.write(40);
            delay(10);
            }
                
            
            
            else if ( tamY >320 && tamY<480){
                
                 servo_fan2.write(80);
            delay(10);
            }
        
        else {
            Serial.println("Tọa độ không thay đổi, không điều khiển.");
        }
    }
    
    }
}