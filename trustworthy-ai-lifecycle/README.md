# Responsible AI Workshop - Towards a (more) trustworthy AI lifecycle

Machine Learning (ML) is being used more and more, and we can find it everywhere today. From recommending content on social networks to optimizing the battery of our smartphone. This technology has made its mark because of the impressive progress it allows in different areas. 

However, among all the observed use cases, we notice that some sectors are reluctant to implement this technology. Autonomous cars are not yet on the road, and it is still difficult to trust a diagnosis made only by a machine. 

This mistrust is quite normal and comes mainly from the fact that we do not know to what extent, and to what degree, we can trust this technology. The fields of autonomous cars or medical diagnostics are unforgiving fields where there is no room for error.

The [MITRE ATLAS™](https://atlas.mitre.org/) framework lists a number of attacks that can be implemented against a ML model. Among them, adversarial attacks. 

In this repository, you will find an [implementation of an adversarial attack](https://github.com/microsoft/responsible-ai-workshop/blob/main/trustworthy_ai_lifecycle/hands_on_tutorials/adverserial_attacks_counterfit.ipynb) executed against a computer vision model using [Counterfit](https://github.com/Azure/counterfit), a tool specially designed to carry out these types of attacks. 

In addition to this demonstration, the guide [Establishing a (more) Trustworthy AI Lifecycle for your AI-powered solutions](https://github.com/microsoft/responsible-ai-workshop/blob/main/trustworthy-ai-lifecycle/docs/guide_building_trustworthy_ai_lifecycle.docx) goes into more details about how the attack works and addresses the question of how to build trust in a ML-based project and the related development lifecycle.

The learning objectives of this guide are to help moving towards a (more) reliable AI lifecycle in order to gradually strengthen the trust we can have in this technology and therefore facilitate its adoption in contexts where it would have a great responsibility.

First, the document will illustrate why it is absolutely necessary to take into account the cybersecurity aspect in the development of projects based on Machine Learning. 
  
To do so, we will implement an adversarial attack on a model designed for the occasion and supposed to represent a critical use case of a company.

Then, we will analyze the classical development cycle of AI in order to:
-	Understand how it is built
-	Determine where potential vulnerabilities may lie
-   Establish a "North Star" to guide us in hardening this development lifecycle.

Finally, we will explain how to strengthen this development lifecycle in order to secure it against the threats we have highlighted and ideally against those we do not yet know. For that we will put forward a certain number of good practices and tools which will allow you to achieve a (more) trustworthy AI Lifecycle.


## Data

For the sake of the Proof of Concept available in the walkthrough, we use the [German Traffic Sign Recognition Benchmark](https://benchmark.ini.rub.de/gtsrb_news.html).


## References

[MITRE ATLAS™](https://atlas.mitre.org/)

[Adversarial Machine Learning - Industry Perspectives](https://arxiv.org/pdf/2002.05646.pdf)

[Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox)

[ENISA - Artificial Intelligence Cybersecurity Challenge](https://www.enisa.europa.eu/publications/artificial-intelligence-cybersecurity-challenges)

[ENISA - Securing Machine Learning Algorithms](https://www.enisa.europa.eu/publications/securing-machine-learning-algorithms)

