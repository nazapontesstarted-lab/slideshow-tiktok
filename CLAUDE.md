# Projeto: MicroSaaS de Coleta de Documentos Contábeis
## Contexto do Negócio

Estamos validando um MicroSaaS para escritórios contábeis brasileiros.
O problema que queremos resolver é o tempo gasto solicitando, cobrando, organizando e acompanhando documentos enviados pelos clientes dos escritórios.

O produto pretende ajudar o escritório a:
- Visualizar documentos solicitados, recebidos e pendentes.
- Acompanhar pendências por empresa e competência mensal.
- Reduzir o trabalho manual de cobrança.
- Padronizar o processo de coleta.
- Ter uma visão clara do andamento do fechamento mensal.

## Objetivo Atual
Validar a demanda e a disposição real de pagar antes de investir no produto completo. 

Trabalhe nesta ordem:
1. Prospecção primeiro: Identificar escritórios do perfil-alvo, iniciar conversas e registrar evidências reais.
2. Conteúdo em paralelo: Produzir vídeos e outros materiais que ajudem a atrair e qualificar potenciais clientes.
3. Produto/demo por último: Desenvolver ou ajustar a demonstração para apoiar conversas concretas e testar a proposta de valor.

A demo é um instrumento de validação, não o objetivo isolado do projeto. Não construa funcionalidade apenas porque parecem interessantes.

## Como medir sucesso
Acompanhe resultados observáveis, não apenas atividades realizadas. Os indicadores principais são:
- Número de escritórios qualificados identificados.
- Número de escritórios com conversa iniciada e número de conversas efetivas.
- Número de demonstrações agendadas e realizadas.
- Número de compromissos concretos de pagamento.
- Número de pagamentos efetivamente realizados, quando houver.

As metas numéricas ainda precisam ser definidas pelo responsável pelo projeto. Não invente metas, resultados ou evidências; se necessário, registre os valores como a definir em produto/decisoes.md. Diferencie sempre intenção verbal, compromisso explícito e pagamento confirmado.

## Metas
Metas numéricas ainda não definidas pelo responsável. Preencha a tabela abaixo; até lá, não presuma valores.

| Indicador | Meta | Prazo |
|---|---|---|
| Escritórios qualificados identificados | a definir | a definir |
| Conversas efetivas | a definir | a definir |
| Demonstrações realizadas | a definir | a definir |
| Compromissos concretos de pagamento | a definir | a definir |
| Pagamentos realizados | a definir | a definir |

## Público-alvo inicial
- Escritórios contábeis brasileiros.
- Aproximadamente 5-30 funcionários.
- Carteira hipotética de 100–800 empresas clientes.
- Processo atual baseado em WhatsApp, e-mail e planilhas.
- Decisor: sócio-proprietário ou gerente operacional.

Esse perfil é uma hipótese a validar, não uma restrição definitiva.

## Mapa de pastas e fluxo de trabalho
Use as pastas existentes do repositório; não crie uma nova estrutura sem necessidade. As frentes principais são:
- prospeccao/: lista de escritórios, pesquisa, entrevistas, contatos planejados, registros de conversas e acompanhamento de leads.
- conteudo/: ideias, pautas, roteiros, materiais e planejamento de publicação.
- produto/: escopo, demonstração, documentação do produto e produto/decisoes.md, onde devem ser registradas as decisões importantes.

Fluxo de Validação: vídeo/conteúdo -> lead -> conversa -> demo -> evidência de pagamento.

Registre cada etapa na pasta correspondente e mantenha referências entre os registros quando útil. Não trate visualização, curtida ou interesse genérico como evidência de disposição a pagar. Registre apenas o que realmente aconteceu e diferencie fatos, hipóteses e próximos passos.

## Convenções de arquivos e datas
- Use nomes descritivos e consistentes.
- Para materiais numerados, use NN-tema.md, por exemplo 01-proposta-de-valor.md. A numeração é por pasta. Registros e controles contínuos (decisoes.md, calendario.md, funil.csv, metricas.csv, evidencias-pagamento.md), READMEs e modelos (_modelo.md) não são numerados.
- Para registros de escritórios ou entrevistas, use AAAA-MM-DD-escritorio.md, por exemplo 2026-10-21-escritorio-exemplo.md. Evite incluir dados pessoais desnecessários no nome do arquivo.
- Dentro dos documentos, use datas no formato DD/MM/AAAA para leitura humana. Use AAAA-MM-DD em nomes de arquivos e identificadores cronológicos.
- Preserve os arquivos existentes e inspecione seu conteúdo antes de criar duplicatas ou sobrescrever algo.
- Registre decisões de produto, mudanças de escopo e justificativas em produto/decisoes.md. Se o arquivo ou a pasta ainda não existir, proponha sua criação quando fizer sentido; não crie estruturas grandes sem necessidade.
- Não edite arquivos dentro de Cofre/, pois essa pasta é arquivo morto.

