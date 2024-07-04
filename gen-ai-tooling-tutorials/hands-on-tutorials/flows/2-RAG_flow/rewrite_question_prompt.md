You are able to reason from previous conversation and the recent question, to come up with a rewrite of the question which is concise but with enough information that people without knowledge of previous conversation can understand the question.

A few examples:

# Example 1
## Previous conversation
user: Who is Bill Clinton?
assistant: Bill Clinton is an American politician who served as the 42nd President of the United States from 1993 to 2001. 
## Question
user: When was he born?
## Rewritten question 
When was Bill Clinton born?

# Example 2
## Previous conversation
user: What is RAI?
assistant: RAI stands for "Responsible AI". It is an approach to developing, assessing, and deploying AI systems in a safe, trustworthy, and ethical way.
## Question
user: Why is it important ? 
## Rewritten question
Why is responsbility in AI important ?

Now comes the actual work - please respond with the rewritten question in the same language as the question, nothing else.

## Previous conversation
{% for item in history %}
{{item["role"]}}: {{item["content"]}}
{% endfor %}
## Question
{{question}}
## Rewritten question