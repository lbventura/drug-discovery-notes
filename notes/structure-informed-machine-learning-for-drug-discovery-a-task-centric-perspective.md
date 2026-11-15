# Structure-informed machine learning for drug discovery: a task centric perspective

Evolution from traditional docking and scoring frameworks toward geometry-informed deep learning architectures that encode protein structures via surface geometry, equivariant representations and multi-modal embeddings.

We classify generative approaches into four core strategies:
- sequence-based generation with 3D conditioning,
- fragment-based linking and growing,
- graph-based generation under structural constraints,
- 3D coordinate-based generation including diffusion models.

Each paradigm balances chemical validity, spatial fidelity and computational tractability in distinct ways, with diffusion-based and point cloud models emerging as powerful tools for synthesizing pocket-complementary molecules in full 3D space. We also discuss the emergence of co-folding models, which unify protein folding and ligand binding into a single predictive framework, bridging the gap between sequence-level learning and structural resolution. Finally, we examine the key challenges of data scarcity, generalization and multi-objective control, and outline future directions toward scalable, interpretable, and physically plausible generation pipelines. 

Five tasks:
1. binding-site identification,
2. pose prediction,
3. interaction and affinity scoring,
4. structure-based virtual screening (SBVS),
5. structure conditioned molecular generation

## Introduction

Central to rational drug design is the structural understanding of protein targets, which enables the identification of novel druggable pockets. For decades, however, progress in structure-based design was limited by the scarcity and cost of experimentally resolved protein structures. Typically these were obtained through X-ray crystallography or cryo-electron microscopy.

Deep learning models as AlphaFold2 have transformed protein structures from rare experimental assets into accessible, proteome-wide computational resources. AlphaFold3 expands this capacity by supporting multimolecular complex modelling - including interactions with ligands, RNA and DNA - enabling end-to-end prediction of drug-target assemblies.

**Traditional structure-based approaches** such as molecular docking and dynamics simulations often **rely** on **rigid** or **pre-selected conformations**, limiting their flexibility, scalability and accuracy.

OTOH, **sequence-based learning frameworks** (e.g, compound-protein interaction prediction) l**ack spatial resolution** and **fail** to **capture** the **geometric** and **physicochemical** complexity of **binding interactions**.

Bridging this gap requires a new generation of structure-aware deep learning models capable of explicitly encoding and leveraging protein structural features across scales and modalities.

3 tightly coupled modeling goals:

1. **Identifying where and how to bind**: binding site detection, structure-based screening, and pose prediction models that localize druggable regions and recover ligand conformations within protein pockets,
2. **Quantifying binding strength:** affinity prediction and interaction scoring models that learn spatial and energetic priors for assessing molecular complementarity,
3. **Designing what to bind**: structure-informed molecular generation, where diverse generative frameworks, ranging from sequence-based to 3D coordinate-based models, construct novel ligands under protein constrains.

## Brief introduction of structure-informed machine learning

Accurate protein structures form the molecular foundation for understanding drug-target interactions; it guides the identification of druggable sites and enables atomic-resolution modeling of binding poses.

## Featurization and modelling of protein structures

**Protein structures are hierarchical, with multiple levels of organization relevant to different modelling objectives.** Because the full atomic representation of the complete protein structure usually becomes intractable, researchers adopt coarse-grained or task-specific structure abstractions - ranging from atomistic detail, to backbone traces, residue level encodings and surface geometries - to strike a balance between informativeness and efficiency.

| Level | Key components | Representative features | Common use cases |
| :--- | :--- | :--- | :--- |
| **Atom level** | Heavy atoms (C, N, O, S, plus F/P/Cl/Br in special cases) | • Atomic properties: charge, hybridization, valence, electronegativity, vdW radius<br>• Bond features: bond type, stereochemistry, H-bond donor/acceptor | Binding affinity prediction, pose evaluation |
| **Backbone level** | Peptide chain (N–Cα–C=O) | • Dihedral angles (φ, ψ)<br>• Secondary structure (helix, sheet, coil)<br>• Connectivity, cis/trans conformation | Conformation modeling, fold classification |
| **Residue level** | 20 natural amino acids | • AAindex-derived descriptors<br>• Physicochemical descriptors (charge, hydrophobicity, volume, polarity), referring to dataset like AAindex[21]<br>• Semantic embeddings from protein language models (e.g. ESM[22], TAPE, and Saprot [23]) | Pocket prediction, interaction classification |
| **Surface level** | Solvent-accessible interface | • Geometric features: curvature, shape index, point normals [24]<br>• Chemical features: electrostatics, hydrophobicity, charge distribution<br>• Chemical features: charge distribution, hydrophilicity, and hydrophobicity [25] | Pocket detection, structure-conditioned generation |

