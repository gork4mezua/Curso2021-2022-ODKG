# -*- coding: utf-8 -*-
"""Task08.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-KsHxVCq-QxG_EhdAyLlFLkRWjwntHDl

**Task 08: Completing missing data**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")

print("\n----------GRAPH1")
print("\n")
print(g1.serialize(format="ttl"))
print("\n----------GRAPH2")
print("\n")
print(g2.serialize(format="ttl"))

"""Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas."""

#Define the namespace
ns = Namespace("http://data.org#")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

#Graph Iteration
print("-- Graph Iteration --")
print("\n-----------------------------------------------------------------------------------Let's check it worked:")

for s,p,o in g1.triples((None,RDF.type,ns.Person)):
  #Let's define a variable with the value for each field in g1. Its value is 0 if data is missing
  print("\nPerson:",s)
  for a,b,c in g1.triples((s,None,None)):
    given1 = g1.value(subject=s, predicate=vcard.Given)
    family1 = g1.value(subject=s, predicate=vcard.Family)
    email1 = g1.value(subject=s, predicate=vcard.EMAIL)
    #Now let's do the same with the fields in g2 for the same subject and add it to g1 if it is not there:
    given2 = g2.value(subject=s, predicate=vcard.Given)
    if not given1 and given2:
      g1.add((s, vcard.Given, given2))
    family2 = g2.value(subject=s, predicate=vcard.Family)
    if not family1 and family2:
      g1.add((s, vcard.Family, family2))
    email2 = g2.value(subject=s, predicate=vcard.EMAIL)
    if not email1 and email2:
        g1.add((s, vcard.EMAIL, email2))

  #Let's see the fields in g2 and the new ones in g1 and let's check that they have been added to g1 by serializing it in turtle format
  print("Fields in g2:",given2,family2,email2)
  print("New fields in g1, after adding from g2:",given1,family1,email1)
print("\n-------------------------------------------------------------Visualization of g1 after adding fields of g2:")
print(g1.serialize(format="ttl"))