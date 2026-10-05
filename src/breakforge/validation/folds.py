"""Small helpers for group-held-out validation splits."""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from typing import TypeVar


Identifier = TypeVar("Identifier", bound=Hashable)


def split_ids_by_fold(
    fold_by_id: Mapping[Identifier, int],
    held_out_fold: int,
) -> tuple[tuple[Identifier, ...], tuple[Identifier, ...]]:
    """Return training and held-out IDs while preserving mapping order."""
    if not fold_by_id:
        raise ValueError("fold_by_id must contain at least one identifier")
    if held_out_fold not in fold_by_id.values():
        raise ValueError("held_out_fold is not present in fold_by_id")

    train_ids = tuple(identifier for identifier, fold in fold_by_id.items() if fold != held_out_fold)
    validation_ids = tuple(
        identifier for identifier, fold in fold_by_id.items() if fold == held_out_fold
    )
    return train_ids, validation_ids
