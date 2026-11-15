# AMIDD Lecture 3: Key Questions in Drug Discovery

## Key questions

1. What is the unmet medical need to be addressed?
2. What is the target and the modality?
3. How much drug reach which body part? What does the **body do to the drug** (pharmacokinetics, **PK**)? What does the **drug do to the body** (pharmacodynamics, **PD**)?
4. What is the toxicity of the drug? Is it justifiable, given the benefits?
5. Who is responsive to the drug? Who is susceptible to adverse events?

## Nobel Prize in Physiology 2023

Awarded to Katalin Kariko and Drew Weissman for their discoveries concerning nucleotide base modifications that enabled the development of effective mRNA vaccines against Covid-19.

The main methods for vaccine production before the pandemic were:

- Recombinant protein,
- Inactive viruses,
- Viral vectors,

The issues with these methods is that large-scale cell culture is rqeuired, which limits rapid production in response to pandemics.

### Vaccines mimic viral infection to activate the immune system in order to protect body from future infections

Key players in the game:

1. Viral proteins - the antigens,
2. Antigen-presenting cells (the dendritic cells),
3. T cells - T comes from Thymus, where they mature,
4. B cells - B comes from bone marrow,

### Coronavirus is a RNA virus infecting human and other species

The viral particle consists of structural proteins: **spike** (S), **envelope** (E), **membrane** (M), **nucleocapsid** (N) and the **ssRNA**.

### The sequence of the spike protein is largely conserved between Corona and related viruses

This is **composed** by about **1300 aminoacids.** Its two subunits, the **S1** (which contains the **receptor-binding domain**) and the **S2** (which contains the polybasic cleavage site and the O-likned glycan residues).

In the **S1**, only a **handful of aminoacids differ** between the human **SARS-CoV-2** and the **bat and pangolin viruses**.

The S1, containing the RBD, is responsible for **identifying and bind to the ACE2** (Angiotensin-Converting Enzyme 2), which is expressed on human respiratory and intestinal epithelial cells.

**The S1 is responsible to breach the host membrane**. It includes the Heptad Repeat 1 (HR1) and HR2 domains.

### Spike protein of coronavirus is responsible for the viral entry into human cells

Once the S1 RBD binds to the ACE2 receptor on a new target cell, the S undergoes a second cleavage event at the S2' site to trigger fusion. Depending on the local protease environment of the host cell, this is achived in either two ways:

1. **Cell surface fusion**: If the host cell expresses high levels of the surface protease TMPRSS2, this enzyme cleaves the S2' site at the cell surface, triggering fusion of the viral envelope with the outer plasma membrane of the host cell.
2. **Endosomal invagination**: Otherwise, the host cell membrane invaginates, engulfing the virus ACE2 complex in a lipid bubble (endosome) via endocytosis. As the endosome is pulled deeper into the cell, its interior undergoes pH drop, which activares a different host protease - Cathespin L - which executes the S2' cleavage from inside the endosomal vesicle.

In both cases, the **cleavage causes the S1 subunit to dissociate**, triggering a **change** in the **S2 subunit**. The **HR1** and **2** domains in **S2 refold**, collapsing into a **six-helix bundle**, overcoming the hydration barriers and **causing the cells to fuse**. Once this happens, **the viral envelope opens** and the **RNA genome is dumped** **into** the host **cytoplams**.

This **triggers host ribosomes to translate the viral replicase proteins**, which **construct** the **replication-transcription complexes** that synthesize both genomic RNA and subgenomic mRNA.

### RNA is transcribed from DNA and translated into protein

The nucleotides from DNA are:
- Cytosine
- Guanine
- Adenine
- Thymine

Those of RNA are the same, with the exception of Uracil, which replaces Thymine.

### Summary

1. What is the unmet medical need to be addressed? A vaccine to prevent a large population from being infected by the coronavirus,
2. What are the targets of our drug? The spike protein,
3. Where should the drug go in the patient's body, what does the body do to the drug, and what does the drug do to the body? Time constraints mean that classical vaccine is not feasible. mRNA vaccines as an alternative.
4. Safety profile?
5. Who is responsive to the drug? Who suffers from adverse events?

### 3 essential challenges for mRNA-based therapies

- **delivery**: mRNAs are too large and charged to pass lipid bilayers, --> Solution: LNP wrapper
- **stability**: mRNAs are degraded, for example, by ribonucleases, --> Solution: Structural modifications of the RNA sequence
- **unwanted immune response**: mRNAs cause immunogenicity --> Solution: Replace the uridine nucleotides of RNA with N1-methylpseudouridine (see slides 29-30 and slide 23 of Lecture 4)

In a nutshell, the larger the structure, the smaller the bioavailability. **Above the size of double-stranded siRNA (10^4 Da), there is no availability** (self-replicating mRNA as 10^5 - 10^8 Da).

### Lipid NanoParticles (LNP) help delivering RNAs into cells and prevent degradation

- Lipid nanoparticles can take mRNA vaccines as cargo and deliver them into human cells.
- In the cell, mRNA encoding of the part of the spike protein sequence is translated into proteins with the human protein translation mechanism.
- **Synthesized proteins will be degraded and exposed on cell surface, which will be recognized by antigen presenting cells.**

LNP is composed of four distinct lipid components:

- **Ionizable** Lipids **(core)**: Possess an amine headgroup with a specific pKa between 6 and 6.5 (pKa is the acid dissoaction constant; it measures how tightly a proton is held by an acid. Lower pKa means that it is a stronger acid which readily donates protons). During manufacturing in an acidic buffer (pH ~ 4), the amines protonate and gain a positive charge. They bind electrostatically to the negatively charged phospate backbone of the RNA, neutralizing it and creating a solid core.
- **PEG**: Populate the exterior surface of the nanoparticle. Prevent the particles from aggregating and shield them from immune clearance in the bloodstream.
- **Cholesterol**: Fills the gaps between the lipid tails, modulating the fluidity and the thermodynamic stability of the lipid bilayer.
- Helper **Phospholipids**: Support the bilayer structure of the nanoparticle surface. 

LNPs enter cell membranes via the following mechanism:

1. When LNPs enter the bloodstream, they adsorb endogeneous proteins (in particular ApoE) to the LNP surface.
2. Since cells possess ApoE receptors on their surface, the LNP binds to these receptors, causing the cell to engulf the nanoparticle via endocytosis.

If it is required to connect to a different organ, then the LNP:

1. needs to be coated with a specific target molecule (active targeting through ligand conjugation),
2. add a highly specific fifth lipid which alters the internal charge distribution and surface biophysics (selective organ targeting)
