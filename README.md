# mesh-annotation
## Introdução
Esse guia mostra como fazer recuperação de informação usando o MESH(Medical Subject Headings) como base de busca conectando-o ao solr

## Guia
### Instalação do Solr
O link a seguir possui o .zip do solr

```http://ftp.unicamp.br/pub/apache/lucene/solr/8.3.0/solr-8.3.0.zip -q```

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

Com o core criado é necessário editar a "inteligencia" da busca, ela ficará localizada seguindo o seguinte caminho: ```server/solr/mesh/conf``` o nome do arquivo é ```managed-schema```. Neste arquivo declararemos os tipos de "fields" que serão usados nos textos, assim como seus formatos.

### Banco de dados
Para adicionarmos novos dados ao nosso core precisamos deixar esses dados num formato xml especifico, para isso primeiramente pegaremos os dados do mesh.
#### Instalando o Mesh
O banco de dados do mesh que iremos usar estará no formato XML. Entrando no link a seguir faca o download no desc2020.zip
```ftp://nlmpubs.nlm.nih.gov/online/mesh/MESH_FILES/xmlmesh/```
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

Para tranformar o mesh em um xml válido usei o pragrama [parseXML2XMLsolr](https://github.com/Iwazo8700/mesh-annotation/blob/master/buid-solr/parseXML2XMLsolr.xq)


### Managed-Schema
Nesse arquivo temos varios tipos de classes a serem declaradas, mas para criarmos um campo de busca focamos na classe \<field\>, nela iremos declarar quais tipos de campos estarão à disponibilidade de busca.

```<field name=_name_ type=_type_ indexed=_boolean_ stored=_boolean_ required=_boolean_ multiValued=_boolean_ />```

Seguindo esse exemplo criaremos um campo de nome DescriptorUI, do tipo string, indexado, guardado, necassário e simples.
```<field name="DescriptorUI" type="string" indexed="true" stored="true" required="true" multiValued="false" />```


