def _1b(s) :
    from Bio.Seq import Seq
    seqTemp = Seq(s)
    revSeqTemp = seqTemp.reverse_complement()
    print revSeqTemp
