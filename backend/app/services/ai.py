import os
import json
from pdf_parser import test_pdf_extraction
from huggingface_hub import InferenceClient

class HuggingFaceAnalyzer:
    def __init__(self):        
        self.client = InferenceClient(
            model="meta-llama/Meta-Llama-3-8B-Instruct"
        )

    def analyze(self, cv_text, job_offer_text):
        prompt = (
            f"Analyze the following CV against the job offer.\n\n"
            f"--- Job Offer ---\n{job_offer_text}\n\n"
            f"--- CV ---\n{cv_text}\n\n"
            f"Please provide:\n"
            f"1. Match percentage\n"
            f"2. Strengths\n"
            f"3. Areas for improvement\n"
            f"Format your response as JSON with the following keys:\n"
            f"match_percentage, strengths, areas_for_improvement"
        )
        
        messages = [
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat_completion(
                messages=messages,
                max_tokens=500,
                temperature=0.7,
                stop=None,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error during analysis: {e}")
            return None

if __name__ == "__main__":
    cv_text = test_pdf_extraction("../../../docs/sample.pdf")
    
    job_offer_text = (
        "We are looking for a software engineer with experience in Python and machine learning. "
        "The ideal candidate should have a strong background in data analysis and be able to work in a team environment. "
        "Experience with cloud platforms is a plus. The candidate should also have excellent communication skills "
        "and be able to adapt to changing requirements. The role involves working on various projects and collaborating "
        "with cross-functional teams. The candidate should be able to work independently and take ownership of their work."
    )
    
    analyzer = HuggingFaceAnalyzer()
    result = analyzer.analyze(cv_text, job_offer_text)
try:
    parsed_result = json.loads(result)
    # Show nicely
    print("Match Percentage:", parsed_result["match_percentage"])
    print("Strengths:", parsed_result["strengths"])
    print("Areas for Improvement:", parsed_result["areas_for_improvement"])
except json.JSONDecodeError:
    print("❌ Could not parse as JSON. Raw output:")
    print(result)
