# Responsible AI Workshop - Building and using Generative AI responsibly

The rapid advancement of Generative AI has brought forth incredible opportunities to transform industries and solve complex problems. However, ensuring the responsible development and deployment of these technologies is crucial to harness their potential effectively.

This module delves into the journey of building and using Generative AI applications responsibly. For that purpose, it contains an end-to-end walkthrough of a Responsible AI Lifecycle (RAIL) that aligns with the core functions of the [AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework) developed by the [National Institute of Standards and Technology (NIST)](https://www.nist.gov/) – Govern, Map, Measure and Manage – with the aim of reducing Generative AI risks and their associated harms:
* **Govern**: Align roles and responsibilities, establish requirements for safe, secure, and trustworthy AI deployment, and thus foster a culture of risk management across the generative AI system lifecycle throughout a consistent AI governance. 
* **Map**: Identify and prioritize AI risks to inform decisions around planning, safeguards, and the appropriateness of a Generative AI system for a given context. This includes impact assessments, [(AI) security threat modeling](https://learn.microsoft.com/en-us/ai/playbook/capabilities/model-development/adversarial-ml-threat-modeling), and [AI red teaming](https://learn.microsoft.com/en-us/security/ai-red-team/). 
* **Measure**: Systematically establish metrics to measure potential AI risks and then measure prioritized AI risks to assess prevalence and effectiveness of mitigations intended to address those risks. This includes also testing for and mitigate fairness-related harms and performance disparities.
* **Manage**: Manage or mitigate identified AI risks. at both the platform and application levels. This also includes safeguard against previously unknown risks by continuously monitoring system performance and developing processes for responding to incidents and, if needed, rolling systems back.

As such, in terms of learning objectives, the guide [Building and using Generative AI responsibly with Azure and beyond](https://github.com/microsoft/responsible-ai-workshop/blob/main/gen-ai-tooling-tutorials/docs/buildling-and-using-gen-ai-responsibly.docx) covers the above core functions, outlines the layers of a Generative AI application where responsible AI mitigations can be implemented starting from the model up to the user experience (UX). It in turn illustrates them via an end-to-end hands-on tutorial with all the  [necessary scripts and other definition files](https://github.com/microsoft/responsible-ai-workshop/blob/main/gen-ai-tooling-tutorials/hands-on-tutorials/) to reproduce the outlined activities.

Eventually, the companion eponym presentation [Building and using Generative AI responsibly with Azure and beyond](https://github.com/microsoft/responsible-ai-workshop/blob/main/gen-ai-tooling-tutorials/ppts/building-and-using-gen-ai-responsibly.pptx) provides a ready-to-use fully annotated content to organize a dedicated session.

## Prerequisites

Before starting this module, you should be familiar with the [Azure AI Studio](https://azure.microsoft.com/en-us/products/ai-studio/). Consider completing the [Introduction to Azure AI Studio] module on [Microsoft Learn](https://docs.microsoft.com/en-us/learn/) before starting this one.

For the sake of the hands-on, and as far as your execution environment is concerned, we recommend that you read the following notes and ensure that the requirements are fulfilled as per instructions:
* [Cloning this workshop GitHub repo](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/cloning-the-repo.md)
* [Fulfilling the prerequisites for the workshop](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/fulfilling-prerequisites.md)
* [Getting started with Azure for your environment](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/getting-started-with-azure.md) 
* [Deploying a Generative AI model in Azure and using it in Python](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/deploying-a-model-in-Azure-and-using-it-in-python.md)

With these prerequisites in place, you will be able to follow along with the hands-on tutorials and build and use Generative AI responsibly.

## Continuing your learning

After completing this module, and to further continue your learning, you might consider the following [Microsoft Learn](https://docs.microsoft.com/en-us/learn/) paths and modules:
* [Responsible Generative AI](https://learn.microsoft.com/en-us/training/modules/responsible-ai-studio/) module.
* [Evaluate generative AI applications](https://learn.microsoft.com/en-us/training/paths/evaluate-generative-ai-apps/) learning path.
* [Operationalize AI responsibly with Azure AI Studio](https://learn.microsoft.com/en-us/training/paths/operationalize-ai-responsibly/) learning path.

You might also read up on [Azure AI Content Saftey](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/) and see what you can adopt for your usage. For more illustrations, see Azure AI Content Safety [playlist](https://www.youtube.com/playlist?list=PLlrxD0HtieHjaQ9bJjyp1T7FeCbmVcPkQ).

Also check out our [Generative AI Learning collection](https://learn.microsoft.com/en-us/collections/zpy7c8zmq6ky0z?WT.mc_id=academic-105485-koreyst) to continue leveling up your Generative AI knowledge!

## References
The above-mentioned AI Risk Management Framework (AI RMF 1.0) is a voluntary framework developed that aims to improve the ability to incorporate trustworthiness considerations into the design, development, use, and evaluation of AI products, services, and systems. It is intended to help organizations better manage risks to individuals, organizations, and society associated with AI:
* [NIST-AI-100-1 AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework): a Framework intended to build on, align with, and support AI risk management efforts by others. For more information, see the [NIST AI RMF homepage](https://www.nist.gov/itl/ai-risk-management-framework). See also the [NIST AI RMF Playbook](https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook) for suggested actions for achieving the outcomes laid out in the framework.
* [NIST-AI-600-1 AI Risk Management Framework: Generative Artificial Intelligence Profile](https://doi.org/10.6028/NIST.AI.600-1): a profile that can help organizations identify unique risks posed by Generative AI and proposes actions for Generative AI risk management that best aligns with their goals and priorities.

## Additional resources
To better understand the risks and harms, you might also consider the following resources:
* [MITRE Adversarial Threat Landscape for Artificial-Intelligence Systems (ATLAS) Framework](https://atlas.mitre.org/matrices/ATLAS)
* [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
