# Study Buddy Microservices Simulated Project

Project Python ini mensimulasikan arsitektur Study Buddy microservices dengan layanan Authentication, Group, Messaging, Reminder, Notification, lengkap dengan simulasi database dan event bus.

## Cara menjalankan

1. Pastikan Python 3.7+ sudah terinstall.
2. Jalankan perintah berikut:

```bash
python main.py
```

## Struktur folder dan file

- `main.py`: Entry point aplikasi demo
- `authentication_service.py`: Service untuk user auth dan registrasi
- `group_service.py`: Service untuk pengelolaan grup dan anggota
- `messaging_service.py`: Service chat grup
- `reminder_service.py`: Service pengingat user
- `notification_service.py`: Service notifikasi push
- `database.py`: Simulasi database PostgreSQL, MongoDB, Firebase Realtime
- `event_bus.py`: Simulasi event bus Kafka untuk komunikasi antar service