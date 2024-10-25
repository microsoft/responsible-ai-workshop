# Responsible AI Workshop - Fulfilling  prerequisites

Before you begin with the workshop, you should ensure that your execution environment fulfill the main technical prerequisites outlined below. 

As such, the workshop notably assumes that you have access to an Azure subscription. If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/en-us/free/).

In addition, most, if not all, of the modules (and related guide(s)) in this workshop contain Jupyter notebooks and python scripts. Here's a note explaining the various prerequisites for these to work properly. 

The **Prerequisites** section of each module of the workshop will provide if needed additional information.

## Execution environment 

The choice of environment depends on your needs and constraints. If you want to run your application locally, we recommend using **Visual Studio Code (VS Code)**, while for a dematerialized version, **Github CodeSpaces** is a good alternative. If you want to integrate other Azure components, **Azure Machine Learning (Azure ML)** also offers a notebook interpreter. Finally, **JupiterLab** is another local solution if you have other specific needs. Once selected, notebooks run in the same way in all environments. 

## VS Code 

[Visual Studio Code (VS Code)](https://code.visualstudio.com/) is a free code editor and development platform that you can use locally on your Linux, MacOS or Windows environments, or connected to remote compute.  

Combined with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) (and the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)), it offers a full environment for Jupyter development that can be enhanced with additional language extensions. If you want a best-in-class, free Jupyter experience with the ability to leverage your compute of choice, this is a great option. Using VS Code, you can develop and run notebooks on remotes and containers.  

Instructions on how to get started with notebooks in VS code (optionally using container) are provided [here](https://code.visualstudio.com/docs/datascience/jupyter-notebooks). 

## CodeSpaces 

[GitHub CodeSpaces](https://docs.github.com/en/codespaces) provide you with cloud-hosted environments where you can edit your notebooks using VS Code or your web browser and store them on GitHub.  

GitHub CodeSpaces offers the same great Jupyter experience as VS Code above, but without needing to install anything on your local environment. GitHub CodeSpaces also allows you to use your cloud compute of your choice. If you don’t want to set up a local environment and prefer a cloud-backed solution, then creating a codespace is a great option. 

Instructions on how to get started with notebooks in your own codespace are provided [here](https://code.visualstudio.com/docs/datascience/jupyter-notebooks). 

## Azure ML 

[Azure Machine Learning (Azure ML)](https://azure.microsoft.com/en-us/services/machine-learning/) provides an end-to-end ML platform to enable you to build and deploy models faster on Azure. 

Azure ML allows you to run notebooks on a virtual machine (VM) or a shared cluster computing environment. If you need a cloud-based solution for your ML workload with experiment tracking, dataset management, and more, we recommend Azure ML. 

To run the Jupyter notebooks in your Machine Learning workspace, please note that if you choose this option, there are two prerequisites: 

1. Having an Azure subscription. If you don't have an Azure subscription yet, you can create a free account [here](https://azure.microsoft.com/free/). 

2. Having a Machine Learning workspace. You will find instructions on how to setup one using the Azure portal [here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace?tabs=python). 

Instructions on how to get started with Azure ML are provided [here](https://aka.ms/aznb-aml). 

Other options to run Jupyter notebooks using products and services from Microsoft and GitHub exist. They can be found here. 

## JupyterLab 

[JupyterLab](https://jupyter.org/) is a web-based interactive development environment for creating such [Jupyter notebooks](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html). 

JupyterLab provides flexible building blocks and an [interface](https://jupyterlab.readthedocs.io/en/stable/user/interface.html) for interactive, exploratory computing with, at its core, the ability to configure and arrange the user interface (UI), manipulate data with [Python](https://www.python.org/) and display inline graphs, e.g., diagrams and/or dashboards from the results, etc. to support a wide range of data science and ML workflows. 

Official instructions on how to install JupyterLab are provided [here](https://jupyter.org/install.html). For Windows 10 users, JupyterLab can be installed for example with the[ Windows Subsystem for Linux (WSL) 2](https://docs.microsoft.com/en-us/windows/wsl/install-win10) or through the [Anaconda open-source distribution](https://www.anaconda.com/products/individual#Downloads). 

## Python version 

Python is a free, cross-platform, open-source developer platform for building many different types of applications. However, choosing a specific Python version may be necessary. We recommend using [Pyenv](https://github.com/pyenv/pyenv) or [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) (with for example the installer [Anaconda Distribution](https://www.anaconda.com/download)) to easily switch between versions in your virtual environments. You will then need to select the correct environment when running the notebook locally. For more information on kernels for **VS Code**, please visit the following [link](https://code.visualstudio.com/docs/python/environments).  