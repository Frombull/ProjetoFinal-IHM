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

**Meu Desempenho**: **simulador de notas** no App Inatel ("quanto preciso tirar na NP2?", média projetada, gráfico, frequência e faltas restantes, alertas de risco, salvar meta). Decidido com o aluno; o resto (detalhes, regras, visual) fica a critério do Claude, sem complicar demais.

- Persona: Lucas Almeida, 3º período, no limite em M210 Otimização I.
- Regras assumidas (confirmar com as reais do Inatel): notas 0-100 por avaliação, média = 35% NP1 + 35% NP2 + 30% média dos labs (L1-L3), aprovação com média >= 60, frequência mínima 75%.
- Extensão opcional para o projeto final: botão "Agendar monitoria" quando o aluno estiver em risco.
- Docs: `3-projeto-final/01-...` (persona e user story), `3-projeto-final/02-...` (análise da tarefa, notação da aula com planos `1 > 2 / 3`; alinhada com a interface), `1-fluxo-de-informacao/diagrama-de-classes.md` (diagrama em Mermaid, fonte única).
- Formato do professor: análise hierárquica numerada (0, 1, 1.1...) com planos; diagrama de classes com `+/-/#`, multiplicidade e composição/agregação. Exemplo da aula (não repetir): reserva de armário do Fab Lab.

## Como é o App Inatel real (prints do aluno, tema escuro)

- Navegação por **menu lateral** (hambúrguer), sem barra inferior. A tela inicial é *Avisos*. Seções do menu: Mensagens Acadêmicas (Avisos), Aproveitamento Escolar (Notas, Frequência, Material Didático, Plano de Ensino, Histórico, Coeficientes), Atividades Complementares, Calendários e Horários (Provas, Horários de Aula...), Financeiro (Tesouraria), Outras Opções (Requerimentos...).
- Barra superior azul-marinho (☰ + título + 🔍), fundo cinza-escuro/preto, botão azul "Autenticar"/"Outro Usuário", fonte Roboto. Tabelas Avaliação | Nota (coluna de avaliação azul-petróleo, nota cinza). Listas com `›` (ex.: Plano de Ensino > Disciplinas Matriculadas). Alternador Data/Turma na tela Provas.
- A tela **Notas** já lista as disciplinas em cards (ex.: "C216 - Sistemas Distribuídos") com tabela de avaliações (NP1, L1, L2, L3...) e um **ícone de gráfico** por disciplina. Por isso o diferencial da nova funcionalidade é a **simulação**, não só o gráfico.
- Os prints não estão no repositório (contêm dados pessoais do aluno).
- O enunciado do wireframe é ambíguo; interpretação adotada: telas da nova funcionalidade **mais** as telas existentes que levam a ela (menu lateral, Notas), com elementos novos marcados como NOVO.

## Estado atual

- [x] Funcionalidade definida (ideia, persona)
- [x] User Story
- [x] Análise da Tarefa (rascunho em `3-projeto-final/02-analise-da-tarefa.md`)
- [x] Diagrama de classes (entrega 1): `1-fluxo-de-informacao/diagrama-de-classes.pdf`, gerado por `build.py` + Chrome headless
- [x] Wireframes (entrega 2), duas versões em `2-wireframe/`, ambas com 8 telas em 2 páginas A4 paisagem, geradas de HTML escrito à mão impresso com Chrome headless:
  - `wireframe.pdf` (v1): tinha barra inferior e Home inventadas; o aluno gostou e pediu para **não sobrescrever**.
  - `wireframe-v2.pdf`: baseada no app real (menu lateral, tela Notas, padrão do Plano de Ensino). Mais fiel ao app; é a recomendada para a entrega.
