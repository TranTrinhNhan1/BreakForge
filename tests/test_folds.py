from importlib import import_module, util


def test_held_out_fold_ids_are_excluded_from_training_ids() -> None:
    module_spec = util.find_spec("breakforge.validation.folds")
    assert module_spec is not None
    split_ids_by_fold = import_module("breakforge.validation.folds").split_ids_by_fold
    fold_by_id = {"series-a": 0, "series-b": 1, "series-c": 0, "series-d": 1}

    train_ids, validation_ids = split_ids_by_fold(fold_by_id, held_out_fold=1)

    assert train_ids == ("series-a", "series-c")
    assert validation_ids == ("series-b", "series-d")
    assert set(train_ids).isdisjoint(validation_ids)
