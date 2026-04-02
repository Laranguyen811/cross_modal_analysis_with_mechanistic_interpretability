import timm
import torch

from vit_prisma.models.base_vit import HookedViT
import pytest

#currently only vit_base_patch16_224 supported (config loading issue)
@pytest.mark.skipif(not torch.cuda.is_available(), reason="Requires CUDA")
def test_loading_timm():
    TOLERANCE = 1e-4

    model_name = "timm/vit_so150m2_patch16_reg1_gap_448.sbb_e200_in12k_ft_in1k"
    batch_size = 5
    channels = 3
    height = 224
    width = 224
    device = "cpu" if not torch.cuda.is_available() else "cuda"

    hooked_model = HookedViT.from_pretrained(model_name, patch_size=32)
    hooked_model.to(device)
    timm_model = timm.create_model(model_name, pretrained=True)
    timm_model.to(device)

    with torch.random.fork_rng():
        torch.manual_seed(1)
        input_image = torch.rand((batch_size, channels, height, width)).to(device)

    hooked_output, timm_output = hooked_model(input_image), timm_model(input_image)

    assert torch.allclose(hooked_output, timm_output, atol=TOLERANCE), f"Model output diverges! Max diff: {torch.max(torch.abs(hooked_output - timm_output))}"

