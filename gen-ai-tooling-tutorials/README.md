# Responsible AI Workshop - Building and using Generative AI responsibly

The rapid advancement of Generative AI has brought forth incredible opportunities to transform industries and solve complex problems. However, ensuring the responsible development and deployment of these technologies is crucial to harness their potential effectively.

This module delves into the journey of building and using Generative AI applications responsibly. For that purpose, it contains an end-to-end walkthrough of a Responsible AI Lifecycle (RAIL) that aligns with the core functions of the [AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework) developed by the [National Institute of Standards and Technology (NIST)](https://www.nist.gov/) – Govern, Map, Measure and Manage – with the aim of reducing Generative AI risks and their associated harms:
* **Govern**: Align roles and responsibilities, establish requirements for safe, secure, and trustworthy AI deployment, and thus foster a culture of risk management across the generative AI system lifecycle throughout a consistent AI governance. 
* **Map**: Identify and prioritize AI risks to inform decisions around planning, safeguards, and the appropriateness of a Generative AI system for a given context. This includes impact assessments, [(AI) security threat modeling](https://learn.microsoft.com/en-us/ai/playbook/capabilities/model-development/adversarial-ml-threat-modeling), and [AI red teaming](https://learn.microsoft.com/en-us/security/ai-red-team/). 
* **Measure**: Systematically establish metrics to measure potential AI risks and then measure prioritized AI risks to assess prevalence and effectiveness of mitigations intended to address those risks. This includes also testing for and mitigate fairness-related harms and performance disparities.
* **Manage**: Manage or mitigate identified AI risks. at both the platform and application levels. This also includes safeguard against previously unknown risks by continuously monitoring system performance and developing processes for responding to incidents and, if needed, rolling systems back.

As such, in terms of learning objectives, the guide [Building and using Generative AI responsibly with Azure and beyond](https://github.com/microsoft/responsible-ai-workshop/blob/main/gen-ai-tooling-tutorials/docs/buildling-and-using-gen-ai-responsibly.docx) covers the above core functions, outlines the layers of a Generative AI application where responsible AI mitigations can be implemented starting from the model up to the user experience (UX). It in turn illustrates them via an end-to-end hands-on tutorial with all the  [necessary scripts and other definition files](https://github.com/microsoft/responsible-ai-workshop/blob/main/gen-ai-tooling-tutorials/hands-on-tutorials/) to reproduce the outlined activities.

Eventually, the companion eponym presentation [Building and using Generative AI responsibly with Azure and beyond](https://github.com/microsoft/responsible-ai-workshop/blob/main/gen-ai-tooling-tutorials/ppts/building-and-using-gen-ai-responsibly.pptx) provides a ready-to-use fully annotated content to organize a dedicated session.

## Additional references
* [AI Risk Management Framework (AI RMF)](https://www.nist.gov/itl/ai-risk-management-framework)
* [AI Risk Management Framework: Generative Artificial Intelligence Profile](https://airc.nist.gov/docs/NIST.AI.600-1.GenAI-Profile.ipd.pdf)
* [MITRE Adversarial Threat Landscape for Artificial-Intelligence Systems (ATLAS) Framework](https://atlas.mitre.org/matrices/ATLAS)
* [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
