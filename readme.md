# 👩🏾‍💻 Pipeline de dados: combinando Python e orientação a objeto (Curso)

#### 📌 Este README contém notas de aula.

Estabelecemos um padrão de ambiente de trabalho de engenharia de dados. Este padrão é feito pela composição do ambiente do projeto por meio da criação das pastas: data_processed, data_raw, notebooks e scripts.

o `wget` é usado para baixar arquivos da internet de forma rápida. Aqui usamos:

```
wget https://raw.githubusercontent.com/alura-cursos/Pipeline-de-dados-combinando-Python-e-orientcao-a-objeto/main/data_raw/dados_empresaA.json
```

_"O comando wget é uma ferramenta de linha de comando amplamente utilizada em sistemas Unix e Linux para baixar arquivos da web"_

- Indico ver as opções de adições de comando. Tem uma que permite baixar o conteúdo do site INTEIRO!! :)

### Criação do ambiente virtual

Antes de criá-lo, tive que atualizar e montar o ambiente no meu computador.
Segui os seguintes comandos:

```
sudo apt-get update
sudo apt-get update -y
python3 -V (conferindo a versão do python)
python3 -m venv .venv (ainda nao funciona)
sudo apt install python3-pip -y (instalando o pip)
sudo apt install python3-venv -y (instalando o venv)
python3 -m venv .venv (funcionando)
```

Agora sim, podemos instalar e ativar!

```
python3 -m venv .venv
source .venv/bin/activate
```
