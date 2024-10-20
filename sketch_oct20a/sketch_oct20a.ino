#define SAMPLE_INTERVAL_MS 200

char buffer[15];
uint32_t t;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  t = millis();
}

void loop() {
  // put your main code here, to run repeatedly:
  if(millis() - t >= SAMPLE_INTERVAL_MS) {
    t = millis();

    sprintf(buffer, "%d,%d,%d", analogRead(A0), analogRead(A1), analogRead(A2));
    Serial.println(buffer);
  }
}
