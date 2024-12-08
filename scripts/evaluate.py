from rouge import Rouge
from bert_score import score

def calculate_rouge(reference, candidate):
    rouge = Rouge()
    scores = rouge.get_scores(candidate, reference)
    return scores

def calculate_bertscore(reference, candidate, model_type="bert-base-uncased"):
    P, R, F1 = score(candidate, reference, model_type=model_type, lang="en")
    return {"precision": P.mean().item(), "recall": R.mean().item(), "f1": F1.mean().item()}

if __name__ == "__main__":
    ref = ["This is the reference."]
    cand = ["This is the candidate."]
    
    print("ROUGE:", calculate_rouge(ref, cand))
    print("BERTScore:", calculate_bertscore(ref, cand))