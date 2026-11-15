# Language Modeling Materializes a World Model of Protein Biology

See https://biohub.ai/papers/esm_protein.pdf?__clerk_synced=true

We propose language modeling to learn unified and general representations that can be scaled to all of protein biology. Based on these representations, we develop a structure prediction model.

Study of the concepts in the language model's representation space reveals a systematic organization aligned with the reductionist understanding of proteins developed through empirical science. Leveraging this organization, we generate a comprehensive map of protein biology.

Generations of ESM models have demonstrated that protein language models develop representations of the biological properties of proteins that drive evolution's selection of amino acids across life.

- ESM1 found representations of biological structure and function from training a transformer on protein sequences at the scale of evolution with a language modeling objective,
- ESM1b used attention heads that correlate with long-range residue-residue contacts in the protein's folded structure,
- ESM2 showed that representations continue to improve with scale and can be projected into atomic resolution 3D structure, matching the accuracy of state-of-the-art structure predictors,
- ESM3 demonstrated that a language model of the joint distribution of protein sequence, structure and function internalized fundamental principles of structure and function sufficient to generate a fluorescent protein highly divergent from the sequence of any other known protein.

In every generation of ESM, improvements in the fidelity of the representations were linked with the number of parameters and the amount of compute used in model training. The representation of the biology of proteins is an emergent phenomenon that arises from training a model to predict the identity of the amino acids in the sequence.

ESMFold does not use a multi sequence alignment as the primary input. It instead builds on unsupervised language modeling as a substrate for representing protein biology. As a foundation to the system, one trained ESM Cambrian with a masked language modeling objective. Since ESMC trains on metagenomic sequences, the training dataset size is expanded by 2 orders of magnitude.

Mechanistic investigation of the representations of the ESMC transformer with sparse coding reveals the concepts the model uses to represent proteins. We find a reduction of protein biology into a system of more basic properties and biological concepts which aare organized hierarchically, across physical scales, levels of complexity and biological abstraction.

## A scaling law of protein language models

ESMC is a family of transformer models trained on protein sequences using the masked language modeling objective. The model is trained to predict the amino acids at randomly masked positions in the context x\M of protein sequences across evoluation.

These models develop representations that contain information about the biological properties encoded by the distribution of protein sequences. The latent representations are formed by the activations of each of the neurons in each of the layers of the network as it processes a sequence.

Representations are continuous, high-dimensional vectors (d), one for each position in the protein's sequence.

The transformer processes information through two primary mechanisms:

1. Self-attention networks which transfer information between representations of positions in the sequence, which alternate with,
2. Feedforward networks which process the representation of each position individually,

Increasing training data is sufficient for continued returns to scaling compute.

### Questions

- What does this across evolution mean?
