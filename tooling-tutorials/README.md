# Responsible AI Workshop - Tooling Tutorials

This module contains a series of hands-on tutorials for Microsoft's most prominent Responsible AI tools/toolkits.

It is primarily designed for developers and data scientists to provide them with jump-start tutorials for using each tool, in the form of Jupyter notebooks. 

## Overview of the available hands-on tutorials

We investigate three categories of Responsible AI tools:

* Tools to **understand the behavior of AI systems**. These in turn fall into two categories covered here:
    - Tools to assess and mitigate fairness issues. Here we focus on **Fairlearn**.
    - Tools to understand and explain AI systems predictions. Here we focus on **InterpretML** and **Error Analysis**.
* Tools to **protect AI systems' data assets**: 
    - Data anonymization using **Presidio**.
    - Differential privacy (DP) with the **SmartNoise** system.
* Dashboards and user interfaces grouping such Responsible AI tools together under a single roof. Here we will look at the **Responsible-AI-Toolbox** (raiwidgets).

Responsible AI is still an underrated subject among data scientists, ML engineers, and other AI practitioners more broadly, and today there is a huge gap between principles and tangible actions when it comes in their day-to-day development lifecycle to implement (more) responsible AI systems: the so-called "Responsible AI Gap".

These tutorials are meant to accompany the guide [Leveraging Responsible AI Tooling for your AI-based solutions](https://github.com/microsoft/responsible-ai-workshop/blob/main/tooling-tutorials/docs/guide_leveraging_responsible_ai_tooling.docx), which tackles exactly this issue and can be found under the docs folder.

As such, in terms of learning objectives, this guide is intended to:
* Share and comment from the intended audience's perspective an [ongoing journey towards Responsible AI (RAI)](https://aka.ms/RAIresources), starting from core principles from which this effort is deeply anchored, to the translation of these principles into a set of practices to adopt, enforce, and evolve company-wide with respect to an end-to-end lifecycle for the design, the development, the deployment, and the monitoring of these AI systems, 
* Give you an overview of the most prominent Responsible AI tools & toolkits we open sourced as (standalone) libraries and dashboards or integrated into [Azure Machine Learning (Azure ML)](https://azure.microsoft.com/en-us/services/machine-learning/), its [responsible machine learning capabilities](https://azure.microsoft.com/en-us/services/machine-learning/responsibleml/), and its [MLOps capabilities](https://azure.microsoft.com/en-us/services/machine-learning/), and where to leverage them in such AI systems' development lifecycle. 


## Links to complete notebook samples 

Please be aware that the notebooks provided in the above hands-on-tutorials are simplified versions of sample notebooks provided as examples in each tool's repository. For the sake of this workshop, the goal is to provide minimal working code for each tool and to aggregate these guides under one roof.
 
If you would like to go further and access more complete demos, we provide the links to the original notebooks below:

- [Fairlearn](https://github.com/fairlearn/fairlearn/blob/main/notebooks/Binary%20Classification%20with%20the%20UCI%20Credit-card%20Default%20Dataset.ipynb)
- [InterpretML](https://github.com/interpretml/interpret-community/blob/master/notebooks/explain-binary-classification-local.ipynb)
- [Error Analysis](https://github.com/microsoft/responsible-ai-widgets/blob/main/notebooks/erroranalysis-dashboard-multiclass.ipynb)
- [Presidio](https://github.com/microsoft/presidio/blob/main/docs/samples/python/presidio_notebook.ipynb)
- [SmartNoise](https://github.com/opendp/smartnoise-samples/blob/master/whitepaper-demos/2-reidentification-attack.ipynb) 
