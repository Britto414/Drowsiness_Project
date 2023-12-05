#include <LiquidCrystal_I2C.h>    
LiquidCrystal_I2C lcd(0x27,16,2); 
char incomingData;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  lcd.begin();      
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Driver Sleep ");
  lcd.setCursor(0,8);
  lcd.print("Detection SYSTEM");
  digitalWrite (LED_BUILTIN, LOW);
  delay(1000);
}

void loop() {
  while (Serial.available()) {
    incomingData = Serial.read();
    if (incomingData == '1') {
      digitalWrite (LED_BUILTIN, HIGH);
      lcd.clear();
      lcd.print("Please wake up");
      Serial.write("LED Turned ON");
    }
    if(incomingData=='2'){
      lcd.clear();
      lcd.print("Not Detected");
    }
    if (incomingData == '0') {
      lcd.clear();
      lcd.print("All Ok");
      lcd.setCursor(0,8);
      lcd.print("Drive Safe");
      digitalWrite (LED_BUILTIN, LOW);
      Serial.write("LED Turned OFF");
    }
    
  }
  
}
