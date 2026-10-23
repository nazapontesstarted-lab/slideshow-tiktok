---
name: analise-formatos
description: Analisa formatos de slideshows para redes sociais (TikTok/Instagram) a partir de exemplos fornecidos pelo usuário. Use quando o usuário pedir para avaliar, comparar ou entender a estrutura de um slideshow, identificar padrões de abertura, desenvolvimento e CTA, ou sugerir adaptações testáveis para divulgar o MicroSaaS de coleta de documentos contábeis.
---

# Análise de formatos de slideshow

Avalia a estrutura e a qualidade de slideshows de redes sociais e propõe adaptações originais e testáveis para o nosso produto. É uma skill somente de análise: ela não gera, publica nem altera nada.

## Antes de analisar

1. Leia as regras de conteúdo e o escopo do produto no `CLAUDE.md` do projeto (seções "Regras para Conteúdo e Prospecção" e "Slideshow Farm").
2. Confirme o que o usuário forneceu: textos dos slides, imagens, prints, links ou descrições. Analise apenas o que foi fornecido.
3. Se o material for insuficiente (por exemplo, um único slide ou uma descrição vaga), peça o que falta ou analise com limitações explícitas.

## Regras

- Responda em português brasileiro, em linguagem direta.
- Não invente métricas de visualização, retenção, conversão ou engajamento. Só cite números que o usuário forneceu, indicando a origem.
- Não afirme que um formato viraliza ou converte sem evidência. Use "pode ajudar" ou "hipótese", nunca garantias.
- Separe sempre observações visuais e de estrutura (o que se vê nos slides) de dados de desempenho (o que as métricas mostram). Sem dados de desempenho, diga que não há.
- Não copie integralmente o conteúdo de concorrentes. Descreva a estrutura e proponha uma versão original.
- Não acesse sites, APIs ou serviços externos sem autorização explícita do usuário.
- Não publique, não agende e não gere apresentações. Não execute `scripts/gerar_farm.py` nem outros scripts de geração.
- Não altere cotas, histórico, `data/temas.json` nem arquivos em `output/`. Esses arquivos podem ser lidos para contexto, nunca modificados.
- Só grave a análise em arquivo se o usuário pedir; nesse caso, proponha o local antes (por exemplo, `conteudo/`, que ainda pode não existir) e não sobrescreva arquivos existentes.
- Nas sugestões, não prometa funcionalidades, resultados ou preços que o produto ainda não entrega. Não invente depoimentos nem casos de clientes. Use dados fictícios identificados como demonstração, quando necessário.
- Respeite o limite de 6 a 12 slides e o CTA único, previstos nas regras de conteúdo do projeto.

## Critérios de avaliação

- **Abertura:** o primeiro slide apresenta um gancho direcionado a donos e gerentes de escritórios contábeis?
- **Desenvolvimento:** cada slide traz uma ideia, e a sequência é lógica e útil por si só?
- **CTA:** o último slide tem uma chamada única, verdadeira e compatível com o produto?
- **Clareza:** o texto é curto, legível no celular e sem jargão desnecessário?
- **Utilidade:** o público aprende ou resolve algo concreto?
- **Ritmo:** o tamanho de cada slide e a progressão mantêm a atenção sem pressa nem repetição?
- **Coerência:** o gancho, o conteúdo e o CTA falam do mesmo problema?

## Saída padrão

Apresente sempre estas sete seções, nesta ordem:

1. **Resumo do formato:** em duas ou três frases, o que o formato faz e para quem.
2. **Estrutura dos slides:** lista slide a slide (abertura, desenvolvimento, CTA) com a função de cada um.
3. **O que funciona bem e por quê:** cada ponto com a justificativa baseada no que foi observado.
4. **Pontos fracos e riscos:** incluindo riscos de clareza, promessa exagerada, cópia ou desalinhamento com o produto.
5. **Hipóteses a testar:** cada uma escrita como hipótese, com o que seria comparado e como medir (sem prever o resultado).
6. **Sugestão de adaptação original para o nosso produto:** uma estrutura própria, com gancho, desenvolvimento e um único CTA, alinhada ao problema de coletar e acompanhar documentos dos clientes.
7. **Grau de confiança e dados que faltam:** confiança (baixa, média ou alta) com o motivo, e a lista do que faltou (exemplos adicionais, métricas reais, contexto da publicação).

Em cada afirmação, deixe claro se é **fato observado**, **hipótese** ou **recomendação**.

## Análise de vários exemplos

Ao receber mais de um exemplo, descreva primeiro cada um resumidamente. Depois liste os padrões recorrentes (aberturas, número de slides, tipo de CTA), indicando em quantos exemplos cada padrão aparece. Com poucos exemplos, avise que o padrão pode ser coincidência e não generalize.
