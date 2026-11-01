"""Gera projeto-final.html (PDF da entrega 3) a partir dos documentos do repositorio.

Fontes reaproveitadas:
  - ../1-fluxo-de-informacao/diagrama-de-classes.md  (diagrama Mermaid)
  - ../2-wireframe/wireframe-v2.pdf                  (2 paginas de wireframe, anexadas ao final)
  - assets/tela-*.png                                (capturas da interface publicada)
Gera projeto-final.html, imprime as paginas-slide com Chrome headless e junta com o wireframe
em projeto-final.pdf. Requer: Chrome instalado e pypdf (pip install pypdf).
"""
import html, re, pathlib

LINK = 'https://frombull.github.io/ProjetoFinal-IHM/'

root = pathlib.Path(__file__).resolve().parent
repo = root.parent

md = (repo / '1-fluxo-de-informacao' / 'diagrama-de-classes.md').read_text(encoding='utf-8')
diagram = html.escape(re.search(r'```mermaid\n(.*?)```', md, re.S).group(1), quote=False)

CSS = '''
@page { size: 960px 540px; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: Roboto, "Segoe UI", Arial, sans-serif; color: #17202e; }

.sl:last-of-type { page-break-after: auto; }
.sl { width: 960px; height: 540px; position: relative; overflow: hidden; page-break-after: always; background: #fff; }
.sl-top { height: 66px; padding: 0 44px; display: flex; align-items: center; gap: 14px; border-bottom: 3px solid #0f2a55; }
.sl-num { width: 30px; height: 30px; border-radius: 50%; background: #0f2a55; color: #fff; display: grid; place-items: center; font-weight: 700; font-size: 15px; }
.sl-top h2 { margin: 0; font-size: 26px; color: #0f2a55; font-weight: 700; }
.sl-top .sl-tag { margin-left: auto; font-size: 12px; color: #5b6b82; }
.sl-body { padding: 18px 44px 0; }
.sl-foot { position: absolute; left: 44px; right: 44px; bottom: 12px; display: flex; justify-content: space-between; font-size: 10.5px; color: #6b7a90; border-top: 1px solid #dde3ec; padding-top: 6px; }

/* capa */
.cv { display: flex; background: #0f2a55; color: #fff; }
.cv-l { width: 560px; padding: 40px 36px 28px 48px; display: flex; flex-direction: column; }
.cv-kicker { font-size: 12px; letter-spacing: .12em; text-transform: uppercase; color: #8fb8f5; }
.cv h1 { margin: 6px 0 4px; font-size: 46px; line-height: 1.05; font-weight: 700; }
.cv-sub { font-size: 16px; color: #cfdcf3; margin-bottom: 18px; }
.cv-id { font-size: 15px; margin-bottom: 14px; }
.cv-id b { font-size: 19px; }
.cv-just { font-size: 12.8px; line-height: 1.5; color: #e4ecf9; }
.cv-just p { margin: 0 0 7px; }
.cv-link { margin-top: auto; background: #fff; color: #0f2a55; border-radius: 8px; padding: 10px 14px; font-size: 12px; }
.cv-link b { display: block; font-size: 10.5px; letter-spacing: .08em; text-transform: uppercase; color: #5b6b82; margin-bottom: 2px; }
.cv-link a { color: #1a5fd0; font-size: 15px; font-weight: 700; text-decoration: none; }
.cv-r { flex: 1; background: linear-gradient(160deg, #16386e, #0a1c3b); display: flex; align-items: center; justify-content: center; gap: 12px; padding-right: 8px; }
.ph { width: 138px; border: 5px solid #05070b; border-radius: 22px; overflow: hidden; background: #000; box-shadow: 0 10px 26px rgba(0, 0, 0, .5); }
.ph img { display: block; width: 100%; }
.ph.mid { width: 150px; margin-top: -26px; }
.ph.lo { margin-top: 44px; }
.ph-cap { text-align: center; font-size: 9.5px; color: #a9c0e6; margin-top: 6px; }

/* user story */
.us { display: flex; gap: 20px; }
.us-persona { width: 250px; background: #f2f6fc; border: 1px solid #d5e0f0; border-radius: 12px; padding: 14px 16px; flex: none; }
.us-av { width: 52px; height: 52px; border-radius: 50%; background: #0f2a55; color: #fff; display: grid; place-items: center; font-size: 24px; font-weight: 700; margin-bottom: 8px; }
.us-persona h3 { margin: 0; font-size: 18px; color: #0f2a55; }
.us-persona .pmeta { font-size: 11.5px; color: #5b6b82; margin-bottom: 8px; }
.us-persona ul { margin: 0; padding-left: 16px; font-size: 11.8px; line-height: 1.45; }
.us-persona li { margin-bottom: 4px; }
.us-main { flex: 1; }
.us-quote { background: #0f2a55; color: #fff; border-radius: 12px; padding: 14px 20px; font-size: 15.5px; line-height: 1.5; }
.us-quote b { color: #8fb8f5; }
.us-h { font-size: 13px; font-weight: 700; color: #0f2a55; margin: 14px 0 6px; text-transform: uppercase; letter-spacing: .06em; }
.us-ac { display: grid; grid-template-columns: 1fr 1fr; gap: 6px 14px; font-size: 12px; line-height: 1.4; }
.us-ac div { display: flex; gap: 8px; }
.us-ac span { flex: none; width: 20px; height: 20px; border-radius: 50%; background: #e3edfb; color: #0f2a55; font-weight: 700; font-size: 11px; display: grid; place-items: center; }
.us-rules { background: #fff8e6; border: 1px solid #f0dca8; border-radius: 8px; padding: 8px 12px; font-size: 11.5px; line-height: 1.45; margin-top: 12px; }

/* analise da tarefa */
.hta-root { position: relative; z-index: 1; margin: 0 auto; width: 430px; text-align: center; background: #0f2a55; color: #fff; border-radius: 10px; padding: 8px 12px; }
.hta-root b { font-size: 15px; }
.plan { font-size: 10.5px; color: #8fb8f5; margin-top: 2px; }
.hta-bar { position: relative; height: 22px; margin: 0 88px; border-top: 2px solid #9db2d1; }
.hta-bar::before { content: ''; position: absolute; left: 50%; top: -22px; height: 22px; border-left: 2px solid #9db2d1; }
.hta-cols { display: flex; gap: 8px; }
.hta-col { flex: 1; position: relative; }
.hta-col::before { content: ''; position: absolute; left: 50%; top: -22px; height: 22px; border-left: 2px solid #9db2d1; }
.hta-h { background: #1a5fd0; color: #fff; border-radius: 8px; padding: 7px 8px; text-align: center; font-size: 12.5px; font-weight: 700; line-height: 1.2; min-height: 48px; display: flex; flex-direction: column; justify-content: center; }
.hta-h .plan { color: #d6e5ff; font-weight: 400; }
.hta-ops { margin-top: 8px; display: grid; gap: 5px; }
.hta-op { background: #eef4fd; border: 1px solid #cfdef5; border-radius: 6px; padding: 5px 7px; font-size: 10.6px; line-height: 1.3; }
.hta-op b { color: #1a5fd0; margin-right: 3px; }
.hta-op.alt { border-style: dashed; background: #fff; }
.hta-sum { display: flex; gap: 10px; margin-top: 12px; font-size: 11px; line-height: 1.4; }
.hta-sum div { flex: 1; background: #f2f6fc; border-radius: 8px; padding: 7px 10px; }
.hta-sum b { color: #0f2a55; }

/* diagrama */
.fi-d { text-align: center; }
.fi-d svg { width: auto !important; max-width: 100% !important; max-height: 372px; height: auto; }
.fi-note { font-size: 11px; color: #44546b; display: flex; gap: 16px; margin-top: 4px; }
.fi-note div { flex: 1; background: #f2f6fc; border-radius: 8px; padding: 6px 10px; line-height: 1.4; }

'''


