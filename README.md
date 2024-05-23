# Treinamento e Deploy de Modelos

<div align="center"> 
    Esse repositório traz o código de um treinamento simples de um modelo KNN com 3 vizinhos mais próximos. Além deste treinamento, neste repositório contém um servidor web baseado no framework Django para responder com as predições deste modelo gerado.
</div>

## 1 - Treinamento

O notebook `treinamento.ipynb` dentro da pasta `treinamento` traz uma forma visual e ilustrativa do processo de análise dos dados da base iris e o treinamento de um modelo baseado em 3-NN.

O modelo é salvo com a extensão `.pkl`, ele será utilizado para o serving do modelo na API construída.

## 2 - API

A API utilizada aqui é baseada na arquitetura MVC (Model, View, Controller).
Nesta API, há apenas a rota `api/predict-model`, a qual traz a resposta da predição solicitada. Abaixo, há o padrão do payload a ser passado, é importante destacar que ela é uma rota POST.

```json
{
    "comprimento_sepala": 3.1,
    "largura_sepala": 2.5,
    "comprimento_petala": 5.4,
    "largura_petala": 0.2
}
```

## 3 - Deploy

A fim de facilitar seu uso, foi desenvolvido uma configuração docker para fazer o deploy da api. Antes de iniciar o processo é preciso que seja instalado o docker no ambiente de execução.

Após a instalação do docker é necessário apenas realizar o build da imagem descrita no arquivo Dockerfile dentro da pasta api. Para o build basta usar o comando:  `docker build -t nome-app .`, com esse comando a imagem será construída. Para a execução dela basta utilizar o comando:  `docker run -p 8000:8000 nome-app`. A partir disto, a api irá ter um servidor local e irá responder na porta  `8000`. 