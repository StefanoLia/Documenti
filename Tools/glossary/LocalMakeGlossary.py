#!/usr/bin/python

import Glossary
import os.path
import sys


def main(args, argsc):
    base_dir = './'
    if argsc > 1:
        base_dir = args[1]
        if base_dir[:-1] != '/':
            base_dir += '/'

    glossary = Glossary.Glossary()

    if not glossary.init():
        print('Errore durante l\'inizializzazione del glossario')

    # Generate a directory that hold all the sections.
    if not os.path.exists(base_dir + 'Glossario'):
        os.makedirs(base_dir + 'Glossario')

    include_file = open(base_dir + 'Glossario.tex', 'w')

    # Iterate over the sections
    for title, section in glossary:
        include_file.write('\input{Sezioni/' + title + '.tex}\n')
        print('Sezione : ' + title)
        # Open the file for output
        file = open(base_dir + 'Glossario/' + title + '.tex', 'w')
        # Write the file header
        file.write("\subsection*{" + title + "}\n")
        file.write("\\begin{itemize}\n")
        # Iterate over the words of the current section
        for word, description in section:
            # Write to file
            file.write('\t\item\n')
            file.write('\t\\textbf{' + word + '}: ' + description + '.\n')
            print('Parola: ' + word + ' Descrizione: ' + description)
        # Write the end of the section
        file.write('\end{itemize}\n')
        # Add a black page
        file.write('\\newpage')
        # Release the resource
        file.close()
    include_file.close()

if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
