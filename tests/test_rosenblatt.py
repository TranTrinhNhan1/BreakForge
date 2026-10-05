from statistics import NormalDist

import structural_break as sb


def test_conditional_gaussian_pit_maps_back_to_its_gaussian_score() -> None:
    normalizer_type = getattr(sb, "CausalGaussianAR1PIT", None)
    assert normalizer_type is not None
    normalizer = normalizer_type().fit([0.0, 1.0, 0.0, -1.0, 0.0, 1.0, 0.0, -1.0])

    observation = normalizer.update(1.2)

    assert 0.0 < observation.pit < 1.0
    assert abs(NormalDist().inv_cdf(observation.pit) - observation.z_score) < 1e-8
