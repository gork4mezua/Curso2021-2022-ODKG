# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fmtSS3q7KcgnX9-eiDTgafkns-u45sU1

**Task 06: Modifying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")
#visualization of the RDF file
for s, p, o in g:
  print(s,p,o)

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))

#print the triple to check that Researcher has been added as a new class
for s, p, o in g.triples((ns.Researcher, None, None)):
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**

"""

g.add((ns.University, RDF.type, RDFS.Class))

#print the triple to check that University has been added as a new class
for s, p, o in g.triples((ns.University, None, None)):
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

g.add((ns.Researcher, RDFS.subClassOf, ns.Person))

#print the triples where Researcher appears to check that Researcher has been added as a subclass of Person
for s, p, o in g.triples((ns.Researcher, None, None)):
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

g.add((ns.JaneSmith, RDF.type, ns.Researcher))

#print the triple to check that Jane Smith has been added as a Researcher
for s, p, o in g.triples((ns.JaneSmith, None, None)):
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**"""

vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
g.add((ns.JaneSmith, vcard.FN, Literal("Jane Smith")))
g.add((ns.JaneSmith, vcard.Given, Literal("Jane")))
g.add((ns.JaneSmith, vcard.Family, Literal("Smith")))

#print all the triples where Jane Smith appears to see what has been added to her
for s, p, o in g.triples((ns.JaneSmith,None,None)):
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

g.add((ns.UPM, RDF.type, ns.University))
#I create a new property (ns.works) to be able to say that John Smith works at UPM
g.add((ns.works,RDF.type,ns.Property))
g.add((ns.JohnSmith, ns.works, ns.UPM))

#let's check that it is correct by printing all the triples where Johhn Smith appears:
for s, p, o in g.triples((ns.JohnSmith,None,None)):
  print(s,p,o)

#I print the whole file in ttl format (for me is easier to visualize the data) to check that the five tasks have been completed been done properly.
print(g.serialize(format="ttl"))
