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

def evaluate_ssc_precis(passage, precis_text, difficulty_type="easy"):
    
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

    # prompt = f"""
    # Assume you are an examiner for the SSC CGL descriptive writing test. Your task is to evaluate the response solely based on the given prompt for the following criteria: Lexical Resource, Grammatical Range and Accuracy, Task Achievement, and Coherence and Cohesion. Assign marks from 0-50 for each criterion based on the provided description. Remain consistent in your assessment even if the same response is submitted multiple times.
    # Evaluate based on the selected difficulty level: {difficulty_type}.

    # 1. **Lexical Resource**: The range and accuracy of vocabulary used in the précis.
    # 2. **Grammatical Range and Accuracy**: The complexity and correctness of the grammar used.
    # 3. **Task Achievement**: How well the précis summarizes the passage and captures the essential points.
    # 4. **Coherence and Cohesion**: The flow of ideas and how well the summary is structured in one coherent paragraph.

    # The précis is expected to:
    # - Be concise, ideally one-third of the original passage length.
    # - Retain the central idea of the passage.
    # - Include essential points and perspectives from the passage.
    # - Be concluded within 100-150 words.
    # - Retain the original voice of the author.
    # - Be written in one paragraph.

    # The SSC CGL précis is evaluated on the following marking scheme {marking_scheme} with description:
    # - **Relevance**: How well the précis summarizes the key points of the passage (10 marks).
    # - **Spelling/Grammar**: Accuracy in spelling and grammar (5 marks).
    # - **Word Limit**: Adherence to the word limit of 100-150 (5 marks).
    # - **Content Quality**: Depth and clarity of the summarized content (8 marks).
    # - **Format**: Proper précis format (5 marks).
    # - **Writing Neatness**: Clarity and neatness of writing (5 marks).
    # - **Effective Sentences**: Use of clear, concise, and varied sentence structures (7 marks).
    # - **Cohesiveness**: Logical flow and transitions between ideas (5 marks).

    # Please evaluate the précis based on these criteria. Provide scores for each category, explain why the scores were assigned, and suggest improvements. Also, provide an example of a perfect 50-mark précis for the question.
    # Remember if there is nothing like the answer is blank then all score will be 0 and also remember this strictly that if the answer is not based on the question or is in other direction then also all the scores will be 0. (please evaluate this very strictly)
    
    # Précis Passage: "{passage}"
    # Précis Text: "{precis_text}"

    # *Final Output (Strictly in JSON format with no extra text or comments)*:
    # {{
    #     "Relevance_Marks": [{{Relevance_Marks}}, "{{Explanation_for_relevance_score}}"],
    #     "Spelling_Grammar_Marks": [{{Spelling_Grammar_Marks}}, "{{Explanation_for_spelling_grammar_score}}"],
    #     "Word_Limit_Marks":[{{Word_Limit_Marks}}, "{{Explanation_for_word_limit_score}}"],
    #     "Content_Quality_Marks": [{{Content_Quality_Marks}}, "{{Explanation_for_content_quality_score}}"],
    #     "Format_Marks": [{{Format_Marks}}, "{{Explanation_for_format_score}}"],
    #     "Writing_Neatness_Marks":[{{Writing_Neatness_Marks}}, "{{Explanation_for_writing_neatness_score}}"],
    #     "Effective_Sentences_Marks": [{{Effective_Sentences_Marks}}, "{{Explanation_for_effective_sentences_score}}"],
    #     "Cohesiveness_Marks": [{{Cohesiveness_Marks}}, "{{Explanation_for_cohesiveness_score}}"],
    #     "Total_Marks": [{{Total_Marks}}, "{{Explanation_for_Total_Marks}}"],
    #     "Strengths": "[List of strengths from the user's answer]",
    #     "Weaknesses": "[List of weaknesses from the user's answer that need improvement]",
    #     "50_Marks_Answer": "[Generate a 50-mark précis answer for the passage, ensuring it addresses all marking criteria comprehensively,  with '90-120 words' in response to {passage}]",
    #     "AI_Suggestions": "[Provide specific suggestions for improvement based on the user's answer in {precis_text}]",
    #     "Improved_Solution": "[Provide a 50-mark improved solution for the user's answer {precis_text} based on the essay question asked which was {passage}]"
    # }}
    # """
    # prompt = f"""
    # Assume you are an examiner for the SSC CGL descriptive writing test. Your task is to evaluate the response solely based on the given prompt for the following criteria: Lexical Resource, Grammatical Range and Accuracy, Task Achievement, and Coherence and Cohesion. Assign marks from 0-50 for each criterion based on the provided description. Remain consistent in your assessment even if the same response is submitted multiple times.
    # Evaluate based on the selected difficulty level: {difficulty_type}.

    # 1. **Lexical Resource**: The range and accuracy of vocabulary used in the précis.
    # 2. **Grammatical Range and Accuracy**: The complexity and correctness of the grammar used.
    # 3. **Task Achievement**: How well the précis summarizes the passage and captures the essential points.
    # 4. **Coherence and Cohesion**: The flow of ideas and how well the summary is structured in one coherent paragraph.

    # The précis is expected to:
    # - Be concise, ideally one-third of the original passage length.
    # - Retain the central idea of the passage.
    # - Include essential points and perspectives from the passage.
    # - Be concluded within 90-120 words.
    # - Retain the original voice of the author.
    # - Be written in one paragraph.

    # The SSC CGL précis is evaluated on the following marking scheme {marking_scheme} with description:
    # - **Relevance**: How well the précis summarizes the key points of the passage (10 marks).
    # - **Spelling/Grammar**: Accuracy in spelling and grammar (5 marks).
    # - **Word Limit**: Adherence to the word limit of 90-120 words (5 marks).
    # - **Content Quality**: Depth and clarity of the summarized content (8 marks).
    # - **Format**: Proper précis format (5 marks).
    # - **Writing Neatness**: Clarity and neatness of writing (5 marks).
    # - **Effective Sentences**: Use of clear, concise, and varied sentence structures (7 marks).
    # - **Cohesiveness**: Logical flow and transitions between ideas (5 marks).

    # Please evaluate the précis based on these criteria. Provide scores for each category, explain why the scores were assigned, and suggest improvements. Also, provide an example of a perfect 50-mark précis for the question.
    # Remember if there is nothing like the answer is blank then all scores will be 0 and also remember this strictly that if the answer is not based on the question or is in another direction then also all the scores will be 0. (please evaluate this very strictly)
    
    # Précis Passage: "{passage}"
    # Précis Text: "{precis_text}"

    # *Final Output (Strictly in JSON format with no extra text or comments)*:
    # {{
    #     "Relevance_Marks": [{{Relevance_Marks}}, "{{Explanation_for_relevance_score}}"],
    #     "Spelling_Grammar_Marks": [{{Spelling_Grammar_Marks}}, "{{Explanation_for_spelling_grammar_score}}"],
    #     "Word_Limit_Marks":[{{Word_Limit_Marks}}, "{{Explanation_for_word_limit_score}}"],
    #     "Content_Quality_Marks": [{{Content_Quality_Marks}}, "{{Explanation_for_content_quality_score}}"],
    #     "Format_Marks": [{{Format_Marks}}, "{{Explanation_for_format_score}}"],
    #     "Writing_Neatness_Marks":[{{Writing_Neatness_Marks}}, "{{Explanation_for_writing_neatness_score}}"],
    #     "Effective_Sentences_Marks": [{{Effective_Sentences_Marks}}, "{{Explanation_for_effective_sentences_score}}"],
    #     "Cohesiveness_Marks": [{{Cohesiveness_Marks}}, "{{Explanation_for_cohesiveness_score}}"],
    #     "Total_Marks": [{{Total_Marks}}, "{{Explanation_for_Total_Marks}}"],
    #     "Strengths": "[List of strengths from the user's answer]",
    #     "Weaknesses": "[List of weaknesses from the user's answer that need improvement]",
    #     "50_Marks_Answer": "[Generate a 50-mark précis answer for the passage, ensuring it addresses all marking criteria comprehensively, with '90-120 words' in response to {passage}]",
    #     "AI_Suggestions": "[Provide actionable suggestions for improvement based on the user's précis answer: {precis_text}. Focus on grammar, clarity, structure, conciseness, and task achievement.]",
    #     "Improved_Solution": "[Refine the user's précis answer: {precis_text} to improve clarity, vocabulary, and content organization while preserving the original meaning and intent, aiming for full marks.]"
    # }}
    # """

    prompt = f"""
    You are an experienced examiner tasked with evaluating précis writing submissions for the SSC CGL descriptive writing test. Your role is to assess the précis based on the specific marking criteria, ensuring adherence to the format, word limit, and retention of the original passage's core message. Follow these instructions to evaluate the précis fairly, objectively, and consistently.

    ### Précis Writing Guidelines:
    1. **Word Limit**: 
    - The précis must not exceed 90 words (in English) or 100 words (in Hindi).
    - Ideally, the précis should be one-third the length of the original passage.
    2. **Central Idea**:
    - Retain the central idea and key points of the original passage.
    - The précis must stay true to the author's intent and tone.
    3. **Structure**:
    - Write the précis in one cohesive paragraph.
    - Avoid unnecessary details or examples from the original passage.
    4. **Language**:
    - Use clear, simple, and concise sentences.
    - Avoid jargon, slang, abbreviations, or personal opinions.
    5. **Originality**:
    - Write in your own words while retaining key terms from the original passage.
    - Do not copy phrases or sentences directly from the passage.
    6. **Title**:
    - Provide a title that accurately reflects the core theme of the précis.

    ### Evaluation Criteria:
    The précis will be scored based on the following parameters:
    1. **Relevance**: Focus on including only essential points and omitting irrelevant details and also if answer is null then its should be scored 0.
    2. **Clarity**: Ensure the ideas are expressed clearly and concisely.
    3. **Adherence to Word Limit**: Stay within the prescribed word limit (90 words in English, 100 words in Hindi).
    4. **Language and Grammar**: Maintain proper grammar, spelling, and punctuation.
    5. **Retention of Original Voice**: Ensure the tone and intent of the original passage are preserved.

    ### Marking Scheme :
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

    ### Scoring Rules:
    1. **Zero for Blank or Entirely Irrelevant Précis**: STRICTLY Award zero marks if the précis is completely off-topic or blank.
    2. **Partial Scoring for Mixed Quality**: Deduct marks proportionally for minor errors or if the précis includes some relevant and some irrelevant content.
    3. **Full Marks for Exceptional Précis**: Award full marks for a précis that is concise, coherent, and error-free, with only minor issues.

    ### Evaluation Instructions:
    1. **Strict Scoring for Errors**: Be fair yet precise, and provide justifications for all deductions.
    2. **Constructive Feedback**: Highlight strengths, weaknesses, and areas for improvement.
    3. **Perfect Précis Example**: Provide a model précis demonstrating a full 50 marks for the given passage.
    4. **Improved User Answer**: Revise the user's précis to show how it can achieve a full 50-mark score.

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
        "Strengths": "[List of strengths in the user's précis]",
        "Weaknesses": "[List of weaknesses and areas of improvement]",
        "50_Marks_Answer": "[Provide a model précis for the given passage: {passage}, that demonstrates a perfect score based on all evaluation criteria.]",
        "AI_Suggestions": "[List specific suggestions to improve the user's précis based on evaluation criteria.]",
        "Improved_Solution": "[Provide a revised version of the user's précis: {precis_text}, that addresses weaknesses and demonstrates how to achieve a full 50-mark score.]"
    }}

    **Original Passage**: "{passage}"  
    **Précis Text**: "{precis_text}"
    """


    
    try:
        # Sending précis and question to Groq API for evaluation
        response = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        
        # Extract the response and process it
        cleaned_content = clean_invalid_chars(response.choices[0].message.content.strip())
        evaluation_result, parse_error = safe_json_parse(cleaned_content)

        result = {
            "Word_Count": len(precis_text.split()),
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
            "raw_response": cleaned_content,
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

    except Exception as e:
        return {"error": f"An error occurred while processing the request: {str(e)}"}

# # Example usage
# question = "Write a précis of the following passage in not more than 90 words."
# passage = """The rise of artificial intelligence (AI) is one of the most profound shifts in human history. From self-driving cars to healthcare applications, AI is revolutionizing the way we live and work. However, the rapid development of this technology raises concerns about its impact on jobs, privacy, and security. As AI continues to evolve, it is crucial that we consider the ethical implications and ensure that its benefits are widely distributed."""
# precis_text = """AI is revolutionizing various sectors, including healthcare and transportation. However, it raises concerns about job losses, privacy, and security. As AI develops, it is important to address these challenges and ensure its responsible use for the benefit of all."""
# type = "medium"
# print(evaluate_ssc_precis(question, precis_text, type))
