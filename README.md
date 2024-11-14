# GSpy
Sistema de Gerenciamento de Consumo de Energia Elétrica ⚡
📋 Descrição Este projeto é um sistema de gerenciamento de consumo de energia elétrica que permite simular o consumo de energia em uma residência, levando em consideração tanto o uso de dispositivos domésticos quanto a previsão de energia solar para o dia. Ele foi criado com o objetivo de ajudar os usuários a monitorar e otimizar seu consumo energético, com a possibilidade de comparar a geração de energia solar com o consumo doméstico.

O sistema permite que o usuário informe o número de horas de uso de diversos dispositivos elétricos e calcule o consumo total de energia. Com isso, o sistema oferece uma visão clara do impacto do uso dos dispositivos e da contribuição da energia solar.

🎯 Funcionalidades Inserção de dados de consumo: O usuário pode inserir o número de horas que usou diversos dispositivos, como luz, aquecedor, ventilador, micro-ondas, entre outros. Previsão de energia solar: O sistema calcula a energia solar prevista para um dia específico da semana (de 1 a 7). Cálculo de consumo energético: Com base nas horas de uso informadas, o sistema calcula o consumo de energia em kWh de cada dispositivo e do total. Comparação entre consumo e geração solar: O sistema informa se o consumo total está dentro ou excede a previsão de geração solar para o dia. 🚀 Como Usar Clone ou baixe o repositório:

bash Copiar código git clone https://github.com/seu_usuario/seu_repositorio.git Entre na pasta do projeto:

bash Copiar código cd caminho/do/seu/repo Execute o script Python:

bash Copiar código python gerenciamento_energia.py Interaja com o sistema:

O programa pedirá que você insira o dia da semana (1 a 7). Depois, será solicitado que você informe as horas de uso de cada dispositivo. O sistema calculará e exibirá o consumo de energia por dispositivo e o consumo total, comparando com a previsão de energia solar. 📊 Exemplo de Execução bash Copiar código Informe o dia da semana (1 - Segunda, 2 - Terça, ..., 7 - Domingo) ou 0 para sair: 3

Previsão de energia solar para hoje (dia 3): 7.00 kWh

Quantas horas você usou o(a) Luz hoje? 5 Quantas horas você usou o(a) Aquecedor hoje? 2 Quantas horas você usou o(a) Eletrodoméstico hoje? 3 Quantas horas você usou o(a) Ventilador hoje? 1 Quantas horas você usou o(a) Micro-ondas hoje? 0 Quantas horas você usou o(a) Computador hoje? 4 Quantas horas você usou o(a) TV hoje? 2

Você consumiu 2.50 kWh com o(a) Luz por 5 horas. Você consumiu 4.00 kWh com o(a) Aquecedor por 2 horas. Você consumiu 4.50 kWh com o(a) Eletrodoméstico por 3 horas. Você consumiu 0.30 kWh com o(a) Ventilador por 1 hora. Você consumiu 0.00 kWh com o(a) Micro-ondas por 0 horas. Você consumiu 3.20 kWh com o(a) Computador por 4 horas. Você consumiu 2.00 kWh com o(a) TV por 2 horas.

Total de energia consumida hoje: 16.50 kWh Você excedeu a previsão de energia solar em 9.50 kWh.

💻 Tecnologias Este projeto foi desenvolvido com as seguintes tecnologias:

Python 3.x Biblioteca padrão do Python (sem dependências externas) ⚙️ Estrutura de Diretórios bash Copiar código . ├── gerenciamento_energia.py # Código-fonte do sistema └── README.md # Este arquivo README 📈 Status e Badges

🛠️ Como Contribuir Faça um fork deste repositório. Crie uma branch para a sua feature (git checkout -b minha-feature). Faça suas modificações e commit as mudanças (git commit -am 'Adiciona nova funcionalidade'). Envie as alterações para o repositório remoto (git push origin minha-feature). Abra um Pull Request. 📄 Licença Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
