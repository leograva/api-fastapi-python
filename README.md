# api-fastapi-python
API Simples com python utilizando a biblioteca FastApi

Para rodar esse script são necessárias duas bibliotecas:

- Fastapi:
Comando de instalação: pip install fastapi

- Uvicorn: 
Comando de instalação: pip install uvicorn

Após instalá-las execute o seguinte comando a partir da pasta onde está localizado o script:

uvicorn main:app --reload

![image](https://user-images.githubusercontent.com/34873898/138542252-77734ec2-392a-4bfc-a0ca-3e92579575b7.png)

Após isso abra o postman e faça a requisição para os endpoints existentes no arquivo

localhost:8000 -> endpoint de boas vindas

![image](https://user-images.githubusercontent.com/34873898/138542335-c1a6efd7-4129-46df-908c-9e4fcb965653.png)

localhost:8000/numeros/{numero} -> endpoint que retorna o nome por extenso dos números(válidos apenas de 1 a 10).

![image](https://user-images.githubusercontent.com/34873898/138542316-2e28b70a-c67b-4622-a616-7d4921188345.png)
