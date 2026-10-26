

import ollama
import pandas as pd
import time

# Load all prompts
df = pd.read_csv("dataset/prompts.csv")

results = []

# Generate a response for every prompt
for index, row in df.iterrows():
    prompt = row["prompt"]

    print(f"\nPrompt {index + 1}: {prompt}")
    print("Generating response...")

    start_time = time.time()

    response = ollama.generate(
        model="llama3.2:1b",
        prompt=prompt
    )

    end_time = time.time()
    response_time = round(end_time - start_time, 2)

    answer = response["response"]

    print("Response:", answer)
    print("Response time:", response_time, "seconds")

    results.append({
        "id": row["id"],
        "domain": row["domain"],
        "prompt_type": row["prompt_type"],
        "prompt": prompt,
        "model": "llama3.2:1b",
        "response": answer,
        "response_time_seconds": response_time
    })

# Save all results to CSV
results_df = pd.DataFrame(results)
results_df.to_csv("dataset/results.csv", index=False)

print("\nAll prompts processed successfully!")
print("Results saved to dataset/results.csv")

# Analyze response times
average_time = results_df["response_time_seconds"].mean()
slowest_prompt = results_df.loc[
    results_df["response_time_seconds"].idxmax()
]

print("\n--- Performance Summary ---")
print(f"Average response time: {average_time:.2f} seconds")
print(f"Slowest prompt: {slowest_prompt['prompt']}")
print(
    f"Slowest response time: "
    f"{slowest_prompt['response_time_seconds']} seconds"
)
