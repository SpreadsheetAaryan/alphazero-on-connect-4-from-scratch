"""
AlphaZero on Connect-4 from Scratch

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - make_empty_board
import numpy as np

def make_empty_board():
    """Return a 6x7 integer numpy array of zeros representing an empty Connect-4 board."""
    # TODO: create a 6x7 integer array of zeros and return it
    return np.zeros(shape=(6, 7), dtype=np.int8)

# Step 2 - column_top_row
def column_top_row(board, column):
    """Return the lowest empty row in `column`, or -1 if the column is full."""
    # TODO: scan the column from the bottom up and return the first empty row index
    for i in range(5, -1, -1):
        if board[i][column] == 0:
            return i
    
    return -1

# Step 3 - drop_piece
def drop_piece(board, column, player):
    # TODO: place `player` in the lowest empty row of `column` and return the new board
    row = column_top_row(board, column)
    if row == -1:
        raise ValueError
    ret = np.array(board)
    ret[row][column] = player
    return ret

# Step 4 - column_full
import numpy as np

def column_full(board, column):
    """Return True if `column` has no empty rows left."""
    # TODO: check whether the column can still accept a piece
    if column_top_row(board, column) == -1:
        return True
    else:
        return False

# Step 5 - valid_moves
def valid_moves(board):
    # TODO: return a list of column indices that still have at least one empty row
    ret = []
    for i in range(7):
        if not column_full(board, i):
            ret.append(i)
    return ret

# Step 6 - four_in_a_row_horizontal
def four_in_a_row_horizontal(board):
    # TODO: scan every row for four consecutive matching non-zero pieces horizontally
    for row in range(len(board)):
        for i in range(4):
            if board[row][i] == 0:
                continue
            else:
                tmp = board[row][i]
                if board[row][i + 1] == tmp and board[row][i + 2] == tmp and board[row][i + 3] == tmp:
                    return tmp
    return 0

# Step 7 - four_in_a_row_vertical
def four_in_a_row_vertical(board):
    # TODO: scan every column for four consecutive matching non-zero pieces vertically
    for i in range(7):
        for j in range(3):
            if board[j][i] == 0:
                continue
            else:
                tmp = board[j][i]
                if board[j + 1][i] == tmp and board[j + 2][i] == tmp and board[j + 3][i] == tmp:
                    return tmp
    
    return 0

# Step 8 - four_in_a_row_diagonal_down_right
def four_in_a_row_diagonal_down_right(board):
    # TODO: scan every down-right diagonal of the 6x7 board for four matching non-zero pieces
    def check_equal(i, j):
        if board[i][j] == 0:
            return 0
        tmp = board[i][j]
        if board[i + 1][j + 1] == tmp and board[i + 2][j + 2] == tmp and board[i + 3][j + 3] == tmp:
            return tmp
        return 0
    
    if check_equal(2, 0) > 0:
        return check_equal(2, 0)
    
    if check_equal(1, 0) > 0:
        return check_equal(1, 0)
    
    if check_equal(2, 1) > 0:
        return check_equal(2, 1)

    if check_equal(0, 0) > 0:
        return check_equal(0, 0)
    
    if check_equal(1, 1) > 0:
        return check_equal(1, 1)

    if check_equal(2, 2) > 0:
        return check_equal(2, 2)

    if check_equal(0, 1) > 0:
        return check_equal(0, 1)
    
    if check_equal(1, 2) > 0:
        return check_equal(1, 2)

    if check_equal(2, 3) > 0:
        return check_equal(2, 3)

    if check_equal(0, 2) > 0:
        return check_equal(0, 2)

    if check_equal(1, 3) > 0:
        return check_equal(1, 3)
    
    if check_equal(0, 3) > 0:
        return check_equal(0, 3)
    
    return 0

# Step 9 - four_in_a_row_diagonal_up_right
def four_in_a_row_diagonal_up_right(board):
    # TODO: scan every up-right diagonal for four consecutive matching non-zero pieces
    def check_equal(i, j):
        if board[i][j] == 0:
            return 0
        tmp = board[i][j]
        if board[i - 1][j + 1] == tmp and board[i - 2][j + 2] == tmp and board[i - 3][j + 3] == tmp:
            return tmp
        return 0
    
    if check_equal(5, 3) > 0:
        return check_equal(5, 3)
    
    if check_equal(5, 2) > 0:
        return check_equal(5, 2)
    
    if check_equal(4, 3) > 0:
        return check_equal(4, 3)

    if check_equal(5, 1) > 0:
        return check_equal(5, 1)
    
    if check_equal(4, 2) > 0:
        return check_equal(4, 2)

    if check_equal(3, 3) > 0:
        return check_equal(3, 3)

    if check_equal(5, 0) > 0:
        return check_equal(5, 0)
    
    if check_equal(4, 1) > 0:
        return check_equal(4, 1)

    if check_equal(3, 2) > 0:
        return check_equal(3, 2)

    if check_equal(4, 0) > 0:
        return check_equal(4, 0)

    if check_equal(3, 1) > 0:
        return check_equal(3, 1)
    
    if check_equal(3, 0) > 0:
        return check_equal(3, 0)
    
    return 0

# Step 10 - check_winner
import numpy as np

def check_winner(board):
    """Return 1 or 2 if that player has four in a row, else 0."""
    # TODO: combine the four direction scans and return the first non-zero result
    if four_in_a_row_vertical(board) > 0:
        return four_in_a_row_vertical(board)
    if four_in_a_row_horizontal(board) > 0:
        return four_in_a_row_horizontal(board)
    if four_in_a_row_diagonal_up_right(board) > 0:
        return four_in_a_row_diagonal_up_right(board)
    if four_in_a_row_diagonal_down_right(board) > 0:
        return four_in_a_row_diagonal_down_right(board)
    return 0

# Step 11 - board_is_full
def board_is_full(board):
    # TODO: return True when no column has an empty slot left
    for i in range(len(board[0])):
        if board[0][i] == 0:
            return False
    return True

# Step 12 - is_terminal
def is_terminal(board):
    # TODO: return (done, winner) using check_winner and board_is_full.
    done = False
    winner = 0
    if check_winner(board) > 0:
        done = True
        winner = int(check_winner(board))
    if board_is_full(board):
        done = True
        winner = int(check_winner(board))
    
    return (done, winner)

# Step 13 - other_player
def other_player(player):
    # TODO: return the opponent's player code (1 <-> 2)
    if player == 1:
        return 2
    else:
        return 1

# Step 14 - step_env
def step_env(board, column, player):
    # TODO: drop piece for player, then return (new_board, done, winner, next_player).
    new_board = drop_piece(board, column, player)
    done, winner = is_terminal(new_board)
    next_player = other_player(player)
    return (new_board, done, winner, next_player)

# Step 15 - encode_board
def encode_board(board, current_player):
    """Encode a 6x7 board as a (2, 6, 7) float32 tensor from current_player's view."""
    # TODO: build two binary planes (current player, opponent) and stack them
    new_board = np.zeros(shape=(2, 6, 7), dtype=np.float32)

    opponent = other_player(current_player)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == current_player:
                new_board[0][i][j] = 1.0
                new_board[1][i][j] = 0.0
            elif board[i][j] == opponent:
                new_board[0][i][j] = 0.0
                new_board[1][i][j] = 1.0
            else:
                new_board[0][i][j] = 0.0
                new_board[1][i][j] = 0.0
    
    return new_board

