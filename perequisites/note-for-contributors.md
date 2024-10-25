# Responsible AI Workshop - Note for contributors 

This note is aimed at content contributors on this [Responsible AI Workshop](https://github.com/microsoft/responsible-ai-workshop) GitHub repo. It provides advice on editing documents on this repo so that they remain consistent and optimized for readers' understanding. 

## Notes management 

When modifying or publishing a document on the repo, the author must **reference the existing notes** for the use of his document and, if these do not exist, he/she should **create a note** and add it to the note directory.  

A note that is missing today may be useful for future documents. 

## Requirements for the creation of any documents 

Whether you are **creating a guide, a presenttaion, a notebook or any other content** on the repo, the following notes should be applied: 

- **Date the document**: certain information may no longer be valid in the future, certain updates may modify the execution of certain code, so dating is essential to place the document in context. 

## Requirements for the creation of notebooks 

Notebooks are used to explain concepts using code that is adapted to the transmission of knowledge. This is the preferred medium for tutorials (as opposed to python files or other languages). 

To maintain consistency and simplify reading, the same structure will be used for each notebook.  

The first section should be the **Download** and **Import libraries** section. This section will call up a requierements.txt file containing all the libraries needed to run the notebook with the version associated. A cell containing the various modules and functions should also be placed here to save time when running the notebook.  

The rest of the notebook should contain as little manipulation as possible for the user, the aim being to have a turnkey tutorial with explanations associated with each part! 

 