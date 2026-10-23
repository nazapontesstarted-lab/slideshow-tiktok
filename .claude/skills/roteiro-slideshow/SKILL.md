---
name: roteiro-slideshow
description: Transforma uma ideia ou objetivo de marketing em um roteiro original de slideshow vertical (TikTok/Instagram) para divulgar o MicroSaaS de coleta de documentos contábeis, no formato de data/temas.json. Use quando o usuário pedir um roteiro, uma pauta, os slides de um tema novo ou a adaptação de uma ideia para slideshow.
---

# Roteiro de slideshow

Cria um roteiro original, slide a slide, a partir de uma ideia ou objetivo. O roteiro é uma **sugestão**: esta skill não gera imagens, apresentações nem publicações, e só grava em `data/temas.json` com aprovação explícita.

## Antes de escrever

1. Leia as regras de conteúdo e o contexto do produto no `CLAUDE.md` (seções "Regras para Conteúdo e Prospecção", "Slideshow Farm" e "Público-alvo inicial").
2. Leia `data/temas.json` para ver a estrutura real e os temas existentes. Hoje ele é uma lista de objetos `{"tema": texto, "slides": [{"titulo": texto, "texto": texto}, ...]}`; confira de novo, pois pode ter mudado. Não modifique o arquivo nesta etapa.
3. Se a ideia ou o objetivo estiver vago, faça no máximo duas perguntas curtas (quem é o público e qual problema o slideshow resolve) ou assuma o público-alvo do `CLAUDE.md` e diga que assumiu.

## Regras

- Escreva em português brasileiro, com linguagem direta para donos e gerentes de escritórios contábeis.
- Formato final: PNG vertical de 1080 × 1920. Use no mínimo 6 slides (o código rejeita menos) e, pela regra editorial do projeto, no máximo 12.
- Estrutura: abertura com gancho voltado ao público, desenvolvimento lógico e último slide com um CTA único, verdadeiro e compatível com o que o produto entrega hoje.
- Uma ideia principal por slide. Título curto e texto conciso, legível no celular. Como referência, os temas atuais têm títulos de até cerca de 35 caracteres e textos de até cerca de 70; é uma observação, não um limite imposto pelo código.
- Não invente estatísticas, depoimentos, casos de clientes, benefícios, resultados ou promessas. Não cite preços, metas ou prazos: eles estão "a definir" no projeto.
- Descreva o produto apenas pelo que o `CLAUDE.md` define: acompanhar documentos solicitados, recebidos e pendentes por empresa e competência mensal. Não prometa automação de WhatsApp, IA nem integrações com sistemas contábeis.
- Não copie integralmente roteiros de concorrentes. Se o usuário fornecer um exemplo, aproveite apenas a estrutura e reescreva o conteúdo com suas próprias palavras.
- O CTA não pode exigir algo que ainda não existe. Ofereça 2 ou 3 opções de CTA e marque que o responsável deve confirmar qual é verdadeiro no momento (por exemplo, o canal de contato).
- Se citar dados fictícios, identifique-os como demonstração.
- Não acesse serviços externos, não gere imagens ou apresentações, não execute `scripts/gerar_farm.py`, não publique nem agende, e não altere cotas, histórico, arquivos existentes ou `output/`.

## Saída padrão

Apresente sempre, nesta ordem:

1. **Objetivo e público:** a ideia recebida, o público e o problema tratado, indicando o que foi assumido.
2. **Roteiro sugerido:** uma tabela ou lista com número do slide, função (abertura, desenvolvimento ou CTA), título e texto.
3. **Opções de CTA:** 2 ou 3 alternativas, com a observação de que o responsável escolhe a verdadeira.
4. **Checagem:** quantidade de slides, ideia única por slide, ausência de números ou promessas inventadas, e pontos que dependem de confirmação.
5. **Entrada proposta para `data/temas.json`:** um bloco JSON com `tema` e `slides` (`titulo` e `texto`), rotulado como **proposta, ainda não gravada**.

## Gravar em `data/temas.json`

Só faça isso depois que o usuário aprovar o roteiro e pedir para gravar:

1. Releia o arquivo e confirme que o nome do tema não existe, ignorando acentos e maiúsculas, nem consta no histórico ou em `output/`.
2. Faça uma cópia do arquivo antes de alterar. Preserve os temas existentes e acrescente apenas o novo, mantendo JSON válido em UTF-8.
3. Valide a estrutura (campos `tema`, `slides`, `titulo`, `texto` e no mínimo 6 slides) e informe o resultado.
4. Não gere a apresentação. A geração é manual e separada, via `gerar_farm.py`, a pedido do usuário.
