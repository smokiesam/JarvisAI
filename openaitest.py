import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Write an application to apply for a job",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
print(response)

'''
{
  "id": "cmpl-82KqgMucDjJVtJ1q59VWEr3R0GDWo",
  "object": "text_completion",
  "created": 1695567490,
  "model": "gpt-3.5-turbo-instruct",
  "choices": [
    {
      "text": "\n\n[Your Name]\n[Your Address]\n[City, State ZIP Code]\n[Email Address]\n[Today\u2019s Date]\n\n[Employer\u2019s Name]\n[Company Name]\n[Address]\n[City, State ZIP Code]\n\nDear [Employer\u2019s Name],\n\nI am writing to express my interest in the [Position] at [Company Name] that I recently came across on [Source]. With [Number] years of experience in [Field/Industry], I am confident that I am a strong candidate for this position.\n\nIn my current role as a [Current Job Title] at [Current Company], I have gained valuable skills in [Relevant Skill 1], [Relevant Skill 2], and [Relevant Skill 3]. I have also completed [Relevant Certification/Education] that has further enhanced my knowledge and expertise in this field. My previous experience includes [Previous Job Title] at [Previous Company] where I successfully [Achievement 1] and [Achievement 2].\n\nI am highly motivated, results-driven, and able to thrive in fast-paced environments. I possess excellent communication, problem-solving, and team collaboration skills. I am also proficient in [Relevant Software/Tool] and have experience in [Other Relevant Skill/Experience].\n\nI am",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 8,
    "completion_tokens": 256,
    "total_tokens": 264
  }
}
'''
