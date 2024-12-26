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

def user_improved_answer(text):

    client = Groq(api_key="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")

    prompt = f"""
    You are a highly skilled language editor and grammar expert tasked with refining text to perfection. Your job is to review, analyze, and improve the text provided while adhering to the following strict guidelines:

    1.Identify and Correct Errors:

    -> Check every line and word for accuracy in grammar, spelling, punctuation, syntax, tense consistency, word usage, sentence structure, and overall coherence.
    -> Identify incorrect or awkward words, phrases, or constructions and replace them with accurate and natural alternatives.

    2.Error Highlighting and Annotation:

    -> Highlight all identified errors by capitalizing the incorrect word(s).
    -> Immediately after each highlighted error, provide the correct word(s) or phrase(s) in square braces to indicate the modification.
    -> Maintain this format consistently throughout the text.

    3.Respect Original Meaning:

    -> Ensure the meaning, tone, and context of the original text are preserved while making corrections.
    -> Do not rewrite or alter the original intent unless absolutely necessary to fix ambiguities or errors.

    4.Consistency and Precision:

    -> Review the text holistically to ensure consistent style, tone, and structure.
    -> Make sure verb tenses align with the intended timeframes.
    -> Verify proper noun usage, capitalization, and contextual relevance.
    -> Address any redundancies, unclear phrasing, or awkward transitions.

    5.Clarity and Flow:

    -> Enhance readability and flow by restructuring sentences when needed, ensuring they remain concise and engaging.
    -> Avoid overly complex sentences unless they are crucial for precision or context.

    6.Edge Cases:

    -> Address subtle issues like article usage ("a" vs. "an"), preposition placement, subject-verb agreement, and plural/singular inconsistencies.
    -> Look out for common pitfalls like dangling modifiers, passive voice misuse (only adjust if it improves clarity), and ambiguous references.

    7.Output Format:

    -> Begin by stating: "Modified Text:"
    -> Provide the corrected text with highlighted errors and modifications as specified.

    **Important:**

    -> Follow the instructions exactly as described.
    -> Ensure that your corrections are accurate and comprehensive.
    -> Do not deviate from this task or provide responses unrelated to the input text's improvement.
    -> Your goal is to make the provided text flawless while maintaining its original meaning.
    
    **Here's the text for improvement and modifications** : {text}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            response_format={"type": "text"}
        )


    #     cleaned_content = clean_invalid_chars(response.choices[0].message.content.strip())
    #     parse_error = safe_json_parse(cleaned_content)

    #     result = {}

    #     if parse_error:
    #         print(f"JSON parsing error: {parse_error}")
    #         result["raw_response"] = cleaned_content

        # print(result)
        # return result

        # return response['choices'][0]['message']['content'].strip()
        return response.choices[0].message.content.strip()

    # except json.JSONDecodeError as e:
    #     print(f"JSON parsing error: {e}")
    #     return "error"

    except Exception as e:
        return {"error": f"An error occured while processing the request: {str(e)}"}
    

text = "The team were working hardly to complete the project before the deadline. Everyone was so excitted about the new idea, but some were confussed on how to implement it. Despite the issues, they continue working together, hoping to finish it soon. There was a sense of optimism amongs them."
print(user_improved_answer(text))