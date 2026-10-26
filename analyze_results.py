
import pandas as pd

# Load the saved results
df = pd.read_csv("dataset/results.csv")

print("===== LOCAL LLM PERFORMANCE REPORT =====")

# Total prompts processed
print("\nTotal prompts processed:", len(df))

# Average response time
print(
    "Average response time:",
    round(df["response_time_seconds"].mean(), 2),
    "seconds"
)

# Fastest response
fastest = df.loc[df["response_time_seconds"].idxmin()]
print("\nFastest prompt:", fastest["prompt"])
print("Fastest response time:", fastest["response_time_seconds"], "seconds")

# Slowest response
slowest = df.loc[df["response_time_seconds"].idxmax()]
print("\nSlowest prompt:", slowest["prompt"])
print("Slowest response time:", slowest["response_time_seconds"], "seconds")

# Average response time by domain
print("\nAverage response time by domain:")
print(df.groupby("domain")["response_time_seconds"].mean().round(2))

print("\nReport generated successfully!")

# Save domain-wise performance report
domain_report = (
    df.groupby("domain")["response_time_seconds"]
    .mean()
    .round(2)
    .reset_index()
)

domain_report.to_csv(
    "dataset/domain_performance.csv",
    index=False
)

print("\nDomain report saved to dataset/domain_performance.csv")