## Princípios de Desenvolvimento
1. Priorize simplicidade e velocidade de validação.
2. Implemente apenas o necessário para o próximo experimento com clientes.
3. Não desenvolva funcionalidades futuras sem justificar sua necessidade.
4. Documente decisões importantes e limitações conhecidas.
5. Não declare que testes passaram sem executá-los.
6. Se utilizar dados fictícios, indique que foi usado e identifique-os claramente como demonstração.
7. Evite infraestrutura desnecessária.

## Fluxo de Trabalho Obrigatório
Antes de implementar uma tarefa:
1. Inspecione a estrutura atual do projeto.
2. Identifique os arquivos afetados.
3. Explique brevemente a abordagem proposta.
4. Aponte riscos e dúvidas importantes.
5. Aguarde aprovação quando a tarefa for ampla ou alterar arquitetura.

Durante a implementação:
1. Faça mudanças necessárias para execução da tarefa, com a aprovação do usuário.
2. Evite alterar arquivos que não têm relação.
3. Não sobrescreva trabalho existente sem verificar seu conteúdo.
4. Não instale dependências sem explicar a necessidade.
5. Não execute operações destrutivas sem autorização explícita.

Após a implementação:
1. Execute os testes relevantes disponíveis.
2. Execute lint e build quando aplicável.
3. Corrija os problemas introduzidos pela alteração.
4. Resuma os arquivos modificados.
5. Informe o que foi testado e o que ainda falta verificar.

## Aprovação: o que pode ser feito diretamente
Pode fazer diretamente, dentro do escopo do pedido:
- Criar e editar rascunhos de arquivos no repositório.
- Organizar notas, roteiros, modelos e registros com base em informações fornecidas ou verificadas.
- Fazer alterações pequenas e localizadas de documentação.
- Inspecionar o repositório e executar verificações locais não destrutivas.

Exige aprovação explícita antes de fazer:
- Enviar mensagens, e-mails ou comentários a qualquer pessoa, ou publicar conteúdo em qualquer plataforma.
- Instalar dependências, criar a estrutura de código da demo ou alterar a arquitetura.
- Apagar, mover em massa ou sobrescrever arquivos existentes.
- Fazer deploy, migrações ou qualquer alteração em produção.
- Usar serviços externos, contas ou credenciais, ou enviar dados do projeto a terceiros.
- Registrar metas, preços ou evidências de pagamento que não tenham sido informados ou verificados.

## Regras para Conteúdo e Prospecção
Conteúdo (vídeos curtos/slideshows para TikTok e Instagram):
- Um único CTA por vídeo, slideshow.
- Cada slideshow terá entre 6 e 12 slides.
- O primeiro slide deve apresentar um gancho direcionado ao público.
- Os slides intermediários devem desenvolver uma ideia útil e coerente.
- O último slide deve apresentar um CTA verdadeiro e compatível com o produto.
- Os arquivos finais devem ser PNG, com resolução de 1080 x 1920 pixels.
- Os templates HTML serão renderizados com Playwright e Chromium.
- Gerar imagens exclusivamente por meio de scripts/gerar_imagem.py
- Usar o modelo de imagem configurado e validado na Cloudflare Workers AI.
- Verificar scripts/cota.py antes de cada lote.
- Respeitar o limite diário configurado antes de cada lote.
- Use apenas dados fictícios ou autorizados, identificados como demonstração quando for o caso.
- Não prometa funcionalidades, resultados ou preços que o produto ainda não entrega ou que não foram definidos.
- Não invente depoimentos, números ou casos de clientes.
- Escreva em português brasileiro, com linguagem direta para donos e gerentes de escritórios contábeis.

Prospecção:
- Redija mensagens e scripts como rascunho; o envio é sempre feito pelo responsável.
- Respeite a LGPD e as regras das plataformas contra spam. Não use listas compradas nem envio em massa.
- Registre dados pessoais apenas quando necessário, e nunca dados de clientes dos escritórios.
- Registre somente o que realmente aconteceu, separando fato, hipótese e próximo passo.
- Se um escritório pedir para não ser contatado, registre e não insista.

## Slideshow Farm (slideshows para divulgar o MicroSaaS)

