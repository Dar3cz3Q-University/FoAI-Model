#!/bin/bash

set -e

TORCH_VERSION="2.5.1"
TORCHVISION_VERSION="0.20.1"
CUDA_TAG="+cu121"
PYTORCH_INDEX="https://download.pytorch.org/whl/cu121"

echo "Installing base Poetry dependencies..."
poetry install --no-root

echo "Installing CUDA-enabled torch and torchvision..."
poetry run pip install \
  torch==${TORCH_VERSION}${CUDA_TAG} \
  torchvision==${TORCHVISION_VERSION}${CUDA_TAG} \
  --index-url ${PYTORCH_INDEX}

echo "torch + torchvision installed with CUDA"

echo "Verifying installation..."
poetry run python -c "
import torch, torchvision
print('🔢 torch:', torch.__version__)
print('🎨 torchvision:', torchvision.__version__)
print('🚀 CUDA available:', torch.cuda.is_available())
if torch.cuda.is_available():
    print('🧠 GPU:', torch.cuda.get_device_name(0))
"

echo "Setup complete."
