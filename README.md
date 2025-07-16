# 🔍 Consulta de DNI con API externa (RENIEC alternativa)

Este proyecto permite consultar datos de personas peruanas por número de DNI usando un servicio externo a RENIEC (https://apis.net.pe).

## Funcionalidades
- Consulta nombre completo a partir de DNI
- Uso de token para acceso autenticado

## Tecnologías
- Python 3
- requests
- python-dotenv
- API `apis.net.pe`

## Cómo usar
1. Instala dependencias:

```bash
pip install requests python-dotenv
```

2. Crea un archivo `.env` con tu token:

```env
RENIEC_TOKEN=tu_token_aqui
```

3. Ejecuta el script:

```bash
python consulta_dni.py
```

✅ Tu token estará protegido y no se subirá a GitHub si usas `.gitignore`

---

Autor: [Luis Vela](https://www.linkedin.com/in/)
