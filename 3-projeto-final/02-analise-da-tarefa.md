# Análise da Tarefa (hierárquica)

Notação da aula: `>` sequência, `/` alternativa (escolha), `*` repetição. Planos descritos ao lado de cada nó.

```
0. Descobrir quanto preciso tirar para ser aprovado
   Plano 0: 1 > 2 > 3 > 4 > 5
│
├── 1. Acessar "Meu Desempenho"
│      Plano 1: 1.1 > (1.2 / 1.3)
│   ├── 1.1 Abrir o App Inatel (já logado)
│   ├── 1.2 Abrir o menu lateral e tocar em "Meu Desempenho"
│   └── 1.3 Atalho: na tela Notas, tocar em "simular" no card da disciplina (vai direto ao passo 4)
│
├── 2. Escolher a disciplina
│      Plano 2: 2.1 > 2.2
│   ├── 2.1 Ver lista de disciplinas com status
│   └── 2.2 Tocar em "M210 - Otimização I"
│
├── 3. Analisar a situação atual
│      Plano 3: 3.1 / 3.2   (em qualquer ordem)
│   ├── 3.1 Ver notas lançadas (NP1, L1 a L3)
│   └── 3.2 Ver barra de frequência e faltas restantes
│
├── 4. Simular cenário
│      Plano 4: 4.1 > 4.2 *> 4.3
│   ├── 4.1 Definir meta de média (padrão 60)
│   ├── 4.2 Ajustar nota simulada da NP2 (slider)   * repete até o aluno ficar satisfeito
│   └── 4.3 Ler nota necessária, média projetada e situação
│
└── 5. Agir sobre o resultado
       Plano 5: A / B / C
    ├── A. Salvar meta (confirmação)
    ├── B. Ver alerta de risco (nota inatingível ou poucas faltas restantes)
    └── C. Voltar e escolher outra disciplina  (volta ao passo 2)
```

## Objetivo, submetas e operações

| Nível | Item |
|---|---|
| Objetivo | Saber a nota necessária para aprovação e planejar faltas |
| Submetas | 1 Acessar, 2 Escolher disciplina, 3 Analisar, 4 Simular, 5 Agir |
| Operações | toques, arraste de slider, leitura de gráfico, confirmação |

## Fluxos alternativos e erros

- **Meta inatingível** (nota necessária > pontos restantes): alerta vermelho com sugestão, em linguagem simples (heurística 9).
- **Frequência abaixo de 75%**: aviso destacado na barra, antes de ser tarde (heurística 5, prevenção de erros).
- **Sem avaliações restantes**: simulador desabilitado, mostra resultado final.
- **Sair sem salvar**: pede confirmação (heurística 3, controle e liberdade).