Each level of representation captures distinct biochemical and spatial features, thereby oferring distinct advantages and limitations;

- Atom-level encodings provide fine-grained resolution required for modeling local complementarity and precise energetic interactions, but are often limited to small subregions due to computational cost,
- Backbone- and residue-level representations offer more scalable alternatives, enabling fold-level reasoning and generalized pattern recognition while sacrificing atomic detail,
- Surface-base representations retain key geometric and chemical interface features relevant to ligand recognition, while reducing input complexity (by omitting internal flexibility or allosteric context).

These representations underpin three major structural modeling paradigms - graph-based, grid-based and surface-based - that define how structural information is integrated into deep learning architectures.

### Protein structure modelling

Once protein structures are appropriately represented, the next challenge lies in designing model architectures that can effectively process and learn from their spatial organization. The choice of modelling paradigm is tightly coupled with the input format:

- atom-level **graphs**, (graph based)
- voxelized spatial **grids**, (grid based)
- molecular **surfaces,** (surface based)

each afford distinct inductive biases and encode spatial relationships, geometric constraints and structural features in different ways.

### Graphs

Graphs are a natural and efficient abstraction for protein structures, capturing spatial or chemical relationships in a flexible format. In **protein graphs**, nodes typically represent atoms, residues or backbone units, and edges encode pairwise proximity (e.g., distance cutoff), physical bonds, or geometric features such as relative angles or orientations.

GNNs have become the foundation for many structure-aware models. Models such as GCN, GraphSAGE, GIN and GAT enable contextual aggregation over neighbouring nodes. As a result, these models capture local topological and spatial correlations, making them well suited for tasks such as **secondary structure prediction, fold classification, or backbone reconstruction.**

To better handle the 3D geometric nature of proteins, SO(3)-equivariant GNNs have been developed. These models preserve rotation and translation equivariance, ensuring that the learned features are invariant to global rigid-body transformations. Examples are GVPs, GBP and DWP. These architectures enable learning directly on the 3D molecular manifold and are particularly beneficial for **capturing structural regularities such as symmetry, repeat motifs and fold topolgy.**

### Grids

These discretize the 3D space around a protein into voxels, where each **voxel encodes local properties** such as atom type, occupancy, charge or hydrophobicity. These representations align naturally with 3D-CNNs, which apply spatial filters to learn hierarchical structural features. As a result, they can directly model:

- volumetric shapes,
- density distributions,
- interaction cavities,

making grid-based methods effective for tasks such as binding-site localization, structure similarity assessment, or local conformation analysis. However, they have key limitations:

- high memory cost,
- low scalability for full-protein or proteome-scale tasks,
- resolution trade-offs (finer grids improve accuracy but increase computation)
- fixed frame assumptions limit flexibility in modeling conformational ensembles.

### Surfaces

Proteins exert their functions primarily through molecular interactions that occur at their surfaces. In structure-aware learning, accurate modeling of **protein surfaces** provides insights into:

- binding-site geometry,
- interface shape complementarity,
- electrostatic patterns,

which are essential for downstream tasks such as:

- pocket detection,
- interface matching,
- ligand generation,

Unlike voxel-based models, they operate directly on interaction-relevant features without modelling the internal atomic structure. Compared with graph-based models, they provide more accurate shape and interface context, especially useful in modeling binding selectivity or identifiying cryptic pockets.

However, they typically require additional pre-processing and are sensitive to structural noise, especially when applied to predicted (rather than experimental) protein structures.

### Structure-informed drug-target binding modelling

Different levels of protein structural representation provide inputs to four core tasks:

- binding-side identification,
- binding strength modelling,
- structure-based virtual screening,
- co-folding models

### Binding site identification

These druggable pockets represent accessible regions with suitable geometric and physicochemical environments for small-molecule binding.

**Classical computation tools (using geometric descriptors or energetic grids) -> 3D voxelized representations of protein structures -> surface-based representations -> end-to-end geometric learning with build-in symmetry awareness and dynamic context**

These models treat the solvent-accessible surface as a point cloud; what differs is how the each point in the cloud is encoded.

A parallel stream is to use DL frameworks that process raw 3D coordinates using rotation- and translation-equivariant architectures, like EquiPocket (E(3)-equivariant GNN for pocket prediction). PocketMiner has a similar but dynamic approach by training on molecular simulations that capture pocket-opening events.

ScanNet integrates atomic- and residue-level embeddings, local coordinate systems and attention mechanisms. It learns hierarchical representations from atomic structures and provides interpretable predictions by attending to relevant spatial neighborhoods.

### Binding strength modelling