def phone(img, cls='', cap=''):
    return f'<div><div class="ph {cls}"><img src="assets/{img}"></div><div class="ph-cap">{cap}</div></div>'


def slide(num, titulo, tag, body, pg):
    return f'''<section class="sl"><div class="sl-top"><div class="sl-num">{num}</div><h2>{titulo}</h2><div class="sl-tag">{tag}</div></div>
<div class="sl-body">{body}</div>
<div class="sl-foot"><span>Marco Di Toro · GES · 150 · Interface Homem-Máquina · Prof. Raphael Pereira</span><span>Meu Desempenho · {pg}</span></div></section>'''


cover = f'''<section class="sl cv">
<div class="cv-l">
  <div class="cv-kicker">Projeto final · Interface Homem-Máquina · Inatel</div>
  <h1>Meu Desempenho</h1>
  <div class="cv-sub">Simulador de notas e frequência para o App Inatel</div>
  <div class="cv-id"><b>Marco Di Toro</b><br>Matrícula 150 · GES (Engenharia de Software)</div>
  <div class="cv-just">
    <p><b>Por quê.</b> Lucas, aluno do 3º período, está no limite da média em Otimização I e já faltou algumas aulas. Hoje ele vê notas e faltas no app, mas faz a conta na calculadora e não sabe quantas aulas ainda pode perder.</p>
    <p><b>Como funciona no app.</b> O item <i>Meu Desempenho</i> entra no menu lateral (Aproveitamento Escolar), e a tela Notas ganha o botão <i>simular</i>. O aluno escolhe a disciplina, ajusta a nota simulada e a meta e vê na hora a nota necessária, a média projetada, gráficos, a frequência e as faltas restantes. Alertas avisam de meta impossível ou risco por falta, e a meta pode ser salva.</p>
  </div>
  <div class="cv-link"><b>Interface publicada (GitHub Pages)</b><a href="{LINK}">{LINK}</a></div>
</div>
<div class="cv-r">
  {phone('tela-lista.png', 'lo', 'Escolher disciplina')}
  {phone('tela-simulador.png', 'mid', 'Simulador')}
  {phone('tela-graficos.png', 'lo', 'Resultado e gráficos')}
</div></section>'''

