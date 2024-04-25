import streamlit as st
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import io
import Dot_Plot_Functions as functions


# Set page configuration
st.set_page_config(page_title="Dot Plot", page_icon='🧬', layout='wide')





def main():
    st.title("Sequence Alignment Visualization")
    
    # Create columns for layout
    left_side, right_side = st.columns([2, 2.2])
    with left_side:
        # Input sequences
        seq1 = st.text_input("Enter Sequence 1", "")
        seq2 = st.text_input("Enter Sequence 2", "")
    
    if not functions.validate_dna_sequence(seq1.upper(), seq2.upper()):
        st.write("Invalid DNA sequence. Please enter only 'A', 'T', 'C', or 'G' characters.")
        st.stop()
    
    # Compute alignment matrix
    alignment_matrix = functions.compute_alignment_matrix(seq1, seq2)
    
    with right_side:
        if seq1 and seq2:
            st.image(functions.draw_matrix(alignment_matrix, seq1, seq2))

if __name__ == "__main__":
    main()
