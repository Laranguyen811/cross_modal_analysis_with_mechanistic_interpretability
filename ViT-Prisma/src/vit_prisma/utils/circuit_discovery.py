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


        

        
        

        
    
