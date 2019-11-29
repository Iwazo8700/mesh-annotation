# ! wget http://ftp.unicamp.br/pub/apache/lucene/solr/8.2.0/solr-8.2.0.zip -q
# ! unzip -qq solr-8.2.0.zip && rm solr-8.2.0.zip
# ! ./solr-8.2.0/bin/solr start -c
# ! ./solr-8.2.0/bin/solr create -c mesh -p 8983

import pysolr

class Mesh_init:

    def __init__(self):
        solr_server_url = 'http://localhost:8983/solr/'
        solr_collection = "mesh"
        self.solr = pysolr.Solr("http://localhost:8983/solr/mesh")
        self.vet = []
        mesh_read = open("c2020.bin", "r")
        i = -1;
        for linha in mesh_read:
            if(linha == "*NEWRECORD\n"):
                i+=1
                self.vet.append([])
                algo = 0
                algo2 = 0
                algo3 = 0
                a = 0
                self.vet[i] = ["", "NM", "", "SY", "", "PI", "", "PA", "", "NO", ""]
            else:
                l = linha.split("= ")
                if("NM" in l[0] and "NM_TH" not in l[0]):
                    self.vet[i][2]+=l[1]
                elif("SY" in l[0]):
                    l2 = l[1].split("|")
                    self.vet[i][4]+=l2[0]
                elif("PI" in l[0]):
                    self.vet[i][6]+=l[1]
                elif("PA" in l[0]):
                    self.vet[i][8]+=l[1]
                elif("NO" in l[0]):
                    self.vet[i][10]+=l[1]
            self.vet[i][0]+=linha
            #comentar esse if e o break
            if(i > 30):
                break;
        for i in range(len(self.vet)):
            indice = "doc_"+str(i)
            self.solr.add([{
                "ID": indice,
                "Body": self.vet[i][0],
                "Name": self.vet[i][2],
                "Synonym": self.vet[i][4],
                "Previous Indexing": self.vet[i][6],
                "Pharmacological Action": self.vet[i][8],
                "Note": self.vet[i][10],
            },],commit=True)
        mesh_read.close()
    def procura(self, palavra, **kwargs):
        name = kwargs.get("name")
        synonym = kwargs.get("synonym")
        previndexing = kwargs.get("previous_indexing")
        pharaction = kwargs.get("pharmacological_action")
        note = kwargs.get("note")
        retorno = {}
        vet = []
        if(not(name) and not(synonym) and not(previndexing) and not(pharaction) and not(note)):
            results = self.solr.search('Name:{}'.format(palavra))
            for result in results:
                if result not in vet:
                    vet.append({
                        "ID": result["ID"],
                        "Body": result["Body"],
                        "Name": result["Name"],
                        "Synonym": result["Synonym"],
                        "Previous_Indexing": result["Previous_Indexing"],
                        "Pharmacological_Action": result["Pharmacological_Action"],
                        "Note": result["Note"],
                    })
            results=(self.solr.search('Synonym:{}'.format(palavra)))
            for result in results:
                if result not in vet:
                    vet.append({
                        "ID": result["ID"],
                        "Body": result["Body"],
                        "Name": result["Name"],
                        "Synonym": result["Synonym"],
                        "Previous_Indexing": result["Previous_Indexing"],
                        "Pharmacological_Action": result["Pharmacological_Action"],
                        "Note": result["Note"],
                    })
            results=(self.solr.search('Previous_Indexing:{}'.format(palavra)))
            for result in results:
                if result not in vet:
                    vet.append({
                        "ID": result["ID"],
                        "Body": result["Body"],
                        "Name": result["Name"],
                        "Synonym": result["Synonym"],
                        "Previous_Indexing": result["Previous_Indexing"],
                        "Pharmacological_Action": result["Pharmacological_Action"],
                        "Note": result["Note"],
                    })
            results=(self.solr.search('Pharmacological_Action:{}'.format(palavra)))
            for result in results:
                if result not in vet:
                    vet.append({
                        "ID": result["ID"],
                        "Body": result["Body"],
                        "Name": result["Name"],
                        "Synonym": result["Synonym"],
                        "Previous_Indexing": result["Previous_Indexing"],
                        "Pharmacological_Action": result["Pharmacological_Action"],
                        "Note": result["Note"],
                    })
            results=(self.solr.search('Note:{}'.format(palavra)))
            for result in results:
                if result not in vet:
                    vet.append({
                        "ID": result["ID"],
                        "Body": result["Body"],
                        "Name": result["Name"],
                        "Synonym": result["Synonym"],
                        "Previous_Indexing": result["Previous_Indexing"],
                        "Pharmacological_Action": result["Pharmacological_Action"],
                        "Note": result["Note"],
                    })
        if(name):
            results = self.solr.search('Name:{}'.format(palavra))
            for result in results:
                if result not in vet:
                    vet.append({
                        "ID": result["ID"],
                        "Body": result["Body"],
                        "Name": result["Name"],
                        "Synonym": result["Synonym"],
                        "Previous_Indexing": result["Previous_Indexing"],
                        "Pharmacological_Action": result["Pharmacological_Action"],
                        "Note": result["Note"],
                    })
        if(synonym):
            results=(self.solr.search('Synonym:{}'.format(palavra)))
            for result in results:
                if result not in vet:
                    vet.append({
                        "ID": result["ID"],
                        "Body": result["Body"],
                        "Name": result["Name"],
                        "Synonym": result["Synonym"],
                        "Previous_Indexing": result["Previous_Indexing"],
                        "Pharmacological_Action": result["Pharmacological_Action"],
                        "Note": result["Note"],
                    })
        if(previndexing):
            results=(self.solr.search('Previous_Indexing:{}'.format(palavra)))
            for result in results:
                if result not in vet:
                    vet.append({
                        "ID": result["ID"],
                        "Body": result["Body"],
                        "Name": result["Name"],
                        "Synonym": result["Synonym"],
                        "Previous_Indexing": result["Previous_Indexing"],
                        "Pharmacological_Action": result["Pharmacological_Action"],
                        "Note": result["Note"],
                    })
        if(pharaction)
            results=(self.solr.search('Pharmacological_Action:{}'.format(palavra)))
            for result in results:
                if result not in vet:
                    vet.append({
                        "ID": result["ID"],
                        "Body": result["Body"],
                        "Name": result["Name"],
                        "Synonym": result["Synonym"],
                        "Previous_Indexing": result["Previous_Indexing"],
                        "Pharmacological_Action": result["Pharmacological_Action"],
                        "Note": result["Note"],
                    })
        if(note):
            results=(self.solr.search('Note:{}'.format(palavra)))
            for result in results:
                if result not in vet:
                    vet.append({
                        "ID": result["ID"],
                        "Body": result["Body"],
                        "Name": result["Name"],
                        "Synonym": result["Synonym"],
                        "Previous_Indexing": result["Previous_Indexing"],
                        "Pharmacological_Action": result["Pharmacological_Action"],
                        "Note": result["Note"],
                    })
        for i in vet:
            print(i)

        return vet

#mesh = Mesh_init()
#ret = mesh.procura("bevonium")
#ret
