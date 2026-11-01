# ProjetoFinal-IHM

Projeto final da matéria **Interface Homem-Máquina** (Engenharia de Software, Inatel, Prof. Raphael Pereira, módulo Ergonomia e Usabilidade). Atividades individuais.

**Objetivo:** desenvolver e documentar uma **nova funcionalidade para o App Inatel**, respeitando a identidade visual do app (cores, tipografia, espaçamentos, componentes responsivos padrão). Pode adaptar o exemplo prático feito em aula, desde que seja coerente com as necessidades dos usuários (persona).

## Aluno

- Nome: Marco Di Toro
- Curso: GES (Engenharia de Software)
- Matrícula: 150

## Entregas

| # | Entrega | Vencimento | Formato | Pasta de contexto |
|---|---------|-----------|---------|-------------------|
| 1 | Fluxo de Informação: diagrama de classes da nova funcionalidade | seg, 02/11/2026 19:59 | PDF no Moodle | `conteudo-de-aula/Entrega Fluxo de informação/` |
| 2 | Wireframe básico (baixa fidelidade) de **todas** as telas do App Inatel com a nova funcionalidade | seg, 09/11/2026 19:59 | PDF no Moodle | `conteudo-de-aula/Entrega testes de usabilidade/` (o nome da pasta não bate com o conteúdo; é a entrega de wireframe) |
| 3 | **Projeto final**: PDF de documentação + interface publicada | sex, 27/11/2026 19:59 | PDF no Moodle | `conteudo-de-aula/Projeto final/` |

## Projeto final: o que entregar

PDF seguindo a ordem do `Exemplo de Formato de Entrega.pdf`:

1. Capa: nome, matrícula, justificativa breve da funcionalidade com base na persona e como funciona no App Inatel, link do projeto (Codepen ou GitHub Pages), tela(s) do projeto num mockup de celular
2. User Story
3. Análise da Tarefa (decomposição hierárquica: objetivo, submetas, operações)
4. Fluxo de Informação (diagrama de classes)
5. Wireframe

**A avaliação é feita exclusivamente sobre a interface publicada** (Codepen ou GitHub Pages). Só código não vale como entrega.

A interface deve simular a tarefa de ponta a ponta, com simulação de input de dados, processamento e feedback ao usuário (diferenciais), além de grid, cores, imagens, animações e interações de qualidade.

### Critérios de avaliação

- Qualidade geral da apresentação do PDF (modelo, coerência, encadeamento, visual)
- Análise da tarefa (objetivo, submetas, operações, notação da metodologia)
- Fluxo de informações (diagrama de classes consistente: entidades, atributos, comportamentos)
- Wireframe (clareza, completude, fidelidade ao planejamento, hierarquia visual, compatibilidade com o fluxo)
- Identidade do Inatel aplicada de forma coerente em todas as telas
- Responsivo para app (várias dimensões mobile, componentes padrão do app)
- Tarefa simulada de ponta a ponta (percurso completo, transições e decisões)
- Input, processamento e feedback (respostas visuais informativas e oportunas)
- Complexidade da tarefa (mais interações, regras de negócio claras e profundidade rendem mais pontos)

## Funcionalidade escolhida

**Meu Desempenho**: painel de desempenho com **simulador de notas** no App Inatel (gráficos de notas por avaliação, barra de frequência com limite de faltas, "quanto preciso tirar na P3?", alertas de risco, salvar meta). Decidido com o aluno; o resto (detalhes, regras, visual) fica a critério do Claude, sem complicar demais.

- Persona: Lucas Almeida, 3º período, no limite em Cálculo II.
- Regras assumidas (confirmar com as reais do Inatel): nota 0-100, aprovação com média >= 60, frequência mínima 75%, pesos P1 30 / P2 30 / P3 30 / Trabalho 10.
- Extensão opcional para o projeto final: botão "Agendar monitoria" quando o aluno estiver em risco.
- Docs: `docs/01-...` (persona e user story), `docs/02-...` (análise da tarefa, notação da aula com planos `1 > 2 / 3`), `docs/03-...` (diagrama de classes em Mermaid, fonte única).
- Formato do professor: análise hierárquica numerada (0, 1, 1.1...) com planos; diagrama de classes com `+/-/#`, multiplicidade e composição/agregação. Exemplo da aula (não repetir): reserva de armário do Fab Lab.

## Estado atual

- [x] Funcionalidade definida (ideia, persona)
- [x] User Story
- [x] Análise da Tarefa (rascunho em `docs/02`)
- [x] Diagrama de classes (entrega 1): `entregas/entrega-1-diagrama-de-classes.pdf`, gerado por `entregas/build.py` + Chrome headless
- [ ] Wireframes (entrega 2)
- [ ] Interface publicada (Codepen/GitHub Pages), código em `app/`, HTML estático + Chart.js
- [ ] PDF final (entrega 3)

Para regerar o PDF da entrega 1: `python entregas/build.py` e imprimir o HTML em PDF com Chrome headless (`--print-to-pdf`, caminhos absolutos).

## Convenções

- Branch principal: `master`.
- Documentação e textos em português (pt-BR).
- Material de aula fica em `conteudo-de-aula/` (somente referência). Documentos de trabalho em `docs/`, código da interface em `app/` (criar quando necessário).