Task: predict the binding strength between small molecules and target proteins. This has implications for:

- virtual screening,
- lead optimization,
- mechanistic understanding of molecular recognition,

Graph-based representations of protein-ligand complexes (both molecular species are encoded as nodes and edges reflecting local structure or interaction context) -> introduction of explicit physical and energetic priors -> introduction of geometrical constraints

###  Structure-based virtual screening

Because of their increasing ability of capturing protein-ligand interactions in both strength and geometry, deep learning models are being integrated into SBVS pipelines. These prioritize candidate molecules based on their predicted poses and affinities within target protein structures, enabling more targeted and scalable compund discovery.

Traditional SBVS:

- pose generation (sampling plausible 3D conformations of ligands within protein binding pockets),
- scoring functions (estimate binding affinity or interaction likelihood)

To overcome the limitations of conventional rigid-body optimization and handcrafted scoring, deep learning models have recently shifted toward structure-aware pose prediction, wherein the protein-ligand binding process is learned directly from data.

**Models like EquiDock and DiffDock formulate pose prediction with blind docking assumptions**. EquiDock represents proteins and ligands as graphs (at the residue or atom level) and applies SE(3)-equivariant neural networks to learn transformation-invariant features (but in a rigid pose). 

DiffDock learns a diffusion-based model that incrementally constructs ligand conformations conditioned on the receptor. The model jointly represents ligand atoms, receptor residues and receptor atoms as an heterogeneous geometric graph, enabling it to capture fine-grained interaction context.

**SurfDock, however, incorporates explicit binding pocket information to improve pose location and accuracy (e.g, it is pocket conditioned).** This constructs a geometric graph comprising ligand atoms, protein surface points and pocket residues, with node features encoding electrostatics, curvature and language semantics. By leveraging a generative diffusion model, it optimizes ligand conformations not just in free space but within the spatial constraints of a predicted pocket, allowing pose sampling to be targeted and physically plausible.

**See practical guidelines on page 9.**

See pLDDT here https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/

The predicted local distance difference test (pLDDT) is a per-residue measure of local confidence. It is scaled from 0 to 100, with higher scores indicating higher confidence and usually a more accurate prediction.

pLDDT measures confidence in the local structure, estimating how well the prediction would agree with an experimental structure. It is based on the local distance difference test Cα (lDDT-Cα), which is a score that does not rely on superposition but assesses the correctness of the local distances (Mariani et al., 2013).

On this basis, a pLDDT above 90 would be taken as the highest accuracy category, in which both the backbone and side chains are typically predicted with high accuracy. In contrast, a pLDDT above 70 usually corresponds to a correct backbone prediction with misplacement of some side chains. 

### Co-folding models

The traditional pipeline for modelling protein-ligand complexes often decouples structure prediction and molecular docking, relying heavily on **experimentally determined protein structures or extensive sampling to estimate binding poses**.

Co-folding models: New class of implicit structure-aware models that predicts protein-ligand complex structures (without relying on experimentally resolved inputs), which jointly model folding and binding.

These offer distinct advantages:

- accommodate induced fit,
- cryptic pocket formation,
- binding-coupled folding,

without the need for exhaustive conformational sampling. This enables applications such as:

- mutation effect modelling,
- cryptic site targeting,
- lead prioritization under limited structural information

scenarios where traditional pipelines often struggle. Several examples of these all-atom co-folding frameworks are:

- RosettaFold All-Atom,
- AlphaFold3
- Chai-1,
- Boltz-1
- Protenix,
- Boltz-2,

Co-folding models, however, exhibit several systematic failure modes:

1. Performance drops for OOD ligands, especially macrocycles, organometallics, covalently bound warheads and ligands with > 50 atoms (because they are underrepresented in the PDB training corpus),
2. Severe overfitting and data leakage are pervasive,
3. Most models are trained on high-resolution crystal structures and fail on lower-confidence regions or in induced-fit/cryptic pocket cases that deviate from the apo template,

Tanimoto similarity: https://greglandrum.github.io/rdkit-blog/posts/2025-07-17-naming-similarity-metrics.html

### Protein structure-informed molecular generation

See Figure 4 for a representation of the 4 approaches:

1. Sequence-based with 3D conditioning (using transformers),
2. Fragment-based linking and growing (through generative model),
3. Graph-based Generation under structural constraints (through EGNN),
4. 3D coordinate-based generation (through generative model) 

### Sequence-based generation with 3D conditioning

Sequence-based generative models typically construct molecules as SMILES of SELFIES strings using molecular language models. Recently structural information - particularly protein binding pocket features - have been introduced to the generative process, bridging 1D sequence outputs with 3D spatial requirements.

