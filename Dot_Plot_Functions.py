import numpy as np
import matplotlib.pyplot as plt
import io


# Function to compute alignment matrix
def compute_alignment_matrix(seq1, seq2):
    alignment_matrix = np.zeros((len(seq2), len(seq1)))
    for i, char1 in enumerate(seq2):
        for j, char2 in enumerate(seq1):
            if char1 == char2:
                alignment_matrix[i, j] = 1
    return alignment_matrix

def draw_matrix(alignment_matrix, seq1, seq2):
    fig, ax = plt.subplots()
    ax.imshow(alignment_matrix, cmap='binary', interpolation='nearest')
    ax.set_xticks(np.arange(len(seq1)))
    ax.set_yticks(np.arange(len(seq2)))
    ax.set_xticklabels(seq1)
    ax.set_yticklabels(seq2)
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
    valid_chars = set('ATCG')
    return all(char in valid_chars for char in sequence1) and all(char in valid_chars for char in sequence2)
