---
name: direcao-de-arte
description: Define e revisa a direção visual dos slideshows verticais (1080 x 1920) do MicroSaaS de coleta de documentos contábeis, compatível com o renderizador atual em Pillow. Use quando o usuário pedir paleta, tipografia, layout de capa, conteúdo e CTA, checagem de legibilidade e contraste, ou consistência visual entre slides.
---

# Direção de arte dos slideshows

Produz uma especificação visual reutilizável e revisa slides ou propostas contra ela. É uma skill de orientação: não gera imagens ou apresentações, não publica e não altera scripts, temas, cotas, histórico nem `output/`. Mudanças em `scripts/modelo_slideshow.py` só são feitas se o usuário pedir, depois de explicar o que será alterado.

## Antes de especificar

1. Leia as regras de conteúdo no `CLAUDE.md` (seções "Regras para Conteúdo e Prospecção" e "Slideshow Farm").
2. Releia `scripts/modelo_slideshow.py` e `data/temas.json`: o código pode ter mudado desde que esta skill foi escrita.
3. Verifique o que existe de fato: `assets/` (não existia na criação desta skill), fontes e logos. Nunca cite um logo, fonte ou arquivo que você não confirmou no disco.

## O que é fato e o que é sugestão

Estado verificado na criação da skill (confirme de novo antes de usar):
- **Marca:** o projeto não define identidade visual oficial, nem logo, nem fontes próprias. Nenhuma cor é "da marca". Não invente cores oficiais; trate qualquer cor como sugestão ou como valor atual da implementação, e peça confirmação ao responsável antes de chamá-la de marca.
- **Renderizador:** Pillow (`modelo_slideshow.py`), com texto sobre fundo liso. Playwright/Chromium e imagens de IA (`gerar_imagem.py`) NÃO fazem parte do fluxo atual de slides; só os cite como evolução futura.
- **Valores atuais no código:** fundo `#F7F1E8`, texto `#202020`, secundária `#6B625A`, destaque `#E87532`. Canvas 1080 x 1920, margem de 100 px. Fonte: Arial do Windows (`C:/Windows/Fonts/arial.ttf`), com Segoe UI como alternativa, ambas somente na versão regular. A hierarquia é feita só por tamanho: cabeçalho 30, título 76, texto 43, rodapé 27.
- **Layout atual:** cabeçalho fixo "GUIA PRÁTICO" com uma barra de destaque no topo; título a partir de y=330; texto a partir de y=650; rodapé fixo "SALVE PARA CONSULTAR DEPOIS" e contador `NN/NN` em y=1795. As linhas de título e texto são centralizadas; cabeçalho e rodapé ficam alinhados à esquerda.

## Princípios visuais

- Uma ideia por slide, texto curto e leitura em poucos segundos no celular.
- Contraste alto e hierarquia clara: título primeiro, texto de apoio depois, elementos de apoio por último.
- Aparência sóbria e confiável, adequada a donos e gerentes de escritórios contábeis. Evite excesso de decoração.
- Consistência: mesma paleta, fonte, margens e posição dos elementos fixos em todos os slides de uma apresentação.

## Paleta (marque cada cor como "valor atual" ou "sugestão")

- Defina funções: fundo, texto principal, texto secundário, destaque e, se necessário, fundo escuro para o slide final.
- Use no máximo uma cor de destaque. Se propor outras cores, indique que são sugestões a validar.
- Calcule o contraste real (fórmula WCAG) em vez de estimar. Medições nos valores atuais, sobre o fundo `#F7F1E8`:
  - `#202020` (texto): 14,5:1, adequado.
  - `#6B625A` (secundária): 5,3:1, adequado para texto de apoio.
  - `#E87532` (destaque): 2,7:1, **insuficiente para texto pequeno**. Hoje ele é usado no cabeçalho de 30 px e no contador de 27 px. Use o destaque em formas grandes e barras e, para texto, uma versão mais escura ou um fundo diferente.

