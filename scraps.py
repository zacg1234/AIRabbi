prompt = f"""You will be provided with a question delimited by angle brackets \
    output a python list of words or phrases that you do not understand from the question. \
    If you understand all of the words and phrases output an empty python list.\
    
    question: <{question}>"""

response = get_completion(prompt, MODEL)
print(response)