Across the models, the common thread is the strategic use of lightweight 3D conditioning - whether through distance matrices, geometric encoders, or fragment-level embeddings - on top of scalable, interpretable sequence generation frameworks.

Less precise than coordinate-level generation, these models are suitable for early-stage virtual screening and scaffold exploration.

### Fragment-based linking and growing

Builds drug-like compounds by assembling or extending chemically meaningful substructures under the structural constrains of a protein target.

Compared to SMILES-based models, they offer greater interpretability and scaffold control; compared to end-to-end 3D coordinate generators, they are more modular and sample-efficient.

### Graph-based generation under structural constraints

Leverages the structural expressiveness of molecular graphs while incorporating explicit constraints from protein target geometry. They construct molecules as atom-bond graphs and condition the generation process on 3D information derived from protein binding sites, typically generated as atomistic graphs or point clouds.

The common theme of the latest generation models is the use of 3D pocket structure not just as context, but as an active constraint guiding atom placement, bond formation, and scaffold growth.

Compared to sequence-based models, they provide better control over molecular topology; compared to 3D coordinate generators, they are often more-sample efficient and easier to train.

### 3D coordinate-based generation

Directly model the Cartesian coordinates of atoms to construct fully resolved molecular conformations. Their architecture varies significantly and they increasingly serve as the backbone for structure-based de novo design.

The advent of diffusion-based generation marked a major leap in 3D molecular modeling. These models treat generation as a reverse-time denoising process that reconstructs atomic coordinates and identities from Gaussian noise, while conditioning on structural features of the target protein.

Such coordinate-level generators are best used as high-precision components for pose refinment and structure-guided optimization, complementing faster graph or sequence-based models upstream.

Despite the progress enabled by recent coordinate-based generative models, most SBDD pipelines still treat the protein binding site as static and rigid. This confines design to a single holo geometry and can miss ligands that stabilize alternative, and sometimes more favorable, pocket conformations.

**Apo:** The 3D conformation of a protein in its unbound, empty state (without a ligand or substrate attached).
**Holo:** Conformation of a protein in its bound state (when a small molecule drug or natural ligand is docked into its binding pocket).
**Apo-Holo Pairs:** A dataset containing the experimentally resolved 3D coordinates of the *exact same protein* in both its unbound (Apo) and bound (Holo) states

### Accuracy and acceptability: canonical structure prediction vs protein-aware generative design

Traditional canonical structured-based drug design - typically involving rigid or semi-flexible docking (e.g, AutoDock Vina or Glide) on static crystallogrpahic or AlphaFold-predicted templates - excels in speed and interpretability for well-defined orthosteric sites but falters on dynamic targets.

Protein-structure-aware generative models treat structures as learnable priors, yielding superior geometric plausibility and multi-modal sampling. Generated ligands exhibit higher synthetic feasibility and downstream compatibility, though they require additional filtering for novelty and ADMET compliance.

While canonical methods remain the gold standard for high-throughput validation, generative designs offer greater accuracy for challenging targets at a cost of ~10-100x higher inference time - hybrid pipelines combining both are emerging as the optimal path forward.

### Challenges and outlook

Key challenges before these models can be reliably deployed in real-world drug discovery pipelines.

1. Data availability and distributional bias. While structure prediction models have made vast protein conformational landscapes accessible, high-quality protein-ligand complex data - especially for underexplored target or non-canonical binding modes - remain sparse. This restricts model generalization and increases the risk of overfitting, particularly for co-folding and 3D generative frameworks.
2. Lack of rigorous benchmarking protocols. Current evaluation relies on retrospective datasets or proxy metrics, which do not always correlated with experimental activity. Cross-task benchmarking - e.g, evaluating generative models not only on geometry but also on impact on downstream tasks (affinity ranking, mutational robustness) - remains underdeveloped.
3. Trade-off between interpretability and expressiveness. Bridging symbolic chemical knowledge with neural architectures remains an open direction toward human-in-the-loop design and hypothesis generation.

Emerging trends:

1. Foundational models trained on multi-modal biochemical data,
2. Reinforcement learning loops with structural feedback,
3. Simulation-augmented generative models, blending ML with physical realism
4. Flexibility modeling - at both protein and ligand levels - will be critical for targeting dynamics or cryptic pockets and for predicting resistance-associated conformational shifts.

## Saved link previews

- [Please stop saying “The Tanimoto similarity is” – RDKit blog](<https://greglandrum.github.io/rdkit-blog/posts/2025-07-17-naming-similarity-metrics.html>)
  A simple tip to explain what you actually did
- [pLDDT: Understanding local confidence \| AlphaFold](<https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/>)
  AlphaFold
