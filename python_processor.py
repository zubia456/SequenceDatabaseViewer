import sys
import re

import xml.dom.minidom
fH = open( 'enzyme_2.xml', 'r' )  
doc = xml.dom.minidom.parse( fH )

fcite = open('E2_citation.txt', 'w')
fauthors = open('E2_authors.txt', 'w')
fseq = open('E2_sequence.txt', 'w')
fstruct = open('E2_struct.txt', 'w')
fref =open('E2_ref.txt', 'w')
entries = doc.getElementsByTagName( 'entry' )


def citationsforarticle(ent):
		citations =ent.getElementsByTagName( 'citation' )

		returncite = []
	
		for cit  in citations:
			if cit.getAttribute('type')!= 'journal article': continue
			dbRefs=cit.getElementsByTagName('dbReference')
		
			pubmedID = None
			for dbRef in dbRefs :
				if dbRef.getAttribute('type') == 'PubMed' :
					pubmedID = int (dbRef.getAttribute('id'))
					
			if not pubmedID : continue
			authors=[]		 
		
			persons = cit.getElementsByTagName('person')
			if not persons :continue
		     
			for person in persons:
				Authors = person.getAttribute('name')
				authors.append(Authors)
			
			if not cit.getElementsByTagName('title'): continue
			Title = cit.getElementsByTagName('title')[0].firstChild.nodeValue
			Journal = cit.getAttribute('name')
			Volume = cit.getAttribute('volume')
			Year = cit.getAttribute('date')
			start = cit.getAttribute('first')
			End = cit.getAttribute('last')
			page = start + '-' + End 

			returncite.append((pubmedID, Title, Journal, Volume, page, Year, authors))

		return returncite

def structureforArticle(ent):
	returnStruct=[]
	dbRefs=ent.getElementsByTagName('dbReference')
	structures = [d for d in dbRefs if d.getAttribute('type')== 'PDB']
	for struct in structures:
			PDBID = struct.getAttribute('id')
			returnStruct.append(PDBID)
	return returnStruct

for entry in entries:
	UNIPROTID = entry.getElementsByTagName('name')[0].firstChild.nodeValue
	FullName =  entry.getElementsByTagName('fullName')[0].firstChild.nodeValue
	organism = entry.getElementsByTagName('organism')[0]
	names = organism.getElementsByTagName('name')
	scientific = None
	for name in names:
		if name.getAttribute('type') == 'scientific':
			scientificName = name.firstChild.nodeValue
	if not scientificName : continue
	
	
	seqs = entry.getElementsByTagName('sequence')
	seqData = None
	for seq in seqs:
		if seq.getAttribute('length'):
			seqData = seq.firstChild.nodeValue
	cites = citationsforarticle(entry)
	Struc = structureforArticle(entry)
	if not seqData: continue			
	     	
	seqData = re.sub('\n', '', seqData)
	
	fseq.write('%s\t%s\t%s\t%s\n'%( UNIPROTID ,FullName,scientificName,seqData))


		
	
	seen = set()
	for cite in cites:
		if not cite[0] in seen:
			
			fcite.write('%d\t%s\t%s\t%s\t%s\t%s\n' %tuple(cite[:6]))
			fref.write('%s\t%d\n' %(UNIPROTID, cite[0]))
			seen.add(cite[0])
		for names in cite[6]:
			fauthors.write('%d\t%s\n' %(cite[0], names))
			
				
	for pdb in Struc:
		fstruct.write('%s\t%s\n' %(UNIPROTID, pdb))
			
				
				


fseq.close()
fcite.close()
fref.close()
fauthors.close()
fstruct.close()
