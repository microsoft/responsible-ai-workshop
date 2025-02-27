# Responsible AI Workshop - Exploring the risks of intelligent agents

According to [wikipedia](https://en.wikipedia.org/wiki/Intelligent_agent), "an intelligent agent is an agent that perceives its environment, takes actions autonomously in order to achieve goals, and may improve its performance with learning or acquiring knowledge." One can define an autonomous (intelligent) agent as being designed to function in the absence of human intervention. One also should stress that intelligent agents are also closely related to software agents that exist for decades.

Agentic as a property can be commonly understood as the application's ability to act in a goal-directed manner, i.e, the application's adaptability to achieve goals with limited direct supervision in a complex environment. In the context of (generative) AI, agentic applications are those that can act autonomously in a goal-directed manner.

The rapid advancement of generative AI has brought forth incredible opportunities to transform industries, adequately revisit the pre-existing software agents' "world", and solve complex problems with various types of capabilities, specifically goal complexity, environment complexity, adaptability, and independence. However, ensuring the responsible development, deployment, reliable operations and monitoring of these technologies is crucial to harness their potential effectively in real-world environments.

This module delves into the journey of building and using autonomous intelligent agents and agentic applications responsibly. There is however NO one-size-fits-all, neither for solution to the challenges posed by these technologies, nor, at the core, for the underlying agentic architectures and related choregraphies they enables. Agentic architectures are (a set of) patterns (much like microservices, or even broad category like analytics) that can be used to design and implement agent and applications to address specific use cases - Just like distributed systems, no single architecture fits all agentic scenarios.

Design factors (use cases, environments, goals, etc.), behavioral composition of individual agents and related constraints, and orchestration differences to create complex behavior through composition of agents working together may lead to different architectures, differents frameworks that highligh different capabilites, etc., and thus ultimately to different associated risks and harms that are key to consider.

In this context, this module explores the safety & security, and other risks associated with such agents and applications and provides insights on how to address these challenges to ensure a trustworthy future.

To this end, the guide [Understanding intelligent agents in Artificial Intelligence](https://github.com/microsoft/responsible-ai-workshop/tree/main/ai-agents-tutorials/docs/understanding-ai-agents.docx) defines the notion of both an agent and agentic application, then reviews the possible architectures while drawing a parallel with the Copilots' environment. This guide is accompanied by a [Hands on tutorial](https://github.com/microsoft/responsible-ai-workshop/tree/main/ai-agents-tutorials/hands-on-tutorials) to "get your hands dirty" through the creation of two built-for-purpose agentic applications.
 
Eventually, the companion eponym presentation [Understanding intelligent agents in Artificial Intelligence](https://github.com/microsoft/responsible-ai-workshop/tree/main/ai-agents-tutorials/ppts/understanding-ai-agents.pptx) provides ready-to-use, fully annotated content to (let you) organize a dedicated session on the above.
 
This primer is accompanied by a second guide [Securing intelligent agents in Artificial Intelligence](https://github.com/microsoft/responsible-ai-workshop/tree/main/ai-agents-tutorials/docs/securing-ai-agents.docx), which in turn on that basis goes deeper on the notions of safety & security, and other risks associated with such agents and applications, and provides insights on how to address these challenges to help ensuring a trustworthy future.

This is (still) a **Work-In-Progress** effort, and content will be added and updated over the time. It's all the more so that we live in a constantly evolving threats landscape, where consequently the risks and challenges associated with AI and intelligent agents are thus also constantly evolving... 
(As for the rest of this Workshop, we welcome your feedback and contributions to this effort. Please feel free to open an issue or submit a pull request with your suggestions.)

## Prerequisites

Before starting this module, you should be familiar with the [Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-foundry/). Consider completing the [Introduction to Azure AI Foundry] module on [Microsoft Learn](https://docs.microsoft.com/en-us/learn/) before starting this one.

Additionally, while not required, a basic understanding of multi-agent orchestration frameworks like [AutoGen](https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-generation-large-language-model-applications/), a state-of-the-art research SDK for Python created by Microsoft Research, [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-architecture?pivots=programming-language-csharp), an enterprise AI SDK for Python, .NET, and Java, etc. is welcome.

For the sake of the hands-on, and as far as your execution environment is concerned, we recommend that you read the following notes and ensure that the requirements are fulfilled as per instructions:
* [Cloning this workshop GitHub repo](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/cloning-the-repo.md)
* [Fulfilling the prerequisites for the workshop](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/fulfilling-prerequisites.md)
* [Getting started with Azure for your environment](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/getting-started-with-azure.md) 
* [Deploying a generative AI model in Azure and using it in Python](https://github.com/microsoft/responsible-ai-workshop/blob/main/perequisites/deploying-a-model-in-Azure-and-using-it-in-python.md)

With these prerequisites in place, you will be able to follow along with the hands-on tutorials and build and use autonomous intelligent agents and agentic applications responsibly.

## Continuing your learning journey

In addition of the above first guide, you might check out the [10 Lessons teaching everything you need to know to start building AI Agents](https://github.com/microsoft/ai-agents-for-beginners). This course on GitHub covers the fundamentals of building AI Agents. Each lesson covers its own topic so start wherever you like.

After completing this module, you might also consider the following [Microsoft Learn](https://docs.microsoft.com/en-us/learn/) paths and modules, or GitHub courses, to continue your learning journey:
* [21 Lessons teaching everything you need to know to start building Generative AI applications](https://github.com/microsoft/generative-ai-for-beginners/) course.
* [Responsible generative AI](https://learn.microsoft.com/en-us/training/modules/responsible-ai-studio/) module.
* [Build a RAG-based agent with your own data using Azure AI Foundry](https://learn.microsoft.com/en-us/training/modules/build-copilot-ai-studio/) module.
* [Evaluate generative AI applications](https://learn.microsoft.com/en-us/training/paths/evaluate-generative-ai-apps/) learning path.
* [Operationalize AI responsibly with Azure AI Foundry](https://learn.microsoft.com/en-us/training/paths/operationalize-ai-responsibly/) learning path.

You might also read up on [Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/) and see what you can adopt for your usage. For more illustrations, see Azure AI Content Safety [playlist](https://www.youtube.com/playlist?list=PLlrxD0HtieHjaQ9bJjyp1T7FeCbmVcPkQ).

Similalry, you might also check out our [Generative AI Learning collection](https://learn.microsoft.com/en-us/collections/zpy7c8zmq6ky0z?WT.mc_id=academic-105485-koreyst) to continue leveling up your Generative AI knowledge!
