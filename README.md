# mesh-annotation
## Introdução
Esse guia mostra como fazer recuperação de informação usando o MESH(Medical Subject Headings) como base de busca conectando-o ao solr

## Guia
### Instalação do Solr
Instale em [solr.zip](http://ftp.unicamp.br/pub/apache/lucene/solr/8.3.0/solr-8.3.0.zip), e extraia-o

### Iniciando o solr
Para iniciar o solr precisamos estar dentro do diretorio "solr-8.3.0", dele digitamos

```bin/solr start```

Deverá aparecer algo desse tipo:

```*** [WARN] *** Your open file limit is currently 1024.  
 It should be set to 65000 to avoid operational disruption. 
 If you no longer wish to see this warning, set SOLR_ULIMIT_CHECKS to false in your profile or solr.in.sh
*** [WARN] ***  Your Max Processes Limit is currently 14152. 
 It should be set to 65000 to avoid operational disruption. 
 If you no longer wish to see this warning, set SOLR_ULIMIT_CHECKS to false in your profile or solr.in.sh
Waiting up to 180 seconds to see Solr running on port 8983 [/]  
Started Solr server on port 8983 (pid=20337). Happy searching!
```
### Começando a editar o solr
Para usarmos o solr precisamos criar um "core", ele será o nome do dicionário. Para isso usaremos o seguinte comando

```bin/solr create -c mesh -p 8983```

Devrá aparecer essa mensagem: 

```Created new core 'mesh'```

Este comando cria um core chamado mesh na porta 8983 do computador, então para acessarmos esse dicionário de busca precisamos acessar a porta local 8983 do computador.

Com o core criado é necessário editar a "inteligencia" da busca, ela ficará localizada seguindo o seguinte caminho: ```server/solr/mesh/conf``` o nome do arquivo é ```managed-schema``` e será explicado em detalhes mais a frente. Neste arquivo declararemos os tipos de "fields" que serão usados nos textos, assim como seus formatos.

O banco de dados do mesh ficara no diretório ```example/exampledocs```.

### Banco de dados
Para adicionarmos novos dados ao nosso core precisamos deixar esses dados num formato xml especifico, para isso primeiramente pegaremos os dados do mesh.
#### Instalando o Mesh
O banco de dados do mesh que iremos usar estará no formato XML. Entrando no link a seguir faca o download no [desc2020.zip](https://github.com/Iwazo8700/mesh-annotation/blob/master/buid-solr/desc2020.zip)

#### Edição do Mesh
Com a base instalada vamos editar esse xml para um xml que possa ser lido pelo solr e ser interpretado como informação, o jeito mais fácil que encontrei para fazer isso foi usando xpath e xquery.
O formato do arquivo que devemos chegar é 
```<add>
     <doc>
     <field name=_nome_ boost=_float_>_valor_</field>
     ...
     <\doc>
     ...
   <\add>
```
onde o boost é opcional.

Para tranformar o mesh em um xml válido usei o pragrama [parseXML2XMLsolr.xq](https://github.com/Iwazo8700/mesh-annotation/blob/master/buid-solr/parseXML2XMLsolr.xq), nele transformamos os seguintes dados em fields:
* DescriptorUI
* ConceptName
* ConceptUI
* EntryTerm
* PreviousIndexing
* Annotation
* ScopeNote
* DateCreated
#### Xpath e Xquery(parseXML2XMLsolr.xq)
A lógica usada para fazer esse programa foi usando caminhos que cheguem aonde quero aplicando a / para passar de uma camada para outra até chegar no termo desejado ou quando existia um termo unico usava a // para ir direto ao ponto. O xquery usei no momento e que se tinha um termo que desejava inserir, mas ele não era simples e precisava pegar esse termo várias vezes, para isso usei o conseito de for do xquery. Tudo que precisei fazer nesse ponto foi codificado na xbase, um editor especializado nesse tipo de situação.

```let $mesh := doc("/home/enzo/Documentos/Docker/desc2020.xml")

return
<add>
{
  for $d in ($mesh//DescriptorRecord)
  return
  <doc>
    <field name="ScopeNote" boost="2.0">{$d//ScopeNote/text()}</field>
  </doc>
}
</add>
```

Nesse trecho por exemplo, defini o caminho do desc2020.xml em $mesh, printei o \<add\>, criei um for que passa por cada DescriptorRecord do arquivo, dentro de cada DescriptorRecord printei um \<doc\>, um \<field name="ScopeNote" boost="2.0"\>, o texto do ScopeNote desse DescriptorRecord e fechei o field com \<\\field\>, finalizando esse doc com o <\doc>. Depois de passar por todos DescriptorRecord, finalizo o documento com o \<\\add\>, adquirindo um documento que começa com <add>, termina com \<\\add\>, e dentro desse add vários \<doc\> e \<\\doc\>, cada um com seu ScopeNote. Lembrando que o boost é opcional e só será usado para definir uma prioridade de field na hora da busca.


### Managed-Schema
#### Field
Nesse arquivo temos varios tipos de classes a serem declaradas, mas para criarmos um campo de busca focamos na classe \<field\>, nela iremos declarar quais tipos de campos estarão à disponibilidade de busca.

```<field name=_name_ type=_type_ indexed=_boolean_ stored=_boolean_ required=_boolean_ multiValued=_boolean_ />```

Seguindo esse exemplo criaremos um campo de nome DescriptorUI, do tipo string, indexado, guardado, necassário e simples:

```<field name="ScopeNote" type="string" indexed="true" stored="true" required="false" multiValued="false" />
```

Após fazer isso precisamos dar um Copyfield para adicionar esse field à busca, seguindo o explo a cima, simplesmente escreveriamos a seguinte linha:

``` <copyField source="ScopeNote" dest="_text_"/>```

Após essa duas linha conseguimos adicionar o campo de ScopeNote na busca.

#### fieldType

O fieldType será usado quando se deseja melhorar a forma com que o texto é trabalhado, então no exemplo do ScopeNote declaramos o tipo como uma string, mas caso desejemos tokenizar as palavras, deixá-las em minisculo, entre outros é preciso criar um tipo especifico para isso.
```
<fieldType name="auto_text" class="solr.TextField" positionIncrementGap="100">
    <analyzer type="index">
            <tokenizer class="solr.KeywordTokenizerFactory" />
            <filter class="solr.LowerCaseFilterFactory" />
            <!-- <filter class="solr.EdgeNGramFilterFactory" minGramSize="2" maxGramSize="15" /> -->
    </analyzer>
    <analyzer type="query">
            <tokenizer class="solr.KeywordTokenizerFactory" />
            <filter class="solr.LowerCaseFilterFactory" />
    </analyzer>
</fieldType>
```
Nesse exmplo criamos um tipo chamado auto_text, definimos entao a classe dela como TextField, o qual tem funções de tokenização e minimização de palavras. No analyzer definimos aonde queremos aplicar as funções, seja no "index", texto a ser procurado, ou na "query", o que será procurado. Dentro do analyzer definimos o que queremos aplicar, no caso estamos aplicando uma tokenização e deixamos todas as letras em minusculo, dessa forma podemos fazer buscas mais precisas em vez da busca por acerto exato.

Para aplicar esse novo tipo colocaremos seu nome no lugar do "type" quando declaramos a field, então para colocarmos esse novo tipo na ScopeNote basta fazer isso:

```<field name="ScopeNote" type="auto_text" indexed="true" stored="true" required="false" multiValued="false" />
```
que essa field já aplicará o novo tipo que criamos, ainda  preciso dar um copyField para adicionarmos essa field à busca.




    


