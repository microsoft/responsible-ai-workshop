# Responsible AI Workshop - End-to-End Responsible AI Lifecycle Walkthrough for non-Generative AI

This module contains an end-to-end walkthrough of a Responsible AI Lifecycle (RAIL) according to the key phases of a typical product development lifecycle while recognizing that AI product development often cycles through these phases iteratively:
* **Assess & Prepare**. Evaluate the products' benefits, the technology, the potential risks, and the team.
* **Design, Build & Document**. Review the impacts, unique considerations, and the documentation practice.
* **Validate & Support**. Select the testing procedures and the support to ensure products work as intended.

In terms of non-Generative AI product development, it is illustrated by following the complete ML workflow on a loan decision use case using [Azure Machine Learning (Azure ML)](https://azure.microsoft.com/en-us/services/machine-learning/) and its [MLOps capabilities](https://azure.microsoft.com/en-us/services/machine-learning/), the integration with [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/), etc. in the context of AI systems embedded in cloud-native applications, and that provides to this purpose an end-to-end illustration spanning a concrete use case: **Implementing a responsible AI lifecycle for MLOps processes**. 

This walkthrough is meant to accompany the eponym illustration guide [Implementing a responsible AI lifecycle for MLOps processes](https://github.com/microsoft/responsible-ai-workshop/blob/main/nongen-ai-lifecycle-walkthrough/docs/implementing-responsible-ai-lifecycle.docx), which tackles exactly this use case and can be found under the docs folder.

## Prerequisites

Before starting this module, and as far as your execution environment is concerned, we recommend that you read the following notes and ensure that the requirements are fulfilled as per instructions:
* [Cloning this workshop GitHub repo](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/cloning-the-repo.md)
* [Fulfilling the prerequisites for the workshop](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/fulfilling-prerequisites.md)
* [Getting started with Azure for your environment](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/getting-started-with-azure.md) 
* [Using the Jupyter notebook in Azure Data Studio](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/using-jupyter-notebooks-in-azure-data-studio.md)
* [Setting up an Azure DevOps environment](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/setting-up-an-azure-devops-env.md)

## Data

For the sake of the walkthrough, we use the [UCI adult dataset](https://archive.ics.uci.edu/ml/datasets/Adult). 

The data folder includes the datasheet documenting the motivation behind the dataset, it's composition, collection procedure and recommended uses.
