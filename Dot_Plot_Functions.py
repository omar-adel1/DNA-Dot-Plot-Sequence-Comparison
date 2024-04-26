import numpy as np
import matplotlib.pyplot as plt
import io


def compute_alignment_matrix(sequence1, sequence2):
    """
    Computes the alignment matrix between two sequences.

    Args:
        sequence1 (str): The first sequence.
        sequence2 (str): The second sequence.

    Returns:
        numpy.ndarray: The alignment matrix.
    """
    alignment_matrix = np.zeros((len(sequence2), len(sequence1)))
    for i, char1 in enumerate(sequence2):
        for j, char2 in enumerate(sequence1):
            if char1 == char2:
                alignment_matrix[i, j] = 1
    return alignment_matrix


def draw_alignment_matrix(alignment_matrix, sequence1, sequence2):
    """
    Draws the alignment matrix as a heatmap.

    Args:
        alignment_matrix (numpy.ndarray): The alignment matrix.
        sequence1 (str): The first sequence.
        sequence2 (str): The second sequence.

    Returns:
        bytes: The image of the alignment matrix.
    """
    fig, ax = plt.subplots()
    ax.imshow(alignment_matrix, cmap='binary', interpolation='nearest')
    ax.set_xticks(np.arange(len(sequence1)))
    ax.set_yticks(np.arange(len(sequence2)))
    ax.set_xticklabels(sequence1)
    ax.set_yticklabels(sequence2)
    ax.set_xlabel('Sequence 1')
    ax.set_ylabel('Sequence 2')
    ax.set_title('Sequence Alignment Matrix')
    
    # Convert plot to image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    
    # Close plot to prevent display
    plt.close(fig)
    
    # Return the value of the buffer
    return buf.getvalue()



def validate_dna_sequence(sequence1, sequence2):
    """
    Validates whether the input sequences consist of valid DNA characters.

    Args:
        sequence1 (str): The first sequence.
        sequence2 (str): The second sequence.

    Returns:
        bool: True if both sequences are valid DNA sequences, False otherwise.
    """
    valid_chars = set('ATCG')
    return all(char in valid_chars for char in sequence1) and all(char in valid_chars for char in sequence2)