# Step 16 - board_to_torch_tensor
def board_to_torch_tensor(board, current_player):
    # TODO: encode the board and return it as a float32 torch tensor of shape (1, 2, 6, 7).
    new_board = encode_board(board, current_player)
    return torch.tensor(new_board, dtype=torch.float32).unsqueeze(0)

# Step 17 - init_conv_backbone
def init_conv_backbone(in_channels=2, hidden_channels=16):
    # TODO: Build a small convolutional backbone preserving the 6x7 spatial shape.
    ret = torch.nn.Sequential(
        nn.Conv2d(in_channels, hidden_channels, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.Conv2d(hidden_channels, hidden_channels, kernel_size=3, padding=1),
        nn.ReLU()
    )

    return ret

# Step 18 - init_policy_head
import torch
import torch.nn as nn

def init_policy_head(hidden_channels=16, num_columns=7):
    """Return an nn.Module mapping (B, hidden_channels, 6, 7) -> (B, num_columns) logits."""
    # TODO: build a small policy head that projects backbone features to column logits
    return nn.Sequential(
        nn.Conv2d(hidden_channels, 2, 1),
        nn.BatchNorm2d(2),
        nn.ReLU(),
        nn.Flatten(),
        nn.Linear(2*6*7, num_columns)
    )

# Step 19 - init_value_head
import torch
import torch.nn as nn

def init_value_head(hidden_channels=16):
    """Return an nn.Module mapping (B, hidden_channels, 6, 7) -> (B, 1) in (-1, 1)."""
    # TODO: build a value head that collapses backbone features to a single bounded scalar per board.
    return nn.Sequential(
        nn.Conv2d(in_channels=hidden_channels, out_channels=1, kernel_size=1, bias=False),
        nn.BatchNorm2d(1),
        nn.ReLU(),

        nn.Flatten(),

        nn.Linear(in_features=42, out_features=1),

        nn.Tanh()
    )

# Step 20 - build_policy_value_net
import torch
import torch.nn as nn

def build_policy_value_net(in_channels=2, hidden_channels=16, num_columns=7):
    """Compose backbone + policy head + value head into one nn.Module."""
    # TODO: build an nn.Module with backbone, policy_head, value_head attributes
    backbone = init_conv_backbone(in_channels, hidden_channels)
    policy_head = init_policy_head(hidden_channels, num_columns)
    value_head = init_value_head(hidden_channels)

    class PolicyValueNet(nn.Module):
        def __init__(self):
            super().__init__()
            self.backbone = backbone
            self.policy_head = policy_head
            self.value_head = value_head
        
        def forward(self, x):
            features = self.backbone(x)
            logits = self.policy_head(features)
            value = self.value_head(features)
            return logits, value
        
    return PolicyValueNet()

# Step 21 - policy_value_forward
import torch
import torch.nn as nn

def policy_value_forward(net, encoded_board):
    """Run encoded_board (B,2,6,7) through net and return (logits, value)."""
    # TODO: call the network on the encoded board and return its two outputs
    return net(encoded_board)

# Step 22 - action_mask
import numpy as np

def action_mask(board):
    # TODO: return a length-7 boolean mask, True where the column is legal
    valid = valid_moves(board)
    ret = np.zeros(7, dtype=bool)
    for i in range(len(valid)):
        ret[valid[i]] = True
    return ret

# Step 23 - masked_policy_logits
import torch

def masked_policy_logits(logits, mask):
    """Set logits at illegal columns to -inf.

    logits: torch.Tensor of shape (..., 7)
    mask:   bool array/tensor of shape (7,), True = legal
    returns: torch.Tensor of same shape as logits
    """
    # TODO: replace logits at illegal columns with negative infinity
    mask = torch.as_tensor(mask, dtype=torch.bool, device=logits.device)
    return logits.masked_fill(~mask, float('-inf'))

# Step 24 - masked_log_softmax
import torch

def masked_log_softmax(logits, mask):
    """Log-softmax of logits with illegal columns (mask=False) forced to -inf."""
    # TODO: mask out illegal columns, then apply log-softmax over the last dim.
    logits = masked_policy_logits(logits, mask)
    return torch.nn.functional.log_softmax(logits, dim=-1)

# Step 25 - sample_action_from_policy
import torch
import torch.nn.functional as F

def sample_action_from_policy(logits, mask, temperature=1.0):
    """Sample a legal column from a tempered masked categorical policy."""
    # TODO: scale logits by temperature, mask illegal columns, sample one index
    logits = masked_policy_logits(logits, mask)
    probabilities = F.softmax(logits / temperature, dim=-1)
    return int(torch.multinomial(probabilities, num_samples=1))

# Step 26 - greedy_action_from_policy
import torch

def greedy_action_from_policy(logits, mask):
    """Return the argmax legal column index from masked policy logits."""
    # TODO: mask out illegal columns then return the argmax as a python int
    logits = masked_policy_logits(logits, mask)
    return int(torch.argmax(logits, dim=-1))

# Step 27 - make_mcts_node
def make_mcts_node(prior=0.0, parent=None):
    # TODO: build a dict with prior, visit_count, value_sum, children, and parent fields.
    node = {
        'prior': prior,
        'visit_count': 0,
        'value_sum': 0.0,
        'children': {},
        'parent': parent,
    }
    return node

# Step 28 - node_q_value
def node_q_value(node):
    # TODO: return the mean value Q = value_sum / visit_count, or 0.0 if visit_count == 0
    if node['visit_count'] == 0:
        return 0.0
    else:
        return node['value_sum'] / node['visit_count']

# Step 29 - ucb_score
import math

def ucb_score(parent, child, c_puct=1.5):
    # TODO: return Q(child) + c_puct * prior * sqrt(N_parent) / (1 + N_child)
    return node_q_value(child) + (c_puct * child['prior'] * math.sqrt(parent['visit_count'])) / (1 + child['visit_count'])

# Step 30 - select_best_child
def select_best_child(node, legal_actions, c_puct=1.5):
    # TODO: return (action, child) maximizing PUCT among legal children of node.
    children = node['children']
    best_score = -9999
    best_node = None
    best_action = -1
    for idx, child in children.items():
        ucb = ucb_score(node, child, c_puct)
        if ucb > best_score and idx in legal_actions:
            best_score = ucb
            best_node = child
            best_action = idx
    
    return best_action, best_node

# Step 31 - select_leaf
def select_leaf(root, c_puct):
    # TODO: walk down the MCTS tree picking the best PUCT child until a non-expanded node is reached
    node = root

    while node['children']:
        action, node = select_best_child(node, node['children'].keys(), c_puct)
    
    return node

# Step 32 - evaluate_with_network
def evaluate_with_network(net, state, to_play):
    # TODO: run net on encoded state and return (masked priors np.ndarray (7,), value float)
    net.eval()
    mask = action_mask(state)
    with torch.no_grad():
        logits, value = policy_value_forward(net, board_to_torch_tensor(state, to_play))
        masked_probs = torch.exp(masked_log_softmax(logits, mask))
    return masked_probs.cpu().numpy().reshape(7), float(value.item())

# Step 33 - expand_node
def expand_node(node, priors):
    # TODO: attach a child node for every legal move with the corresponding network prior
    board = node['board']
    valid = valid_moves(board)
    for move in valid:
        new_board = drop_piece(board, move, node['to_play'])
        child = make_mcts_node(priors[move], node)
        child['to_play'] = other_player(node['to_play'])
        child['board'] = new_board
        node['children'][move] = child

    node['is_expanded'] = True
    return

# Step 34 - backup_value
def backup_value(leaf, value):
    # TODO: walk from leaf up through parents, updating visit_count and value_sum with alternating signs
    node = leaf
    curr_val = value

    while node['parent'] != None:
        node['visit_count'] += 1
        node['value_sum'] += curr_val
        curr_val *= -1
        node = node['parent']
    
    node['visit_count'] += 1
    node['value_sum'] += curr_val
    
    return

# Step 35 - run_one_simulation
def run_one_simulation(root, net, c_puct):
    if 'is_expanded' not in root:
        root['is_expanded'] = False
        
    leaf = select_leaf(root, c_puct)
    done, winner = is_terminal(leaf['board'])

    if done:
        value = 1 if winner == leaf['to_play'] else -1
        backup_value(leaf, value)
        return

    probs, val = evaluate_with_network(net, leaf['board'], leaf['to_play'])
    expand_node(leaf, probs)
    backup_value(leaf, val)

    return

# Step 36 - run_mcts
def run_mcts(state, to_play, net, num_simulations, c_puct):
    # TODO: build a fresh root for (state, to_play) and run num_simulations PUCT simulations
    root = make_mcts_node(prior=1.0)
    root['board'] = state
    root['to_play'] = to_play

    for i in range(num_simulations):
        run_one_simulation(root, net, c_puct)
    
    return root

# Step 37 - visit_count_policy
import torch.nn.functional as F

def visit_count_policy(root, temperature=1.0):
    # TODO: convert root child visit counts into a length-7 probability vector over columns
    ret = torch.zeros(size=(7, ), dtype=torch.float64)

    for i, child in enumerate(root['children'].keys()):
        ret[child] = root['children'][child]['visit_count']
    
    if temperature == 0:
        ret[torch.argmax(ret)] = 1.0
        ret[ret != 1.0] = 0.0
        return ret

    ret = ret ** (1 / temperature)

    if ret.sum() == 0:
        return torch.ones(7, dtype=torch.float64) / 7

    ret = ret / ret.sum()

    return ret

# Step 38 - mcts_choose_action
def mcts_choose_action(state, to_play, net, num_simulations, c_puct, temperature=1.0):
    # TODO: Run MCTS at the given state and return (action, visit-count policy vector).
    root = run_mcts(state, to_play, net, num_simulations, c_puct)
    policy = visit_count_policy(root, temperature)

    return int(torch.argmax(policy)), policy.numpy()

# Step 39 - record_self_play_step
def record_self_play_step(history, board, policy, to_play):
    # TODO: append a dict with 'board', 'policy', 'to_play' to history and return history
    history.append({
        'board': board.copy(),
        'policy': policy.copy(),
        'to_play': to_play
    })
    return history

# Step 40 - play_self_play_game
def play_self_play_game(net, num_simulations, c_puct, temperature=1.0):
    # TODO: play one Connect-4 game with both sides driven by MCTS, recording every step
    board = make_empty_board()
    history = []
    to_play = 1

    winner = -1

    while True:
        action, policy = mcts_choose_action(board, to_play, net, num_simulations, c_puct, temperature)
        history = record_self_play_step(history, board, policy, to_play)
        board, done, winner, to_play = step_env(board, action, to_play) 
        if done:
            break

    return history, winner

# Step 41 - assign_value_targets
def assign_value_targets(history, winner):
    # TODO: return a new list of step dicts each annotated with a 'value' target in {-1.0, 0.0, 1.0}.
    ret = [di.copy() for di in history]
    
    for di in ret:
        val = 0.0
        if winner == 1:
            if di['to_play'] == 1:
                val = 1.0
            else:
                val = -1.0
        elif winner == 2:
            if di['to_play'] == 1:
                val = -1.0
            else:
                val = 1.0
        
        di['value'] = val
    
    return ret

# Step 42 - generate_self_play_batch
def generate_self_play_batch(net, num_games, num_simulations, c_puct, temperature=1.0):
    # TODO: play num_games self-play games and return a flat list of labelled step dicts.
    ret = []
    for i in range(num_games):
        history, winner = play_self_play_game(net, num_simulations, c_puct, temperature)
        history = assign_value_targets(history, winner)
        for di in history:
            ret.append(di)
    
    return ret

# Step 43 - value_loss_mse
import torch

def value_loss_mse(predicted_values, target_values):
    # TODO: return the mean squared error between predicted and target values
    return torch.nn.functional.mse_loss(predicted_values, target_values)

# Step 44 - policy_loss_cross_entropy
import torch

def policy_loss_cross_entropy(predicted_log_probs, target_policy):
    """Cross-entropy between MCTS target policy and network log-probs. Returns scalar tensor."""
    # TODO: compute -sum(target * log_probs) per row, then average over the batch
    return -(target_policy * predicted_log_probs).sum(dim=1).mean()

# Step 45 - l2_regularization_loss
def l2_regularization_loss(net):
    # TODO: return the sum of squared L2 norms of all trainable parameters in net
    ret = None
    for param in net.parameters():
        if param.requires_grad == False:
            continue
        
        val = torch.sum(param ** 2)
        if ret is None:
            ret = val
        else:
            ret = ret + val
    
    if ret is None:
        return torch.tensor(0.0)
    
    return ret

# Step 46 - combined_loss
def combined_loss(predicted_log_probs, predicted_values, target_policy, target_values, net, policy_weight=1.0, value_weight=1.0, l2_weight=1e-4):
    # TODO: combine policy CE, value MSE, and L2 reg into a single weighted training loss.
    mse = value_loss_mse(predicted_values, target_values)
    ce = policy_loss_cross_entropy(predicted_log_probs, target_policy)
    l2 = l2_regularization_loss(net)

    tot = mse * value_weight + ce * policy_weight + l2 * l2_weight
    return (tot, {
        'policy': ce,
        'value': mse,
        'l2': l2
    })

# Step 47 - encode_batch_states
import torch 

def encode_batch_states(boards, to_plays):
    # TODO: encode each (board, to_play) and stack into a (B, C, 6, 7) float tensor
    ret = []
    for board, player in zip(boards, to_plays):
        ret.append(encode_board(board, player))
    
    return torch.tensor(ret)

# Step 48 - iterate_minibatches
def iterate_minibatches(buffer, batch_size, seed=None):
    """Yield shuffled minibatches of step dicts of size <= batch_size."""
    # TODO: shuffle indices and yield contiguous slices of the buffer
    rng = np.random.default_rng(seed)
    indices = rng.permutation(len(buffer))

    for start in range(0, len(buffer), batch_size):
        batch_indices = indices[start:start + batch_size]
        yield [buffer[i] for i in batch_indices]

# Step 49 - training_step
def training_step(net, optimizer, minibatch,
                  policy_weight=1.0, value_weight=1.0, l2_weight=1e-4):

    # Encode each board
    encoded_boards = np.stack([
        encode_board(step['board'], step['to_play'])
        for step in minibatch
    ])

    # Convert inputs/targets to PyTorch tensors
    encoded_boards = torch.tensor(encoded_boards, dtype=torch.float32)

    target_policy = torch.tensor(
        np.stack([step['policy'] for step in minibatch]),
        dtype=torch.float32
    )

    target_values = torch.tensor(
        [step['value'] for step in minibatch],
        dtype=torch.float32
    )

    # Forward pass
    logits, predicted_values = policy_value_forward(
        net, encoded_boards
    )

    # Build action masks
    masks = np.stack([
        action_mask(step['board'])
        for step in minibatch
    ])

    masks = torch.tensor(masks, dtype=torch.bool)

    # Masked log probabilities
    log_probs = masked_log_softmax(logits, masks)

    # Combined loss
    loss, components = combined_loss(
        log_probs,
        predicted_values,
        target_policy,
        target_values,
        net,
        policy_weight=policy_weight,
        value_weight=value_weight,
        l2_weight=l2_weight
    )

    # Optimizer update
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    return {
        'total': loss.item(),
        'policy': components['policy'].item(),
        'value': components['value'].item(),
        'l2': components['l2'].item()
    }

# Step 50 - training_epoch
def training_epoch(net, optimizer, buffer, batch_size, seed=None,
                   policy_weight=1.0, value_weight=1.0, l2_weight=1e-4):

    totals = {
        'total': 0.0,
        'policy': 0.0,
        'value': 0.0,
        'l2': 0.0
    }

    num_batches = 0

    for minibatch in iterate_minibatches(buffer, batch_size, seed):
        losses = training_step(
            net,
            optimizer,
            minibatch,
            policy_weight=policy_weight,
            value_weight=value_weight,
            l2_weight=l2_weight
        )

        for key in totals:
            totals[key] += losses[key]

        num_batches += 1

    if num_batches == 0:
        return totals

    for key in totals:
        totals[key] /= num_batches

    return totals

# Step 51 - self_play_iteration
def self_play_iteration(net, optimizer, num_games, num_simulations, c_puct, batch_size, num_epochs=1, temperature=1.0):
    # TODO: generate a self-play buffer, then train on it for num_epochs and return buffer_size + losses
    buffer = generate_self_play_batch(
        net,
        num_games,
        num_simulations,
        c_puct,
        temperature,
    )

    losses = []
    for _ in range(num_epochs):
        epoch_losses = training_epoch(
            net,
            optimizer,
            buffer,
            batch_size
        )
        losses.append(epoch_losses)

    return {
        "buffer_size": len(buffer),
        "losses": losses,
    }

# Step 52 - train_loop
def train_loop(net, optimizer, num_iterations, num_games, num_simulations, c_puct, batch_size, num_epochs=1, temperature=1.0):
    # TODO: run self_play_iteration num_iterations times and collect each returned dict into a list.
    ret = []
    for i in range(num_iterations):
        losses = self_play_iteration(net, optimizer, num_games, num_simulations, c_puct, batch_size, num_epochs, temperature)
        ret.append(losses)
    return ret

# Step 53 - random_policy_action
def random_policy_action(state, to_play, rng=None):
    # TODO: pick a uniformly random legal column on the given board
    if rng is None:
        rng = np.random.default_rng()

    legal_moves = valid_moves(state)

    return int(rng.choice(legal_moves))

# Step 54 - greedy_agent_action
def greedy_agent_action(net, state, to_play):
    # TODO: run one forward pass and return the argmax legal column for to_play.
    encoded = encode_board(state, to_play)
    encoded = torch.tensor(
        encoded,
        dtype=torch.float32
    ).unsqueeze(0)
    logits, val = policy_value_forward(net, encoded)
    legal_moves = valid_moves(state)

    logits = logits[0]

    mask = torch.full_like(logits, float('-inf'))
    mask[legal_moves] = 0.0

    masked_logits = logits + mask

    return int(torch.argmax(masked_logits).item())

# Step 55 - play_one_match
def play_one_match(agent_one, agent_two, starting_player=1):
    # TODO: play a full Connect-4 game between two callable agents and return the winner code.
    state = make_empty_board()
    to_play = starting_player

    while True:
        if to_play == 1:
            action = agent_one(state, to_play)
        else:
            action = agent_two(state, to_play)

        state, done, winner, next_player = step_env(state, action, to_play)

        if done:
            return winner

        to_play = other_player(to_play)

# Step 56 - match_win_rate
def match_win_rate(agent_one, agent_two, num_matches, alternate_starts=True):
    # TODO: play num_matches games and tally wins, losses, draws for agent_one
    results = {
        'wins': 0,
        'losses': 0,
        'draws': 0
    }

    for i in range(num_matches):
        starting_player = 1
        if alternate_starts:
            starting_player = 1 if i % 2 == 0 else 2

        winner = play_one_match(
            agent_one,
            agent_two,
            starting_player
        )

        if winner == 1:
            results['wins'] += 1
        elif winner == 2:
            results['losses'] += 1
        else:
            results['draws'] += 1

    return results

# Step 57 - evaluate_against_random
def evaluate_against_random(net, num_matches, seed=None):
    # TODO: play num_matches between greedy net agent and a seeded random baseline
    rng = np.random.default_rng(seed)

    def greedy_agent(state, to_play):
        return greedy_agent_action(net, state, to_play)

    def random_agent(state, to_play):
        return random_policy_action(state, to_play, rng)

    return match_win_rate(
        greedy_agent,
        random_agent,
        num_matches,
        alternate_starts=True
    )

