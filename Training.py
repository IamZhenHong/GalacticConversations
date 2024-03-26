from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open("data.jsonl", "rb"),
  purpose="fine-tune"
)


client.fine_tuning.jobs.create(
  training_file="file-abc123", 
  model="babbage-002",
)