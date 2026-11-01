"""Gera entrega-1-diagrama-de-classes.html a partir de docs/03-diagrama-de-classes.md."""
import html, re, pathlib
root = pathlib.Path(__file__).resolve().parent
md = (root.parent / 'docs/03-diagrama-de-classes.md').read_text(encoding='utf-8')
diagram = html.escape(re.search(r'```mermaid\n(.*?)```', md, re.S).group(1), quote=False)
page = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>Entrega 1 - Diagrama de Classes</title>
<style>
@page {{ size: A4 landscape; margin: 10mm; }}
body {{ font-family: Arial, Helvetica, sans-serif; color:#111; margin:0; }}
header {{ border-bottom: 3px solid #0b3c78; padding-bottom:4px; margin-bottom:6px; }}
h1 {{ font-size:18px; margin:0; color:#0b3c78; }}
.meta {{ font-size:11px; margin-top:3px; }}
p {{ font-size:11px; margin:3px 0; }}
.mermaid {{ text-align:center; }}
.mermaid svg {{ width:auto !important; max-width:100% !important; max-height:158mm; height:auto; }}
</style></head><body>
<header>
<h1>Fluxo de Informação: Diagrama de Classes</h1>
<div class="meta"><b>Marco Di Toro</b> | GES | Matrícula 150 | S205 Interface Homem-Máquina | Prof. Raphael Pereira</div>
</header>
<p><b>Funcionalidade:</b> <i>Meu Desempenho</i>, painel de desempenho com simulador de notas para o App Inatel. O aluno acompanha notas e frequência por disciplina e simula quanto precisa tirar nas avaliações restantes para ser aprovado.</p>
<div class="mermaid">
{diagram}
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.9.1/mermaid.min.js"></script>
<script>mermaid.initialize({{startOnLoad:true, theme:'neutral'}});</script>
</body></html>'''
(root / 'entrega-1-diagrama-de-classes.html').write_text(page, encoding='utf-8')