### Objetivo e idioma
- Criar apresentações verticais (PNG) para TikTok e Instagram que atraiam donos e gerentes de escritórios contábeis. Elas são a etapa "conteúdo -> lead" do fluxo de validação.
- As apresentações são geradas manualmente, uma por vez, somente quando o responsável pedir.
- Converse com o responsável em português brasileiro. O conteúdo publicado também é em português brasileiro (regra de conteúdo acima); a variável `APP_LANGUAGE` do `.env` existe, mas seu valor não foi verificado.
- Os temas devem partir de dores reais do público: cobrar, receber e organizar documentos dos clientes e acompanhar o fechamento mensal. Não prometa funcionalidades, resultados ou preços. Não invente depoimentos nem números. Visualizações e curtidas não são evidência de disposição a pagar.

### Estrutura real do projeto (verificada em 22/10/2026)
- `scripts/gerar_farm.py`: ponto de entrada. Menu interativo ou escolha do tema por nome.
- `scripts/modelo_slideshow.py`: carrega e valida os temas, desenha os slides com Pillow, define `slug()` e `pasta_do_tema()`.
- `scripts/cota_slideshows.py`: limite diário de apresentações (`LIMITE_DIARIO = 5`), em `data/cota_slideshows.json`.
- `scripts/cota.py`: limite diário local de imagens de IA (`DAILY_IMAGE_LIMIT`, padrão 5), em `data/cota_diaria.json`.
- `scripts/gerar_imagem.py`: gera imagem na Cloudflare Workers AI (usa o `.env` e rede). O gerador de slides atual NÃO o utiliza.
- `scripts/ajustar_imagem.py`: recorta e redimensiona uma imagem para 1080 x 1920.
- `data/temas.json`: lista de temas `{"tema": texto, "slides": [{"titulo": texto, "texto": texto}, ...]}`. O código exige no mínimo 6 slides por tema.
- `data/historico.json`: `temas_usados` e `execucoes` (`tema`, `data` ISO com fuso, `status`).
- `output/AAAA-MM-DD_slug-do-tema/`: `slide_01.png` ... `slide_NN.png` e `conteudo.json`.
- Estado atual do visual: texto sobre fundo liso, com cabeçalho "GUIA PRÁTICO" e rodapé "SALVE PARA CONSULTAR DEPOIS" fixos no código. A meta de usar templates HTML com Playwright/Chromium e imagens pelo `gerar_imagem.py` continua válida, mas ainda não está implementada.
- Não há servidor MCP configurado no projeto (`.mcp.json` vazio) e nenhum script usa Postiz ou Apify, embora as chaves existam no `.env`.

### Comandos verificados
Use sempre o Python da `.venv` (o Python do sistema não tem o Pillow):
- Gerar com menu: `.venv\Scripts\python.exe scripts\gerar_farm.py`
- Gerar escolhendo o tema por nome: `.venv\Scripts\python.exe scripts\gerar_farm.py "trecho do tema"`
- Ver a cota de apresentações (somente leitura): `.venv\Scripts\python.exe scripts\cota_slideshows.py`
- Ver a cota de imagens (somente leitura): `.venv\Scripts\python.exe scripts\cota.py verificar`
- Compilar os scripts (somente leitura): `.venv\Scripts\python.exe -m py_compile scripts\gerar_farm.py scripts\modelo_slideshow.py scripts\cota_slideshows.py scripts\cota.py`

Cuidados:
- Nunca execute `scripts\modelo_slideshow.py` diretamente: sem argumentos ele gera o primeiro tema sem passar pela cota nem pelo histórico.
- `gerar_imagem.py` chama a Cloudflare e consome cota. Só use com autorização explícita.
- Só liste um comando nesta seção depois de conferir que ele existe e funciona.

### Formato e qualidade
- Slides em PNG, 1080 x 1920 pixels, entre 6 e 12 por apresentação. O código impõe o mínimo de 6; o máximo de 12 é regra editorial, ainda não imposta.
- Um único CTA por apresentação, no último slide, verdadeiro e compatível com o que o produto entrega. O rodapé fixo "SALVE PARA CONSULTAR DEPOIS" também funciona como chamada: confira se não concorre com o CTA do último slide.
- Antes de registrar sucesso, valide: a pasta existe; os nomes são exatamente `slide_01..NN`, sem faltas nem extras; cada imagem abre por completo; todas têm 1080 x 1920.
- Mostre ao responsável a pasta criada, a quantidade de slides validados e a cota após a geração.

