// C++ code
struct Button {
  int pin;
  bool state;
  const char* name;
};

Button buttons[] = {
  {2, false, "button a"},
  {4, false, "button b"},
  {5, false, "button rst"},
  {18, false, "button clb"}
};

void setup() {
  for (auto &btn : buttons) {
    pinMode(btn.pin, INPUT_PULLUP);
  }
  Serial.begin(9600);
}

void loop() {
  for (auto &btn : buttons) {
    if (digitalRead(btn.pin) == LOW && !btn.state) {
      Serial.print(btn.name);
      Serial.println(" pressed");
      btn.state = true;
    }
    if (digitalRead(btn.pin) == HIGH && btn.state) {
      btn.state = false;
      Serial.print(btn.name);
      Serial.println(" not pressed");
    }
  }
}