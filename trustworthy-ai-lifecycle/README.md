# Responsible AI Workshop - Towards a (more) trustworthy AI lifecycle for non-Generative AI

Artificial Intelligence (AI) is being used more and more, and we can find it everywhere today. From recommending content on social networks to optimizing the battery of our smartphone for non-Generative AI, and with now the ability to create create new data, including visual content, text, audio, code etc.
for Generative AI, this technology has made its mark because of the impressive progress it allows in different areas. 

However, among all the observed use cases, we notice that some sectors are reluctant to implement such a technology. Autonomous cars are not yet on the road, and it is still difficult to trust a diagnosis made only by a machine. 

This mistrust is quite normal and comes mainly from the fact that we do not know to what extent, and to what degree, we can trust this technology. The fields of autonomous cars or medical diagnostics are unforgiving fields where there is no room for error.

The [MITRE Adversarial Threat Landscape for Artificial-Intelligence Systems (ATLAS™)](https://atlas.mitre.org/) framework lists a number of attacks that can be implemented against a ML model. 

Among them, adversarial attacks (and perturbations) are a growing concern in the field of Machine Learning (ML). As an illustration, you will find, in this repository, an [implementation of an adversarial attack againt a ML model](https://github.com/microsoft/responsible-ai-workshop/blob/main/nongen-ai-tooling-tutorials/hands-on-tutorials/adverserial_attacks_counterfit/adverserial_attacks_counterfit.ipynb) executed against a computer vision model using [Counterfit](https://github.com/Azure/counterfit), i.e., a tool specially designed to carry out these types of attacks. 

In addition to this demonstration, the guide [Framing a (more) Trustworthy AI Lifecycle for your AI-powered solutions](https://github.com/microsoft/responsible-ai-workshop/blob/main/trustworthy-ai-lifecycle/docs/framing-trustworthy-ai-lifecycle.docx) goes into more details about how the attack works and addresses the question of how to build trust in a ML-based project and the related development lifecycle.

The learning objectives of this guide are to help moving towards a (more) reliable AI lifecycle in order to gradually strengthen the trust we can have in this technology and therefore facilitate its adoption in contexts where it would have a great responsibility.

First, the document will illustrate why it is absolutely necessary to take into account the cybersecurity aspect in the development of projects based on ML. 
  
To do so, we will implement an adversarial attack on a ML model designed for the occasion and supposed to represent a critical use case of a company.

Then, we will analyze the classical development cycle of AI in order to:
* Understand how it is built
* Determine where potential vulnerabilities may lie
* Establish a "North Star" to guide us in hardening this development lifecycle.

Finally, we will explain how to strengthen this development lifecycle in order to secure it against the threats we have highlighted and ideally against those we do not yet know. For that we will put forward a certain number of good practices and tools which will allow you to achieve a (more) trustworthy AI Lifecycle.

## Data

For the sake of the Proof of Concept available in the walkthrough, we use the [German Traffic Sign Recognition Benchmark](https://benchmark.ini.rub.de/gtsrb_news.html).

## References

* [MITRE Adversarial Threat Landscape for Artificial-Intelligence Systems (ATLAS™)](https://atlas.mitre.org/matrices/ATLAS)
* [Adversarial Machine Learning - Industry Perspectives](https://arxiv.org/pdf/2002.05646.pdf)
* [Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox)
* [AI Risk Assessment - Best practices and guidance to secure AI systems](https://github.com/Azure/AI-Security-Risk-Assessment/blob/main/AI_Risk_Assessment_v4.1.4.pdf)

## Additional references

* [ENISA Report: Artificial Intelligence Cybersecurity Challenges](https://www.enisa.europa.eu/publications/artificial-intelligence-cybersecurity-challenges)
* [ENISA Report: Securing Machine Learning Algorithms](https://www.enisa.europa.eu/publications/securing-machine-learning-algorithms)
* [ENISA Report: Multilayer Framework for Good Cybersecurity Practices for AI](https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai)   
* [Microsoft Security Development Lifecycle (SDL)](https://www.microsoft.com/en-us/securityengineering/sdl)
* [Microsoft SDL practices](https://www.microsoft.com/en-us/securityengineering/sdl/practices)
* [Microsoft Threat Modeling](https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling)
* [Threat Taconomy - Failure Modes in Machine Learning](https://learn.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning)
* [Threat Modeling AI/ML Systems and Dependencies](https://learn.microsoft.com/en-us/security/engineering/threat-modeling-aiml)