story = slide(1, 'User Story', 'persona e critérios de aceitação', '''
<div class="us">
  <div class="us-persona">
    <div class="us-av">L</div>
    <h3>Lucas Almeida</h3>
    <div class="pmeta">20 anos · 3º período · Engenharia de Software</div>
    <ul>
      <li>Mora em república, estuda à noite e nos fins de semana, usa o celular o tempo todo.</li>
      <li><b>Dor:</b> “Quanto eu preciso tirar na NP2?” e “Posso faltar na sexta?” não têm resposta rápida no app.</li>
      <li><b>Objetivo:</b> decidir onde investir o tempo de estudo e quando pode faltar, sem ansiedade.</li>
    </ul>
  </div>
  <div class="us-main">
    <div class="us-quote"><b>Como</b> aluno do 3º período com a média no limite em Otimização I,<br>
      <b>quero</b> simular a nota que ainda preciso tirar e acompanhar minha frequência em gráficos,<br>
      <b>para</b> saber exatamente quanto preciso na NP2 para ser aprovado e quantas faltas ainda posso ter, planejando meus estudos.</div>
    <div class="us-h">Critérios de aceitação</div>
    <div class="us-ac">
      <div><span>1</span>Ver a lista de disciplinas matriculadas com a situação (em dia, em risco).</div>
      <div><span>4</span>Ajustar uma nota hipotética (slider) e ver média projetada e situação atualizarem na hora.</div>
      <div><span>2</span>Ver as notas lançadas, a barra de frequência e o limite de faltas.</div>
      <div><span>5</span>Receber alerta quando a meta for inatingível ou o limite de faltas estiver perto.</div>
      <div><span>3</span>Definir uma meta de média e receber a nota necessária nas avaliações restantes.</div>
      <div><span>6</span>Salvar a meta e receber confirmação.</div>
    </div>
    <div class="us-rules"><b>Regras de negócio (premissas do projeto):</b> notas de 0 a 100 por avaliação · média = 35% NP1 + 35% NP2 + 30% média dos laboratórios · aprovação com média ≥ 60 · frequência mínima de 75%.
      Exemplo (M210): NP1 48 e laboratórios 70/65/60 → precisa de <b>68</b> na NP2; média máxima possível 71.</div>
  </div>
</div>''', 'User Story')


def col(titulo, plano, ops):
    itens = ''.join(f'<div class="hta-op{" alt" if a else ""}"><b>{n}</b>{t}</div>' for n, t, a in ops)
    return f'<div class="hta-col"><div class="hta-h">{titulo}<div class="plan">{plano}</div></div><div class="hta-ops">{itens}</div></div>'


