import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer


def generateText(sentence):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2-large")
    model = TFGPT2LMHeadModel.from_pretrained("gpt2-large", pad_token_id=tokenizer.eos_token_id)
    # prompt = "Answer to this sentence: '"
    # promptSentence = prompt + sentence + "'"
    input_ids = tokenizer.encode(sentence, return_tensors='tf')
    output = model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, early_stopping=True,
                            eos_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    response = response.replace(sentence, '')
    response = response.replace('"', '')
    response = "\n".join([line for line in response.splitlines() if line.strip()])

    return response
