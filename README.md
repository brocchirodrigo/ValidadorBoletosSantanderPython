# Construtor simplificado e validador de linha digitável Santander!

  -> Feito em Python e não requer outras bibliotécas (recomendado usar a versão 3.8)
  -> Referência da documentação oficial do Banco Santander Brasil
    * Constrói a linha conforme a especificação do Santander
    ** Possível revalidar a linha com as funções disponíveis

## Construtor de linha

- Executar o main.py
  - Passar a data de vencimento sendo ano (4 dígitos), mês (2 dígitos) e dia (2 dígitos) => 2020-03-21
  - Valor como texto separado apenas por ponto na casa de centavos (99999.99)
  - O cedente (que são os últimos 6 dígitos do convênio Santander)
  - Por último os 12 dígitos do nosso número (não precisa passar o 13º dígito do nosso número, o código calcula e gera o dígito verificador).

** Como resultado será gerada a linha digitável e o código de barras Santander.

## Funções disponíveis

from ValidateGroup import ValidateGroup
  - Passar na "verifyTicket" até 12 número que serão o nosso número do boleto (verifyTicket(*000000000000*))

from ValidateDigitCode import verifyTicketCode
  - A linha de código de barras do Santander possui 4 sequências numéricas que possui um dígito validador e essa função faz um cálculo simples para definir o dígito de cada bloco.

from ValidateDigitCode import verifyTicketCode
  - Calcula o dígito que é gerado sobre a definição do código de barras e inserido na linha digitável (5º dígito verificador ligado ao código de barras).