hta = slide(2, 'Análise da Tarefa', 'decomposição hierárquica (HTA)', f'''
<div class="hta-root"><b>0. Descobrir quanto preciso tirar para ser aprovado</b><div class="plan">Plano 0: 1 &gt; 2 &gt; 3 &gt; 4 &gt; 5</div></div>
<div class="hta-bar"></div>
<div class="hta-cols">
  {col('1. Acessar<br>Meu Desempenho', 'Plano 1: 1.1 &gt; (1.2 / 1.3)', [('1.1', 'Abrir o app (já logado)', 0), ('1.2', 'Menu ☰ › tocar em Meu Desempenho', 0), ('1.3', 'Atalho: tela Notas › “simular” (vai ao passo 3)', 1)])}
  {col('2. Escolher<br>a disciplina', 'Plano 2: 2.1 &gt; 2.2', [('2.1', 'Ver a lista com a situação de cada disciplina', 0), ('2.2', 'Tocar em M210 - Otimização I', 0)])}
  {col('3. Analisar a<br>situação atual', 'Plano 3: 3.1 / 3.2 (qualquer ordem)', [('3.1', 'Ver notas lançadas e a que falta', 0), ('3.2', 'Ver frequência e faltas restantes', 0)])}
  {col('4. Simular<br>cenário', 'Plano 4: 4.1 &gt; (4.2 / 4.3)* &gt; 4.4', [('4.1', 'Definir a meta de média (padrão 60)', 0), ('4.2', 'Ajustar a nota simulada (slider) *', 0), ('4.3', 'Ajustar as aulas que vai faltar (+ / −) *', 0), ('4.4', 'Ler nota necessária, média projetada e situação', 0)])}
  {col('5. Agir sobre<br>o resultado', 'Plano 5: 5.1 &gt; (5.2 / 5.3)', [('5.1', 'Ler os alertas; se a meta é inatingível, “Ajustar meta” e voltar a 4.4', 0), ('5.2', 'Salvar a meta e ler a confirmação', 0), ('5.3', 'Sair (confirma se não salvou) e voltar ao passo 2', 0)])}
</div>
<div class="hta-sum">
  <div><b>Objetivo:</b> saber a nota necessária para a aprovação e planejar as faltas.</div>
  <div><b>Submetas:</b> 1 acessar · 2 escolher a disciplina · 3 analisar · 4 simular · 5 agir.</div>
  <div><b>Operações:</b> tocar, arrastar o slider, digitar ou usar + / −, ler gráficos e alertas, confirmar.</div>
  <div><b>Notação:</b> <b>&gt;</b> sequência · <b>/</b> alternativa · <b>*</b> repetição · borda tracejada = caminho alternativo.</div>
</div>''', 'Análise da Tarefa')

fluxo = slide(3, 'Fluxo de Informação (Diagrama de Classes)', 'mesmas classes e métodos do código da interface', f'''
<div class="fi-d"><div class="mermaid">
{diagram}
</div></div>
<div class="fi-note">
  <div><b>Aluno</b> cursa várias <b>DisciplinaCursada</b>, que possuem (composição) <b>Avaliacao</b> e <b>Frequencia</b>. O aluno define uma <b>Meta</b> por disciplina.</div>
  <div>O <b>Simulador</b> não guarda estado: recebe disciplina, meta e notas hipotéticas e devolve um <b>Cenario</b> com média projetada, situação e <b>Alerta</b>s.</div>
</div>''', 'Fluxo de Informação')

page = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>Projeto Final - Meu Desempenho - Marco Di Toro</title>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.9.1/mermaid.min.js"></script>
<script>mermaid.initialize({{startOnLoad:true, theme:'neutral'}});</script>
</head><body>
{cover}
{story}
{hta}
{fluxo}</body></html>'''
(root / 'projeto-final.html').write_text(page, encoding='utf-8')
print('ok', len(page))

# --- PDF: slides (Chrome headless) + wireframe da entrega 2 ---
import subprocess, tempfile
from pypdf import PdfReader, PdfWriter

CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
slides_pdf = pathlib.Path(tempfile.gettempdir()) / 'projeto-final-slides.pdf'
subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--virtual-time-budget=20000',
                f'--print-to-pdf={slides_pdf}', (root / 'projeto-final.html').as_uri()], check=True, capture_output=True)
w = PdfWriter()
for f in (slides_pdf, repo / '2-wireframe' / 'wireframe-v2.pdf'):
    for p in PdfReader(str(f)).pages:
        w.add_page(p)
w.add_metadata({'/Title': 'Projeto Final - Meu Desempenho (App Inatel) - Marco Di Toro'})
with open(root / 'projeto-final.pdf', 'wb') as fh:
    w.write(fh)
print('pdf ok', len(w.pages), 'paginas')