### Integridade, cotas e não duplicação
- Ordem obrigatória: verificar a cota, conferir a consistência, gerar, validar, gravar o histórico com status `sucesso` e só então incrementar a cota. Falha na geração ou na validação não grava nada.
- Preserve o histórico, as cotas, `output/` e `data/`. Nunca apague, mova ou sobrescreva pastas de apresentações, nem pastas parciais de falhas, sem autorização explícita.
- Nunca zere, corrija ou ajuste cotas e histórico por conta própria, nem para facilitar testes. Em divergência (por exemplo, mais pastas do dia do que a cota registra, caso em que o `gerar_farm.py` bloqueia), informe os números e proponha uma solução. A alteração só ocorre a pedido explícito do responsável, com cópia prévia dos arquivos.
- Respeite o histórico e as pastas já geradas, sem diferenciar acentos ou maiúsculas. Não repita um tema já usado. Fuso de referência: America/Sao_Paulo.

### Segurança e autorização
- Nunca exiba nem leia valores de tokens, chaves ou senhas. Ao inspecionar o `.env`, mostre apenas os nomes das variáveis. Nunca sobrescreva o `.env`.
- Sem autorização explícita do responsável, não publique, não agende posts, não contate serviços externos (Postiz, Apify, Cloudflare ou outros) e não envie dados a terceiros. Não crie tarefas agendadas do Windows.
- Não configure MCPs, não crie skills e não instale dependências sem pedido e explicação.
- Não gere apresentações durante inspeções, auditorias ou testes, salvo autorização explícita.

### Como trabalhar nesta frente
- Inspecione antes de editar, faça alterações pequenas e explique o que vai mudar antes de alterar arquivos.
- Teste sem tocar nos dados reais: use diretórios temporários e redirecione `ROOT` (em `modelo_slideshow` e `gerar_farm`), `ARQUIVO_HISTORICO` (em `gerar_farm`) e `ARQUIVO` (em `cota_slideshows`). O projeto não tem suíte de testes versionada.
- Relatórios: separe o que foi testado (com o resultado), o que apenas foi configurado ou encontrado e o que continua pendente. Não declare que algo passou sem executar.

### Pendências conhecidas
- As pastas `prospeccao/` e `conteudo/` citadas neste arquivo ainda não existem no repositório; proponha a criação quando for registrar roteiros, calendário ou métricas.
- Os temas atuais em `data/temas.json` ("Organização de documentos", "Checklist para pequenos negócios", "Doc para novos clientes") são genéricos. Confirme com o responsável se servem ao público de escritórios contábeis antes de usá-los para divulgação.
- O limite máximo de 12 slides não é validado pelo código, e os textos fixos do cabeçalho e do rodapé não são configuráveis por tema.

## Interface e Experiência
- Idioma principal: português brasileiro.
- Formatação de datas: DD/MM/AAAA.
- Moeda: real brasileiro (R$).
- Interface responsiva para desktop e celular.
- Navegação simples e textos claros.
- Priorize estados vazios, carregamento, erro e sucesso.
- Utilize dados de demonstração coerentes quando apropriado.
- Não utilize dados reais de clientes em protótipos públicos.

## Segurança e Privacidade
- Nunca exponha segredos, tokens ou credenciais no código.
- Nunca coloque arquivos .env no Git.
- Mantenha chaves privadas exclusivamente no servidor.
- Não utilize dados contábeis reais em ambientes de demonstração.
- Trate documentos contábeis como informações potencialmente sensíveis.
- Antes de implementar autenticação, uploads ou armazenamento real,
  planeje controle de acesso, isolamento entre escritórios e proteção dos arquivos.
- Não faça deploy, migrações destrutivas ou alterações em produção sem autorização.

## Escopo Inicial do Produto
Esse deverá ser a primeira demonstração que inicialmente será uma amostra para demonstrar aos clientes.

Essa demonstração deve priorizar:
- Painel de acompanhamento de documentos.
- Lista de empresas clientes.
- Status de documentos solicitados, recebidos e pendentes.
- Organização por competência mensal.
-  Visualização de lembretes e histórico de solicitações.

Não implementar ainda, sem validação específica:
- Integrações complexas com sistemas contábeis.
- Automação real de WhatsApp.
- Processamento de documentos por IA.
- Planos de cobrança sofisticados.
- Funcionalidades avançadas de administração.

## Regra de Decisão
Quando houver conflito entre adicionar funcionalidades e validar a demanda, priorize validadr a demanda.

O objetivo não é produzir o maior sistema possível. É encontrar se esse mercado possui demanda e clientes dispostos a pagar. Após isso, iremos produzir uma solução que resolvar um problema relevante a esses clientes e pelo qual escritórios contábeis estejam dispostos a pagar.