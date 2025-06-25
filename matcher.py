from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')
def compute_cosine_similarity(resume_text, job_description):
    """
    Compute cosine similarity between resume text and job description.
    """
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_desc_embedding = model.encode(job_description, convert_to_tensor=True)

    cosine_scores = util.pytorch_cos_sim(resume_embedding, job_desc_embedding)
    return cosine_scores.item()
