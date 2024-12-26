from groq import Groq
import re
import json

def clean_invalid_chars(text):
    return re.sub(r'[\x00-\x1F\x7F]', '', text)

def safe_json_parse(text):
    try:
        return json.loads(text), None
    except json.JSONDecodeError as e:
        return None, str(e)


def evaluate_ssc_essay(question, essay_text, difficulty_type="easy"):
    
    client = Groq(api_key="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")  
    
    marking_scheme = {
        "Relevance": 10,
        "Spelling_Grammar": 5,
        "Word_Limit": 5,
        "Content_Quality": 8,
        "Format": 5,
        "Writing_Neatness": 5,
        "Effective_Sentences": 7,
        "Cohesiveness": 5
    }
    
    
    
    prompt = f"""
    You are an experienced examiner tasked with evaluating essays for the SSC CGL descriptive writing test. Your role is to assess the essay provided based on specific marking criteria and provide constructive feedback to guide improvement. Follow these instructions to ensure consistent, fair, and objective evaluation.

    ### Evaluation Criteria:
    The essay will be scored on the following criteria:
    1. **Content**: Evaluate the relevance, depth, and adequacy of information, including examples and arguments. Does the essay sufficiently address the essay topic with appropriate reasoning and evidence? and also if answer is null then its should be scored 0.
    2. **Organization**: Assess the logical structure and flow of the essay. Is the content well-organized into introduction, body, and conclusion with smooth transitions?
    3. **Language and Vocabulary**: Evaluate the use of language for clarity, precision, and variety. Is the vocabulary appropriate and impactful? Are sentence structures varied and effective?
    4. **Coherence and Cohesion**: Examine the logical connection between ideas and paragraphs. Are transitions between sections seamless? Is the essay cohesive overall?
    5. **Contextual Relevance**: Does the essay stay focused on the topic? Are all arguments and examples contextually appropriate and on-point?
    6. **Word Limit**: Ensure adherence to the specified word limit (200-250 words). Deduct marks for significant deviations.

    ### Marking Scheme:
    Allocate marks based on the following weightage:
    - **Relevance**: 10 marks
    - **Spelling and Grammar**: 5 marks
    - **Word Limit**: 5 marks
    - **Content Quality**: 8 marks
    - **Format**: 5 marks
    - **Writing Neatness**: 5 marks
    - **Effective Sentences**: 7 marks
    - **Cohesiveness**: 5 marks

    ### Difficulty Level: {difficulty_type}
    This evaluation uses a difficulty level of "{difficulty_type}" to calibrate the strictness of evaluation and the depth of content expected.

    ### Evaluation Instructions:
    1. **Scoring**: Score each criterion objectively with some little bit of leniency. For each criterion, assign marks from 0 to the maximum allowed and provide a clear explanation for the score.
    2. **Zero for Irrelevance**: Award zero marks across all criteria for essays that are entirely irrelevant to the topic or blank.
    3. **Constructive Feedback**: Provide strengths and weaknesses for each response, including specific suggestions to improve.
    4. **Model 50-Marks Answer**: Create a comprehensive, perfect 50-marks response for the essay question to serve as a benchmark.
    5. **Suggestions for Improvement**: Based on the evaluation, suggest actionable ways the candidate can enhance their essay.
    6. **Refinement of User Answer**: Modify the user’s submitted essay to demonstrate how it can achieve a full 50-mark score while retaining its original ideas and intent.

    ### Scoring Rules:
    1. **Zero for Blank or Fully Irrelevant Answers**: STRICTLY Award zero marks only if the letter is blank or entirely irrelevant to the topic.
    2. **Partial Scoring for Mixed Relevance**: If some sentences are relevant and others are not, assign marks based on the relevant portions without penalizing heavily for minor mistakes.
    3. **Full Marks for High-Quality Answers**: Award full 50 marks for answers that are almost perfect, with only minor errors or omissions. Do not deduct marks for insignificant issues.


    ### Expected Output (JSON Format Only):
    Provide the evaluation in the following format:

    {{
        "Relevance_Marks": [{{Relevance_Marks}}, "{{Explanation for relevance score}}"],
        "Spelling_Grammar_Marks": [{{Spelling_Grammar_Marks}}, "{{Explanation for spelling and grammar score}}"],
        "Word_Limit_Marks": [{{Word_Limit_Marks}}, "{{Explanation for word limit score}}"],
        "Content_Quality_Marks": [{{Content_Quality_Marks}}, "{{Explanation for content quality score}}"],
        "Format_Marks": [{{Format_Marks}}, "{{Explanation for format score}}"],
        "Writing_Neatness_Marks": [{{Writing_Neatness_Marks}}, "{{Explanation for writing neatness score}}"],
        "Effective_Sentences_Marks": [{{Effective_Sentences_Marks}}, "{{Explanation for effective sentences score}}"],
        "Cohesiveness_Marks": [{{Cohesiveness_Marks}}, "{{Explanation for cohesiveness score}}"],
        "Total_Marks": [{{Total_Marks}}, "{{Summary of overall evaluation}}"],
        "Strengths": "[List of strengths in the user's essay]",
        "Weaknesses": "[List of weaknesses and areas of improvement]",
        "50_Marks_Answer": "[Provide a model essay for the question: {question}, that demonstrates a perfect score based on all evaluation criteria.]",
        "AI_Suggestions": "[List specific suggestions to improve the user's essay based on evaluation criteria.]",
        "Improved_Solution": "[Provide a revised version of the user's essay: {essay_text}, that addresses weaknesses and demonstrates how to achieve a full 50-mark score.]"
    }}

    **Essay Question**: "{question}"  
    **Essay Text**: "{essay_text}"
    """

    try:
        # Sending essay and question to Groq API for evaluation
        response = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        
        # Extract the response and process it
        # result = response['choices'][0]['message']['content'].strip()
        cleaned_content = clean_invalid_chars(response.choices[0].message.content.strip())
        
        evaluation_result, parse_error = safe_json_parse(cleaned_content)

        result = {
            "Word_Count": len(essay_text.split()),
            "Relevance_Marks": "N/A",
            "Spelling_Grammar_Marks": "N/A",
            "Word_Limit_Marks": "N/A",
            "Content_Quality_Marks": "N/A",
            "Format_Marks": "N/A",
            "Writing_Neatness_Marks": "N/A",
            "Effective_Sentences_Marks": "N/A",
            "Cohesiveness_Marks": "N/A",
            "Total_Marks": "N/A",
            "Strengths": "N/A",
            "Weaknesses": "N/A",
            "50_Marks_Answer": "N/A",
            "AI_Suggestions": "N/A",
            "Improved_Solution": "N/A"
        }

        if parse_error:
            print(f"JSON parsing error: {parse_error}")
            result["raw_response"] = cleaned_content

        # Populate result fields
        for key in result.keys():
            if key in evaluation_result:
                result[key] = evaluation_result.get(key, "N/A")

        
        print(result)
        return result

    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        return {
            "error": "Invalid response format from AI model",
            "raw_response":cleaned_content,
            "Relevance_Marks": "N/A",
            "Spelling_Grammar_Marks": "N/A",
            "Content_Quality_Marks": "N/A",
            "Format_Marks": "N/A",
            "Effective_Sentences_Marks": "N/A",
            "Cohesiveness_Marks": "N/A",
            "Total_Score": "N/A",
            "Strengths": "N/A",
            "Weaknesses": "N/A",
            "50_Marks_Answer": "N/A",
            "AI_Suggestions": "N/A",
            "Improved_Solution": "N/A"
        }

    except Exception as e:
        return {"error": f"An error occurred while processing the request: {str(e)}"}



