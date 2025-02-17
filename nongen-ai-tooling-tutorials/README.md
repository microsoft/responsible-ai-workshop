# Responsible AI Workshop - Non-generative AI tooling tutorials

This module contains a series of hands-on tutorials for Microsoft's most prominent responsible AI (RAI) tools/toolkits for non-generative, a.k.a. traditional, AI systems.

It is primarily designed for developers and data scientists to provide them with jump-start tutorials for using each tool, in the form of Jupyter notebooks. 

## Overview of the available hands-on tutorials

We investigate three categories of RAI tools:

* Tools to **understand the behavior of AI systems**. These in turn fall into two categories covered here:
    - Tools to assess and mitigate fairness issues. Here we focus on **Fairlearn**.
    - Tools to understand and explain AI systems predictions. Here we focus on **InterpretML** and **Error Analysis**.
* Tools to **understand how an AI model might be compromised** by adverserial attacks:
    - Using **Counterfit** to perform a white-box attack on a vanilla model
    - Using **Counterfit** to perform a black-box attack on a vanilla model
    - Tools to avoid these attacks
* Tools to **protect AI systems' data assets**: 
    - Data anonymization using **Presidio**.
    - Differential privacy (DP) with the **SmartNoise** system.
* Dashboards and user interfaces grouping such RAI tools together under a single roof. Here we will look at the so-called **[Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox)** (with the RAI dashboard, widgets, and scorecard).

Responsible AI is still an underrated subject among data scientists, ML engineers, and other AI practitioners more broadly, and today there is a huge gap between principles and tangible actions when it comes in their day-to-day development lifecycle to implement (more) responsible (non-generative vs. generative) AI systems: the so-called "Responsible AI Gap".

These tutorials are meant to accompany the guide [Leveraging responsible AI tooling for your non-generative AI-based solutions](https://github.com/microsoft/responsible-ai-workshop/blob/main/nongen-ai-tooling-tutorials/docs/leveraging-responsible-ai-tooling.docx), which tackles exactly this issue and can be found under the docs folder.

As such, in terms of learning objectives for non-generative AI systems, this guide is intended to give you an overview of the most prominent RAI tools & toolkits we open sourced as (standalone) libraries and dashboards or integrated into [Azure Machine Learning (Azure ML)](https://azure.microsoft.com/en-us/services/machine-learning/), its [responsible machine learning capabilities](https://azure.microsoft.com/en-us/services/machine-learning/responsibleml/), and its [MLOps capabilities](https://azure.microsoft.com/en-us/services/machine-learning/), and where to leverage them in such AI systems' development lifecycle. 

## Links to complete notebook samples 

Please be aware that the notebooks provided in the above hands-on-tutorials are simplified versions of sample notebooks provided as examples in each tool's repository. For the sake of this workshop, the goal is to provide minimal working code for each tool and to aggregate these guides under one roof.
 
If you would like to go further and access more complete demos, we provide the links to the original notebooks below:

* [Fairlearn](https://github.com/fairlearn/fairlearn/blob/main/notebooks/Binary%20Classification%20with%20the%20UCI%20Credit-card%20Default%20Dataset.ipynb)
* [InterpretML](https://github.com/interpretml/interpret-community/blob/master/notebooks/explain-binary-classification-local.ipynb)
* [Error Analysis](https://github.com/microsoft/responsible-ai-widgets/blob/main/notebooks/erroranalysis-dashboard-multiclass.ipynb)
* [Presidio](https://github.com/microsoft/presidio/blob/main/docs/samples/python/presidio_notebook.ipynb)
* [SmartNoise](https://github.com/opendp/smartnoise-samples/blob/master/whitepaper-demos/2-reidentification-attack.ipynb) 
* [Counterfit](https://github.com/Azure/counterfit)

## Prerequisites

Before starting this module, and as far as your execution environment is concerned, we recommend that you read the following notes and ensure that the requirements are fulfilled as per instructions:
* [Cloning this workshop GitHub repo](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/cloning-the-repo.md)
* [Fulfilling the prerequisites for the workshop](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/fulfilling-prerequisites.md)

## Continuing your learning journey

In addition to the above content, you might consider the following Azure ML [RAI dashboard and scorecard samples](https://github.com/Azure/azureml-examples/tree/main/sdk/python/responsible-ai) to continue your learning journey. 

To this end, you can first:
* Watch a deep dive into the RAI dashboard and scorecard [here]. This video explains how to understand and assess your model insights in order to train and deploy your machine learning models more responsibly, demoes how to generate Responsible AI insights through CLI/SDK/UI in Azure ML, and also give you a tour of the RAI dashboard and scorecard.
* Read more about how to generate the RAI dashboard [here](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-responsible-ai-dashboard-sdk-cli?tabs=yaml) and RAI scorecard [here](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-responsible-ai-scorecard). 

## Additional references

In addition to this module, for the learning objectives, you might also consider the following resources:
* [ENISA Report: Artificial Intelligence Cybersecurity Challenges](https://www.enisa.europa.eu/publications/artificial-intelligence-cybersecurity-challenges)
* [ENISA Report: Securing Machine Learning Algorithms](https://www.enisa.europa.eu/publications/securing-machine-learning-algorithms)
* [ENISA Report: Multilayer Framework for Good Cybersecurity Practices for AI](https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai)   
* [Microsoft Security Development Lifecycle (SDL)](https://www.microsoft.com/en-us/securityengineering/sdl)
* [Microsoft SDL practices](https://www.microsoft.com/en-us/securityengineering/sdl/practices)
* [Microsoft Threat Modeling](https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling)
* [Threat Taconomy - Failure Modes in Machine Learning](https://learn.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning)
* [Threat Modeling AI/ML Systems and Dependencies](https://learn.microsoft.com/en-us/security/engineering/threat-modeling-aiml)