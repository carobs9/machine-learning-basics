
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
from datasets import load_dataset
from transformers import Trainer, TrainingArguments
from transformers import DataCollatorForTokenClassification
from transformers import pipeline
import PyPDF2 

tokenizer = AutoTokenizer.from_pretrained('dccuchile/bert-base-spanish-wwm-uncased')
data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)

# functions
def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        num_pages = len(pdf_reader.pages)

        # Loop through all pages and extract text
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text

def tokenize_and_align_tags(records):
    # Tokenize the input words. This will break words into subtokens if necessary.
    # For instance, "ChatGPT" might become ["Chat", "##G", "##PT"].
    tokenized_results = tokenizer(records["tokens"], truncation=True, is_split_into_words=True)

    input_tags_list = []

    # Iterate through each set of tags in the records.
    for i, given_tags in enumerate(records["ner_tags"]):
        # Get the word IDs corresponding to each token. This tells us to which original word each token corresponds.
        word_ids = tokenized_results.word_ids(batch_index=i)

        previous_word_id = None
        input_tags = []

        # For each token, determine which tag it should get.
        for wid in word_ids:
            # If the token does not correspond to any word (e.g., it's a special token), set its tag to -100.
            if wid is None:
                input_tags.append(-100)
            # If the token corresponds to a new word, use the tag for that word.
            elif wid != previous_word_id:
                input_tags.append(given_tags[wid])
            # If the token is a subtoken (i.e., part of a word we've already tagged), set its tag to -100.
            else:
                input_tags.append(-100)
            previous_word_id = wid

        input_tags_list.append(input_tags)

    # Add the assigned tags to the tokenized results.
    # In the Hugging Face Transformers library, a model recognizes the labels parameter
    # for computing losses along with logits (predictions)
    tokenized_results["labels"] = input_tags_list

    return tokenized_results