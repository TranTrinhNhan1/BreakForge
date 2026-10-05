# Selected references

This reading list covers methods that informed the project or its research branches. It is selective: a citation does not imply that a method was part of the public API or performed well in the experiments. Bibliographic details are linked to publisher, proceedings, or author-maintained primary records where available.

## Conditional normalization and score models

- Murray Rosenblatt (1952). “Remarks on a Multivariate Transformation.” *The Annals of Mathematical Statistics*, 23(3), 470–472. [DOI: 10.1214/aoms/1177729394](https://doi.org/10.1214/aoms/1177729394). The conditional transform motivates the project's sequential PIT representation. The public implementation is a fitted Gaussian AR(1) approximation and does not guarantee independent innovations under misspecification.
- Aapo Hyvärinen (2005). “Estimation of Non-Normalized Statistical Models by Score Matching.” *Journal of Machine Learning Research*, 6(24), 695–709. [JMLR article](https://jmlr.org/papers/v6/hyvarinen05a.html). Score matching informed exploratory conditional density and score-evidence branches; it is not used by the compact public reference.

## Change-point detection and sequential testing

- E. S. Page (1954). “Continuous Inspection Schemes.” *Biometrika*, 41(1–2), 100–115. [Oxford Academic article](https://academic.oup.com/biomet/article-abstract/41/1-2/100/456627); DOI: [10.1093/biomet/41.1-2.100](https://doi.org/10.1093/biomet/41.1-2.100). A classic sequential inspection reference for cumulative evidence; the public detector uses simple CUSUM channels but does not claim Page's calibrated operating guarantees.
- Ryan Prescott Adams and David J. C. MacKay (2007). “Bayesian Online Changepoint Detection.” arXiv:0710.3742. [arXiv](https://arxiv.org/abs/0710.3742). Posterior inference over run length motivated Bayesian online branches and contextualized the difference between evidence and a posterior probability.
- Jie Li, Paul Fearnhead, Piotr Fryzlewicz, and Tengyao Wang (2024). “Automatic Change-Point Detection in Time Series via Deep Learning.” *Journal of the Royal Statistical Society: Series B (Statistical Methodology)*, 86(2), 273–285. [DOI: 10.1093/jrsssb/qkae004](https://doi.org/10.1093/jrsssb/qkae004). A learned offline detector reference; its offline evaluation setting is distinct from this repository's prefix-only API.

## Kernel and distribution comparison

- Zaïd Harchaoui, Éric Moulines, and Francis R. Bach (2008). “Kernel Change-Point Analysis.” *Advances in Neural Information Processing Systems 21*. [Proceedings paper](https://proceedings.neurips.cc/paper/2008/hash/08b255a5d42b89b0585260b6f2360bdd-Abstract.html). A direct kernel change-point method that informed nonparametric comparisons.
- Arthur Gretton, Karsten M. Borgwardt, Malte J. Rasch, Bernhard Schölkopf, and Alexander Smola (2012). “A Kernel Two-Sample Test.” *Journal of Machine Learning Research*, 13(25), 723–773. [JMLR article](https://jmlr.org/papers/v13/gretton12a.html). Provides maximum mean discrepancy and two-sample testing context for kernel and random-feature change statistics.
- Ali Rahimi and Benjamin Recht (2007). “Random Features for Large-Scale Kernel Machines.” *Advances in Neural Information Processing Systems 20*. [NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2007/hash/013a006f03dbc5392effeb8f18fda755-Abstract.html). Random Fourier features informed computationally smaller kernel screens.
- Makoto Yamada, Taiji Suzuki, Takafumi Kanamori, Hirotaka Hachiya, and Masashi Sugiyama (2011). “Relative Density-Ratio Estimation for Robust Distribution Comparison.” *Advances in Neural Information Processing Systems 24*. [NeurIPS proceedings](https://papers.neurips.cc/paper_files/paper/2011/hash/d1f255a373a3cef72e03aa9d980c7eca-Abstract.html). Relative density ratios motivated exploratory pre/post distribution comparisons; those experiments remain subject to the validation labels in [results](results.md).

## Optimal transport

- Kevin C. Cheng, Shuchin Aeron, Michael C. Hughes, Erika Hussey, and Eric L. Miller (2020). “Optimal Transport Based Change Point Detection and Time Series Segment Clustering.” In *Proceedings of ICASSP 2020*. [Author-posted paper](https://arxiv.org/abs/1911.01325). Wasserstein two-sample comparisons motivated transport-based change and segment summaries; the public core has no transport dependency.
- Marco Cuturi (2013). “Sinkhorn Distances: Lightspeed Computation of Optimal Transport.” *Advances in Neural Information Processing Systems 26*. [NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2013/hash/af21d0c97db2e27e13572cbf59eb343d-Abstract.html). Entropic regularization and Sinkhorn scaling informed the computational context for transport experiments.

## Spectral, higher-order, and multiscale representations

- Patrick L. Brockett, Melvin J. Hinich, and Douglas M. Patterson (1988). “Bispectral-Based Tests for the Detection of Gaussianity and Linearity in Time Series.” *Journal of the American Statistical Association*, 83(403), 657–664. [DOI: 10.1080/01621459.1988.10478645](https://doi.org/10.1080/01621459.1988.10478645). This classical bispectral diagnostic informed higher-order dependence experiments. It is an offline test under its stated assumptions, not a causal streaming guarantee.
- Marc Raimondo and Nader Tajvidi (2004). “A Peaks over Threshold Model for Change-Point Detection by Wavelets.” *Statistica Sinica*, 14, 395–412. [Journal article](https://www3.stat.sinica.edu.tw/statistica/j14n2/j14n24/j14n24.html). Its multiresolution and thresholding perspective informed exploratory wavelet screens; it does not validate the project's tested configuration.
- Stéphane Mallat (2012). “Group Invariant Scattering.” *Communications on Pure and Applied Mathematics*, 65(10), 1331–1398. [DOI: 10.1002/cpa.21413](https://doi.org/10.1002/cpa.21413), [author preprint](https://arxiv.org/abs/1101.2286). Wavelet scattering motivated multiscale representation experiments and gives context for higher-order information beyond the power spectrum. The public reference detector does not implement scattering.

## Dynamical systems and observation-driven score models

- Steven L. Brunton, Joshua L. Proctor, and J. Nathan Kutz (2016). “Discovering Governing Equations from Data by Sparse Identification of Nonlinear Dynamical Systems.” *Proceedings of the National Academy of Sciences*, 113(15), 3932–3937. [DOI: 10.1073/pnas.1517384113](https://doi.org/10.1073/pnas.1517384113). Sparse identification informed a local transition-equation feasibility branch; the original system-identification results do not establish detection performance for heterogeneous streaming series.
- Drew Creal, Siem Jan Koopman, and André Lucas (2013). “Generalized Autoregressive Score Models with Applications.” *Journal of Applied Econometrics*, 28(5), 777–795. [DOI: 10.1002/jae.1279](https://doi.org/10.1002/jae.1279). Score-driven parameter updates informed conditional AR/GARCH experiments. The tested BreakForge branch was a specific exploratory configuration, not a general GAS implementation.

## Koopman and DMD

- Jonathan H. Tu, Clarence W. Rowley, Dirk M. Luchtenburg, Steven L. Brunton, and J. Nathan Kutz (2014). “On Dynamic Mode Decomposition: Theory and Applications.” *Journal of Computational Dynamics*, 1(2), 391–421. [DOI: 10.3934/jcd.2014.1.391](https://doi.org/10.3934/jcd.2014.1.391), [arXiv:1312.0041](https://arxiv.org/abs/1312.0041). DMD foundations and operator interpretation informed the project's local dynamics features.
- Georg A. Gottwald and Federica Gugole (2020). “Detecting Regime Transitions in Time Series Using Dynamic Mode Decomposition.” *Journal of Statistical Physics*, 179, 1028–1045. [DOI: 10.1007/s10955-019-02392-3](https://doi.org/10.1007/s10955-019-02392-3), [author preprint](https://arxiv.org/abs/1904.09082). A direct regime-transition application that informed the DMD experiments; its system and assumptions differ from heterogeneous univariate streams.

## Signatures, rough paths, and time-series geometry

- Ilya Chevyrev and Andrey Kormilitzin (2016). “A Primer on the Signature Method in Machine Learning.” arXiv:1603.03788. [arXiv](https://arxiv.org/abs/1603.03788). A practical introduction to path signatures that informed sequential path-feature experiments.
- Terry J. Lyons (1998). “Differential Equations Driven by Rough Signals.” *Revista Matemática Iberoamericana*, 14(2), 215–310. [DOI: 10.4171/RMI/240](https://doi.org/10.4171/RMI/240). Mathematical foundations for rough-path methods explored in the research archive.
- Chin-Chia Michael Yeh, Yan Zhu, Liudmila Ulanova, Nurjahan Begum, Yifei Ding, Hoang Anh Dau, Diego Furtado Silva, Abdullah Mueen, and Eamonn Keogh (2016). “Matrix Profile I: All Pairs Similarity Joins for Time Series: A Unifying View That Includes Motifs, Discords and Shapelets.” In *2016 IEEE International Conference on Data Mining*, 1317–1322. [DOI: 10.1109/ICDM.2016.0179](https://doi.org/10.1109/ICDM.2016.0179). Subsequence novelty and profile-based geometry informed local novelty screens.
- Lucas Lacasa, Bartolo Luque, Fernando Ballesteros, Jordi Luque, and Juan Carlos Nuño (2008). “From Time Series to Complex Networks: The Visibility Graph.” *Proceedings of the National Academy of Sciences*, 105(13), 4972–4975. [DOI: 10.1073/pnas.0709247105](https://doi.org/10.1073/pnas.0709247105). A graph representation reference for exploratory time-series geometry.

## Conformal inference

- Denis Volkhonskiy, Evgeny Burnaev, Ilia Nouretdinov, Alexander Gammerman, and Vladimir Vovk (2017). “Inductive Conformal Martingales for Change-Point Detection.” In *Proceedings of the Sixth Workshop on Conformal and Probabilistic Prediction and Applications*, PMLR 60, 132–153. [PMLR paper](https://proceedings.mlr.press/v60/volkhonskiy17a.html). Conformal martingale change evidence informed online calibration experiments; time dependence still requires explicit assumptions.
- Vladimir Vovk, Ivan Petej, Ilia Nouretdinov, Ernst Ahlberg, Lars Carlsson, and Alex Gammerman (2021). “Retrain or Not Retrain: Conformal Test Martingales for Change-Point Detection.” In *Proceedings of the Tenth Symposium on Conformal and Probabilistic Prediction and Applications*, PMLR 152, 191–210. [PMLR paper](https://proceedings.mlr.press/v152/vovk21b.html). An online conformal test-martingale proposal relevant to shift detection and retraining decisions.

## Learned and foundation-model representations

- Sana Tonekaboni, Danny Eytan, and Anna Goldenberg (2021). “Unsupervised Representation Learning for Time Series with Temporal Neighborhood Coding.” In *International Conference on Learning Representations (ICLR 2021)*. [arXiv:2106.00750](https://arxiv.org/abs/2106.00750). TNC motivated a candidate representation branch; its original tasks do not by themselves establish break-detection transfer.
- Noah Hollmann, Samuel Müller, Lennart Purucker, Arjun Krishnakumar, Max Körfer, Shi Bin Hoo, Robin Tibor Schirrmeister, and Frank Hutter (2025). “Accurate Predictions on Small Data with a Tabular Foundation Model.” *Nature*, 637, 319–326. [DOI: 10.1038/s41586-024-08328-6](https://doi.org/10.1038/s41586-024-08328-6). TabPFN informed feasibility work on learned tabular heads; its original scope and benchmark do not demonstrate causal streaming or structural-break performance.

## Validation and leakage

The project's most important validation guidance comes from its own documented postmortems rather than one paper: [exact-stream and nested validation protocol](validation.md), [research journey](research_journey.md), and the [curated archive index](../research_archive/README.md). These records distinguish inference causality from fold-independent estimation and selection-aware reporting.

## Reference maintenance

Before adding a citation, verify the title, author list, year, venue, and DOI or stable preprint URL against a publisher, proceedings, or author-maintained primary record. For rapidly changing foundation models, pin the checkpoint and license separately; a paper citation alone does not establish model licensing or data provenance.
