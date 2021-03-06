# Copyright (c) 2021, salesforce.com, inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

python lorenz_attractor.py --lr 1e-3 --encoder_type bgru --dropout 0.7 --rate_lambda 1.0 --ortho_lambda 0.1 --recon_lambda 500.0 --epochs 40 --masked_recon true --encoder_rnn_num_layers 4 --encoder_rnn_hidden_size 256 --cov_diag_reg 1e-4 --obj det --use_prior_pi false --use_dim_pi false --vae_alpha 1. --vae_beta 1.1 --vae_gamma 1. --vae_zeta 0.1 --split_rate 0.8 --gpuid 0
