# Funcionalidade, persona e User Story

## Funcionalidade: Meu Desempenho (painel de desempenho + simulador de notas)

Nova área do App Inatel onde o aluno acompanha, por disciplina, suas notas e frequência em gráficos e **simula** quanto precisa tirar nas avaliações restantes para ser aprovado, e quantas faltas ainda pode ter.

## Persona

**Lucas Almeida, 20 anos, 3º período de Engenharia de Software.**
- Mora em república, estuda à noite e nos fins de semana, usa o celular o tempo todo.
- Está no limite de média em Cálculo II (foi mal na P1 e na P2) e já faltou algumas aulas.
- Hoje confere notas no portal, faz a conta na calculadora e não sabe ao certo quantas faltas ainda pode ter.
- **Dor:** "Quanto eu preciso tirar na P3 para passar?" e "Posso faltar na sexta?" não têm resposta rápida no app.
- **Objetivo:** decidir onde investir o tempo de estudo e quando pode faltar, sem ansiedade.

Justificativa: a informação de notas e faltas existe, mas dispersa e sem projeção. Transformar esses dados em gráfico e simulação reduz carga cognitiva (heurística 6, reconhecimento em vez de lembrança) e dá visibilidade do status (heurística 1).

## User Story

> **Como** aluno do 3º período com a média no limite em Cálculo II,
> **quero** simular a nota que ainda preciso tirar e acompanhar minha frequência em gráficos,
> **para** saber exatamente quanto preciso na P3 para ser aprovado e quantas faltas ainda posso ter, planejando meus estudos.

### Critérios de aceitação
1. Ver a lista de disciplinas com situação (aprovado, em risco, reprovado por falta/nota).
2. Ver o gráfico de notas por avaliação e a barra de frequência com o limite de faltas.
3. Definir uma meta de média e receber a nota necessária nas avaliações restantes.
4. Ajustar uma nota hipotética (slider) e ver média projetada e situação atualizarem na hora.
5. Receber alerta quando a meta for inatingível ou o limite de faltas estiver perto.
6. Salvar a meta e receber confirmação.

## Regras de negócio (premissas; confirmar com as regras reais do Inatel)

- Nota de 0 a 100; cada avaliação vale seus pontos (pesos somam 100). Média = soma dos pontos obtidos.
- Aprovação: média final >= 60.
- Frequência mínima: 75% das aulas dadas (máx. 25% de faltas).
- Cálculo II (exemplo): P1 (30), P2 (30), P3 (30), Trabalho (10).
- Situação possível: Aprovado (já garantido), Em risco (depende das avaliações restantes), Reprovado por nota (inatingível), Reprovado por falta.