## Tipografia e hierarquia

- Fonte: use somente as que existem. Hoje, Arial e Segoe UI do Windows; a regular é carregada, e as versões em negrito (`arialbd.ttf`, `segoeuib.ttf`) existem na máquina, mas o código ainda não as usa. Trocar para negrito é uma sugestão que exige alterar o script e a aprovação do usuário.
- Escala de referência (valores atuais, em px): título 76, texto 43, rótulos 27 a 30. Em celular, evite texto de apoio abaixo de cerca de 40 px; os rótulos pequenos são só elementos secundários.
- Título: até 3 linhas. Pelo cálculo do código (linhas de cerca de 104 px com o espaçamento atual, a partir de y=330), uma quarta linha invade o início do texto em y=650. Se o título tiver mais de 3 linhas, reduza o texto do título ou reposicione o bloco de texto; não deixe sobrepor.
- Texto: poucas linhas, sem parágrafos longos. Os temas atuais têm títulos de até cerca de 35 caracteres e textos de até cerca de 70.

## Layout por tipo de slide

- **Capa (slide 1):** gancho voltado ao público, título em destaque, sem rodapé concorrente. Nada de excesso de elementos.
- **Conteúdo (slides intermediários):** título curto, uma ideia e um texto de apoio. Mantenha número e posição do contador iguais em todos.
- **CTA (último slide):** um único CTA, verdadeiro e compatível com o produto, em destaque. Evite que o rodapé fixo "SALVE PARA CONSULTAR DEPOIS" dispute atenção com ele; sugira mudar ou ocultar o rodapé neste slide (alteração no script, a pedir ao usuário). Nunca coloque preço, prazo ou promessa não definidos.
- **Margens e zona segura:** mantenha a margem lateral de 100 px. Como sugestão, não coloque informação essencial muito perto do topo e da base, onde a interface das redes costuma cobrir o conteúdo; a distância ideal não foi verificada, então confirme com um teste em publicação privada antes de fixar um valor.
- **Alinhamento:** escolha um padrão por apresentação (centralizado ou à esquerda) e use-o em todos os elementos de texto. O código atual mistura os dois.

## Ícones, formas e decoração

- Use poucas formas simples (barras, círculos, linhas) na cor de destaque. Hoje só existe a barra do cabeçalho.
- Ícones só se vierem de arquivos que existam no projeto ou de formas desenhadas pelo código. Não use logos de terceiros nem invente o logo da marca.
- Dados de exemplo ou telas do produto devem ser fictícios e identificados como demonstração.

## Lista de verificação

1. O slide mede 1080 x 1920 e foi validado em PNG?
2. O contraste de cada texto com o fundo é de pelo menos 4,5:1 (texto pequeno) ou 3:1 (texto grande)?
3. O título cabe em 3 linhas e não invade o texto?
4. Há uma ideia principal e hierarquia clara?
5. Nenhum texto fica a menos de 100 px das bordas laterais?
6. As cores, as fontes e as posições fixas são iguais em todos os slides?
7. O último slide tem um único CTA verdadeiro, sem concorrência do rodapé?
8. Nada no slide promete funcionalidades, preços ou resultados indefinidos, nem usa dados que pareçam reais?
9. Cada afirmação sobre arquivos, fontes ou logos foi confirmada no disco?

## Saída padrão

Entregue, nesta ordem:
1. **Princípios visuais.**
2. **Paleta e tipografia**, com cada item marcado como "valor atual do código", "confirmado pelo responsável" ou "sugestão".
3. **Regras de layout** para capa, conteúdo e CTA.
4. **Verificação de legibilidade e contraste**, com as razões calculadas.
5. **Orientações de consistência** entre slides.
6. **Recomendações compatíveis com o renderizador atual**, separando o que funciona hoje do que exigiria mudar o script (a pedir ao usuário).
7. **Limitações:** o que não foi verificado (por exemplo, a aparência real nas redes).
