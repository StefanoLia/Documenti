PARSER = ../../../Tools/glossary/Parse.py
GENERATOR = ../../../Tools/glossary/MakeGlossary.py
CORRECTOR = ../../../Tools/glossary/FixMarkup.py

update :
	$(PARSER) ../..

fix :
	$(CORRECTOR) ../..

pdf :
	$(GENERATOR) ../..
	pdflatex Glossario.tex
	pdflatex Glossario.tex
	rm Glossario.aux Glossario.log Glossario.out Glossario.toc