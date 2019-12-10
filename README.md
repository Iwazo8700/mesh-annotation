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
Para usarmos o solr precisamos criar um "core", ele será o nome do dicionário. Para isso usaremos o seguinte comando

```bin/solr create -c mesh -p 8983```

Este comando cria um core chamado mesh na porta 8983 do computador, então para acessarmos esse dicionário de busca precisamos acessar a porta local 8983 do computador.

Com o core criado é necessário editar a "inteligencia" da busca, ela ficará localizada seguindo o seguinte caminho: ```server/solr/mesh/conf``` o nome do arquivo é ```managed-schema```. Neste arquivo declararemos os tipos de "fields" que serão usados nos textos, assim como seus formatos.
### Managed-Schema
Nele temos dois tipos principais de classes, a <field> e a <fieldType>, a field será usada para declarar novos campos de busca, e a fieldType para especificar como será a entrada e saida da field 

### Instalando o Mesh
O banco de dados do mesh que iremos usar estará no formato XML
Entrando no link a seguir faca o download no desc2020.zip
```ftp://nlmpubs.nlm.nih.gov/online/mesh/MESH_FILES/xmlmesh/```
