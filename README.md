# String Client-Server ZeroMQ

- [Introdução](#Introdução)
- [Dependencias](#Dependências)
- [Vídeo Demonstrativo](#Vídeo-Demonstrativo)

# Introdução

Essa aplicação implementa um par cliente-servidor utilizando ZeroMQ que realiza operações entre duas strings. Tais operações incluem: Concatenação, Distancia de Levenshtein e Checagem de igualdade.

Nessa aplicação, quando conectado com o servidor, multiplos clientes podem enviar os dados necessários para que o servidor possa realizar uma determinada tarefa desajada e retornar uma determinada resposta.

Sockets ZeroMQ conseguem suportar multiplas comunicações, ou seja, um único servidor consegue escutar a partir de várias portas, ao mesmo tempo, utilizando uma operação de bloqueio ```receive```.

# Dependências

- zmq

# Vídeo Demonstrativo

[Link para o Vídeo](https://drive.google.com/file/d/16N8JhvequKdAEb6OQ-TJU4-Znjmr4vLG/view?usp=sharing)
