# s3 data
### s3 papkasi strukturasi

    ├── merchant_1
        └── location_1
            └── camera_1
                └── #har kunlik rasmlar date bo'yicha ochilgan folderda saqlanadi (2022-10-9)
            └── camera_2
                └── #har kunlik rasmlar date bo'yicha ochilgan folderda saqlanadi (2022-10-9)

### papkalar haqida ma'lumot
* merchant_ID - Mijoz IDsi (masalan: AloqaBank Idsi 1)
* location_ID - Mijozning filiallari IDsi (masalan: AloqaBankning ITpardagi filiali IDsi 1, Squaredagisining IDsi 2)
* camera_ID - Har bitta bino(filial)da bir nechta kamera bo'lishi mumkin(masalan: kirish eshigidagi kamera IDsi 1, chiqish eshigidagi kamera IDsi 2 va h.z)
* yyyy-mm-dd - Har bir kameradan olingan rasmlar o'sha rasmlar olingan kun sanasi bilan nomlangan papkada saqlanadi(masalan: 2022-10-09)


### s3 data - :point_right: [Bu yerda](https://drive.google.com/drive/folders/18A2Ehy1_ZwvIdjRTQ-4alojpUGQOZ3OE?usp=sharing)

- Linkni bosganingizda `merchant_1`ni ko'rasiz 
- O'shani download qilasiz
- Unzip qiling 
- `data/` folderiga borib `s3` papkani yaratasiz  
- `s3`ga `merchant_1` ni tashlaysiz

**NOTE**: Bu data githubga push qilinmasligi kerak

