from datasets import load_dataset
import numpy as np

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

age_list = dataset["train"]["age"]
age_array = np.array(age_list)
