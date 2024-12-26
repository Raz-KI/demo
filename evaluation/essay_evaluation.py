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
    
    # prompt = f"""
    # Assume you are an examiner for the SSC CGL descriptive writing test. Your task is to evaluate the response solely based on the given prompt for the following criteria: Lexical Resource, Grammatical Range and Accuracy, Task Achievement, and Coherence and Cohesion. Assign marks from 0-50 for criterion based on provided description. Remain consistent in your assessment even if the same response is submitted multiple times.
    # Evaluate based on the selected difficulty level: {difficulty_type}.

    # 1. **Lexical Resource**: The range and accuracy of vocabulary used in the essay.
    # 2. **Grammatical Range and Accuracy**: The complexity and correctness of the grammar used.
    # 3. **Task Achievement**: How well the essay addresses the question, providing relevant arguments and supporting details.
    # 4. **Coherence and Cohesion**: The flow and organization of ideas and the use of transitions between sentences and paragraphs.

    # The essay is expected to follow the structure of:
    # - **Introduction**: Brief introduction of the topic and your thesis statement.
    # - **Body**: 2-3 paragraphs with clear topic sentences, development, examples, and a summary at the end.
    # - **Conclusion**: Restate your position and summarize key points.

    # The SSC CGL essay is evaluated on the following marking scheme {marking_scheme} with description:
    # - **Relevance**: How well the essay addresses the topic (10 marks).
    # - **Spelling/Grammar**: Accuracy in spelling and grammar (5 marks).
    # - **Word Limit**: Adherence to the word limit (5 marks).
    # - **Content Quality**: Depth and clarity of content (8 marks).
    # - **Format**: Proper essay format (5 marks).
    # - **Writing Neatness**: Clarity and neatness of writing (5 marks).
    # - **Effective Sentences**: Use of varied and clear sentence structures (7 marks).
    # - **Cohesiveness**: Logical flow and transitions between ideas (5 marks).

    # Please evaluate the essay based on these criteria. Provide scores for each category, explain why the scores were assigned, and suggest improvements. Also, give an example of a perfect 50-mark answer for the question.'And also the total marks given should be out of 50'.
    # Remember if there is nothing like the answer is blank then all score will be 0 and also remember this strictly that if the answer is not based on the question or is in other direction then also all the scores will be 0. (please evaluate this very strictly)
    
    # Essay Question: "{question}"
    # Essay Text: "{essay_text}"

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
    #     "50_Marks_Answer": "[Generate a 50-mark answer for the essay question of SSC CGL descriptive part, ensuring it addresses all marking criteria comprehensively, with '200-250 words' in response to {question}]",
    #     "AI_Suggestions": "[Provide specific suggestions for improvement based on the user's answer in {essay_text}]",
    #     "Improved_Solution": "[Provide a 50-mark improved solution for the user's answer {essay_text} based on the essay question asked which was {question}]"
    # }}
    # """

    # prompt = f"""
    # You are an examiner for the SSC CGL descriptive writing test. Your task is to **strictly and objectively evaluate the provided response** based solely on the given essay question and specific marking criteria. Ensure consistency in evaluation, even if the same response is submitted multiple times. Responses must adhere closely to the essay topic; irrelevant or blank answers should be awarded zero marks in all categories. 
    # Evaluate based on the selected difficulty level: {difficulty_type}.
    
    # ### Evaluation Criteria:
    # 1. **Lexical Resource**: Evaluate the range, accuracy, and appropriateness of vocabulary used in the essay.
    # 2. **Grammatical Range and Accuracy**: Assess the complexity and correctness of sentence structures, punctuation, and grammar.
    # 3. **Task Achievement**: Measure how well the essay addresses the essay question, provides relevant arguments, and includes adequate supporting details.
    # 4. **Coherence and Cohesion**: Examine the logical flow of ideas, effective transitions between sentences/paragraphs, and overall organization of content.

    # ### Essay Format Guidelines:
    # 1. **Introduction**:  
    # - Briefly introduce the topic and provide a clear thesis statement (the writer's position).  
    # - Establish the context and mention the main points to be covered.

    # 2. **Body**:  
    # - Write 2-3 paragraphs. Each should include:
    #     - A topic sentence to introduce the paragraph's main idea.
    #     - Development with examples, arguments, or explanations.
    #     - A summary to reinforce the point discussed.
    # - Ensure clarity, relevance, and balanced coverage of the topic.

    # 3. **Conclusion**:  
    # - Restate the central idea or thesis.
    # - Summarize the key points from the body.
    # - End with a future outlook, suggestion, or impactful statement.

    # ### Marking Scheme and Weightage:
    # The essay will be evaluated out of **50 marks**, distributed as follows:
    # - **Relevance (10 marks)**: How well the essay addresses the topic and its requirements. Irrelevant essays score zero.  
    # - **Spelling/Grammar (5 marks)**: Assess spelling accuracy and grammatical correctness.  
    # - **Word Limit (5 marks)**: Adherence to the word limit (200-250 words); exceeding or undercutting limits impacts scores.  
    # - **Content Quality (8 marks)**: Depth, clarity, and reasoning within the content.  
    # - **Format (5 marks)**: Adherence to the standard essay structure (introduction, body, conclusion).  
    # - **Writing Neatness (5 marks)**: Assess clarity, readability, and neatness.  
    # - **Effective Sentences (7 marks)**: Use of varied, impactful, and error-free sentence structures.  
    # - **Cohesiveness (5 marks)**: Logical transitions and smooth flow of ideas.

    # ### Evaluation Instructions:
    # 1. Score each criterion from 0 to its respective maximum marks, with a clear explanation for the assigned score.  
    # 2. Total marks must not exceed 50.  
    # 3. For irrelevant answers, assign 0 marks to all categories.  
    # 4. Provide constructive feedback highlighting strengths and weaknesses of the essay.

    # ### Final Output (Strictly JSON Format with No Additional Text):
    # {{
    #     "Relevance_Marks": [{{Relevance_Marks}}, "{{Explanation_for_relevance_score}}"],
    #     "Spelling_Grammar_Marks": [{{Spelling_Grammar_Marks}}, "{{Explanation_for_spelling_grammar_score}}"],
    #     "Word_Limit_Marks": [{{Word_Limit_Marks}}, "{{Explanation_for_word_limit_score}}"],
    #     "Content_Quality_Marks": [{{Content_Quality_Marks}}, "{{Explanation_for_content_quality_score}}"],
    #     "Format_Marks": [{{Format_Marks}}, "{{Explanation_for_format_score}}"],
    #     "Writing_Neatness_Marks": [{{Writing_Neatness_Marks}}, "{{Explanation_for_writing_neatness_score}}"],
    #     "Effective_Sentences_Marks": [{{Effective_Sentences_Marks}}, "{{Explanation_for_effective_sentences_score}}"],
    #     "Cohesiveness_Marks": [{{Cohesiveness_Marks}}, "{{Explanation_for_cohesiveness_score}}"],
    #     "Total_Marks": [{{Total_Marks}}, "{{Explanation_for_Total_Marks}}"],
    #     "Strengths": "[List of strengths in the user's answer.]",
    #     "Weaknesses": "[List of weaknesses in the user's answer that require improvement.]",
    #     "50_Marks_Answer": "[Generate a comprehensive, perfect 50-mark response for the question: {question}, adhering strictly to the marking criteria of relevance, grammar, content depth, structure, and cohesiveness. Ensure the response is within the word limit and demonstrates excellence in vocabulary, transitions, argument development, and conclusion.]",
    #     "AI_Suggestions": "[Provide actionable suggestions to improve the user's answer: {essay_text} , based on the evaluation criteria.]",
    #     "Improved_Solution": "[Refine the user's submitted answer: {essay_text}, based on the essay question: {question}. Retain the original ideas and structure while addressing weaknesses in grammar, vocabulary, flow, and content depth. Enhance the response to meet all evaluation criteria and achieve a full 50-mark score without deviating from the user's intent or tone.]"
    # }}
    # Essay Question: "{question}"
    # Essay Text: "{essay_text}"
    # """
    
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

        # try:
        #     result["Relevance_Marks"] = evaluation_result.get("Relevance_Marks", "N/A")
        # except Exception as e:
        #     print(f"Error extracting Relevance marks: {e}")

        # try:
        #     result["Spelling_Grammar_Marks"] = evaluation_result.get("Spelling_Grammar_Marks", "N/A")
        # except Exception as e:
        #     print(f"Error extracting Spelling Grammar Marks: {e}")

        # try:
        #     result["Word_Limit_Marks"] = evaluation_result.get("Word_Limit_Marks", "N/A")
        # except Exception as e:
        #     print(f"Error extracting Word Limit Marks: {e}")

        # try:
        #     result["Content_Quality_Marks"] = evaluation_result.get("Content_Quality_Marks", "N/A")
        # except Exception as e:
        #     print(f"Error extracting Content Quality Marks: {e}")

        # try:
        #     result["Format_Marks"] = evaluation_result.get("Format_Marks", "N/A")
        # except Exception as e:
        #     print(f"Error extracting Format Marks: {e}")

        # try:
        #     result["Writing_Neatness_Marks"] = evaluation_result.get("Writing_Neatness_Marks", "N/A")
        # except Exception as e:
        #     print(f"Error extracting Writing Neatness Marks: {e}")

        # try:
        #     result["Effective_Sentences_Marks"] = evaluation_result.get("Effective_Sentences_Marks", "N/A")
        # except Exception as e:
        #     print(f"Error extracting Effective Sentences Marks: {e}")

        # try:
        #     result["Cohesiveness_Marks"] = evaluation_result.get("Cohesiveness_Marks", "N/A")
        # except Exception as e:
        #     print(f"Error extracting Cohesiveness Marks: {e}")

        # try:
        #     result["Total_Marks"] = evaluation_result.get("Total_Marks", "N/A")
        # except Exception as e:
        #     print(f"Error extracting Total Marks: {e}")

        # try:
        #     result["Strengths"] = evaluation_result.get("Strengths", "N/A")
        # except Exception as e:
        #     print(f"Error extracting Strengths: {e}")

        # try:
        #     result["Weaknesses"] = evaluation_result.get("Weaknesses", "N/A")
        # except Exception as e:
        #     print(f"Error extracting Weaknesses: {e}")

        # try:
        #     result["50_Marks_Answer"] = evaluation_result.get("50_Marks_Answer", "N/A")
        # except Exception as e:
        #     print(f"Error extracting 50 Marks Answer: {e}")

        # try:
        #     result["AI_Suggestions"] = evaluation_result.get("AI_Suggestions", "N/A")
        # except Exception as e:
        #     print(f"Error extracting AI Suggestions: {e}")

        # try:
        #     result["Improved_Solution"] = evaluation_result.get("Improved_Solution", "N/A")
        # except Exception as e:
        #     print(f"Error extracting Improved Solution: {e}")

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



