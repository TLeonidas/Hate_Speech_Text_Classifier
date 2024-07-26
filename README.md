# Monitoring Harmful Text in Online Platforms

## Overview
This repository hosts the RandomForest classifier model designed for detecting harmful text AGAINST GROUPS. 
The model classifies text into one of three categories: "Offensive or Hateful", "Neutral or Ambiguous", and "Not Hate". 
Achieving an accuracy of 92.5%, this model was developed through the combination of three distinct datasets, ensuring robustness and reliability in varied contexts. 
It was presented at the prestigious annual Gulf Coast Conference & Expo on AI.

Model Details
Model Type: RandomForest Classifier
Accuracy: 92.5%
Labels:
0: Neutral or Ambiguous
1: Not Hate
2: Offensive or Hateful
Training Data: Augmented version of [this dataset](https://huggingface.co/datasets/TLeonidas/twitter-hate-speech-en-240ksamples) (279k+ rows)

## Dataset
The model was trained on a concatenated dataset from three distinct sources, curated to encompass a wide range of linguistic expressions and contexts. 
The datasets were preprocessed and balanced to ensure fair representation across all categories.

## Performance
The model achieves an accuracy of 92.5%, evaluated on a held-out test set.

## Contributing
We welcome contributions to improve the model and extend its applicability. 
