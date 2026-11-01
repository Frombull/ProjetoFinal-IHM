# Análise da Tarefa (hierárquica)

Notação da aula: `>` sequência, `/` alternativa (escolha), `*` repetição. Planos descritos ao lado de cada nó.
Coerente com a interface publicada (`interface/`) e com os wireframes (telas 1 a 8).

```
0. Descobrir quanto preciso tirar para ser aprovado
   Plano 0: 1 > 2 > 3 > 4 > 5
│
├── 1. Acessar "Meu Desempenho"
│      Plano 1: 1.1 > (1.2 / 1.3)
│   ├── 1.1 Abrir o App Inatel (já logado)
│   ├── 1.2 Abrir o menu lateral e tocar em "Meu Desempenho"   (segue para o passo 2)
│   └── 1.3 Atalho: na tela Notas, tocar em "simular" no card da disciplina   (vai direto ao passo 3)
│
├── 2. Escolher a disciplina
│      Plano 2: 2.1 > 2.2
│   ├── 2.1 Ver a lista de disciplinas com a situação de cada uma
│   └── 2.2 Tocar em "M210 - Otimização I"
│
├── 3. Analisar a situação atual
│      Plano 3: 3.1 / 3.2   (em qualquer ordem)
│   ├── 3.1 Ver as notas lançadas (NP1, laboratórios) e a que falta
│   └── 3.2 Ver a barra de frequência e as faltas restantes
│
├── 4. Simular cenário
│      Plano 4: 4.1 > (4.2 / 4.3)* > 4.4
│   ├── 4.1 Definir a meta de média (padrão 60)
│   ├── 4.2 Ajustar a nota simulada (slider)           * repete até o aluno ficar satisfeito
│   ├── 4.3 Ajustar as aulas que pretende faltar (+ / −)  * idem
│   └── 4.4 Ler nota necessária, média projetada e situação
│
└── 5. Agir sobre o resultado
       Plano 5: 5.1 > (5.2 / 5.3)
    ├── 5.1 Ler os alertas (meta inatingível, poucas faltas restantes)
    │         se a meta é inatingível: tocar em "Ajustar meta" e voltar ao passo 4.4
    ├── 5.2 Salvar a meta e ler a confirmação
    └── 5.3 Sair do simulador (confirma se há alteração não salva) e voltar ao passo 2
```

## Objetivo, submetas e operações

| Nível | Item |
|---|---|
| Objetivo | Saber a nota necessária para aprovação e planejar as faltas |
| Submetas | 1 Acessar, 2 Escolher disciplina, 3 Analisar, 4 Simular, 5 Agir |
| Operações | tocar, arrastar o slider, digitar ou tocar em + / −, ler gráficos e alertas, confirmar |

## Fluxos alternativos e erros

- **Meta inatingível** (nota necessária > 100): alerta vermelho com a média máxima possível e botão "Ajustar meta para X"; "Salvar meta" fica desabilitado (heurística 9, ajudar a reconhecer e corrigir erros).
- **Meta digitada fora de 60 a 100 ou vazia**: o campo balança, mostra a mensagem e volta ao último valor válido (heurística 5, prevenção de erros).
- **Frequência perto ou abaixo de 75%**: aviso destacado no topo, antes de ser tarde (heurística 5).
- **Aprovação já garantida**: aviso verde, sem necessidade de nota nas próximas avaliações.
- **Sem avaliações restantes**: o simulador mostra só o resultado final (sem sliders, sem meta, sem salvar).
- **Aprovação por nota impossível**: alerta explica a média máxima e orienta falar com o professor.
- **Sair sem salvar**: pede confirmação (heurística 3, controle e liberdade).
