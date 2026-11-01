# Funcionalidade, persona e User Story

## Funcionalidade: Meu Desempenho (simulador de notas + situação por disciplina)

Novo item no menu lateral do App Inatel (seção *Aproveitamento Escolar*, ao lado de Notas e Frequência) e novo botão *simular* nos cards da tela Notas. O app já mostra notas e um gráfico por disciplina; a novidade é **simular** quanto o aluno precisa tirar nas avaliações restantes para ser aprovado, com média projetada, alertas e quantas faltas ainda pode ter.

## Persona

**Lucas Almeida, 20 anos, 3º período de Engenharia de Software.**
- Mora em república, estuda à noite e nos fins de semana, usa o celular o tempo todo.
- Está no limite de média em Otimização I (foi mal na NP1) e já faltou algumas aulas.
- Hoje vê as notas na tela Notas do app, faz a conta na calculadora e não sabe ao certo quantas faltas ainda pode ter.
- **Dor:** "Quanto eu preciso tirar na NP2 para passar?" e "Posso faltar na sexta?" não têm resposta rápida no app.
- **Objetivo:** decidir onde investir o tempo de estudo e quando pode faltar, sem ansiedade.

Justificativa: a informação de notas e faltas existe, mas dispersa e sem projeção. Transformar esses dados em gráfico e simulação reduz carga cognitiva (heurística 6, reconhecimento em vez de lembrança) e dá visibilidade do status (heurística 1).

## User Story

> **Como** aluno do 3º período com a média no limite em Otimização I,
> **quero** simular a nota que ainda preciso tirar e acompanhar minha frequência em gráficos,
> **para** saber exatamente quanto preciso na NP2 para ser aprovado e quantas faltas ainda posso ter, planejando meus estudos.

### Critérios de aceitação
1. Ver a lista de disciplinas matriculadas com situação (em dia, em risco).
2. Ver as notas lançadas, a barra de frequência e o limite de faltas.
3. Definir uma meta de média e receber a nota necessária nas avaliações restantes.
4. Ajustar uma nota hipotética (slider) e ver média projetada e situação atualizarem na hora.
5. Receber alerta quando a meta for inatingível ou o limite de faltas estiver perto.
6. Salvar a meta e receber confirmação.

## Regras de negócio (premissas; confirmar com as regras reais do Inatel)

- Notas de 0 a 100 por avaliação, como na tela Notas do app (NP1, NP2, L1, L2, L3...).
- Média = 35% NP1 + 35% NP2 + 30% média dos laboratórios (L1 a L3). Pesos assumidos.
- Aprovação: média >= 60.
- Frequência mínima: 75% das aulas dadas (máx. 25% de faltas).
- Exemplo (M210 Otimização I): NP1 = 48, laboratórios 70/65/60 (média 65). Nota necessária na NP2 para média 60: **68**. Média máxima possível: 71.
- Situação possível: Aprovado (já garantido), Em risco (depende das avaliações restantes), Reprovado por nota (inatingível), Reprovado por falta.
