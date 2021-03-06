# Copyright (c) 2021, salesforce.com, inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

# -*- coding: utf-8 -*-

# Copyright 2019 Shigeki Karita
#  Apache 2.0  (http://www.apache.org/licenses/LICENSE-2.0)

"""Mask module."""

from distutils.version import LooseVersion

import torch

is_torch_1_2_plus = LooseVersion(torch.__version__) >= LooseVersion('1.2.0')
datatype = torch.bool if is_torch_1_2_plus else torch.uint8


def subsequent_mask(size, device="cpu", dtype=datatype):
    """Create mask for subsequent steps (1, size, size).

    :param int size: size of mask
    :param str device: "cpu" or "cuda" or torch.Tensor.device
    :param torch.dtype dtype: result dtype
    :rtype: torch.Tensor
    >>> subsequent_mask(3)
    [[1, 0, 0],
     [1, 1, 0],
     [1, 1, 1]]
    """
    ret = torch.ones(size, size, device=device, dtype=dtype)
    return torch.tril(ret, out=ret)


def target_mask(ys_in_pad, ignore_id):
    """Create mask for decoder self-attention.

    :param torch.Tensor ys_pad: batch of padded target sequences (B, Lmax)
    :param int ignore_id: index of padding
    :param torch.dtype dtype: result dtype
    :rtype: torch.Tensor
    """
    ys_mask = ys_in_pad != ignore_id
    m = subsequent_mask(ys_mask.size(-1), device=ys_mask.device).unsqueeze(0)
    return ys_mask.unsqueeze(-2) & m



def make_context_mask(size, left_context, right_context, device="cpu", dtype=datatype):
    """Create mask for encoder self-attention with limited context.

    :param int size: max input length in the minibatch.
    :param int left_context: how may frames in the past to look at.
    :param int right_context: how many frames in the future to look at.
    :rtype: torch.Tensor
    """
    ret = torch.ones(size, size, device=device, dtype=dtype)
    return ret.triu(-left_context).tril(right_context)
