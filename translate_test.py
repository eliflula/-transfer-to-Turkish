    

from csv_trans import translate

if __name__ == "__main__":
    # multiprocessing.freeze_support()

    file="C:\\Users\\elift\\Desktop\\test\\rag_instruct_benchmark_tester.csv"

    source_language="en"
    target_language="tr"



    translate(file, source_language, target_language, sep=',')

