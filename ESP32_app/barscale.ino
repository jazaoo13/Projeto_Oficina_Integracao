#include <HX711.h>
#include <HardwareSerial.h>
#include <WiFi.h>
#include <ArduinoJson.h>
#include <HTTPClient.h>

#define ADDO  15    //Data Out
#define ADSK  4     //SCK
#define RX 16
#define TX 17
#define BOT1 13
#define BOT2 12
#define DEBTIME 200

struct Botao{
  const uint8_t PIN;
  bool pressed;
};
Botao b1 = {BOT1, false};

HX711 mod_carga;
HardwareSerial leitor(2);     //2 -> RX2/TX2, pinos 16/17

char activate_msg[9] = {0x7e, 0, 8, 1, 0, 2, 1, 0xab, 0xcd};      //mensagem de ativação do leitor de cod
char confirm[7] = {2, 0, 0, 1, 0, 0x33, 0x31};                    //confirmação
String sconfirm(confirm);
char msg[32];                                                     //vetor que recebe a resposta do leitor de cod
String s;
unsigned long last_button_time;

void IRAM_ATTR ISR_tara(){    //interrupção de tara da balança
  if(millis() - last_button_time > DEBTIME){  //debounce
    b1.pressed = true;    
    last_button_time = millis();
  }
}


void post_data(String cod, double peso){
  if(WiFi.status() == WL_CONNECTED){
    HTTPClient http;
    String url = "http://[IP-Servidor]:5000/update_database";
    http.begin(url);
    DynamicJsonDocument jsonDoc(200);
    jsonDoc["cod_barra"] = cod;
    jsonDoc["peso"] = -peso;

    String payload;
    serializeJson(jsonDoc, payload);

    Serial.println(payload);

    http.addHeader("Content-Type", "application/json");
    int response = http.POST(payload);
    http.end();
    if(response > 0){
      Serial.println(response);
    }else{
      Serial.println("ERROR: ");
      Serial.println(response);
    }
  }
}


void setup() {
  Serial.begin(115200);
  leitor.begin(115200,SERIAL_8N1,RX,TX);

  const char* ssid = "Rede";
  const char* pword = "Senha";

  pinMode(ADDO, INPUT_PULLUP);
  pinMode(ADSK, OUTPUT);
  pinMode(b1.PIN, INPUT_PULLUP);

  mod_carga.begin(ADDO, ADSK);    //Configurações da balança
  mod_carga.set_runavg_mode();    //Modo media movel
  mod_carga.set_scale(224.1);     //Escala calculada
  mod_carga.tare();               //Tara

  attachInterrupt(b1.PIN, ISR_tara, FALLING);       //definição da interrupção de tara

  WiFi.begin(ssid,pword);
  Serial.print("Conectando...");
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  Serial.print("Conectado a: ");
  Serial.println(WiFi.localIP());

}

void loop() {
  if(b1.pressed){       //Tratamento da interrupção de tara
    b1.pressed = false;
    mod_carga.tare();
  }
  s = leitor.readStringUntil('\n');
  if(!s.equals(NULL)) post_data(s,mod_carga.get_units());
}
