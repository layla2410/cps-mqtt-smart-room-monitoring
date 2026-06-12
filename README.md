# Smart Room Monitoring - MQTT Communication

Project akhir Cyber Physical System: implementasi komunikasi MQTT menggunakan Python (paho-mqtt) dan Mosquitto Broker, dengan studi kasus Smart Room Monitoring.
Nama: Layla 'Afifah Ramadhani
NIM: 245150301111007
Kelas: Cyber Physical System A

## Struktur Topik

```
home/room1/temperature
home/room1/humidity
home/room1/motion
home/room1/light/status
home/room2/temperature
home/room2/humidity
```

## Requirements

- Python 3.x
- Mosquitto Broker (running on localhost:1883)
- Library: paho-mqtt

## Instalasi

1. Install Mosquitto Broker (Windows): download dari https://mosquitto.org/download/, lalu pastikan service "Mosquitto Broker" berjalan (cek di Services)

2. Setup Python environment:
```bash
python -m venv venv
venv\Scripts\activate
pip install paho-mqtt
```

## Cara Menjalankan

Setiap skenario membutuhkan 2 terminal: subscriber (jalankan dulu) dan publisher.

### Skenario 1: Komunikasi Dasar Publisher-Subscriber
Terminal 1:
```bash
python subscriber_basic.py
```
Terminal 2:
```bash
python publisher_basic.py
```
Publisher mengirim data suhu ke topik `home/room1/temperature` dengan QoS 0, subscriber menerima dan menampilkannya.

### Skenario 2: Pengiriman Data dengan QoS Berbeda (0, 1, 2)
Terminal 1:
```bash
python subscriber_qos.py
```
Terminal 2:
```bash
python publisher_qos.py
```
Publisher mengirim data secara bergantian dengan QoS 0, 1, dan 2 ke topik yang sama.

### Skenario 3: Penggunaan Beberapa Topik
Terminal 1:
```bash
python subscriber_multitopic.py
```
Terminal 2:
```bash
python publisher_multitopic.py
```
Publisher mengirim ke 5 topik berbeda (room1: temperature, humidity, motion; room2: temperature, humidity). Subscriber hanya subscribe ke 3 topik spesifik (`home/room1/temperature`, `home/room1/humidity`, `home/room2/temperature`).

### Skenario 4: Wildcard `+`
Terminal 1:
```bash
python subscriber_wildcard_plus.py
```
Terminal 2:
```bash
python publisher_multitopic.py
```
Subscriber subscribe ke `home/+/temperature`, sehingga menerima data temperature dari **room1 dan room2** sekaligus.

### Skenario 5: Wildcard `#`
Terminal 1:
```bash
python subscriber_wildcard_hash.py
```
Terminal 2:
```bash
python publisher_multitopic.py
```
Subscriber subscribe ke `home/room1/#`, sehingga menerima **semua data** dari room1 (temperature, humidity, motion).

## Struktur File

```
cps_mqtt_project/
├── publisher_basic.py
├── subscriber_basic.py
├── publisher_qos.py
├── subscriber_qos.py
├── publisher_multitopic.py
├── subscriber_multitopic.py
├── subscriber_wildcard_plus.py
├── subscriber_wildcard_hash.py
├── screenshots/
├── docs/
└── README.md
```

## Penjelasan QoS

- **QoS 0** (At most once): pesan dikirim sekali tanpa konfirmasi, bisa hilang jika koneksi terputus
- **QoS 1** (At least once): ada acknowledgment (PUBACK), pesan dijamin diterima tapi bisa duplikat
- **QoS 2** (Exactly once): handshake 4 langkah, paling reliable tapi overhead paling besar

## Penjelasan Wildcard

- **`+`**: menggantikan satu level topik (contoh: `home/+/temperature` cocok dengan `home/room1/temperature` dan `home/room2/temperature`)
- **`#`**: menggantikan semua level topik di bawahnya (contoh: `home/room1/#` cocok dengan semua topik di bawah `home/room1/`)

## Author

[Layla 'Afifah Ramadhani] - [245150301111007]
[GitHub: https://github.com/layla2410/cps-mqtt-smart-room-monitoring]
