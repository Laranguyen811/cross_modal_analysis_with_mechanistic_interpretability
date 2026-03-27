from copy import deepcopy
from functools import partial
import numpy as np
from typing import List, Tuple, Dict, Union, Optional, Callable, Any
from tqdm import tqdm
import torch
from vit_prisma.utils.experiments import get_act_hook
import warnings
import matplotlib.pyplot as plt
import networkx as nx
from collections import OrderedDict
from vit_prisma.utils.ioi_utils import show_pp
import graphviz 
from vit_prisma.utils import detect_architectures
from torch import Tensor

def get_hook_tuple(model:Any,
                   layer: int,
                   head_idx: int,
                   comp: str=None, 
                   input: bool=False,
                   n_layers: int=12) -> Tuple[str, Callable]:
    '''
    Helper function to create a hook tuple for a given layer and head index.
    Args:
        model (Any): The model for which to create the hook tuple.
        layer (int): The layer number for which to create the hook tuple.
        head_idx (int): The head index for which to create the hook tuple.
        comp (str, optional): The computation for which to create the hook tuple. Defaults to None.
        input (bool, optional): Whether to include the input in the hook tuple. Defaults to False.
        n_layers (int, optional): The total number of layers in the model. Defaults to 12.
    Returns:
        Tuple[str, Callable]: A tuple containing the hook name and the hook function.
    '''
    arch = detect_architectures(model)
    HOOKS = {}

    if comp in ["q", "k", "v"]:
        hook_pattern = HOOKS[arch][comp]
        assert comp in ["q", "k", "v"], f"Invalid comp: {comp}. Must be one of 'q', 'k', or 'v'."
        assert head_idx is not None, f"head_idx must be provided when comp is one of 'q', 'k', or 'v'."
        return hook_pattern.format(layer=layer, head_idx=head_idx)
    elif head_idx is None:
        if layer < n_layers:    
            hook_pattern = HOOKS[arch]["mlp_out" if not input else "resid_mid"] 
        else:
            hook_pattern = HOOKS[arch]["resid_post"]
        return hook_pattern.format(layer=layer, head_idx=head_idx)

def patch_all(z: Tensor,
              source_act: Tensor,
               hook: Tensor,) -> Tensor:
    '''
    Patch the activations of a model with the activations from a source model.
    Args:
        z (Tensor): The activations of the model to be patched.
        source_act (Tensor): The activations from the source model to patch with.
        hook (Tensor): The hook tensor indicating where to patch.
        Returns:
        Tensor: The patched activations.
    '''
    z[:] = source_act[hook]
    return z

def patch_positions(
        z: Tensor,
        source_act: Tensor,
        hook: Tensor,
        positions: List[int],
) -> Tensor:
    '''
    Patch the activations of a model at specific positions with the activations from a source model.
    Args:
        z (Tensor): The activations of the model to be patched.
        source_act (Tensor): The activations from the source model to patch with.
        hook (Tensor): The hook tensor indicating where to patch.
        positions (List[int]): The list of positions to patch.
    Returns:
        Tensor: The patched activations.
    '''
    if positions is None: # Same as patch all
        raise NotImplementedError(
            "Patching all positions is not implemented in patch_positions. Use patch_all instead."
        )
    else:
        batch = z.shape[0]
        cur_positions = Tensor(positions)
        if len(cur_positions.shape) == 0:
            cur_positions = cur_positions.unsqueeze(0)
        for pos in cur_positions: 
            z[torch.arange(batch), pos] = source_act[torch.arange(batch), pos]
        return z

def get_datasets(text: str,
                 dataset: Any) -> Tuple[Tensor, Tensor]:
    '''
    Get the datasets for the circuit discovery experiments.
    Returns:
        Tuple[Tensor, Tensor]: A tuple containing the input and output datasets.
    '''
    batch_size = 1
    orig = text
    # TODO: Add support for more datasets


    

        

        
        

        
    
