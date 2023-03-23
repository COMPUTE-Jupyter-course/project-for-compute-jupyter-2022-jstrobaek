import sqlite3 as sql
from pathlib import Path
from typing import List

import pandas as pd
from pandas import DataFrame
from Bio.PDB import Selection, Structure


def sql_to_df(db_file: Path, query: str = 'SELECT * FROM MS2data') -> DataFrame:
    """Connect to SQLite DB and read with Pandas using the specified quiry.
    """

    con = sql.connect(db_file)

    return pd.read_sql(query, con)

def eu_dist(structure: Structure, a: int, b: int) -> float:
    """Calculate euclidean distance between the alpha carbons of the specified residues.
    """

    chain_1 = Selection.unfold_entities(structure, 'R')[a].get_parent().id

    chain_2 = Selection.unfold_entities(structure, 'R')[b].get_parent().id

    atom_1 = structure[0][chain_1][a]['CA']

    atom_2 = structure[0][chain_2][b]['CA']

    return atom_2 - atom_1

def locate_xls(structure: Structure,
               sequence_combined: str,
               xls: List[str], cutoff: int) -> List[List]:
    """Generate list of cross-linking residue pairs.
    """

    xl_atom_pairs = []

    for xl in xls:

        split_xl = xl.split('--')

        peptide_1 = split_xl[0].strip('-.()0123456789')

        k_pos_p1 = peptide_1.find('K') + 1

        peptide_2 = split_xl[1].strip('-.()0123456789')

        k_pos_p2 = peptide_2.find('K') + 1

        euclidean_distance = 10000

        tmp_distance = 10000

        mult_occ_p1 = [x for x in range(len(sequence_combined))
                       if sequence_combined.find(peptide_1, x) == x]

        mult_occ_p2 = [x for x in range(len(sequence_combined))
                       if sequence_combined.find(peptide_2, x) == x]

        seq_pos_p1_k = 0

        seq_pos_p2_k = 0

        for pos_1 in mult_occ_p1:

            for pos_2 in mult_occ_p2:

                a = pos_1 + k_pos_p1 + 1

                b = pos_2 + k_pos_p2 + 1

                if tmp_distance > eu_dist(structure, a, b):

                    tmp_distance = eu_dist(structure, a, b)

                    seq_pos_p1_k = pos_1 + k_pos_p1

                    seq_pos_p2_k = pos_2 + k_pos_p2

        if ((peptide_1 in sequence_combined) and
            (peptide_2 in sequence_combined)):

            a = seq_pos_p1_k + 1

            b = seq_pos_p2_k + 1

            euclidean_distance = eu_dist(structure, a, b)

        if euclidean_distance <= cutoff:

            xl_atom_pairs.append([str(seq_pos_p1_k - 1), str(seq_pos_p2_k - 1)])

    return xl_atom_pairs
