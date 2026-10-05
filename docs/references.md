# Selected references

This is a short reading list for methods that informed the research direction. It is not an exhaustive survey, and inclusion does not imply that the cited method was used successfully in this repository. Bibliographic details below were checked against the linked publisher, proceedings, or arXiv records.

## Conditional normalization and PIT

- Murray Rosenblatt (1952). “Remarks on a Multivariate Transformation.” *The Annals of Mathematical Statistics*, 23(3), 470–472. [DOI: 10.1214/aoms/1177729394](https://doi.org/10.1214/aoms/1177729394). Foundational conditional transform motivating sequential PIT representations. The public implementation is a parametric Gaussian AR(1) example, not a general guarantee of independent normalized innovations.

## Change-point detection and sequential testing

- E. S. Page (1954). “Continuous Inspection Schemes.” *Biometrika*, 41(1–2), 100–115. [Oxford Academic article](https://academic.oup.com/biomet/article-abstract/41/1-2/100/456627?login=false); DOI: 10.1093/biomet/41.1-2.100. Classic sequential accumulation and inspection reference motivating CUSUM-style evidence.
- Ryan Prescott Adams and David J. C. MacKay (2007). “Bayesian Online Changepoint Detection.” arXiv:0710.3742. [arXiv](https://arxiv.org/abs/0710.3742). Online posterior inference over run length; relevant to the Bayesian detector family explored in the research.

## Kernel methods

- Zaïd Harchaoui, Éric Moulines, and Francis R. Bach (2008). “Kernel Change-Point Analysis.” In *Advances in Neural Information Processing Systems 21*. [Proceedings paper](https://proceedings.neurips.cc/paper/2008/hash/08b255a5d42b89b0585260b6f2360bdd-Abstract.html). Develops a kernel-based change-point analysis approach; useful context for the project's nonparametric feature investigations.

## Koopman and DMD

- Jonathan H. Tu, Clarence W. Rowley, Dirk M. Luchtenburg, Steven L. Brunton, and J. Nathan Kutz (2014). “On Dynamic Mode Decomposition: Theory and Applications.” *Journal of Computational Dynamics*, 1(2), 391–421. [DOI: 10.3934/jcd.2014.1.391](https://doi.org/10.3934/jcd.2014.1.391), [arXiv:1312.0041](https://arxiv.org/abs/1312.0041). Review and theoretical treatment relevant to windowed dynamics features.
- Georg A. Gottwald and Federica Gugole (2020). “Detecting Regime Transitions in Time Series Using Dynamic Mode Decomposition.” *Journal of Statistical Physics*, 179, 1028–1045. [DOI: 10.1007/s10955-019-02392-3](https://doi.org/10.1007/s10955-019-02392-3). A direct DMD regime-transition application; its assumptions and use case differ from this project's heterogeneous univariate task.

## Optimal transport

- Kevin C. Cheng, Shuchin Aeron, Michael C. Hughes, Erika Hussey, and Eric L. Miller (2020). “Optimal Transport Based Change Point Detection and Time Series Segment Clustering.” In *ICASSP 2020*. [arXiv:1911.01325](https://arxiv.org/abs/1911.01325). Distributional change and segment clustering with Wasserstein distances, relevant to the explored transport family.

## Signatures and rough paths

- Ilya Chevyrev and Andrey Kormilitzin (2016). “A Primer on the Signature Method in Machine Learning.” arXiv:1603.03788. [arXiv](https://arxiv.org/abs/1603.03788). Accessible introduction to path signatures as sequential features.
- Terry J. Lyons (1998). “Differential Equations Driven by Rough Signals.” *Revista Matemática Iberoamericana*, 14(2), 215–310. [DOI: 10.4171/RMI/240](https://doi.org/10.4171/RMI/240). Mathematical foundations for rough-path methods that motivated signature-based sequence representations.

## Conformal inference

- Denis Volkhonskiy, Evgeny Burnaev, Ilia Nouretdinov, Alexander Gammerman, and Vladimir Vovk (2017). “Inductive Conformal Martingales for Change-Point Detection.” In *Proceedings of the Sixth Workshop on Conformal and Probabilistic Prediction and Applications*, PMLR 60, 132–153. [PMLR](https://proceedings.mlr.press/v60/volkhonskiy17a.html). Sequential exchangeability testing and conformal evidence; dependence assumptions need explicit treatment in time series.
- Vladimir Vovk, Ivan Petej, Ilia Nouretdinov, Ernst Ahlberg, Lars Carlsson, and Alex Gammerman (2021). “Retrain or Not Retrain: Conformal Test Martingales for Change-Point Detection.” arXiv:2102.10439. [arXiv](https://arxiv.org/abs/2102.10439). Conformal martingale proposals for detecting when a prediction model should be retrained.

## Learned representations and foundation models

- Abhimanyu Das, Weihao Kong, Rajat Sen, and Yichen Zhou (2024). “A Decoder-Only Foundation Model for Time-Series Forecasting.” In *Proceedings of the 41st International Conference on Machine Learning*, PMLR 235, 10148–10167. [PMLR](https://proceedings.mlr.press/v235/das24c.html), [arXiv:2310.10688](https://arxiv.org/abs/2310.10688). Example of broad pretrained forecasting representations; forecasting benchmarks do not establish transfer to structural-break detection.
- Jie Li, Paul Fearnhead, Piotr Fryzlewicz, and Tengyao Wang (2022). “Automatic Change-Point Detection in Time Series via Deep Learning.” arXiv:2211.03860. [arXiv](https://arxiv.org/abs/2211.03860). Learned offline change-point detection reference; it is not an online detector claim for this repository.

## Validation and leakage

- The project’s strongest validation guidance comes from its own documented postmortems rather than one paper: [exact-stream and nested validation protocol](validation.md), [research journey](research_journey.md), and the locally preserved audit index in [`research_archive/README.md`](../research_archive/README.md). Those records distinguish causal inference from fold-independent estimation and selection-aware reporting.

## Reference maintenance

Before adding a citation, verify title, author list, year, venue, and DOI or stable preprint URL from the publisher/proceedings/arXiv record. This list is intentionally selective. Research into rapidly changing foundation models should pin model/checkpoint versions and licensing separately from citing a paper.
