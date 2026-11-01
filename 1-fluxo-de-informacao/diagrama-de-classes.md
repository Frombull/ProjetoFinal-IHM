# Diagrama de Classes (Fluxo de Informação)

Fonte do diagrama (Mermaid). Usado na entrega 1 e no PDF final. Visibilidade: `+` público, `-` privado.

```mermaid
classDiagram
    direction LR
    class Aluno {
        -nome: string
        -matricula: string
        -curso: string
        -periodo: number
        +listarDisciplinas() DisciplinaCursada[]
        +definirMeta(disc: DisciplinaCursada, valor: number) Meta
        +simular(disc: DisciplinaCursada, hipoteses: Avaliacao[]) Cenario
    }

    class DisciplinaCursada {
        -codigo: string
        -nome: string
        -professor: string
        -notaMinima: number = 60
        +calcularMedia() number
        +pontosRestantes() number
        +situacao() Situacao
    }

    class Avaliacao {
        -nome: string
        -peso: number
        -nota: number
        -data: string
        -realizada: boolean
        +registrarNota(nota: number) void
    }

    class Frequencia {
        -aulasDadas: number
        -faltas: number
        -minimo: number = 75
        +percentual() number
        +faltasRestantes() number
    }

    class Meta {
        -valor: number = 60
        -atingivel: boolean
        +verificar() boolean
        +salvar() void
    }

    class Simulador {
        +notaNecessaria(disc: DisciplinaCursada, meta: Meta) number
        +projetar(disc: DisciplinaCursada, hipoteses: Avaliacao[]) Cenario
    }

    class Cenario {
        -mediaProjetada: number
        -situacao: Situacao
        +gerarAlertas() Alerta[]
    }

    class Alerta {
        -tipo: string
        -nivel: string
        -mensagem: string
        +exibir() void
    }

    class Situacao {
        <<enumeration>>
        APROVADO
        EM_RISCO
        REPROVADO_NOTA
        REPROVADO_FALTA
    }

    Aluno "1" --> "0..*" DisciplinaCursada : cursa
    DisciplinaCursada "1" *-- "1..*" Avaliacao : possui
    DisciplinaCursada "1" *-- "1" Frequencia : possui
    Aluno "1" --> "0..*" Meta : define
    Meta "0..*" --> "1" DisciplinaCursada : refere-se a
    Simulador ..> DisciplinaCursada : usa
    Simulador ..> Meta : usa
    Simulador ..> Cenario : cria
    Cenario "1" *-- "0..*" Alerta : gera
    DisciplinaCursada ..> Situacao : retorna
    Cenario ..> Situacao : retorna
```

## Leitura do diagrama

- **Aluno** cursa várias **DisciplinaCursada** (a disciplina no contexto do aluno, com suas notas e faltas).
- **Composição** (losango cheio): `Avaliacao` e `Frequencia` só existem dentro da disciplina cursada. `Alerta` só existe dentro de um `Cenario`.
- **Meta** é definida pelo aluno para uma disciplina; é o que o usuário salva no passo 5.A da análise da tarefa.
- **Simulador** não guarda estado: recebe disciplina, meta e notas hipotéticas e devolve um **Cenario** com média projetada, situação e alertas. É o que alimenta os gráficos e o feedback da tela.