- [x] Interface (entrega 3), codigo em `3-projeto-final/interface/` (HTML/CSS/JS puros + Chart.js em `vendor/`, sem build). Tema escuro do app, menu lateral, telas Avisos/Notas (com botao "simular")/lista de disciplinas/simulador (sliders, meta, alertas, 3 graficos, faltas, salvar meta em localStorage, confirmacao ao sair). `js/model.js` espelha o diagrama de classes (mesmos nomes). Painel lateral so no desktop (roteiro de teste, tamanhos de tela). Deep links: `#/notas`, `#/desempenho`, `#/simulador/M210`.
- [x] PDF final (entrega 3): `3-projeto-final/projeto-final.pdf` (capa, User Story, Analise da Tarefa, Fluxo de Informacao + as 2 paginas do `wireframe-v2.pdf`). Gerado por `python 3-projeto-final/build.py` (precisa de Chrome e pypdf). O link do projeto fica na constante `LINK` do script.
- [x] Publicacao (feita em 14/11/2026): repo publico e Pages ativo (source = GitHub Actions). Interface no ar em `https://frombull.github.io/ProjetoFinal-IHM/` (todos os arquivos respondem 200). O workflow `.github/workflows/pages.yml` publica `3-projeto-final/interface` a cada push nessa pasta (ou via `gh workflow run pages.yml`). A copia `https://github.com/Frombull/meu-desempenho-inatel` pode ser apagada.
- [x] PDF v2 com menos texto: `3-projeto-final/projeto-final-v2.pdf`, gerado por `python 3-projeto-final/build-v2.py` (v1 mantido). Mesma estrutura, textos da capa, User Story, Analise da Tarefa e Fluxo enxugados.
- [ ] Antes de enviar: o aluno abre o PDF e a interface (inclusive no celular) para conferir. Foram testados so em Chrome headless (360 e 390 px, desktop); do PDF so se conferiu a contagem de paginas e as paginas-slide como imagem.

### Envio no Moodle (feito pelo aluno)
- Entrega 1 (02/11 19:59): `1-fluxo-de-informacao/diagrama-de-classes.pdf`
- Entrega 2 (09/11 19:59): `2-wireframe/wireframe-v2.pdf` (v1 mantida, nao sobrescrever). **Nota: 100.**
- Entrega 3 (27/11 19:59): `3-projeto-final/projeto-final.pdf` (avaliacao e sobre a interface publicada)

### Pendencias e duvidas em aberto
- Regras reais do Inatel (pesos 35/35/30, media 60, frequencia 75%) sao premissas; se o aluno souber as reais, ajustar `js/data.js`, `js/model.js` e os docs.
- Interpretacao do enunciado do wireframe (so telas novas ou todas do app) ainda nao confirmada com o professor.
- O PDF "Testes de Usabilidade" em `conteudo-de-aula/Entrega testes de usabilidade/` nunca foi lido.
- Extensao opcional "Agendar monitoria" nao foi feita (exigiria atualizar diagrama e wireframe, ja entregues).
- Dados do aluno na interface sao ficticios (Lucas Almeida); nao usar dados pessoais reais.

### Como regerar
- PDF final: `python 3-projeto-final/build.py` (Chrome + `pip install pypdf`). Reaproveita o diagrama (`1-fluxo-de-informacao/diagrama-de-classes.md`) e `2-wireframe/wireframe-v2.pdf`. Se a interface mudar, retirar novas capturas (`3-projeto-final/assets/tela-*.png`, 390x844, dsf 2) com puppeteer-core + Chrome antes.
- Testar a interface: abrir `3-projeto-final/interface/index.html` direto (sem servidor). Fluxo completo: Avisos > menu > Meu Desempenho > M210 > slider/meta/faltas > Salvar.

Para regerar o PDF da entrega 1: `python 1-fluxo-de-informacao/build.py` e imprimir o HTML em PDF com Chrome headless (`--print-to-pdf`, caminhos absolutos).

## Convenções

- Branch principal: `master`.
- Documentação e textos em português (pt-BR).
- Uma pasta por entrega, com tudo dela dentro (fontes, HTML, PDF final):
  - `1-fluxo-de-informacao/`: diagrama de classes
  - `2-wireframe/`: wireframes
  - `3-projeto-final/`: persona, user story, análise da tarefa, `interface/` (código publicado) e o PDF final
- Material de aula fica em `conteudo-de-aula/` (somente referência).
